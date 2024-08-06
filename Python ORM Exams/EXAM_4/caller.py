import os
import django
from django.db.models import Q, Count

from main_app.models import TennisPlayer, Tournament, Match

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


def get_tennis_players(search_name: str = None, search_country: str = None):
    if search_name is None and search_country is None:
        return ''

    elif search_name is not None and search_country is not None:
        query = Q(full_name__icontains=search_name) & Q(country__icontains=search_country)
        tennis_players = TennisPlayer.objects.filter(query).order_by('ranking')

        if not tennis_players:
            return ''

        result = []

        for player in tennis_players:
            result.append(f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}")

        return '\n'.join(result)

    elif search_name is not None and search_country is None:
        query = Q(full_name__icontains=search_name)
        tennis_players = TennisPlayer.objects.filter(query).order_by('ranking')

        if not tennis_players:
            return ''

        result = []

        for player in tennis_players:
            result.append(f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}")

        return '\n'.join(result)

    elif search_name is None and search_country is not None:
        query = Q(country__icontains=search_country)
        tennis_players = TennisPlayer.objects.filter(query).order_by('ranking')

        if not tennis_players:
            return ''

        result = []

        for player in tennis_players:
            result.append(f"Tennis Player: {player.full_name}, country: {player.country}, ranking: {player.ranking}")

        return '\n'.join(result)


def get_top_tennis_player():
    top_player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()

    if not TennisPlayer.objects.all() or not top_player:
        return ''

    return f"Top Tennis Player: {top_player.full_name} with {top_player.number_of_wins} wins."


def get_tennis_player_by_matches_count():
    top_tennis_player = TennisPlayer.objects.prefetch_related('players_matches').annotate(
        num_of_matches=Count('players_matches')).order_by('-num_of_matches', 'ranking').first()

    if not top_tennis_player or top_tennis_player.players_matches.count() == 0:
        return ''

    return f"Tennis Player: {top_tennis_player.full_name} with {top_tennis_player.players_matches.count()} matches played."


def get_tournaments_by_surface_type(surface: str = None):
    if not Tournament.objects.all() or surface is None:
        return ''

    tournaments = (Tournament.objects.prefetch_related('tournament_matches').
                   filter(surface_type__icontains=surface).
                   order_by('-start_date'))

    if not tournaments:
        return ''

    result = []

    for tournament in tournaments:
        result.append(f"Tournament: {tournament.name}, "
                      f"start date: {tournament.start_date}, "
                      f"matches: {tournament.tournament_matches.count()}")

    return '\n'.join(result)


def get_latest_match_info():
    match = (Match.objects.
             prefetch_related('players').
             order_by('-date_played', '-id').
             first())

    if match is None:
        return ''

    players = match.players.order_by('full_name')
    player1_full_name = players.first().full_name
    player2_full_name = players.last().full_name
    winner_full_name = match.winner.full_name if match.winner else 'TBA'

    return (f"Latest match played on: {match.date_played}, "
            f"tournament: {match.tournament.name}, "
            f"score: {match.score}, "
            f"players: {player1_full_name} vs {player2_full_name}, "
            f"winner: {winner_full_name}, "
            f"summary: {match.summary}")


def get_matches_by_tournament(tournament_name: str = None):
    matches = Match.objects.select_related('tournament', 'winner').filter(tournament__name__exact=tournament_name).order_by('-date_played')

    if not matches or not Tournament.objects.all() or tournament_name is None:
        return "No matches found."

    result = []

    for match in matches:
        result.append(f"Match played on: {match.date_played}, score: {match.score}, winner: {match.winner.full_name if match.winner else 'TBA'}")

    return '\n'.join(result)