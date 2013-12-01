"""Classes representing CaBi stations and trips

"""

from geopy.point import Point
from geopy import distance
from lxml import objectify
from pycabi import utils

CABI_STATUS_URL = "http://www.capitalbikeshare.com/data/stations/bikeStations.xml"


class Station(object):
    """CaBi station

    Most instance variable names are PEP-8 versions of the fields in the CaBi
    station status XML file
    (see https://github.com/dbarlett/pycabi/wiki/Station-Status), except for
    file_id, which is used because id is a built-in Python function.

    """

    def __init__(
        self,
        file_id=None,
        name=None,
        terminal_name=None,
        last_comm_with_server=None,
        latitude=None,
        longitude=None,
        altitude=None,
        installed=None,
        locked=None,
        install_date=None,
        removal_date=None,
        temporary=None,
        public=None,
        nb_bikes=None,
        nb_empty_docks=None,
        latest_update_time=None,
    ):
        """Create a Station

        :param file_id: id from station status XML file
        :type file_id: str
        :param name: station name (e.g. "10th & U St NW")
        :type name: str
        :param terminal_name: terminal name (e.g. "31111")
        :type terminal_name: str
        :param last_comm_with_server: latest communication
        :type last_comm_with_server: datetime.datetime
        :param latitude: latitude
        :type latitude: float
        :param longitude: longitude
        :type longitude: float
        :param altitude: altitude, in kilometers
        :type altitude: float
        :param installed: is station installed
        :type installed: bool
        :param locked: is station locked
        :type locked: bool
        :param install_date: installation date
        :type install_date: datetime.datetime
        :param removal_date: removal date
        :type removal_date: datetime.datetime
        :param temporary: is station temporary
        :type temporary: bool
        :param public: is station public
        :type public: bool
        :param nb_bikes: number of bikes
        :type nb_bikes: int
        :param nb_empty_docks: number of empty docks
        :type nb_empty_docks: int
        :param latest_update_time: latest update
        :type latest_update_time: datetime.datetime

        """
        self.file_id = file_id
        self.name = name
        self.terminal_name = terminal_name
        self.last_comm_with_server = last_comm_with_server
        self.location = Point(latitude, longitude, altitude)
        self.installed = installed
        self.locked = locked
        self.install_date = install_date
        self.removal_date = removal_date
        self.temporary = temporary
        self.public = public
        self.nb_bikes = nb_bikes
        self.nb_empty_docks = nb_empty_docks
        self.removal_date = removal_date

    def __str__(self):
        return "{0} ({1})".format(
            self.name,
            self.terminal_name,
        )


def get_system_status(status_file=CABI_STATUS_URL):
    """
    :param status_file: URL, file, or file-like object (see lxml.etree.parse())
    :type status_file: str,file
    :returns: dict of terminals, keyed by terminalName
    :rtype: dict

    """
    tree = objectify.parse(status_file)
    root = tree.getroot()
    stations = {}
    for child in root.iterchildren():
        s = Station(
            file_id=child["id"].text,
            name=child["name"].text,
            terminal_name=child["terminalName"].text,
            last_comm_with_server=utils.parse_timestamp(child["lastCommWithServer"].text),
            latitude=child["lat"].text,
            longitude=child["long"].text,
            installed=child["installed"].text,
            locked=child["locked"].text,
            temporary=child["temporary"].text,
            public=child["public"].text,
            nb_bikes=child["nbBikes"].text,
            nb_empty_docks=child["nbEmptyDocks"].text,
        )
        if child["installDate"].text:
            s.install_date = utils.parse_timestamp(child["installDate"].text)
        if child["removalDate"].text:
            s.removal_date = utils.parse_timestamp(child["removalDate"].text)
        stations[child["terminalName"].text] = s
    return stations
