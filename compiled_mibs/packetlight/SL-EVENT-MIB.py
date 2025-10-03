# SNMP MIB module (SL-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-EVENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:50 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

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
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlGenEventType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swUpgradeEvent", 1),
          ("remoteUnitFailEvent", 2),
          ("alsOperStatus", 3))
    )



class SlEventType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("edDate", 1),
          ("rstProv", 2),
          ("edIp", 3),
          ("initPm", 4),
          ("dltIpRoute", 5),
          ("edSys", 6),
          ("setSid", 7),
          ("addUser", 8),
          ("dltUser", 9),
          ("rmvFac", 10),
          ("rstFac", 11),
          ("edFac", 12),
          ("oprLoopback", 13),
          ("rlsLoopback", 14),
          ("entAps", 15),
          ("dltAps", 16),
          ("oprProtSw", 17),
          ("rlsProtSw", 18),
          ("oprAco", 19),
          ("rstProvCommit", 20),
          ("savProvStart", 21),
          ("savProvComplete", 22),
          ("savProvFailed", 23),
          ("swLoadUpgrade", 24))
    )



class SlEventInventoryAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("removed", 2))
    )



class SlEventInventoryType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("psu", 1),
          ("optics", 2),
          ("fan", 3))
    )



# MIB Managed Objects in the order of their OIDs

_SlEventConfig_ObjectIdentity = ObjectIdentity
slEventConfig = _SlEventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1)
)
_SlEventConfigTable_Object = MibTable
slEventConfigTable = _SlEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1)
)
if mibBuilder.loadTexts:
    slEventConfigTable.setStatus("current")
_SlEventConfigEntry_Object = MibTableRow
slEventConfigEntry = _SlEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1)
)
slEventConfigEntry.setIndexNames(
    (0, "SL-EVENT-MIB", "slEventIfIndex"),
    (0, "SL-EVENT-MIB", "slEventType"),
)
if mibBuilder.loadTexts:
    slEventConfigEntry.setStatus("current")
_SlEventIfIndex_Type = InterfaceIndex
_SlEventIfIndex_Object = MibTableColumn
slEventIfIndex = _SlEventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 1),
    _SlEventIfIndex_Type()
)
slEventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEventIfIndex.setStatus("current")
_SlEventType_Type = SlEventType
_SlEventType_Object = MibTableColumn
slEventType = _SlEventType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 2),
    _SlEventType_Type()
)
slEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEventType.setStatus("current")


class _SlEventVal_Type(DisplayString):
    """Custom type slEventVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlEventVal_Type.__name__ = "DisplayString"
_SlEventVal_Object = MibTableColumn
slEventVal = _SlEventVal_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 3),
    _SlEventVal_Type()
)
slEventVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEventVal.setStatus("current")


class _SlEventUser_Type(DisplayString):
    """Custom type slEventUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlEventUser_Type.__name__ = "DisplayString"
_SlEventUser_Object = MibTableColumn
slEventUser = _SlEventUser_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 4),
    _SlEventUser_Type()
)
slEventUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEventUser.setStatus("current")


class _SlEventCtag_Type(DisplayString):
    """Custom type slEventCtag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlEventCtag_Type.__name__ = "DisplayString"
_SlEventCtag_Object = MibTableColumn
slEventCtag = _SlEventCtag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 5),
    _SlEventCtag_Type()
)
slEventCtag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEventCtag.setStatus("current")


class _SlEventTid_Type(DisplayString):
    """Custom type slEventTid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlEventTid_Type.__name__ = "DisplayString"
_SlEventTid_Object = MibTableColumn
slEventTid = _SlEventTid_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 6),
    _SlEventTid_Type()
)
slEventTid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEventTid.setStatus("current")
_SlEventInventoryTable_Object = MibTable
slEventInventoryTable = _SlEventInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2)
)
if mibBuilder.loadTexts:
    slEventInventoryTable.setStatus("current")
_SlEventInventoryEntry_Object = MibTableRow
slEventInventoryEntry = _SlEventInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1)
)
slEventInventoryEntry.setIndexNames(
    (0, "SL-EVENT-MIB", "slEventInventoryIfIndex"),
    (0, "SL-EVENT-MIB", "slEventInventoryType"),
)
if mibBuilder.loadTexts:
    slEventInventoryEntry.setStatus("current")
_SlEventInventoryIfIndex_Type = InterfaceIndex
_SlEventInventoryIfIndex_Object = MibTableColumn
slEventInventoryIfIndex = _SlEventInventoryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 1),
    _SlEventInventoryIfIndex_Type()
)
slEventInventoryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEventInventoryIfIndex.setStatus("current")
_SlEventInventoryAction_Type = SlEventInventoryAction
_SlEventInventoryAction_Object = MibTableColumn
slEventInventoryAction = _SlEventInventoryAction_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 2),
    _SlEventInventoryAction_Type()
)
slEventInventoryAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEventInventoryAction.setStatus("current")
_SlEventInventoryType_Type = SlEventInventoryType
_SlEventInventoryType_Object = MibTableColumn
slEventInventoryType = _SlEventInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 3),
    _SlEventInventoryType_Type()
)
slEventInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slEventInventoryType.setStatus("current")


class _SlEventInventorySerial_Type(DisplayString):
    """Custom type slEventInventorySerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlEventInventorySerial_Type.__name__ = "DisplayString"
_SlEventInventorySerial_Object = MibTableColumn
slEventInventorySerial = _SlEventInventorySerial_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 4),
    _SlEventInventorySerial_Type()
)
slEventInventorySerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEventInventorySerial.setStatus("current")
_SlEventInventoryPartnum_Type = DisplayString
_SlEventInventoryPartnum_Object = MibTableColumn
slEventInventoryPartnum = _SlEventInventoryPartnum_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 5),
    _SlEventInventoryPartnum_Type()
)
slEventInventoryPartnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slEventInventoryPartnum.setStatus("current")
_SlGenEventConfigTable_Object = MibTable
slGenEventConfigTable = _SlGenEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3)
)
if mibBuilder.loadTexts:
    slGenEventConfigTable.setStatus("current")
_SlGenEventConfigEntry_Object = MibTableRow
slGenEventConfigEntry = _SlGenEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1)
)
slGenEventConfigEntry.setIndexNames(
    (0, "SL-EVENT-MIB", "slGenEventIfIndex"),
    (0, "SL-EVENT-MIB", "slGenEventType"),
)
if mibBuilder.loadTexts:
    slGenEventConfigEntry.setStatus("current")
_SlGenEventIfIndex_Type = InterfaceIndex
_SlGenEventIfIndex_Object = MibTableColumn
slGenEventIfIndex = _SlGenEventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 1),
    _SlGenEventIfIndex_Type()
)
slGenEventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slGenEventIfIndex.setStatus("current")
_SlGenEventType_Type = SlGenEventType
_SlGenEventType_Object = MibTableColumn
slGenEventType = _SlGenEventType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 2),
    _SlGenEventType_Type()
)
slGenEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slGenEventType.setStatus("current")


class _SlGenEventVal_Type(DisplayString):
    """Custom type slGenEventVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlGenEventVal_Type.__name__ = "DisplayString"
_SlGenEventVal_Object = MibTableColumn
slGenEventVal = _SlGenEventVal_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 3),
    _SlGenEventVal_Type()
)
slGenEventVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slGenEventVal.setStatus("current")


class _SlGenEventUser_Type(DisplayString):
    """Custom type slGenEventUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlGenEventUser_Type.__name__ = "DisplayString"
_SlGenEventUser_Object = MibTableColumn
slGenEventUser = _SlGenEventUser_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 4),
    _SlGenEventUser_Type()
)
slGenEventUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slGenEventUser.setStatus("current")


class _SlGenEventCtag_Type(DisplayString):
    """Custom type slGenEventCtag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlGenEventCtag_Type.__name__ = "DisplayString"
_SlGenEventCtag_Object = MibTableColumn
slGenEventCtag = _SlGenEventCtag_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 5),
    _SlGenEventCtag_Type()
)
slGenEventCtag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slGenEventCtag.setStatus("current")


class _SlGenEventTid_Type(DisplayString):
    """Custom type slGenEventTid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlGenEventTid_Type.__name__ = "DisplayString"
_SlGenEventTid_Object = MibTableColumn
slGenEventTid = _SlGenEventTid_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 6),
    _SlGenEventTid_Type()
)
slGenEventTid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slGenEventTid.setStatus("current")
_SlEventTraps_ObjectIdentity = ObjectIdentity
slEventTraps = _SlEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2)
)
_SlEventTraps0_ObjectIdentity = ObjectIdentity
slEventTraps0 = _SlEventTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0)
)

# Managed Objects groups


# Notification objects

slEventTrap0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 2)
)
slEventTrap0.setObjects(
      *(("SL-EVENT-MIB", "slEventIfIndex"),
        ("SL-EVENT-MIB", "slEventType"),
        ("SL-EVENT-MIB", "slEventVal"),
        ("SL-EVENT-MIB", "slEventUser"))
)
if mibBuilder.loadTexts:
    slEventTrap0.setStatus(
        "current"
    )

slEventInventoryTrap0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 3)
)
slEventInventoryTrap0.setObjects(
      *(("SL-EVENT-MIB", "slEventInventoryIfIndex"),
        ("SL-EVENT-MIB", "slEventInventoryAction"),
        ("SL-EVENT-MIB", "slEventInventoryType"),
        ("SL-EVENT-MIB", "slEventInventorySerial"),
        ("SL-EVENT-MIB", "slEventInventoryPartnum"))
)
if mibBuilder.loadTexts:
    slEventInventoryTrap0.setStatus(
        "current"
    )

slGenEventTrap0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 4)
)
slGenEventTrap0.setObjects(
      *(("SL-EVENT-MIB", "slGenEventIfIndex"),
        ("SL-EVENT-MIB", "slGenEventType"),
        ("SL-EVENT-MIB", "slGenEventVal"),
        ("SL-EVENT-MIB", "slGenEventUser"))
)
if mibBuilder.loadTexts:
    slGenEventTrap0.setStatus(
        "current"
    )

slEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 2)
)
slEventTrap.setObjects(
      *(("SL-EVENT-MIB", "slEventIfIndex"),
        ("SL-EVENT-MIB", "slEventType"),
        ("SL-EVENT-MIB", "slEventVal"),
        ("SL-EVENT-MIB", "slEventUser"))
)
if mibBuilder.loadTexts:
    slEventTrap.setStatus(
        "current"
    )

slEventInventoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 3)
)
slEventInventoryTrap.setObjects(
      *(("SL-EVENT-MIB", "slEventInventoryIfIndex"),
        ("SL-EVENT-MIB", "slEventInventoryAction"),
        ("SL-EVENT-MIB", "slEventInventoryType"),
        ("SL-EVENT-MIB", "slEventInventorySerial"),
        ("SL-EVENT-MIB", "slEventInventoryPartnum"))
)
if mibBuilder.loadTexts:
    slEventInventoryTrap.setStatus(
        "current"
    )

slGenEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 4)
)
slGenEventTrap.setObjects(
      *(("SL-EVENT-MIB", "slGenEventIfIndex"),
        ("SL-EVENT-MIB", "slGenEventType"),
        ("SL-EVENT-MIB", "slGenEventVal"),
        ("SL-EVENT-MIB", "slGenEventUser"))
)
if mibBuilder.loadTexts:
    slGenEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-EVENT-MIB",
    **{"SlGenEventType": SlGenEventType,
       "SlEventType": SlEventType,
       "SlEventInventoryAction": SlEventInventoryAction,
       "SlEventInventoryType": SlEventInventoryType,
       "slEventMib": slEventMib,
       "slEventConfig": slEventConfig,
       "slEventConfigTable": slEventConfigTable,
       "slEventConfigEntry": slEventConfigEntry,
       "slEventIfIndex": slEventIfIndex,
       "slEventType": slEventType,
       "slEventVal": slEventVal,
       "slEventUser": slEventUser,
       "slEventCtag": slEventCtag,
       "slEventTid": slEventTid,
       "slEventInventoryTable": slEventInventoryTable,
       "slEventInventoryEntry": slEventInventoryEntry,
       "slEventInventoryIfIndex": slEventInventoryIfIndex,
       "slEventInventoryAction": slEventInventoryAction,
       "slEventInventoryType": slEventInventoryType,
       "slEventInventorySerial": slEventInventorySerial,
       "slEventInventoryPartnum": slEventInventoryPartnum,
       "slGenEventConfigTable": slGenEventConfigTable,
       "slGenEventConfigEntry": slGenEventConfigEntry,
       "slGenEventIfIndex": slGenEventIfIndex,
       "slGenEventType": slGenEventType,
       "slGenEventVal": slGenEventVal,
       "slGenEventUser": slGenEventUser,
       "slGenEventCtag": slGenEventCtag,
       "slGenEventTid": slGenEventTid,
       "slEventTraps": slEventTraps,
       "slEventTraps0": slEventTraps0,
       "slEventTrap0": slEventTrap0,
       "slEventInventoryTrap0": slEventInventoryTrap0,
       "slGenEventTrap0": slGenEventTrap0,
       "slEventTrap": slEventTrap,
       "slEventInventoryTrap": slEventInventoryTrap,
       "slGenEventTrap": slGenEventTrap}
)
