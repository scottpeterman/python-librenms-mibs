# SNMP MIB module (SL-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:14 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(tftpStatus,) = mibBuilder.importSymbols(
    "RAD-MIB",
    "tftpStatus")

(slAlarmActive,
 slAlarmIfIndex,
 slAlarmServiceAffect,
 slAlarmSeverity,
 slAlarmType) = mibBuilder.importSymbols(
    "SL-ALARM-MIB",
    "slAlarmActive",
    "slAlarmIfIndex",
    "slAlarmServiceAffect",
    "slAlarmSeverity",
    "slAlarmType")

(edfaIfIndex,
 edfaOperControlMode,
 edfaStatus) = mibBuilder.importSymbols(
    "SL-EDFA-MIB",
    "edfaIfIndex",
    "edfaOperControlMode",
    "edfaStatus")

(slEventIfIndex,
 slEventInventoryAction,
 slEventInventoryIfIndex,
 slEventInventoryPartnum,
 slEventInventorySerial,
 slEventInventoryType,
 slEventType,
 slEventUser,
 slEventVal,
 slGenEventIfIndex,
 slGenEventType,
 slGenEventUser,
 slGenEventVal) = mibBuilder.importSymbols(
    "SL-EVENT-MIB",
    "slEventIfIndex",
    "slEventInventoryAction",
    "slEventInventoryIfIndex",
    "slEventInventoryPartnum",
    "slEventInventorySerial",
    "slEventInventoryType",
    "slEventType",
    "slEventUser",
    "slEventVal",
    "slGenEventIfIndex",
    "slGenEventType",
    "slGenEventUser",
    "slGenEventVal")

(packetlight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "packetlight")

(optApsConfigActiveConnectionRx,
 optApsConfigUserWorkingIndex) = mibBuilder.importSymbols(
    "SL-OPT-APS-MIB",
    "optApsConfigActiveConnectionRx",
    "optApsConfigUserWorkingIndex")

(slTestsIfLoopIfIndex,
 slTestsIfLoopType,
 slTestsTrapsLoopbackActive) = mibBuilder.importSymbols(
    "SL-TESTS-MIB",
    "slTestsIfLoopIfIndex",
    "slTestsIfLoopType",
    "slTestsTrapsLoopbackActive")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

slAlarmTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 101)
)
slAlarmTrapV1.setObjects(
      *(("SL-ALARM-MIB", "slAlarmIfIndex"),
        ("SL-ALARM-MIB", "slAlarmType"),
        ("SL-ALARM-MIB", "slAlarmSeverity"),
        ("SL-ALARM-MIB", "slAlarmServiceAffect"),
        ("SL-ALARM-MIB", "slAlarmActive"))
)
if mibBuilder.loadTexts:
    slAlarmTrapV1.setStatus(
        ""
    )

slTestsTrapsLoopbackTableChangedV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 122)
)
slTestsTrapsLoopbackTableChangedV1.setObjects(
      *(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"),
        ("SL-TESTS-MIB", "slTestsIfLoopType"),
        ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
)
if mibBuilder.loadTexts:
    slTestsTrapsLoopbackTableChangedV1.setStatus(
        ""
    )

edfaStatusChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 128)
)
edfaStatusChangeV1.setObjects(
      *(("SL-EDFA-MIB", "edfaIfIndex"),
        ("SL-EDFA-MIB", "edfaStatus"))
)
if mibBuilder.loadTexts:
    edfaStatusChangeV1.setStatus(
        ""
    )

edfaControlModeChangeV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 129)
)
edfaControlModeChangeV1.setObjects(
      *(("SL-EDFA-MIB", "edfaIfIndex"),
        ("SL-EDFA-MIB", "edfaOperControlMode"))
)
if mibBuilder.loadTexts:
    edfaControlModeChangeV1.setStatus(
        ""
    )

optApsTrapSwitchoverV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 130)
)
optApsTrapSwitchoverV1.setObjects(
      *(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"),
        ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
)
if mibBuilder.loadTexts:
    optApsTrapSwitchoverV1.setStatus(
        ""
    )

slEventTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 131)
)
slEventTrapV1.setObjects(
      *(("SL-EVENT-MIB", "slEventIfIndex"),
        ("SL-EVENT-MIB", "slEventType"),
        ("SL-EVENT-MIB", "slEventVal"),
        ("SL-EVENT-MIB", "slEventUser"))
)
if mibBuilder.loadTexts:
    slEventTrapV1.setStatus(
        ""
    )

tftpStatusChangeTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 132)
)
tftpStatusChangeTrapV1.setObjects(
    ("RAD-MIB", "tftpStatus")
)
if mibBuilder.loadTexts:
    tftpStatusChangeTrapV1.setStatus(
        ""
    )

slEventInventoryTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 133)
)
slEventInventoryTrapV1.setObjects(
      *(("SL-EVENT-MIB", "slEventInventoryIfIndex"),
        ("SL-EVENT-MIB", "slEventInventoryAction"),
        ("SL-EVENT-MIB", "slEventInventoryType"),
        ("SL-EVENT-MIB", "slEventInventorySerial"),
        ("SL-EVENT-MIB", "slEventInventoryPartnum"))
)
if mibBuilder.loadTexts:
    slEventInventoryTrapV1.setStatus(
        ""
    )

slGenEventTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 134)
)
slGenEventTrapV1.setObjects(
      *(("SL-EVENT-MIB", "slGenEventIfIndex"),
        ("SL-EVENT-MIB", "slGenEventType"),
        ("SL-EVENT-MIB", "slGenEventVal"),
        ("SL-EVENT-MIB", "slGenEventUser"))
)
if mibBuilder.loadTexts:
    slGenEventTrapV1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-TRAP-MIB",
    **{"slAlarmTrapV1": slAlarmTrapV1,
       "slTestsTrapsLoopbackTableChangedV1": slTestsTrapsLoopbackTableChangedV1,
       "edfaStatusChangeV1": edfaStatusChangeV1,
       "edfaControlModeChangeV1": edfaControlModeChangeV1,
       "optApsTrapSwitchoverV1": optApsTrapSwitchoverV1,
       "slEventTrapV1": slEventTrapV1,
       "tftpStatusChangeTrapV1": tftpStatusChangeTrapV1,
       "slEventInventoryTrapV1": slEventInventoryTrapV1,
       "slGenEventTrapV1": slGenEventTrapV1}
)
