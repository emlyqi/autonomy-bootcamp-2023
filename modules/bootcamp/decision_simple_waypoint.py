"""
BOOTCAMPERS TO COMPLETE.

Travel to designated waypoint.
"""

from .. import commands
from .. import drone_report

# Disable for bootcamp use
# pylint: disable-next=unused-import
from .. import drone_status
from .. import location
from ..private.decision import base_decision


# Disable for bootcamp use
# No enable
# pylint: disable=duplicate-code,unused-argument


class DecisionSimpleWaypoint(base_decision.BaseDecision):
    """
    Travel to the designed waypoint.
    """

    def __init__(self, waypoint: location.Location, acceptance_radius: float) -> None:
        """
        Initialize all persistent variables here with self.
        """
        self.waypoint = waypoint
        print(f"Waypoint: {waypoint}")

        self.acceptance_radius = acceptance_radius

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============

        self.min_flight_boundary = -60
        self.max_flight_boundary = 60

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

    def run(
        self, report: drone_report.DroneReport, landing_pad_locations: "list[location.Location]"
    ) -> commands.Command:
        """
        Make the drone fly to the waypoint.

        You are allowed to create as many helper methods as you want,
        as long as you do not change the __init__() and run() signatures.

        This method will be called in an infinite loop, something like this:

        ```py
        while True:
            report, landing_pad_locations = get_input()
            command = Decision.run(report, landing_pad_locations)
            put_output(command)
        ```
        """
        # Default command
        command = commands.Command.create_null_command()

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============

        # Do something based on the report and the state of this class...

        if (
            self.waypoint.location_x >= self.min_flight_boundary
            and self.waypoint.location_x <= self.max_flight_boundary
            and self.waypoint.location_y >= self.min_flight_boundary
            and self.waypoint.location_y <= self.max_flight_boundary
        ):
            distance_from_waypoint = (
                self.waypoint.location_x - report.position.location_x
            ) ** 2 + (self.waypoint.location_y - report.position.location_y) ** 2

            if report.status == drone_status.DroneStatus.HALTED:

                if distance_from_waypoint < self.acceptance_radius**2:
                    command = commands.Command.create_land_command()

                else:
                    command = commands.Command.create_set_relative_destination_command(
                        self.waypoint.location_x, self.waypoint.location_y
                    )

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

        return command
