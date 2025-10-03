# SNMP MIB module (HH3C-SECHIGH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SECHIGH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:50 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cSecHigh = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171)
)
if mibBuilder.loadTexts:
    hh3cSecHigh.setRevisions(
        ("2021-02-03 00:00",
         "2021-01-06 00:00",
         "2020-05-29 00:00",
         "2017-09-16 20:20")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSecHighMonitor_ObjectIdentity = ObjectIdentity
hh3cSecHighMonitor = _Hh3cSecHighMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1)
)
_Hh3cSecHighHgMonitorAlarmVar_ObjectIdentity = ObjectIdentity
hh3cSecHighHgMonitorAlarmVar = _Hh3cSecHighHgMonitorAlarmVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1)
)
_Hh3cSecHighHgMonitorAlarmType_Type = Integer32
_Hh3cSecHighHgMonitorAlarmType_Object = MibScalar
hh3cSecHighHgMonitorAlarmType = _Hh3cSecHighHgMonitorAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 1),
    _Hh3cSecHighHgMonitorAlarmType_Type()
)
hh3cSecHighHgMonitorAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmType.setStatus("current")
_Hh3cSecHighHgMonitorAlarmSrcChassis_Type = Integer32
_Hh3cSecHighHgMonitorAlarmSrcChassis_Object = MibScalar
hh3cSecHighHgMonitorAlarmSrcChassis = _Hh3cSecHighHgMonitorAlarmSrcChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 2),
    _Hh3cSecHighHgMonitorAlarmSrcChassis_Type()
)
hh3cSecHighHgMonitorAlarmSrcChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmSrcChassis.setStatus("current")
_Hh3cSecHighHgMonitorAlarmSrcSlot_Type = Integer32
_Hh3cSecHighHgMonitorAlarmSrcSlot_Object = MibScalar
hh3cSecHighHgMonitorAlarmSrcSlot = _Hh3cSecHighHgMonitorAlarmSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 3),
    _Hh3cSecHighHgMonitorAlarmSrcSlot_Type()
)
hh3cSecHighHgMonitorAlarmSrcSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmSrcSlot.setStatus("current")
_Hh3cSecHighHgMonitorAlarmSrcChip_Type = Integer32
_Hh3cSecHighHgMonitorAlarmSrcChip_Object = MibScalar
hh3cSecHighHgMonitorAlarmSrcChip = _Hh3cSecHighHgMonitorAlarmSrcChip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 4),
    _Hh3cSecHighHgMonitorAlarmSrcChip_Type()
)
hh3cSecHighHgMonitorAlarmSrcChip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmSrcChip.setStatus("current")
_Hh3cSecHighHgMonitorAlarmSrcPort_Type = Integer32
_Hh3cSecHighHgMonitorAlarmSrcPort_Object = MibScalar
hh3cSecHighHgMonitorAlarmSrcPort = _Hh3cSecHighHgMonitorAlarmSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 5),
    _Hh3cSecHighHgMonitorAlarmSrcPort_Type()
)
hh3cSecHighHgMonitorAlarmSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmSrcPort.setStatus("current")
_Hh3cSecHighHgMonitorAlarmDstChassis_Type = Integer32
_Hh3cSecHighHgMonitorAlarmDstChassis_Object = MibScalar
hh3cSecHighHgMonitorAlarmDstChassis = _Hh3cSecHighHgMonitorAlarmDstChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 6),
    _Hh3cSecHighHgMonitorAlarmDstChassis_Type()
)
hh3cSecHighHgMonitorAlarmDstChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmDstChassis.setStatus("current")
_Hh3cSecHighHgMonitorAlarmDstSlot_Type = Integer32
_Hh3cSecHighHgMonitorAlarmDstSlot_Object = MibScalar
hh3cSecHighHgMonitorAlarmDstSlot = _Hh3cSecHighHgMonitorAlarmDstSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 7),
    _Hh3cSecHighHgMonitorAlarmDstSlot_Type()
)
hh3cSecHighHgMonitorAlarmDstSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmDstSlot.setStatus("current")
_Hh3cSecHighHgMonitorAlarmDstChip_Type = Integer32
_Hh3cSecHighHgMonitorAlarmDstChip_Object = MibScalar
hh3cSecHighHgMonitorAlarmDstChip = _Hh3cSecHighHgMonitorAlarmDstChip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 8),
    _Hh3cSecHighHgMonitorAlarmDstChip_Type()
)
hh3cSecHighHgMonitorAlarmDstChip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmDstChip.setStatus("current")
_Hh3cSecHighHgMonitorAlarmDstPort_Type = Integer32
_Hh3cSecHighHgMonitorAlarmDstPort_Object = MibScalar
hh3cSecHighHgMonitorAlarmDstPort = _Hh3cSecHighHgMonitorAlarmDstPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 9),
    _Hh3cSecHighHgMonitorAlarmDstPort_Type()
)
hh3cSecHighHgMonitorAlarmDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmDstPort.setStatus("current")


class _Hh3cSecHighHgMonitorAlarmReason_Type(OctetString):
    """Custom type hh3cSecHighHgMonitorAlarmReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Hh3cSecHighHgMonitorAlarmReason_Type.__name__ = "OctetString"
_Hh3cSecHighHgMonitorAlarmReason_Object = MibScalar
hh3cSecHighHgMonitorAlarmReason = _Hh3cSecHighHgMonitorAlarmReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 1, 10),
    _Hh3cSecHighHgMonitorAlarmReason_Type()
)
hh3cSecHighHgMonitorAlarmReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmReason.setStatus("current")
_Hh3cSecHighHgMonitorAlarmTrap_ObjectIdentity = ObjectIdentity
hh3cSecHighHgMonitorAlarmTrap = _Hh3cSecHighHgMonitorAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 2)
)
_Hh3cSecHighHgMonitorAlarmNotifications_ObjectIdentity = ObjectIdentity
hh3cSecHighHgMonitorAlarmNotifications = _Hh3cSecHighHgMonitorAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 2, 0)
)
_Hh3cSecHighFaultMonitor_ObjectIdentity = ObjectIdentity
hh3cSecHighFaultMonitor = _Hh3cSecHighFaultMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3)
)
_Hh3cSecHighFaultAlmVar_ObjectIdentity = ObjectIdentity
hh3cSecHighFaultAlmVar = _Hh3cSecHighFaultAlmVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1)
)
_Hh3cSecHighFaultAlmType_Type = Integer32
_Hh3cSecHighFaultAlmType_Object = MibScalar
hh3cSecHighFaultAlmType = _Hh3cSecHighFaultAlmType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1, 1),
    _Hh3cSecHighFaultAlmType_Type()
)
hh3cSecHighFaultAlmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighFaultAlmType.setStatus("current")
_Hh3cSecHighFaultAlmChassis_Type = Integer32
_Hh3cSecHighFaultAlmChassis_Object = MibScalar
hh3cSecHighFaultAlmChassis = _Hh3cSecHighFaultAlmChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1, 2),
    _Hh3cSecHighFaultAlmChassis_Type()
)
hh3cSecHighFaultAlmChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighFaultAlmChassis.setStatus("current")
_Hh3cSecHighFaultAlmSlot_Type = Integer32
_Hh3cSecHighFaultAlmSlot_Object = MibScalar
hh3cSecHighFaultAlmSlot = _Hh3cSecHighFaultAlmSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1, 3),
    _Hh3cSecHighFaultAlmSlot_Type()
)
hh3cSecHighFaultAlmSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighFaultAlmSlot.setStatus("current")
_Hh3cSecHighFaultAlmDstChassis_Type = Integer32
_Hh3cSecHighFaultAlmDstChassis_Object = MibScalar
hh3cSecHighFaultAlmDstChassis = _Hh3cSecHighFaultAlmDstChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1, 4),
    _Hh3cSecHighFaultAlmDstChassis_Type()
)
hh3cSecHighFaultAlmDstChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighFaultAlmDstChassis.setStatus("current")
_Hh3cSecHighFaultAlmDstSlot_Type = Integer32
_Hh3cSecHighFaultAlmDstSlot_Object = MibScalar
hh3cSecHighFaultAlmDstSlot = _Hh3cSecHighFaultAlmDstSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1, 5),
    _Hh3cSecHighFaultAlmDstSlot_Type()
)
hh3cSecHighFaultAlmDstSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighFaultAlmDstSlot.setStatus("current")
_Hh3cSecHighFaultAlmChip_Type = Integer32
_Hh3cSecHighFaultAlmChip_Object = MibScalar
hh3cSecHighFaultAlmChip = _Hh3cSecHighFaultAlmChip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1, 6),
    _Hh3cSecHighFaultAlmChip_Type()
)
hh3cSecHighFaultAlmChip.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighFaultAlmChip.setStatus("current")


class _Hh3cSecHighFaultAlmInfo_Type(OctetString):
    """Custom type hh3cSecHighFaultAlmInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Hh3cSecHighFaultAlmInfo_Type.__name__ = "OctetString"
_Hh3cSecHighFaultAlmInfo_Object = MibScalar
hh3cSecHighFaultAlmInfo = _Hh3cSecHighFaultAlmInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 1, 7),
    _Hh3cSecHighFaultAlmInfo_Type()
)
hh3cSecHighFaultAlmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighFaultAlmInfo.setStatus("current")
_Hh3cSecHighFaultAlmTrap_ObjectIdentity = ObjectIdentity
hh3cSecHighFaultAlmTrap = _Hh3cSecHighFaultAlmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 2)
)
_Hh3cSecHighFaultAlmTrapPre_ObjectIdentity = ObjectIdentity
hh3cSecHighFaultAlmTrapPre = _Hh3cSecHighFaultAlmTrapPre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 2, 0)
)
_Hh3cSecHighTemperMonitor_ObjectIdentity = ObjectIdentity
hh3cSecHighTemperMonitor = _Hh3cSecHighTemperMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2)
)
_Hh3cSecHighTemperAlarmVar_ObjectIdentity = ObjectIdentity
hh3cSecHighTemperAlarmVar = _Hh3cSecHighTemperAlarmVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 1)
)
_Hh3cSecHighTemperAlarmChassis_Type = Integer32
_Hh3cSecHighTemperAlarmChassis_Object = MibScalar
hh3cSecHighTemperAlarmChassis = _Hh3cSecHighTemperAlarmChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 1, 1),
    _Hh3cSecHighTemperAlarmChassis_Type()
)
hh3cSecHighTemperAlarmChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighTemperAlarmChassis.setStatus("current")
_Hh3cSecHighTemperAlarmSlot_Type = Integer32
_Hh3cSecHighTemperAlarmSlot_Object = MibScalar
hh3cSecHighTemperAlarmSlot = _Hh3cSecHighTemperAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 1, 2),
    _Hh3cSecHighTemperAlarmSlot_Type()
)
hh3cSecHighTemperAlarmSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighTemperAlarmSlot.setStatus("current")
_Hh3cSecHighTemperAlarmHotspotIndx_Type = Integer32
_Hh3cSecHighTemperAlarmHotspotIndx_Object = MibScalar
hh3cSecHighTemperAlarmHotspotIndx = _Hh3cSecHighTemperAlarmHotspotIndx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 1, 3),
    _Hh3cSecHighTemperAlarmHotspotIndx_Type()
)
hh3cSecHighTemperAlarmHotspotIndx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighTemperAlarmHotspotIndx.setStatus("current")
_Hh3cSecHighTemperAlarmCurTemper_Type = Integer32
_Hh3cSecHighTemperAlarmCurTemper_Object = MibScalar
hh3cSecHighTemperAlarmCurTemper = _Hh3cSecHighTemperAlarmCurTemper_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 1, 4),
    _Hh3cSecHighTemperAlarmCurTemper_Type()
)
hh3cSecHighTemperAlarmCurTemper.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighTemperAlarmCurTemper.setStatus("current")
_Hh3cSecHighTemperAlarmLimit_Type = Integer32
_Hh3cSecHighTemperAlarmLimit_Object = MibScalar
hh3cSecHighTemperAlarmLimit = _Hh3cSecHighTemperAlarmLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 1, 5),
    _Hh3cSecHighTemperAlarmLimit_Type()
)
hh3cSecHighTemperAlarmLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighTemperAlarmLimit.setStatus("current")
_Hh3cSecHighTemperAlarmTrap_ObjectIdentity = ObjectIdentity
hh3cSecHighTemperAlarmTrap = _Hh3cSecHighTemperAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 2)
)
_Hh3cSecHighTemperAlmTrapPre_ObjectIdentity = ObjectIdentity
hh3cSecHighTemperAlmTrapPre = _Hh3cSecHighTemperAlmTrapPre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 2, 0)
)
_Hh3cSecHighParityErrorMonitor_ObjectIdentity = ObjectIdentity
hh3cSecHighParityErrorMonitor = _Hh3cSecHighParityErrorMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3)
)
_Hh3cSecHighParityErrorAlarmVar_ObjectIdentity = ObjectIdentity
hh3cSecHighParityErrorAlarmVar = _Hh3cSecHighParityErrorAlarmVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3, 1)
)
_Hh3cSecHighParityErrorAlarmChassis_Type = Integer32
_Hh3cSecHighParityErrorAlarmChassis_Object = MibScalar
hh3cSecHighParityErrorAlarmChassis = _Hh3cSecHighParityErrorAlarmChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3, 1, 1),
    _Hh3cSecHighParityErrorAlarmChassis_Type()
)
hh3cSecHighParityErrorAlarmChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighParityErrorAlarmChassis.setStatus("current")
_Hh3cSecHighParityErrorAlarmSlot_Type = Integer32
_Hh3cSecHighParityErrorAlarmSlot_Object = MibScalar
hh3cSecHighParityErrorAlarmSlot = _Hh3cSecHighParityErrorAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3, 1, 2),
    _Hh3cSecHighParityErrorAlarmSlot_Type()
)
hh3cSecHighParityErrorAlarmSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighParityErrorAlarmSlot.setStatus("current")
_Hh3cSecHighParityErrorAlarmChipUnit_Type = Integer32
_Hh3cSecHighParityErrorAlarmChipUnit_Object = MibScalar
hh3cSecHighParityErrorAlarmChipUnit = _Hh3cSecHighParityErrorAlarmChipUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3, 1, 3),
    _Hh3cSecHighParityErrorAlarmChipUnit_Type()
)
hh3cSecHighParityErrorAlarmChipUnit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecHighParityErrorAlarmChipUnit.setStatus("current")
_Hh3cSecHighParityErrorAlarmTrap_ObjectIdentity = ObjectIdentity
hh3cSecHighParityErrorAlarmTrap = _Hh3cSecHighParityErrorAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3, 2)
)
_Hh3cSecHighParityErrorAlarmTrapPre_ObjectIdentity = ObjectIdentity
hh3cSecHighParityErrorAlarmTrapPre = _Hh3cSecHighParityErrorAlarmTrapPre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cSecHighHgMonitorAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 2, 0, 1)
)
hh3cSecHighHgMonitorAlarmNotification.setObjects(
      *(("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmType"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmSrcChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmSrcSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmSrcChip"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmSrcPort"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmDstChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmDstSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmDstChip"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmDstPort"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighHgMonitorAlarmReason"))
)
if mibBuilder.loadTexts:
    hh3cSecHighHgMonitorAlarmNotification.setStatus(
        "current"
    )

hh3cSecHighFaultMonChipAlmNotifi = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 2, 0, 1)
)
hh3cSecHighFaultMonChipAlmNotifi.setObjects(
      *(("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmType"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmChip"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmInfo"))
)
if mibBuilder.loadTexts:
    hh3cSecHighFaultMonChipAlmNotifi.setStatus(
        "current"
    )

hh3cSecHighFaultMonChipAlmResu = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 2, 0, 2)
)
hh3cSecHighFaultMonChipAlmResu.setObjects(
      *(("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmType"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmChip"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmInfo"))
)
if mibBuilder.loadTexts:
    hh3cSecHighFaultMonChipAlmResu.setStatus(
        "current"
    )

hh3cSecHighFaultMonHgAlmNotifi = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 2, 0, 3)
)
hh3cSecHighFaultMonHgAlmNotifi.setObjects(
      *(("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmType"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmDstChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmDstSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmInfo"))
)
if mibBuilder.loadTexts:
    hh3cSecHighFaultMonHgAlmNotifi.setStatus(
        "current"
    )

hh3cSecHighFaultMonHgAlmResu = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 1, 3, 2, 0, 4)
)
hh3cSecHighFaultMonHgAlmResu.setObjects(
      *(("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmType"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmDstChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmDstSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighFaultAlmInfo"))
)
if mibBuilder.loadTexts:
    hh3cSecHighFaultMonHgAlmResu.setStatus(
        "current"
    )

hh3cSecHighTemperAlarmNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 2, 2, 0, 1)
)
hh3cSecHighTemperAlarmNotify.setObjects(
      *(("HH3C-SECHIGH-MIB", "hh3cSecHighTemperAlarmChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighTemperAlarmSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighTemperAlarmHotspotIndx"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighTemperAlarmCurTemper"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighTemperAlarmLimit"))
)
if mibBuilder.loadTexts:
    hh3cSecHighTemperAlarmNotify.setStatus(
        "current"
    )

hh3cSecHighParityErrorAlarmNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 171, 3, 2, 0, 1)
)
hh3cSecHighParityErrorAlarmNotify.setObjects(
      *(("HH3C-SECHIGH-MIB", "hh3cSecHighParityErrorAlarmChassis"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighParityErrorAlarmSlot"),
        ("HH3C-SECHIGH-MIB", "hh3cSecHighParityErrorAlarmChipUnit"))
)
if mibBuilder.loadTexts:
    hh3cSecHighParityErrorAlarmNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SECHIGH-MIB",
    **{"hh3cSecHigh": hh3cSecHigh,
       "hh3cSecHighMonitor": hh3cSecHighMonitor,
       "hh3cSecHighHgMonitorAlarmVar": hh3cSecHighHgMonitorAlarmVar,
       "hh3cSecHighHgMonitorAlarmType": hh3cSecHighHgMonitorAlarmType,
       "hh3cSecHighHgMonitorAlarmSrcChassis": hh3cSecHighHgMonitorAlarmSrcChassis,
       "hh3cSecHighHgMonitorAlarmSrcSlot": hh3cSecHighHgMonitorAlarmSrcSlot,
       "hh3cSecHighHgMonitorAlarmSrcChip": hh3cSecHighHgMonitorAlarmSrcChip,
       "hh3cSecHighHgMonitorAlarmSrcPort": hh3cSecHighHgMonitorAlarmSrcPort,
       "hh3cSecHighHgMonitorAlarmDstChassis": hh3cSecHighHgMonitorAlarmDstChassis,
       "hh3cSecHighHgMonitorAlarmDstSlot": hh3cSecHighHgMonitorAlarmDstSlot,
       "hh3cSecHighHgMonitorAlarmDstChip": hh3cSecHighHgMonitorAlarmDstChip,
       "hh3cSecHighHgMonitorAlarmDstPort": hh3cSecHighHgMonitorAlarmDstPort,
       "hh3cSecHighHgMonitorAlarmReason": hh3cSecHighHgMonitorAlarmReason,
       "hh3cSecHighHgMonitorAlarmTrap": hh3cSecHighHgMonitorAlarmTrap,
       "hh3cSecHighHgMonitorAlarmNotifications": hh3cSecHighHgMonitorAlarmNotifications,
       "hh3cSecHighHgMonitorAlarmNotification": hh3cSecHighHgMonitorAlarmNotification,
       "hh3cSecHighFaultMonitor": hh3cSecHighFaultMonitor,
       "hh3cSecHighFaultAlmVar": hh3cSecHighFaultAlmVar,
       "hh3cSecHighFaultAlmType": hh3cSecHighFaultAlmType,
       "hh3cSecHighFaultAlmChassis": hh3cSecHighFaultAlmChassis,
       "hh3cSecHighFaultAlmSlot": hh3cSecHighFaultAlmSlot,
       "hh3cSecHighFaultAlmDstChassis": hh3cSecHighFaultAlmDstChassis,
       "hh3cSecHighFaultAlmDstSlot": hh3cSecHighFaultAlmDstSlot,
       "hh3cSecHighFaultAlmChip": hh3cSecHighFaultAlmChip,
       "hh3cSecHighFaultAlmInfo": hh3cSecHighFaultAlmInfo,
       "hh3cSecHighFaultAlmTrap": hh3cSecHighFaultAlmTrap,
       "hh3cSecHighFaultAlmTrapPre": hh3cSecHighFaultAlmTrapPre,
       "hh3cSecHighFaultMonChipAlmNotifi": hh3cSecHighFaultMonChipAlmNotifi,
       "hh3cSecHighFaultMonChipAlmResu": hh3cSecHighFaultMonChipAlmResu,
       "hh3cSecHighFaultMonHgAlmNotifi": hh3cSecHighFaultMonHgAlmNotifi,
       "hh3cSecHighFaultMonHgAlmResu": hh3cSecHighFaultMonHgAlmResu,
       "hh3cSecHighTemperMonitor": hh3cSecHighTemperMonitor,
       "hh3cSecHighTemperAlarmVar": hh3cSecHighTemperAlarmVar,
       "hh3cSecHighTemperAlarmChassis": hh3cSecHighTemperAlarmChassis,
       "hh3cSecHighTemperAlarmSlot": hh3cSecHighTemperAlarmSlot,
       "hh3cSecHighTemperAlarmHotspotIndx": hh3cSecHighTemperAlarmHotspotIndx,
       "hh3cSecHighTemperAlarmCurTemper": hh3cSecHighTemperAlarmCurTemper,
       "hh3cSecHighTemperAlarmLimit": hh3cSecHighTemperAlarmLimit,
       "hh3cSecHighTemperAlarmTrap": hh3cSecHighTemperAlarmTrap,
       "hh3cSecHighTemperAlmTrapPre": hh3cSecHighTemperAlmTrapPre,
       "hh3cSecHighTemperAlarmNotify": hh3cSecHighTemperAlarmNotify,
       "hh3cSecHighParityErrorMonitor": hh3cSecHighParityErrorMonitor,
       "hh3cSecHighParityErrorAlarmVar": hh3cSecHighParityErrorAlarmVar,
       "hh3cSecHighParityErrorAlarmChassis": hh3cSecHighParityErrorAlarmChassis,
       "hh3cSecHighParityErrorAlarmSlot": hh3cSecHighParityErrorAlarmSlot,
       "hh3cSecHighParityErrorAlarmChipUnit": hh3cSecHighParityErrorAlarmChipUnit,
       "hh3cSecHighParityErrorAlarmTrap": hh3cSecHighParityErrorAlarmTrap,
       "hh3cSecHighParityErrorAlarmTrapPre": hh3cSecHighParityErrorAlarmTrapPre,
       "hh3cSecHighParityErrorAlarmNotify": hh3cSecHighParityErrorAlarmNotify}
)
