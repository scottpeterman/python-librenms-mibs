# SNMP MIB module (MITEL-APPCMN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mitel\MITEL-APPCMN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:42 2025
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

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "MITEL-CMNALM-MIB",
    "ItuPerceivedSeverity")

(mitelConfCompliances,
 mitelConfGroups,
 mitelIdentification,
 mitelPropApplications) = mibBuilder.importSymbols(
    "MITEL-MIB",
    "mitelConfCompliances",
    "mitelConfGroups",
    "mitelIdentification",
    "mitelPropApplications")

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

mitelAppCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2)
)
if mibBuilder.loadTexts:
    mitelAppCommon.setRevisions(
        ("2014-02-11 12:00",
         "2005-02-21 21:34",
         "2004-01-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MitelAppCmnObjects_ObjectIdentity = ObjectIdentity
mitelAppCmnObjects = _MitelAppCmnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mitelAppCmnObjects.setStatus("current")
_MitelAppTable_Object = MibTable
mitelAppTable = _MitelAppTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mitelAppTable.setStatus("current")
_MitelAppTableEntry_Object = MibTableRow
mitelAppTableEntry = _MitelAppTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1)
)
mitelAppTableEntry.setIndexNames(
    (0, "MITEL-APPCMN-MIB", "mitelAppTblProductOid"),
)
if mibBuilder.loadTexts:
    mitelAppTableEntry.setStatus("current")
_MitelAppTblProductOid_Type = ObjectIdentifier
_MitelAppTblProductOid_Object = MibTableColumn
mitelAppTblProductOid = _MitelAppTblProductOid_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 1),
    _MitelAppTblProductOid_Type()
)
mitelAppTblProductOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAppTblProductOid.setStatus("current")
_MitelAppTblProductManufacturer_Type = DisplayString
_MitelAppTblProductManufacturer_Object = MibTableColumn
mitelAppTblProductManufacturer = _MitelAppTblProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 2),
    _MitelAppTblProductManufacturer_Type()
)
mitelAppTblProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAppTblProductManufacturer.setStatus("current")
_MitelAppTblProductName_Type = DisplayString
_MitelAppTblProductName_Object = MibTableColumn
mitelAppTblProductName = _MitelAppTblProductName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 3),
    _MitelAppTblProductName_Type()
)
mitelAppTblProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAppTblProductName.setStatus("current")
_MitelAppTblProductVersion_Type = DisplayString
_MitelAppTblProductVersion_Object = MibTableColumn
mitelAppTblProductVersion = _MitelAppTblProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 4),
    _MitelAppTblProductVersion_Type()
)
mitelAppTblProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAppTblProductVersion.setStatus("current")
_MitelAppTblProductDescr_Type = DisplayString
_MitelAppTblProductDescr_Object = MibTableColumn
mitelAppTblProductDescr = _MitelAppTblProductDescr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 5),
    _MitelAppTblProductDescr_Type()
)
mitelAppTblProductDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAppTblProductDescr.setStatus("current")
_MitelAppTblAppAlrmStatus_Type = ItuPerceivedSeverity
_MitelAppTblAppAlrmStatus_Object = MibTableColumn
mitelAppTblAppAlrmStatus = _MitelAppTblAppAlrmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 6),
    _MitelAppTblAppAlrmStatus_Type()
)
mitelAppTblAppAlrmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAppTblAppAlrmStatus.setStatus("current")


class _MitelAppNumberOfApps_Type(Integer32):
    """Custom type mitelAppNumberOfApps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MitelAppNumberOfApps_Type.__name__ = "Integer32"
_MitelAppNumberOfApps_Object = MibScalar
mitelAppNumberOfApps = _MitelAppNumberOfApps_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 2),
    _MitelAppNumberOfApps_Type()
)
mitelAppNumberOfApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelAppNumberOfApps.setStatus("current")
_MitelComplAppCommon_ObjectIdentity = ObjectIdentity
mitelComplAppCommon = _MitelComplAppCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 1, 5)
)
if mibBuilder.loadTexts:
    mitelComplAppCommon.setStatus("current")
_MitelGrpAppCommon_ObjectIdentity = ObjectIdentity
mitelGrpAppCommon = _MitelGrpAppCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 3)
)
if mibBuilder.loadTexts:
    mitelGrpAppCommon.setStatus("current")

# Managed Objects groups

mitelGrpAppCmn = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1027, 5, 2, 3, 1)
)
mitelGrpAppCmn.setObjects(
      *(("MITEL-APPCMN-MIB", "mitelAppTblProductOid"),
        ("MITEL-APPCMN-MIB", "mitelAppTblProductManufacturer"),
        ("MITEL-APPCMN-MIB", "mitelAppTblProductName"),
        ("MITEL-APPCMN-MIB", "mitelAppTblProductVersion"),
        ("MITEL-APPCMN-MIB", "mitelAppTblProductDescr"),
        ("MITEL-APPCMN-MIB", "mitelAppTblAppAlrmStatus"))
)
if mibBuilder.loadTexts:
    mitelGrpAppCmn.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mitelComplAppCmn = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1027, 5, 1, 5, 1)
)
mitelComplAppCmn.setObjects(
    ("MITEL-APPCMN-MIB", "mitelGrpAppCmn")
)
if mibBuilder.loadTexts:
    mitelComplAppCmn.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-APPCMN-MIB",
    **{"mitelAppCommon": mitelAppCommon,
       "mitelAppCmnObjects": mitelAppCmnObjects,
       "mitelAppTable": mitelAppTable,
       "mitelAppTableEntry": mitelAppTableEntry,
       "mitelAppTblProductOid": mitelAppTblProductOid,
       "mitelAppTblProductManufacturer": mitelAppTblProductManufacturer,
       "mitelAppTblProductName": mitelAppTblProductName,
       "mitelAppTblProductVersion": mitelAppTblProductVersion,
       "mitelAppTblProductDescr": mitelAppTblProductDescr,
       "mitelAppTblAppAlrmStatus": mitelAppTblAppAlrmStatus,
       "mitelAppNumberOfApps": mitelAppNumberOfApps,
       "mitelComplAppCommon": mitelComplAppCommon,
       "mitelComplAppCmn": mitelComplAppCmn,
       "mitelGrpAppCommon": mitelGrpAppCommon,
       "mitelGrpAppCmn": mitelGrpAppCmn}
)
