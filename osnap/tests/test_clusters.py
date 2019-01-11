from context import analyze, data

reno = data.Community(source='ltdb', cbsafips='39900')
columns = ['median_household_income', 'p_poverty_rate', 'p_unemployment_rate']


# Aspatial Clusters

def test_gm():

    gm = analyze.cluster(reno, columns=columns, method='gm', best_model=True)
    assert len(gm.census.gm.unique()) > 6


def test_ward():

    ward = analyze.cluster(reno, columns=columns, method='ward')
    assert len(ward.census.ward.unique()) == 6


def test_spectral():

    spectral = analyze.cluster(reno, columns=columns, method='spectral')
    assert len(spectral.census.spectral.unique()) == 6


def test_kmeans():

    kmeans = analyze.cluster(reno, columns=columns, method='kmeans')
    assert len(kmeans.census.kmeans.unique()) == 6


def test_aff_prop():

    aff_prop = analyze.cluster(reno, columns=columns, method='ap',
                               preference=-100)
    assert len(aff_prop.census.ap.unique()) == 4


def test_hdbscan():

    hdbscan = analyze.cluster(reno, columns=columns, method='hdbscan')
    assert len(hdbscan.census.hdbscan.unique()) == 30


# Spatial Clusters

def test_spenc():

    spenc = analyze.cluster_spatial(reno, columns=columns, method='spenc')
    assert len(spenc.census.spenc.unique()) == 7


def test_maxp():

    maxp = analyze.cluster_spatial(reno, columns=columns, method='max_p',
                                   initial=10)
    assert len(maxp.census.max_p.unique()) == 11


def test_ward_spatial():

    ward_spatial = analyze.cluster_spatial(reno, columns=columns,
                                           method='ward_spatial')
    assert len(ward_spatial.census.ward_spatial.unique()) == 7


def test_skater():

    skater = analyze.cluster_spatial(reno, columns=columns, method='skater',
                                     n_clusters=10)
    assert len(skater.census.skater.unique()) == 14


def test_azp():
    azp = analyze.cluster_spatial(reno, columns=columns, method='azp')
    assert len(azp.census.azp.unique()) == 7
