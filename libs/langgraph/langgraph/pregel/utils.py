from langgraph.checkpoint.base import ChannelVersions


def get_new_channel_versions(
    previous_versions: ChannelVersions, current_versions: ChannelVersions
) -> ChannelVersions:
    """Get subset of current_versions that are newer than previous_versions."""
    if previous_versions:
        version_type = type(next(iter(current_versions.values()), None))
        null_version = version_type()  # type: ignore[misc]
        new_versions = {
            k: v
            for k, v in current_versions.items()
            if v > previous_versions.get(k, null_version)  # type: ignore[operator]
        }
    else:
        new_versions = current_versions

    return new_versions
