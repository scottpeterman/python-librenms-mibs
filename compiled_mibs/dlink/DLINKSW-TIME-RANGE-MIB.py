# SNMP MIB module (DLINKSW-TIME-RANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-TIME-RANGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:03 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

dlinkSwTimeRangeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 50)
)
if mibBuilder.loadTexts:
    dlinkSwTimeRangeMIB.setRevisions(
        ("2013-03-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DTimeRangeMIBNotifications_ObjectIdentity = ObjectIdentity
dTimeRangeMIBNotifications = _DTimeRangeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 0)
)
_DTimeRangeMIBObjects_ObjectIdentity = ObjectIdentity
dTimeRangeMIBObjects = _DTimeRangeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1)
)
_DTimeRangeProfileTable_Object = MibTable
dTimeRangeProfileTable = _DTimeRangeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1)
)
if mibBuilder.loadTexts:
    dTimeRangeProfileTable.setStatus("current")
_DTimeRangeProfileEntry_Object = MibTableRow
dTimeRangeProfileEntry = _DTimeRangeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1)
)
dTimeRangeProfileEntry.setIndexNames(
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileName"),
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfilePeriodType"),
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileStartDayOfWeek"),
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileStartHour"),
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileStartMinute"),
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileEndDayOfWeek"),
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileEndHour"),
    (0, "DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileEndMinute"),
)
if mibBuilder.loadTexts:
    dTimeRangeProfileEntry.setStatus("current")


class _DTimeRangeProfileName_Type(DisplayString):
    """Custom type dTimeRangeProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DTimeRangeProfileName_Type.__name__ = "DisplayString"
_DTimeRangeProfileName_Object = MibTableColumn
dTimeRangeProfileName = _DTimeRangeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 1),
    _DTimeRangeProfileName_Type()
)
dTimeRangeProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfileName.setStatus("current")


class _DTimeRangeProfilePeriodType_Type(Integer32):
    """Custom type dTimeRangeProfilePeriodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("weekly", 2))
    )


_DTimeRangeProfilePeriodType_Type.__name__ = "Integer32"
_DTimeRangeProfilePeriodType_Object = MibTableColumn
dTimeRangeProfilePeriodType = _DTimeRangeProfilePeriodType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 2),
    _DTimeRangeProfilePeriodType_Type()
)
dTimeRangeProfilePeriodType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfilePeriodType.setStatus("current")


class _DTimeRangeProfileStartDayOfWeek_Type(Integer32):
    """Custom type dTimeRangeProfileStartDayOfWeek based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("notApplicable", 8))
    )


_DTimeRangeProfileStartDayOfWeek_Type.__name__ = "Integer32"
_DTimeRangeProfileStartDayOfWeek_Object = MibTableColumn
dTimeRangeProfileStartDayOfWeek = _DTimeRangeProfileStartDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 3),
    _DTimeRangeProfileStartDayOfWeek_Type()
)
dTimeRangeProfileStartDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfileStartDayOfWeek.setStatus("current")


class _DTimeRangeProfileStartHour_Type(Unsigned32):
    """Custom type dTimeRangeProfileStartHour based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DTimeRangeProfileStartHour_Type.__name__ = "Unsigned32"
_DTimeRangeProfileStartHour_Object = MibTableColumn
dTimeRangeProfileStartHour = _DTimeRangeProfileStartHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 4),
    _DTimeRangeProfileStartHour_Type()
)
dTimeRangeProfileStartHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfileStartHour.setStatus("current")


class _DTimeRangeProfileStartMinute_Type(Unsigned32):
    """Custom type dTimeRangeProfileStartMinute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DTimeRangeProfileStartMinute_Type.__name__ = "Unsigned32"
_DTimeRangeProfileStartMinute_Object = MibTableColumn
dTimeRangeProfileStartMinute = _DTimeRangeProfileStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 5),
    _DTimeRangeProfileStartMinute_Type()
)
dTimeRangeProfileStartMinute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfileStartMinute.setStatus("current")


class _DTimeRangeProfileEndDayOfWeek_Type(Integer32):
    """Custom type dTimeRangeProfileEndDayOfWeek based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7),
          ("notApplicable", 8))
    )


_DTimeRangeProfileEndDayOfWeek_Type.__name__ = "Integer32"
_DTimeRangeProfileEndDayOfWeek_Object = MibTableColumn
dTimeRangeProfileEndDayOfWeek = _DTimeRangeProfileEndDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 6),
    _DTimeRangeProfileEndDayOfWeek_Type()
)
dTimeRangeProfileEndDayOfWeek.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfileEndDayOfWeek.setStatus("current")


class _DTimeRangeProfileEndHour_Type(Unsigned32):
    """Custom type dTimeRangeProfileEndHour based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DTimeRangeProfileEndHour_Type.__name__ = "Unsigned32"
_DTimeRangeProfileEndHour_Object = MibTableColumn
dTimeRangeProfileEndHour = _DTimeRangeProfileEndHour_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 7),
    _DTimeRangeProfileEndHour_Type()
)
dTimeRangeProfileEndHour.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfileEndHour.setStatus("current")


class _DTimeRangeProfileEndMinute_Type(Unsigned32):
    """Custom type dTimeRangeProfileEndMinute based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DTimeRangeProfileEndMinute_Type.__name__ = "Unsigned32"
_DTimeRangeProfileEndMinute_Object = MibTableColumn
dTimeRangeProfileEndMinute = _DTimeRangeProfileEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 8),
    _DTimeRangeProfileEndMinute_Type()
)
dTimeRangeProfileEndMinute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTimeRangeProfileEndMinute.setStatus("current")
_DTimeRangeProfileRowStatus_Type = RowStatus
_DTimeRangeProfileRowStatus_Object = MibTableColumn
dTimeRangeProfileRowStatus = _DTimeRangeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 1, 1, 1, 9),
    _DTimeRangeProfileRowStatus_Type()
)
dTimeRangeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dTimeRangeProfileRowStatus.setStatus("current")
_DTimeRangeMIBConformance_ObjectIdentity = ObjectIdentity
dTimeRangeMIBConformance = _DTimeRangeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 2)
)
_DTimeRangeCompliances_ObjectIdentity = ObjectIdentity
dTimeRangeCompliances = _DTimeRangeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 2, 1)
)
_DTimeRangeGroups_ObjectIdentity = ObjectIdentity
dTimeRangeGroups = _DTimeRangeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 2, 2)
)

# Managed Objects groups

dTimeRangeProfileCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 2, 2, 1)
)
dTimeRangeProfileCfgGroup.setObjects(
    ("DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileRowStatus")
)
if mibBuilder.loadTexts:
    dTimeRangeProfileCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dTimeRangeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 50, 2, 1, 1)
)
dTimeRangeCompliance.setObjects(
    ("DLINKSW-TIME-RANGE-MIB", "dTimeRangeProfileCfgGroup")
)
if mibBuilder.loadTexts:
    dTimeRangeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-TIME-RANGE-MIB",
    **{"dlinkSwTimeRangeMIB": dlinkSwTimeRangeMIB,
       "dTimeRangeMIBNotifications": dTimeRangeMIBNotifications,
       "dTimeRangeMIBObjects": dTimeRangeMIBObjects,
       "dTimeRangeProfileTable": dTimeRangeProfileTable,
       "dTimeRangeProfileEntry": dTimeRangeProfileEntry,
       "dTimeRangeProfileName": dTimeRangeProfileName,
       "dTimeRangeProfilePeriodType": dTimeRangeProfilePeriodType,
       "dTimeRangeProfileStartDayOfWeek": dTimeRangeProfileStartDayOfWeek,
       "dTimeRangeProfileStartHour": dTimeRangeProfileStartHour,
       "dTimeRangeProfileStartMinute": dTimeRangeProfileStartMinute,
       "dTimeRangeProfileEndDayOfWeek": dTimeRangeProfileEndDayOfWeek,
       "dTimeRangeProfileEndHour": dTimeRangeProfileEndHour,
       "dTimeRangeProfileEndMinute": dTimeRangeProfileEndMinute,
       "dTimeRangeProfileRowStatus": dTimeRangeProfileRowStatus,
       "dTimeRangeMIBConformance": dTimeRangeMIBConformance,
       "dTimeRangeCompliances": dTimeRangeCompliances,
       "dTimeRangeCompliance": dTimeRangeCompliance,
       "dTimeRangeGroups": dTimeRangeGroups,
       "dTimeRangeProfileCfgGroup": dTimeRangeProfileCfgGroup}
)
