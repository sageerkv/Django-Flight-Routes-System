from django.shortcuts import render
from django.db.models import Max, Min
from .models import AirportRouteNode
from .forms import AirportRouteNodeForm, NthNodeSearchForm, ShortestBetweenForm


def add_node(request):
    msg = None
    if request.method == "POST":
        form = AirportRouteNodeForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Route node added successfully!"
    else:
        form = AirportRouteNodeForm()

    nodes = AirportRouteNode.objects.all()
    return render(request, "routes/add_node.html", {"form": form, "msg": msg, "nodes": nodes})


def find_nth_node(request):
    result = None
    error = None

    if request.method == "POST":
        form = NthNodeSearchForm(request.POST)
        if form.is_valid():
            route_name = form.cleaned_data["route_name"]
            airport_code = form.cleaned_data["airport_code"]
            direction = form.cleaned_data["direction"]
            n = form.cleaned_data["n"]

            try:
                current = AirportRouteNode.objects.get(route_name=route_name, airport_code=airport_code)
                if direction == "L":
                    target_position = current.position - n
                else:
                    target_position = current.position + n

                result = AirportRouteNode.objects.filter(route_name=route_name, position=target_position).first()
                if not result:
                    error = f"No node found at position {target_position} in route {route_name}."
            except AirportRouteNode.DoesNotExist:
                error = "Selected airport does not exist in this route."
    else:
        form = NthNodeSearchForm()

    return render(request, "routes/find_nth_node.html", {"form": form, "result": result, "error": error})


def reports(request):
    longest_node = None
    shortest_between_node = None
    shortest_error = None

    # Longest Node (based on duration) per route or global? We'll show global + allow filtering
    route_name = request.GET.get("route_name", "").strip()
    qs = AirportRouteNode.objects.all()
    if route_name:
        qs = qs.filter(route_name=route_name)

    longest_node = qs.order_by("-duration").first()

    # Shortest between two airports (POST)
    if request.method == "POST":
        form = ShortestBetweenForm(request.POST)
        if form.is_valid():
            route_name_f = form.cleaned_data["route_name"]
            start_code = form.cleaned_data["start_airport_code"]
            end_code = form.cleaned_data["end_airport_code"]

            start_node = AirportRouteNode.objects.filter(route_name=route_name_f, airport_code=start_code).first()
            end_node = AirportRouteNode.objects.filter(route_name=route_name_f, airport_code=end_code).first()

            if not start_node or not end_node:
                shortest_error = "Start or End airport not found in the given route."
            else:
                left_pos = min(start_node.position, end_node.position)
                right_pos = max(start_node.position, end_node.position)

                between_qs = AirportRouteNode.objects.filter(
                    route_name=route_name_f,
                    position__gt=left_pos,
                    position__lt=right_pos
                )

                if not between_qs.exists():
                    shortest_error = "No intermediate nodes exist between the selected airports."
                else:
                    shortest_between_node = between_qs.order_by("duration").first()
    else:
        form = ShortestBetweenForm()

    return render(
        request,
        "routes/reports.html",
        {
            "route_name": route_name,
            "longest_node": longest_node,
            "form": form,
            "shortest_between_node": shortest_between_node,
            "shortest_error": shortest_error,
        },
    )
