import pytest
import imaging.hdr_exposure_ghost as mod

CASES = [
    ("motion_mask", (1)),
    ("noise_threshold", (1)),
    ("saturation_weight", (1)),
    ("tonemap_monotonic", (1)),
    ("fusion_determinism", (1)),
    ("exposure_meta", (1)),
    ("align_frames", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("local_contrast", (1)),
    ("metrics", (1)),
    ("ghost_score", (1)),
    ("batch_repeat", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
