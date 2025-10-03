# SNMP MIB module (DLINKSW-CABLE-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-CABLE-DIAG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:43 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwCableDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 58)
)
if mibBuilder.loadTexts:
    dlinkSwCableDiagMIB.setRevisions(
        ("2013-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlinkCableDiagStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("ok", 1),
          ("open", 2),
          ("short", 3),
          ("openOrShort", 4),
          ("crosstalk", 5),
          ("unKnown", 6),
          ("noCable", 7),
          ("shutdown", 8))
    )



# MIB Managed Objects in the order of their OIDs

_DCableDiagNotifications_ObjectIdentity = ObjectIdentity
dCableDiagNotifications = _DCableDiagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 0)
)
_DCableDiagObjects_ObjectIdentity = ObjectIdentity
dCableDiagObjects = _DCableDiagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1)
)
_DCableDiagIfTable_Object = MibTable
dCableDiagIfTable = _DCableDiagIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 1)
)
if mibBuilder.loadTexts:
    dCableDiagIfTable.setStatus("current")
_DCableDiagIfEntry_Object = MibTableRow
dCableDiagIfEntry = _DCableDiagIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 1, 1)
)
dCableDiagIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dCableDiagIfEntry.setStatus("current")


class _DCableDiagIfAction_Type(Integer32):
    """Custom type dCableDiagIfAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("test", 2),
          ("clear", 3))
    )


_DCableDiagIfAction_Type.__name__ = "Integer32"
_DCableDiagIfAction_Object = MibTableColumn
dCableDiagIfAction = _DCableDiagIfAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 1, 1, 1),
    _DCableDiagIfAction_Type()
)
dCableDiagIfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dCableDiagIfAction.setStatus("current")
_DCableDiagResultTable_Object = MibTable
dCableDiagResultTable = _DCableDiagResultTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2)
)
if mibBuilder.loadTexts:
    dCableDiagResultTable.setStatus("current")
_DCableDiagResultEntry_Object = MibTableRow
dCableDiagResultEntry = _DCableDiagResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1)
)
dCableDiagResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dCableDiagResultEntry.setStatus("current")
_DCableDiagResultPair1Status_Type = DlinkCableDiagStatus
_DCableDiagResultPair1Status_Object = MibTableColumn
dCableDiagResultPair1Status = _DCableDiagResultPair1Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 1),
    _DCableDiagResultPair1Status_Type()
)
dCableDiagResultPair1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair1Status.setStatus("current")
_DCableDiagResultPair2Status_Type = DlinkCableDiagStatus
_DCableDiagResultPair2Status_Object = MibTableColumn
dCableDiagResultPair2Status = _DCableDiagResultPair2Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 2),
    _DCableDiagResultPair2Status_Type()
)
dCableDiagResultPair2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair2Status.setStatus("current")
_DCableDiagResultPair3Status_Type = DlinkCableDiagStatus
_DCableDiagResultPair3Status_Object = MibTableColumn
dCableDiagResultPair3Status = _DCableDiagResultPair3Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 3),
    _DCableDiagResultPair3Status_Type()
)
dCableDiagResultPair3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair3Status.setStatus("current")
_DCableDiagResultPair4Status_Type = DlinkCableDiagStatus
_DCableDiagResultPair4Status_Object = MibTableColumn
dCableDiagResultPair4Status = _DCableDiagResultPair4Status_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 4),
    _DCableDiagResultPair4Status_Type()
)
dCableDiagResultPair4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair4Status.setStatus("current")
_DCableDiagResultPair1Length_Type = Integer32
_DCableDiagResultPair1Length_Object = MibTableColumn
dCableDiagResultPair1Length = _DCableDiagResultPair1Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 5),
    _DCableDiagResultPair1Length_Type()
)
dCableDiagResultPair1Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair1Length.setStatus("current")
if mibBuilder.loadTexts:
    dCableDiagResultPair1Length.setUnits("meters")
_DCableDiagResultPair2Length_Type = Integer32
_DCableDiagResultPair2Length_Object = MibTableColumn
dCableDiagResultPair2Length = _DCableDiagResultPair2Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 6),
    _DCableDiagResultPair2Length_Type()
)
dCableDiagResultPair2Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair2Length.setStatus("current")
if mibBuilder.loadTexts:
    dCableDiagResultPair2Length.setUnits("meters")
_DCableDiagResultPair3Length_Type = Integer32
_DCableDiagResultPair3Length_Object = MibTableColumn
dCableDiagResultPair3Length = _DCableDiagResultPair3Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 7),
    _DCableDiagResultPair3Length_Type()
)
dCableDiagResultPair3Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair3Length.setStatus("current")
if mibBuilder.loadTexts:
    dCableDiagResultPair3Length.setUnits("meters")
_DCableDiagResultPair4Length_Type = Integer32
_DCableDiagResultPair4Length_Object = MibTableColumn
dCableDiagResultPair4Length = _DCableDiagResultPair4Length_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 8),
    _DCableDiagResultPair4Length_Type()
)
dCableDiagResultPair4Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultPair4Length.setStatus("current")
if mibBuilder.loadTexts:
    dCableDiagResultPair4Length.setUnits("meters")


class _DCableDiagResultStatus_Type(Integer32):
    """Custom type dCableDiagResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRun", 0),
          ("processing", 1),
          ("lastTestOk", 2),
          ("lastTestFailed", 3))
    )


_DCableDiagResultStatus_Type.__name__ = "Integer32"
_DCableDiagResultStatus_Object = MibTableColumn
dCableDiagResultStatus = _DCableDiagResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 1, 2, 1, 9),
    _DCableDiagResultStatus_Type()
)
dCableDiagResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dCableDiagResultStatus.setStatus("current")
_DCableDiagConformance_ObjectIdentity = ObjectIdentity
dCableDiagConformance = _DCableDiagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 2)
)
_DCableDiagCompliances_ObjectIdentity = ObjectIdentity
dCableDiagCompliances = _DCableDiagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 2, 1)
)
_DCableDiagGroups_ObjectIdentity = ObjectIdentity
dCableDiagGroups = _DCableDiagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 2, 1, 2)
)

# Managed Objects groups

dCableDiagBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 2, 1, 2, 1)
)
dCableDiagBasicGroup.setObjects(
      *(("DLINKSW-CABLE-DIAG-MIB", "dCableDiagIfAction"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair1Status"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair2Status"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair3Status"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair4Status"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair1Length"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair2Length"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair3Length"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultPair4Length"),
        ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagResultStatus"))
)
if mibBuilder.loadTexts:
    dCableDiagBasicGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dCableDiagCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 58, 2, 1, 1)
)
dCableDiagCompliance.setObjects(
    ("DLINKSW-CABLE-DIAG-MIB", "dCableDiagBasicGroup")
)
if mibBuilder.loadTexts:
    dCableDiagCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-CABLE-DIAG-MIB",
    **{"DlinkCableDiagStatus": DlinkCableDiagStatus,
       "dlinkSwCableDiagMIB": dlinkSwCableDiagMIB,
       "dCableDiagNotifications": dCableDiagNotifications,
       "dCableDiagObjects": dCableDiagObjects,
       "dCableDiagIfTable": dCableDiagIfTable,
       "dCableDiagIfEntry": dCableDiagIfEntry,
       "dCableDiagIfAction": dCableDiagIfAction,
       "dCableDiagResultTable": dCableDiagResultTable,
       "dCableDiagResultEntry": dCableDiagResultEntry,
       "dCableDiagResultPair1Status": dCableDiagResultPair1Status,
       "dCableDiagResultPair2Status": dCableDiagResultPair2Status,
       "dCableDiagResultPair3Status": dCableDiagResultPair3Status,
       "dCableDiagResultPair4Status": dCableDiagResultPair4Status,
       "dCableDiagResultPair1Length": dCableDiagResultPair1Length,
       "dCableDiagResultPair2Length": dCableDiagResultPair2Length,
       "dCableDiagResultPair3Length": dCableDiagResultPair3Length,
       "dCableDiagResultPair4Length": dCableDiagResultPair4Length,
       "dCableDiagResultStatus": dCableDiagResultStatus,
       "dCableDiagConformance": dCableDiagConformance,
       "dCableDiagCompliances": dCableDiagCompliances,
       "dCableDiagCompliance": dCableDiagCompliance,
       "dCableDiagGroups": dCableDiagGroups,
       "dCableDiagBasicGroup": dCableDiagBasicGroup}
)
