# SNMP MIB module (SL-DRY-CON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-DRY-CON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:45 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slDryConMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlDryConOut_ObjectIdentity = ObjectIdentity
slDryConOut = _SlDryConOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 1)
)


class _SlDryConAlarmCutoff_Type(Integer32):
    """Custom type slDryConAlarmCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dummy", 1)
    )


_SlDryConAlarmCutoff_Type.__name__ = "Integer32"
_SlDryConAlarmCutoff_Object = MibScalar
slDryConAlarmCutoff = _SlDryConAlarmCutoff_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 1),
    _SlDryConAlarmCutoff_Type()
)
slDryConAlarmCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDryConAlarmCutoff.setStatus("current")
_SlDryConOutTable_Object = MibTable
slDryConOutTable = _SlDryConOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    slDryConOutTable.setStatus("current")
_SlDryConOutEntry_Object = MibTableRow
slDryConOutEntry = _SlDryConOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1)
)
slDryConOutEntry.setIndexNames(
    (0, "SL-DRY-CON-MIB", "slDryConOutIndex"),
)
if mibBuilder.loadTexts:
    slDryConOutEntry.setStatus("current")


class _SlDryConOutIndex_Type(Integer32):
    """Custom type slDryConOutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SlDryConOutIndex_Type.__name__ = "Integer32"
_SlDryConOutIndex_Object = MibTableColumn
slDryConOutIndex = _SlDryConOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 1),
    _SlDryConOutIndex_Type()
)
slDryConOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDryConOutIndex.setStatus("current")


class _SlDryConOutCommand_Type(Integer32):
    """Custom type slDryConOutCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2),
          ("clear", 3))
    )


_SlDryConOutCommand_Type.__name__ = "Integer32"
_SlDryConOutCommand_Object = MibTableColumn
slDryConOutCommand = _SlDryConOutCommand_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 2),
    _SlDryConOutCommand_Type()
)
slDryConOutCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDryConOutCommand.setStatus("current")
_SlDryConOutActiveStatus_Type = TruthValue
_SlDryConOutActiveStatus_Object = MibTableColumn
slDryConOutActiveStatus = _SlDryConOutActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 3),
    _SlDryConOutActiveStatus_Type()
)
slDryConOutActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDryConOutActiveStatus.setStatus("current")
_SlDryConIn_ObjectIdentity = ObjectIdentity
slDryConIn = _SlDryConIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2)
)


class _SlDryConLastChange_Type(Integer32):
    """Custom type slDryConLastChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dummy", 1)
    )


_SlDryConLastChange_Type.__name__ = "Integer32"
_SlDryConLastChange_Object = MibScalar
slDryConLastChange = _SlDryConLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 1),
    _SlDryConLastChange_Type()
)
slDryConLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDryConLastChange.setStatus("current")
_SlDryConInTable_Object = MibTable
slDryConInTable = _SlDryConInTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    slDryConInTable.setStatus("current")
_SlDryConInEntry_Object = MibTableRow
slDryConInEntry = _SlDryConInEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1)
)
slDryConInEntry.setIndexNames(
    (0, "SL-DRY-CON-MIB", "slDryConInIndex"),
)
if mibBuilder.loadTexts:
    slDryConInEntry.setStatus("current")


class _SlDryConInIndex_Type(Integer32):
    """Custom type slDryConInIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SlDryConInIndex_Type.__name__ = "Integer32"
_SlDryConInIndex_Object = MibTableColumn
slDryConInIndex = _SlDryConInIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 1),
    _SlDryConInIndex_Type()
)
slDryConInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDryConInIndex.setStatus("current")


class _SlDryConInDescription_Type(DisplayString):
    """Custom type slDryConInDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlDryConInDescription_Type.__name__ = "DisplayString"
_SlDryConInDescription_Object = MibTableColumn
slDryConInDescription = _SlDryConInDescription_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 2),
    _SlDryConInDescription_Type()
)
slDryConInDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDryConInDescription.setStatus("current")


class _SlDryConInSeverity_Type(Integer32):
    """Custom type slDryConInSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("cleared", 4),
          ("notification", 5))
    )


_SlDryConInSeverity_Type.__name__ = "Integer32"
_SlDryConInSeverity_Object = MibTableColumn
slDryConInSeverity = _SlDryConInSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 3),
    _SlDryConInSeverity_Type()
)
slDryConInSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDryConInSeverity.setStatus("current")


class _SlDryConInEnable_Type(Integer32):
    """Custom type slDryConInEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SlDryConInEnable_Type.__name__ = "Integer32"
_SlDryConInEnable_Object = MibTableColumn
slDryConInEnable = _SlDryConInEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 4),
    _SlDryConInEnable_Type()
)
slDryConInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDryConInEnable.setStatus("current")


class _SlDryConInPolarity_Type(Integer32):
    """Custom type slDryConInPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeClose", 1),
          ("activeOpen", 2))
    )


_SlDryConInPolarity_Type.__name__ = "Integer32"
_SlDryConInPolarity_Object = MibTableColumn
slDryConInPolarity = _SlDryConInPolarity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 5),
    _SlDryConInPolarity_Type()
)
slDryConInPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDryConInPolarity.setStatus("current")


class _SlDryConInStatus_Type(Integer32):
    """Custom type slDryConInStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SlDryConInStatus_Type.__name__ = "Integer32"
_SlDryConInStatus_Object = MibTableColumn
slDryConInStatus = _SlDryConInStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 6),
    _SlDryConInStatus_Type()
)
slDryConInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDryConInStatus.setStatus("current")


class _SlDryConInAlmType_Type(Integer32):
    """Custom type slDryConInAlmType based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("aircompr", 1),
          ("aircond", 2),
          ("airdryd", 3),
          ("batdschrg", 4),
          ("battery", 5),
          ("clfan", 6),
          ("cpmajor", 7),
          ("cpminor", 8),
          ("engine", 9),
          ("engoprg", 10),
          ("explgs", 11),
          ("firdetr", 12),
          ("fire", 13),
          ("flood", 14),
          ("fuse", 15),
          ("gen", 16),
          ("hiair", 17),
          ("hihum", 18),
          ("hitemp", 19),
          ("hiwtr", 20),
          ("intruder", 21),
          ("lwbatvg", 22),
          ("lwfuel", 23),
          ("lwhum", 24),
          ("lwpres", 25),
          ("lwtemp", 26),
          ("lwwtr", 27),
          ("misc", 28),
          ("opendr", 29),
          ("pump", 30),
          ("power", 31),
          ("pwrX", 32),
          ("rect", 33),
          ("recthi", 34),
          ("rectlo", 35),
          ("smoke", 36),
          ("toxicgas", 37),
          ("ventn", 38))
    )


_SlDryConInAlmType_Type.__name__ = "Integer32"
_SlDryConInAlmType_Object = MibTableColumn
slDryConInAlmType = _SlDryConInAlmType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 7),
    _SlDryConInAlmType_Type()
)
slDryConInAlmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDryConInAlmType.setStatus("current")
_SlDryConTraps_ObjectIdentity = ObjectIdentity
slDryConTraps = _SlDryConTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 3)
)

# Managed Objects groups


# Notification objects

slDryConStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 7, 3, 1)
)
slDryConStatusChangeTrap.setObjects(
      *(("SL-DRY-CON-MIB", "slDryConInIndex"),
        ("SL-DRY-CON-MIB", "slDryConInStatus"),
        ("SL-DRY-CON-MIB", "slDryConInAlmType"))
)
if mibBuilder.loadTexts:
    slDryConStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-DRY-CON-MIB",
    **{"slDryConMib": slDryConMib,
       "slDryConOut": slDryConOut,
       "slDryConAlarmCutoff": slDryConAlarmCutoff,
       "slDryConOutTable": slDryConOutTable,
       "slDryConOutEntry": slDryConOutEntry,
       "slDryConOutIndex": slDryConOutIndex,
       "slDryConOutCommand": slDryConOutCommand,
       "slDryConOutActiveStatus": slDryConOutActiveStatus,
       "slDryConIn": slDryConIn,
       "slDryConLastChange": slDryConLastChange,
       "slDryConInTable": slDryConInTable,
       "slDryConInEntry": slDryConInEntry,
       "slDryConInIndex": slDryConInIndex,
       "slDryConInDescription": slDryConInDescription,
       "slDryConInSeverity": slDryConInSeverity,
       "slDryConInEnable": slDryConInEnable,
       "slDryConInPolarity": slDryConInPolarity,
       "slDryConInStatus": slDryConInStatus,
       "slDryConInAlmType": slDryConInAlmType,
       "slDryConTraps": slDryConTraps,
       "slDryConStatusChangeTrap": slDryConStatusChangeTrap}
)
