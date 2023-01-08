def areTheyConcussed(LAthreshold, AAthreshold, LA, AA):
    # code

    """
    :param LAthreshold:
    :param AAthreshold:
    :param LA:
    :param AA:
    :return:

    TODO: add sophistication to diagnostic:
    - create degrees of impact severity that reflect on participant overview:
        (concept)
            % of threshold      color       severity
            85                  red         high
            60                  orange      medium
            40                  yellow      moderate
            <30%                green       normal
    - WTSC
    - Multiple impact adjustment
    - EEG
    - Cumulative impact over time
    - blood oxygen bias??

    """

    if LA > LAthreshold or AA > AAthreshold:
        return True
    return False
