from django.shortcuts import render, redirect
from django.db.models import Count
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(name__contains="Baseball"),
		"womens_leagues": League.objects.filter(name__contains="Women"),
		"hockey_leagues": League.objects.filter(name__contains="Hockey"),
		"not_footbal_leagues": League.objects.exclude(sport="Football"),
		"conferences_leagues": League.objects.filter(name__contains="Conference"),
		# Level 1 continued queries
		"atlantic_leagues": League.objects.filter(name__contains="Atlantic"),
		"dallas_teams": Team.objects.filter(location__contains="Dallas"),
		"raptors_teams": Team.objects.filter(team_name__contains="Raptors"),
		"city_teams": Team.objects.filter(location__contains="City"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"teams_by_location": Team.objects.order_by('location'),
		"teams_by_name_desc": Team.objects.order_by('-team_name'),
		"cooper_players": Player.objects.filter(last_name__contains="Cooper"),
		"joshuas": Player.objects.filter(first_name__contains="Joshua"),
		"cooper_not_joshua": Player.objects.filter(last_name__contains="Cooper").exclude(first_name__contains="Joshua"),
		"alex_wyatt_players": Player.objects.filter(first_name__in=["Alexander","Wyatt"]),
		# Level 2 (ForeignKey relationship) queries
		"atlantic_soccer_teams": Team.objects.filter(league__name="Atlantic Soccer Conference").order_by("id"),
		"boston_penguins_players": Player.objects.filter(curr_team__location="Boston", curr_team__team_name="Penguins").order_by("id"),
		"ic_baseball_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference").order_by("id"),
		"american_football_lopez": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name="Lopez").order_by("id"),
		"football_players": Player.objects.filter(curr_team__league__sport="Football").order_by("id"),
		"teams_with_sophia": Team.objects.filter(curr_players__first_name="Sophia").order_by("curr_players__id").distinct(),
		"leagues_with_sophia": League.objects.filter(teams__curr_players__first_name="Sophia").order_by("teams__curr_players__id").distinct(),
		"flores_not_roughriders": Player.objects.filter(last_name="Flores").exclude(curr_team__location="Washington", curr_team__team_name="Roughriders").order_by("id"),
		# Level 3 (ManyToMany relationship) queries
		"samuel_evans_teams": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans").order_by("id"),
		"manitoba_tiger_cats_players": Player.objects.filter(all_teams__location="Manitoba", all_teams__team_name="Tiger-Cats").order_by("id"),
		"former_wichita_vikings_players": Player.objects.filter(all_teams__location="Wichita", all_teams__team_name="Vikings").exclude(curr_team__location="Wichita", curr_team__team_name="Vikings").order_by("id"),
		"jacob_gray_past_teams": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(curr_players__first_name="Jacob", curr_players__last_name="Gray").order_by("id"),
		"joshuas_atlantic_baseball_players": Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players").distinct().order_by("id"),
		"teams_with_12_players": Team.objects.annotate(player_count=Count("all_players")).filter(player_count__gte=12).order_by("id"),
		"players_by_team_count": Player.objects.annotate(team_count=Count("all_teams")).order_by("team_count", "id"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
