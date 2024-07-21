from .models import LevelConfig


def get_xp_for_next_level(current_level):
    try:
        config = LevelConfig.objects.get(level=current_level+1)
        return config.xp_required
    except LevelConfig.DoesNotExist:
        return None


def award_experience(user, xp):
    user.experience += xp
    while True:
        next_level_xp = get_xp_for_next_level(user.level)
        if next_level_xp is not None and user.experience >= next_level_xp:
            user.level += 1
        else:
            break
    user.save()
