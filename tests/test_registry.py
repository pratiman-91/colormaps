from colormaps._registry import _sanitize_name, build_registry, COLLECTIONS


class TestSanitizeName:
    def test_normal_name(self):
        assert _sanitize_name('viridis') == 'viridis'

    def test_digit_prefix(self):
        assert _sanitize_name('3wave') == 'N3wave'

    def test_underscore_prefix(self):
        assert _sanitize_name('_hidden') == 'N_hidden'

    def test_hyphen_replaced(self):
        assert _sanitize_name('blue-red') == 'blue_red'

    def test_plus_replaced(self):
        assert _sanitize_name('blue+red') == 'blue_red'

    def test_combined(self):
        assert _sanitize_name('3blue-red+green') == 'N3blue_red_green'


class TestBuildRegistry:
    def test_returns_dict(self):
        reg = build_registry()
        assert isinstance(reg, dict)

    def test_non_empty(self):
        reg = build_registry()
        assert len(reg) > 0

    def test_every_key_has_reversed_variant(self):
        reg = build_registry()
        for key in list(reg.keys()):
            if not key.endswith('_r'):
                assert key + '_r' in reg

    def test_values_are_rgb_paths(self):
        reg = build_registry()
        for v in reg.values():
            assert v.endswith('.rgb')

    def test_no_keys_start_with_digit(self):
        reg = build_registry()
        for key in reg:
            assert not key[0].isdigit()

    def test_no_keys_contain_hyphen_or_plus(self):
        reg = build_registry()
        for key in reg:
            assert '-' not in key
            assert '+' not in key


class TestCollections:
    def test_count(self):
        assert len(COLLECTIONS) == 11

    def test_expected_names(self):
        for name in ['carbonplan', 'cartocolors', 'cmocean', 'scientific', 'tableau']:
            assert name in COLLECTIONS
