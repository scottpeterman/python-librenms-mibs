# SNMP MIB module (F3-DATAEXPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-DATAEXPORT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:55 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(IpVersion,
 PerfCounter64) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "IpVersion",
    "PerfCounter64")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 StorageType,
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "VariablePointer")


# MODULE-IDENTITY

f3DataExportMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30)
)
if mibBuilder.loadTexts:
    f3DataExportMIB.setRevisions(
        ("2013-10-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DataExportType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("esal3pm", 1),
          ("twamppm", 2),
          ("flowbyteratepm", 3))
    )


# MIB Managed Objects in the order of their OIDs

_F3DataExportConfigObjects_ObjectIdentity = ObjectIdentity
f3DataExportConfigObjects = _F3DataExportConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1)
)
_F3DataExportTypes_Type = DataExportType
_F3DataExportTypes_Object = MibScalar
f3DataExportTypes = _F3DataExportTypes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 1),
    _F3DataExportTypes_Type()
)
f3DataExportTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportTypes.setStatus("current")


class _F3DataExportReportInterval_Type(Integer32):
    """Custom type f3DataExportReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_F3DataExportReportInterval_Type.__name__ = "Integer32"
_F3DataExportReportInterval_Object = MibScalar
f3DataExportReportInterval = _F3DataExportReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 2),
    _F3DataExportReportInterval_Type()
)
f3DataExportReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportReportInterval.setStatus("current")
_F3DataExportIpVersion_Type = IpVersion
_F3DataExportIpVersion_Object = MibScalar
f3DataExportIpVersion = _F3DataExportIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 3),
    _F3DataExportIpVersion_Type()
)
f3DataExportIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportIpVersion.setStatus("current")
_F3DataExportServerIpv4Addr_Type = IpAddress
_F3DataExportServerIpv4Addr_Object = MibScalar
f3DataExportServerIpv4Addr = _F3DataExportServerIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 4),
    _F3DataExportServerIpv4Addr_Type()
)
f3DataExportServerIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportServerIpv4Addr.setStatus("current")
_F3DataExportServerIpv6Addr_Type = Ipv6Address
_F3DataExportServerIpv6Addr_Object = MibScalar
f3DataExportServerIpv6Addr = _F3DataExportServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 5),
    _F3DataExportServerIpv6Addr_Type()
)
f3DataExportServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportServerIpv6Addr.setStatus("current")
_F3DataExportUserName_Type = DisplayString
_F3DataExportUserName_Object = MibScalar
f3DataExportUserName = _F3DataExportUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 6),
    _F3DataExportUserName_Type()
)
f3DataExportUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportUserName.setStatus("current")
_F3DataExportPassword_Type = DisplayString
_F3DataExportPassword_Object = MibScalar
f3DataExportPassword = _F3DataExportPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 7),
    _F3DataExportPassword_Type()
)
f3DataExportPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportPassword.setStatus("current")
_F3DataExportPath_Type = DisplayString
_F3DataExportPath_Object = MibScalar
f3DataExportPath = _F3DataExportPath_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 8),
    _F3DataExportPath_Type()
)
f3DataExportPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportPath.setStatus("current")
_F3DataExportConfigObjectTable_Object = MibTable
f3DataExportConfigObjectTable = _F3DataExportConfigObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9)
)
if mibBuilder.loadTexts:
    f3DataExportConfigObjectTable.setStatus("current")
_F3DataExportConfigObjectEntry_Object = MibTableRow
f3DataExportConfigObjectEntry = _F3DataExportConfigObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1)
)
f3DataExportConfigObjectEntry.setIndexNames(
    (0, "F3-DATAEXPORT-MIB", "f3DataExportConfigObjectEntity"),
)
if mibBuilder.loadTexts:
    f3DataExportConfigObjectEntry.setStatus("current")
_F3DataExportConfigObjectEntity_Type = VariablePointer
_F3DataExportConfigObjectEntity_Object = MibTableColumn
f3DataExportConfigObjectEntity = _F3DataExportConfigObjectEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1, 1),
    _F3DataExportConfigObjectEntity_Type()
)
f3DataExportConfigObjectEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3DataExportConfigObjectEntity.setStatus("current")
_F3DataExportConfigObjectStorageType_Type = StorageType
_F3DataExportConfigObjectStorageType_Object = MibTableColumn
f3DataExportConfigObjectStorageType = _F3DataExportConfigObjectStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1, 2),
    _F3DataExportConfigObjectStorageType_Type()
)
f3DataExportConfigObjectStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DataExportConfigObjectStorageType.setStatus("current")
_F3DataExportConfigObjectRowStatus_Type = RowStatus
_F3DataExportConfigObjectRowStatus_Object = MibTableColumn
f3DataExportConfigObjectRowStatus = _F3DataExportConfigObjectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 1, 9, 1, 3),
    _F3DataExportConfigObjectRowStatus_Type()
)
f3DataExportConfigObjectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3DataExportConfigObjectRowStatus.setStatus("current")
_F3DataExportCounterObjects_ObjectIdentity = ObjectIdentity
f3DataExportCounterObjects = _F3DataExportCounterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 2)
)
_F3DataExportServerXferPass_Type = PerfCounter64
_F3DataExportServerXferPass_Object = MibScalar
f3DataExportServerXferPass = _F3DataExportServerXferPass_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 2, 1),
    _F3DataExportServerXferPass_Type()
)
f3DataExportServerXferPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DataExportServerXferPass.setStatus("current")
_F3DataExportServerXferFail_Type = PerfCounter64
_F3DataExportServerXferFail_Object = MibScalar
f3DataExportServerXferFail = _F3DataExportServerXferFail_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 2, 2),
    _F3DataExportServerXferFail_Type()
)
f3DataExportServerXferFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3DataExportServerXferFail.setStatus("current")
_F3DataExportActionObjects_ObjectIdentity = ObjectIdentity
f3DataExportActionObjects = _F3DataExportActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 3)
)


class _F3DataExportClearStatsAction_Type(Integer32):
    """Custom type f3DataExportClearStatsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("clear", 1))
    )


_F3DataExportClearStatsAction_Type.__name__ = "Integer32"
_F3DataExportClearStatsAction_Object = MibScalar
f3DataExportClearStatsAction = _F3DataExportClearStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 3, 1),
    _F3DataExportClearStatsAction_Type()
)
f3DataExportClearStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3DataExportClearStatsAction.setStatus("current")
_F3DataExportConformance_ObjectIdentity = ObjectIdentity
f3DataExportConformance = _F3DataExportConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4)
)
_F3DataExportCompliances_ObjectIdentity = ObjectIdentity
f3DataExportCompliances = _F3DataExportCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 1)
)
_F3DataExportGroups_ObjectIdentity = ObjectIdentity
f3DataExportGroups = _F3DataExportGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2)
)

# Managed Objects groups

f3DataExportConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2, 1)
)
f3DataExportConfigGroup.setObjects(
      *(("F3-DATAEXPORT-MIB", "f3DataExportTypes"),
        ("F3-DATAEXPORT-MIB", "f3DataExportReportInterval"),
        ("F3-DATAEXPORT-MIB", "f3DataExportIpVersion"),
        ("F3-DATAEXPORT-MIB", "f3DataExportServerIpv4Addr"),
        ("F3-DATAEXPORT-MIB", "f3DataExportServerIpv6Addr"),
        ("F3-DATAEXPORT-MIB", "f3DataExportUserName"),
        ("F3-DATAEXPORT-MIB", "f3DataExportPassword"),
        ("F3-DATAEXPORT-MIB", "f3DataExportPath"))
)
if mibBuilder.loadTexts:
    f3DataExportConfigGroup.setStatus("current")

f3DataExportCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2, 2)
)
f3DataExportCounterGroup.setObjects(
      *(("F3-DATAEXPORT-MIB", "f3DataExportServerXferPass"),
        ("F3-DATAEXPORT-MIB", "f3DataExportServerXferFail"))
)
if mibBuilder.loadTexts:
    f3DataExportCounterGroup.setStatus("current")

f3DataExportActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 2, 3)
)
f3DataExportActionGroup.setObjects(
    ("F3-DATAEXPORT-MIB", "f3DataExportClearStatsAction")
)
if mibBuilder.loadTexts:
    f3DataExportActionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3DataExportCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 30, 4, 1, 1)
)
f3DataExportCompliance.setObjects(
      *(("F3-DATAEXPORT-MIB", "f3DataExportConfigGroup"),
        ("F3-DATAEXPORT-MIB", "f3DataExportCounterGroup"),
        ("F3-DATAEXPORT-MIB", "f3DataExportActionGroup"))
)
if mibBuilder.loadTexts:
    f3DataExportCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-DATAEXPORT-MIB",
    **{"DataExportType": DataExportType,
       "f3DataExportMIB": f3DataExportMIB,
       "f3DataExportConfigObjects": f3DataExportConfigObjects,
       "f3DataExportTypes": f3DataExportTypes,
       "f3DataExportReportInterval": f3DataExportReportInterval,
       "f3DataExportIpVersion": f3DataExportIpVersion,
       "f3DataExportServerIpv4Addr": f3DataExportServerIpv4Addr,
       "f3DataExportServerIpv6Addr": f3DataExportServerIpv6Addr,
       "f3DataExportUserName": f3DataExportUserName,
       "f3DataExportPassword": f3DataExportPassword,
       "f3DataExportPath": f3DataExportPath,
       "f3DataExportConfigObjectTable": f3DataExportConfigObjectTable,
       "f3DataExportConfigObjectEntry": f3DataExportConfigObjectEntry,
       "f3DataExportConfigObjectEntity": f3DataExportConfigObjectEntity,
       "f3DataExportConfigObjectStorageType": f3DataExportConfigObjectStorageType,
       "f3DataExportConfigObjectRowStatus": f3DataExportConfigObjectRowStatus,
       "f3DataExportCounterObjects": f3DataExportCounterObjects,
       "f3DataExportServerXferPass": f3DataExportServerXferPass,
       "f3DataExportServerXferFail": f3DataExportServerXferFail,
       "f3DataExportActionObjects": f3DataExportActionObjects,
       "f3DataExportClearStatsAction": f3DataExportClearStatsAction,
       "f3DataExportConformance": f3DataExportConformance,
       "f3DataExportCompliances": f3DataExportCompliances,
       "f3DataExportCompliance": f3DataExportCompliance,
       "f3DataExportGroups": f3DataExportGroups,
       "f3DataExportConfigGroup": f3DataExportConfigGroup,
       "f3DataExportCounterGroup": f3DataExportCounterGroup,
       "f3DataExportActionGroup": f3DataExportActionGroup}
)
