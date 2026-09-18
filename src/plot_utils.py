from __future__ import annotations

from typing import Dict

from src import config as cfg


def get_panel_colors(panel: str = "default") -> Dict[str, str]:
    """Return a color palette dictionary for the requested panel.

    panel="panel5" returns the dedicated Panel 5 palette when available.
    Any unknown panel falls back to cfg.colors.
    """
    panel_key = panel.strip().lower()

    if panel_key == "panel5" and hasattr(cfg, "panel5_colors"):
        return dict(cfg.panel5_colors)

    return dict(cfg.colors)


def get_species_color(species: str, panel: str = "default", fallback: str = "#999999") -> str:
    """Return a single species color from a panel palette with fallback."""
    palette = get_panel_colors(panel)
    return palette.get(species, fallback)
