# SNMP MIB module (RUCKUS-UNLEASHED-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-UNLEASHED-EVENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:54 2025
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

(ruckusEvents,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusEvents")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruckusUnleashedEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusUnleashedEventTraps_ObjectIdentity = ObjectIdentity
ruckusUnleashedEventTraps = _RuckusUnleashedEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1)
)
_RuckusUnleashedEventObjects_ObjectIdentity = ObjectIdentity
ruckusUnleashedEventObjects = _RuckusUnleashedEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2)
)
_RuckusUnleashedEventSerial_Type = OctetString
_RuckusUnleashedEventSerial_Object = MibScalar
ruckusUnleashedEventSerial = _RuckusUnleashedEventSerial_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 1),
    _RuckusUnleashedEventSerial_Type()
)
ruckusUnleashedEventSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventSerial.setStatus("current")
_RuckusUnleashedEventNEID_Type = OctetString
_RuckusUnleashedEventNEID_Object = MibScalar
ruckusUnleashedEventNEID = _RuckusUnleashedEventNEID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 2),
    _RuckusUnleashedEventNEID_Type()
)
ruckusUnleashedEventNEID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventNEID.setStatus("current")
_RuckusUnleashedEventSeverity_Type = OctetString
_RuckusUnleashedEventSeverity_Object = MibScalar
ruckusUnleashedEventSeverity = _RuckusUnleashedEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 3),
    _RuckusUnleashedEventSeverity_Type()
)
ruckusUnleashedEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventSeverity.setStatus("current")
_RuckusUnleashedEventType_Type = OctetString
_RuckusUnleashedEventType_Object = MibScalar
ruckusUnleashedEventType = _RuckusUnleashedEventType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 4),
    _RuckusUnleashedEventType_Type()
)
ruckusUnleashedEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventType.setStatus("current")
_RuckusUnleashedEventTime_Type = OctetString
_RuckusUnleashedEventTime_Object = MibScalar
ruckusUnleashedEventTime = _RuckusUnleashedEventTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 5),
    _RuckusUnleashedEventTime_Type()
)
ruckusUnleashedEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventTime.setStatus("current")


class _RuckusUnleashedEventStatus_Type(Integer32):
    """Custom type ruckusUnleashedEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raise", 1),
          ("clear", 2))
    )


_RuckusUnleashedEventStatus_Type.__name__ = "Integer32"
_RuckusUnleashedEventStatus_Object = MibScalar
ruckusUnleashedEventStatus = _RuckusUnleashedEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 6),
    _RuckusUnleashedEventStatus_Type()
)
ruckusUnleashedEventStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventStatus.setStatus("current")
_RuckusUnleashedEventTitle_Type = OctetString
_RuckusUnleashedEventTitle_Object = MibScalar
ruckusUnleashedEventTitle = _RuckusUnleashedEventTitle_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 7),
    _RuckusUnleashedEventTitle_Type()
)
ruckusUnleashedEventTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventTitle.setStatus("current")
_RuckusUnleashedEventContent_Type = OctetString
_RuckusUnleashedEventContent_Object = MibScalar
ruckusUnleashedEventContent = _RuckusUnleashedEventContent_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 8),
    _RuckusUnleashedEventContent_Type()
)
ruckusUnleashedEventContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventContent.setStatus("current")
_RuckusUnleashedEventOccurTime_Type = OctetString
_RuckusUnleashedEventOccurTime_Object = MibScalar
ruckusUnleashedEventOccurTime = _RuckusUnleashedEventOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 10),
    _RuckusUnleashedEventOccurTime_Type()
)
ruckusUnleashedEventOccurTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventOccurTime.setStatus("current")
_RuckusUnleashedEventAPRadioIndex_Type = OctetString
_RuckusUnleashedEventAPRadioIndex_Object = MibScalar
ruckusUnleashedEventAPRadioIndex = _RuckusUnleashedEventAPRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 11),
    _RuckusUnleashedEventAPRadioIndex_Type()
)
ruckusUnleashedEventAPRadioIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPRadioIndex.setStatus("current")
_RuckusUnleashedEventClientMacAddr_Type = OctetString
_RuckusUnleashedEventClientMacAddr_Object = MibScalar
ruckusUnleashedEventClientMacAddr = _RuckusUnleashedEventClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 15),
    _RuckusUnleashedEventClientMacAddr_Type()
)
ruckusUnleashedEventClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventClientMacAddr.setStatus("current")
_RuckusUnleashedEventAPMacAddr_Type = OctetString
_RuckusUnleashedEventAPMacAddr_Object = MibScalar
ruckusUnleashedEventAPMacAddr = _RuckusUnleashedEventAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 18),
    _RuckusUnleashedEventAPMacAddr_Type()
)
ruckusUnleashedEventAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPMacAddr.setStatus("current")
_RuckusUnleashedEventSSID_Type = OctetString
_RuckusUnleashedEventSSID_Object = MibScalar
ruckusUnleashedEventSSID = _RuckusUnleashedEventSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 23),
    _RuckusUnleashedEventSSID_Type()
)
ruckusUnleashedEventSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventSSID.setStatus("current")
_RuckusUnleashedEventIpAddr_Type = OctetString
_RuckusUnleashedEventIpAddr_Object = MibScalar
ruckusUnleashedEventIpAddr = _RuckusUnleashedEventIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 2, 30),
    _RuckusUnleashedEventIpAddr_Type()
)
ruckusUnleashedEventIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusUnleashedEventIpAddr.setStatus("current")
_RuckusUnleashedEventTrapSwitchCmd_ObjectIdentity = ObjectIdentity
ruckusUnleashedEventTrapSwitchCmd = _RuckusUnleashedEventTrapSwitchCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3)
)


class _RuckusUnleashedEventAPJoinTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusUnleashedEventAPJoinTrapSwitchCmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusUnleashedEventAPJoinTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusUnleashedEventAPJoinTrapSwitchCmd_Object = MibScalar
ruckusUnleashedEventAPJoinTrapSwitchCmd = _RuckusUnleashedEventAPJoinTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3, 1),
    _RuckusUnleashedEventAPJoinTrapSwitchCmd_Type()
)
ruckusUnleashedEventAPJoinTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPJoinTrapSwitchCmd.setStatus("current")


class _RuckusUnleashedEventAPLostTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusUnleashedEventAPLostTrapSwitchCmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusUnleashedEventAPLostTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusUnleashedEventAPLostTrapSwitchCmd_Object = MibScalar
ruckusUnleashedEventAPLostTrapSwitchCmd = _RuckusUnleashedEventAPLostTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3, 5),
    _RuckusUnleashedEventAPLostTrapSwitchCmd_Type()
)
ruckusUnleashedEventAPLostTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPLostTrapSwitchCmd.setStatus("current")


class _RuckusUnleashedEventAPSystemColdStartTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusUnleashedEventAPSystemColdStartTrapSwitchCmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusUnleashedEventAPSystemColdStartTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusUnleashedEventAPSystemColdStartTrapSwitchCmd_Object = MibScalar
ruckusUnleashedEventAPSystemColdStartTrapSwitchCmd = _RuckusUnleashedEventAPSystemColdStartTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3, 31),
    _RuckusUnleashedEventAPSystemColdStartTrapSwitchCmd_Type()
)
ruckusUnleashedEventAPSystemColdStartTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPSystemColdStartTrapSwitchCmd.setStatus("current")


class _RuckusUnleashedEventAPSystemWarmStartTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusUnleashedEventAPSystemWarmStartTrapSwitchCmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusUnleashedEventAPSystemWarmStartTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusUnleashedEventAPSystemWarmStartTrapSwitchCmd_Object = MibScalar
ruckusUnleashedEventAPSystemWarmStartTrapSwitchCmd = _RuckusUnleashedEventAPSystemWarmStartTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3, 32),
    _RuckusUnleashedEventAPSystemWarmStartTrapSwitchCmd_Type()
)
ruckusUnleashedEventAPSystemWarmStartTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPSystemWarmStartTrapSwitchCmd.setStatus("current")


class _RuckusUnleashedEventAPRadioOnTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusUnleashedEventAPRadioOnTrapSwitchCmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusUnleashedEventAPRadioOnTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusUnleashedEventAPRadioOnTrapSwitchCmd_Object = MibScalar
ruckusUnleashedEventAPRadioOnTrapSwitchCmd = _RuckusUnleashedEventAPRadioOnTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3, 130),
    _RuckusUnleashedEventAPRadioOnTrapSwitchCmd_Type()
)
ruckusUnleashedEventAPRadioOnTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPRadioOnTrapSwitchCmd.setStatus("current")


class _RuckusUnleashedEventAPRadioOffTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusUnleashedEventAPRadioOffTrapSwitchCmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusUnleashedEventAPRadioOffTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusUnleashedEventAPRadioOffTrapSwitchCmd_Object = MibScalar
ruckusUnleashedEventAPRadioOffTrapSwitchCmd = _RuckusUnleashedEventAPRadioOffTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3, 131),
    _RuckusUnleashedEventAPRadioOffTrapSwitchCmd_Type()
)
ruckusUnleashedEventAPRadioOffTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPRadioOffTrapSwitchCmd.setStatus("current")


class _RuckusUnleashedEventMasterAPSwitchTrapSwitchCmd_Type(Integer32):
    """Custom type ruckusUnleashedEventMasterAPSwitchTrapSwitchCmd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RuckusUnleashedEventMasterAPSwitchTrapSwitchCmd_Type.__name__ = "Integer32"
_RuckusUnleashedEventMasterAPSwitchTrapSwitchCmd_Object = MibScalar
ruckusUnleashedEventMasterAPSwitchTrapSwitchCmd = _RuckusUnleashedEventMasterAPSwitchTrapSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 3, 138),
    _RuckusUnleashedEventMasterAPSwitchTrapSwitchCmd_Type()
)
ruckusUnleashedEventMasterAPSwitchTrapSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusUnleashedEventMasterAPSwitchTrapSwitchCmd.setStatus("current")

# Managed Objects groups


# Notification objects

ruckusUnleashedEventAPJoinTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1, 1)
)
ruckusUnleashedEventAPJoinTrap.setObjects(
      *(("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSerial"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventNEID"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSeverity"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventType"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTime"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventStatus"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTitle"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPJoinTrap.setStatus(
        "current"
    )

ruckusUnleashedEventAPLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1, 5)
)
ruckusUnleashedEventAPLostTrap.setObjects(
      *(("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSerial"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventNEID"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSeverity"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventType"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTime"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventStatus"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTitle"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPMacAddr"))
)
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPLostTrap.setStatus(
        "current"
    )

ruckusUnleashedEventAPSystemColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1, 31)
)
ruckusUnleashedEventAPSystemColdStartTrap.setObjects(
      *(("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSerial"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventNEID"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSeverity"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventType"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTime"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventStatus"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTitle"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPMacAddr"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventOccurTime"))
)
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPSystemColdStartTrap.setStatus(
        "current"
    )

ruckusUnleashedEventAPSystemWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1, 32)
)
ruckusUnleashedEventAPSystemWarmStartTrap.setObjects(
      *(("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSerial"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventNEID"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSeverity"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventType"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTime"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventStatus"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTitle"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPMacAddr"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventOccurTime"))
)
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPSystemWarmStartTrap.setStatus(
        "current"
    )

ruckusUnleashedEventAPRadioOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1, 130)
)
ruckusUnleashedEventAPRadioOn.setObjects(
      *(("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSerial"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventNEID"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSeverity"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventType"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTime"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventStatus"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTitle"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPMacAddr"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPRadioIndex"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventOccurTime"))
)
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPRadioOn.setStatus(
        "current"
    )

ruckusUnleashedEventAPRadioOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1, 131)
)
ruckusUnleashedEventAPRadioOff.setObjects(
      *(("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSerial"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventNEID"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSeverity"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventType"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTime"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventStatus"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTitle"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPMacAddr"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventAPRadioIndex"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventOccurTime"))
)
if mibBuilder.loadTexts:
    ruckusUnleashedEventAPRadioOff.setStatus(
        "current"
    )

ruckusUnleashedEventMasterAPSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 15, 1, 138)
)
ruckusUnleashedEventMasterAPSwitch.setObjects(
      *(("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSerial"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventNEID"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventSeverity"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventType"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTime"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventStatus"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventTitle"),
        ("RUCKUS-UNLEASHED-EVENT-MIB", "ruckusUnleashedEventContent"))
)
if mibBuilder.loadTexts:
    ruckusUnleashedEventMasterAPSwitch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-UNLEASHED-EVENT-MIB",
    **{"ruckusUnleashedEventMIB": ruckusUnleashedEventMIB,
       "ruckusUnleashedEventTraps": ruckusUnleashedEventTraps,
       "ruckusUnleashedEventAPJoinTrap": ruckusUnleashedEventAPJoinTrap,
       "ruckusUnleashedEventAPLostTrap": ruckusUnleashedEventAPLostTrap,
       "ruckusUnleashedEventAPSystemColdStartTrap": ruckusUnleashedEventAPSystemColdStartTrap,
       "ruckusUnleashedEventAPSystemWarmStartTrap": ruckusUnleashedEventAPSystemWarmStartTrap,
       "ruckusUnleashedEventAPRadioOn": ruckusUnleashedEventAPRadioOn,
       "ruckusUnleashedEventAPRadioOff": ruckusUnleashedEventAPRadioOff,
       "ruckusUnleashedEventMasterAPSwitch": ruckusUnleashedEventMasterAPSwitch,
       "ruckusUnleashedEventObjects": ruckusUnleashedEventObjects,
       "ruckusUnleashedEventSerial": ruckusUnleashedEventSerial,
       "ruckusUnleashedEventNEID": ruckusUnleashedEventNEID,
       "ruckusUnleashedEventSeverity": ruckusUnleashedEventSeverity,
       "ruckusUnleashedEventType": ruckusUnleashedEventType,
       "ruckusUnleashedEventTime": ruckusUnleashedEventTime,
       "ruckusUnleashedEventStatus": ruckusUnleashedEventStatus,
       "ruckusUnleashedEventTitle": ruckusUnleashedEventTitle,
       "ruckusUnleashedEventContent": ruckusUnleashedEventContent,
       "ruckusUnleashedEventOccurTime": ruckusUnleashedEventOccurTime,
       "ruckusUnleashedEventAPRadioIndex": ruckusUnleashedEventAPRadioIndex,
       "ruckusUnleashedEventClientMacAddr": ruckusUnleashedEventClientMacAddr,
       "ruckusUnleashedEventAPMacAddr": ruckusUnleashedEventAPMacAddr,
       "ruckusUnleashedEventSSID": ruckusUnleashedEventSSID,
       "ruckusUnleashedEventIpAddr": ruckusUnleashedEventIpAddr,
       "ruckusUnleashedEventTrapSwitchCmd": ruckusUnleashedEventTrapSwitchCmd,
       "ruckusUnleashedEventAPJoinTrapSwitchCmd": ruckusUnleashedEventAPJoinTrapSwitchCmd,
       "ruckusUnleashedEventAPLostTrapSwitchCmd": ruckusUnleashedEventAPLostTrapSwitchCmd,
       "ruckusUnleashedEventAPSystemColdStartTrapSwitchCmd": ruckusUnleashedEventAPSystemColdStartTrapSwitchCmd,
       "ruckusUnleashedEventAPSystemWarmStartTrapSwitchCmd": ruckusUnleashedEventAPSystemWarmStartTrapSwitchCmd,
       "ruckusUnleashedEventAPRadioOnTrapSwitchCmd": ruckusUnleashedEventAPRadioOnTrapSwitchCmd,
       "ruckusUnleashedEventAPRadioOffTrapSwitchCmd": ruckusUnleashedEventAPRadioOffTrapSwitchCmd,
       "ruckusUnleashedEventMasterAPSwitchTrapSwitchCmd": ruckusUnleashedEventMasterAPSwitchTrapSwitchCmd}
)
