# SNMP MIB module (TELESTE-LUMINATO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teleste\TELESTE-LUMINATO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:03 2025
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

(luminato,) = mibBuilder.importSymbols(
    "TELESTE-ROOT-MIB",
    "luminato")

(Float,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "Float")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1)
)
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")


class _GeneralStatus_Type(Integer32):
    """Custom type generalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("statusAlert", 1),
          ("statusCritical", 2),
          ("statusError", 3),
          ("statusWarning", 4),
          ("statusNotice", 5),
          ("statusInformational", 6),
          ("statusDebug", 7))
    )


_GeneralStatus_Type.__name__ = "Integer32"
_GeneralStatus_Object = MibScalar
generalStatus = _GeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 2),
    _GeneralStatus_Type()
)
generalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generalStatus.setStatus("current")


class _RedundancyStatus_Type(Integer32):
    """Custom type redundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              24,
              32,
              40,
              64)
        )
    )
    namedValues = NamedValues(
        *(("redundancyStandalone", 1),
          ("redundancyMaster", 16),
          ("redundancyMasterHandover", 24),
          ("redundancyBackup", 32),
          ("redundancyBackupHandover", 40),
          ("redundancyError", 64))
    )


_RedundancyStatus_Type.__name__ = "Integer32"
_RedundancyStatus_Object = MibScalar
redundancyStatus = _RedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 3),
    _RedundancyStatus_Type()
)
redundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyStatus.setStatus("optional")
_HwSerialNumber_Type = DisplayString
_HwSerialNumber_Object = MibScalar
hwSerialNumber = _HwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 10),
    _HwSerialNumber_Type()
)
hwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSerialNumber.setStatus("current")
_HwType_Type = DisplayString
_HwType_Object = MibScalar
hwType = _HwType_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 11),
    _HwType_Type()
)
hwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwType.setStatus("current")
_HwVersion_Type = DisplayString
_HwVersion_Object = MibScalar
hwVersion = _HwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 12),
    _HwVersion_Type()
)
hwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersion.setStatus("current")
_SwVersion_Type = DisplayString
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 13),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")
_UpTime_Type = TimeTicks
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 14),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")
_CumulativeUptime_Type = TimeTicks
_CumulativeUptime_Object = MibScalar
cumulativeUptime = _CumulativeUptime_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 1, 15),
    _CumulativeUptime_Type()
)
cumulativeUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cumulativeUptime.setStatus("current")
_StatusCode_ObjectIdentity = ObjectIdentity
statusCode = _StatusCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2)
)
_InterfaceTypeTable_Object = MibTable
interfaceTypeTable = _InterfaceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 1)
)
if mibBuilder.loadTexts:
    interfaceTypeTable.setStatus("current")
_InterfaceTypeEntry_Object = MibTableRow
interfaceTypeEntry = _InterfaceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 1, 1)
)
interfaceTypeEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "interfaceTypeId"),
)
if mibBuilder.loadTexts:
    interfaceTypeEntry.setStatus("current")


class _InterfaceTypeId_Type(Integer32):
    """Custom type interfaceTypeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_InterfaceTypeId_Type.__name__ = "Integer32"
_InterfaceTypeId_Object = MibTableColumn
interfaceTypeId = _InterfaceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 1, 1, 1),
    _InterfaceTypeId_Type()
)
interfaceTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceTypeId.setStatus("current")
_StatusCodeDeviceTable_Object = MibTable
statusCodeDeviceTable = _StatusCodeDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 2)
)
if mibBuilder.loadTexts:
    statusCodeDeviceTable.setStatus("current")
_StatusCodeDeviceEntry_Object = MibTableRow
statusCodeDeviceEntry = _StatusCodeDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 2, 1)
)
statusCodeDeviceEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "scdObjectId"),
)
if mibBuilder.loadTexts:
    statusCodeDeviceEntry.setStatus("current")
_ScdObjectId_Type = Unsigned32
_ScdObjectId_Object = MibTableColumn
scdObjectId = _ScdObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 2, 1, 1),
    _ScdObjectId_Type()
)
scdObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scdObjectId.setStatus("current")
_ScdObjectValue_Type = Integer32
_ScdObjectValue_Object = MibTableColumn
scdObjectValue = _ScdObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 2, 1, 2),
    _ScdObjectValue_Type()
)
scdObjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scdObjectValue.setStatus("current")
_ScdObjectDescriptor_Type = DisplayString
_ScdObjectDescriptor_Object = MibTableColumn
scdObjectDescriptor = _ScdObjectDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 2, 1, 3),
    _ScdObjectDescriptor_Type()
)
scdObjectDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scdObjectDescriptor.setStatus("current")
_ScdObjectAlarmValue_Type = Integer32
_ScdObjectAlarmValue_Object = MibTableColumn
scdObjectAlarmValue = _ScdObjectAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 2, 1, 4),
    _ScdObjectAlarmValue_Type()
)
scdObjectAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scdObjectAlarmValue.setStatus("current")
_StatusCodeModuleTable_Object = MibTable
statusCodeModuleTable = _StatusCodeModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 3)
)
if mibBuilder.loadTexts:
    statusCodeModuleTable.setStatus("current")
_StatusCodeModuleEntry_Object = MibTableRow
statusCodeModuleEntry = _StatusCodeModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 3, 1)
)
statusCodeModuleEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "scmModuleId"),
    (0, "TELESTE-LUMINATO-MIB", "scmObjectId"),
)
if mibBuilder.loadTexts:
    statusCodeModuleEntry.setStatus("current")


class _ScmModuleId_Type(Integer32):
    """Custom type scmModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ScmModuleId_Type.__name__ = "Integer32"
_ScmModuleId_Object = MibTableColumn
scmModuleId = _ScmModuleId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 3, 1, 1),
    _ScmModuleId_Type()
)
scmModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmModuleId.setStatus("current")
_ScmObjectId_Type = Unsigned32
_ScmObjectId_Object = MibTableColumn
scmObjectId = _ScmObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 3, 1, 2),
    _ScmObjectId_Type()
)
scmObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmObjectId.setStatus("current")
_ScmObjectValue_Type = Integer32
_ScmObjectValue_Object = MibTableColumn
scmObjectValue = _ScmObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 3, 1, 3),
    _ScmObjectValue_Type()
)
scmObjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmObjectValue.setStatus("current")
_ScmObjectDescriptor_Type = DisplayString
_ScmObjectDescriptor_Object = MibTableColumn
scmObjectDescriptor = _ScmObjectDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 3, 1, 4),
    _ScmObjectDescriptor_Type()
)
scmObjectDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmObjectDescriptor.setStatus("current")
_ScmObjectAlarmValue_Type = Integer32
_ScmObjectAlarmValue_Object = MibTableColumn
scmObjectAlarmValue = _ScmObjectAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 3, 1, 5),
    _ScmObjectAlarmValue_Type()
)
scmObjectAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmObjectAlarmValue.setStatus("current")
_StatusCodeInterfaceTable_Object = MibTable
statusCodeInterfaceTable = _StatusCodeInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 4)
)
if mibBuilder.loadTexts:
    statusCodeInterfaceTable.setStatus("current")
_StatusCodeInterfaceEntry_Object = MibTableRow
statusCodeInterfaceEntry = _StatusCodeInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 4, 1)
)
statusCodeInterfaceEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "interfaceTypeId"),
    (0, "TELESTE-LUMINATO-MIB", "scmModuleId"),
    (0, "TELESTE-LUMINATO-MIB", "sciInterfaceId"),
    (0, "TELESTE-LUMINATO-MIB", "sciObjectId"),
)
if mibBuilder.loadTexts:
    statusCodeInterfaceEntry.setStatus("current")


class _SciInterfaceId_Type(Integer32):
    """Custom type sciInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SciInterfaceId_Type.__name__ = "Integer32"
_SciInterfaceId_Object = MibTableColumn
sciInterfaceId = _SciInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 4, 1, 1),
    _SciInterfaceId_Type()
)
sciInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sciInterfaceId.setStatus("current")
_SciObjectId_Type = Unsigned32
_SciObjectId_Object = MibTableColumn
sciObjectId = _SciObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 4, 1, 2),
    _SciObjectId_Type()
)
sciObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sciObjectId.setStatus("current")
_SciObjectValue_Type = Integer32
_SciObjectValue_Object = MibTableColumn
sciObjectValue = _SciObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 4, 1, 3),
    _SciObjectValue_Type()
)
sciObjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sciObjectValue.setStatus("current")
_SciObjectDescriptor_Type = DisplayString
_SciObjectDescriptor_Object = MibTableColumn
sciObjectDescriptor = _SciObjectDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 4, 1, 4),
    _SciObjectDescriptor_Type()
)
sciObjectDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sciObjectDescriptor.setStatus("current")
_SciObjectAlarmValue_Type = Integer32
_SciObjectAlarmValue_Object = MibTableColumn
sciObjectAlarmValue = _SciObjectAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 4, 1, 5),
    _SciObjectAlarmValue_Type()
)
sciObjectAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sciObjectAlarmValue.setStatus("current")
_StatusCodeTransportStreamTable_Object = MibTable
statusCodeTransportStreamTable = _StatusCodeTransportStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 5)
)
if mibBuilder.loadTexts:
    statusCodeTransportStreamTable.setStatus("current")
_StatusCodeTransportStreamEntry_Object = MibTableRow
statusCodeTransportStreamEntry = _StatusCodeTransportStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 5, 1)
)
statusCodeTransportStreamEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "interfaceTypeId"),
    (0, "TELESTE-LUMINATO-MIB", "scmModuleId"),
    (0, "TELESTE-LUMINATO-MIB", "sciInterfaceId"),
    (0, "TELESTE-LUMINATO-MIB", "sctsTransportStreamId"),
    (0, "TELESTE-LUMINATO-MIB", "sctsObjectId"),
)
if mibBuilder.loadTexts:
    statusCodeTransportStreamEntry.setStatus("current")


class _SctsTransportStreamId_Type(Integer32):
    """Custom type sctsTransportStreamId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_SctsTransportStreamId_Type.__name__ = "Integer32"
_SctsTransportStreamId_Object = MibTableColumn
sctsTransportStreamId = _SctsTransportStreamId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 5, 1, 1),
    _SctsTransportStreamId_Type()
)
sctsTransportStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctsTransportStreamId.setStatus("current")
_SctsObjectId_Type = Unsigned32
_SctsObjectId_Object = MibTableColumn
sctsObjectId = _SctsObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 5, 1, 2),
    _SctsObjectId_Type()
)
sctsObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctsObjectId.setStatus("current")
_SctsObjectValue_Type = Integer32
_SctsObjectValue_Object = MibTableColumn
sctsObjectValue = _SctsObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 5, 1, 3),
    _SctsObjectValue_Type()
)
sctsObjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctsObjectValue.setStatus("current")
_SctsObjectDescriptor_Type = DisplayString
_SctsObjectDescriptor_Object = MibTableColumn
sctsObjectDescriptor = _SctsObjectDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 5, 1, 4),
    _SctsObjectDescriptor_Type()
)
sctsObjectDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctsObjectDescriptor.setStatus("current")
_SctsObjectAlarmValue_Type = Integer32
_SctsObjectAlarmValue_Object = MibTableColumn
sctsObjectAlarmValue = _SctsObjectAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 5, 1, 5),
    _SctsObjectAlarmValue_Type()
)
sctsObjectAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sctsObjectAlarmValue.setStatus("current")
_StatusCodeServiceTable_Object = MibTable
statusCodeServiceTable = _StatusCodeServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6)
)
if mibBuilder.loadTexts:
    statusCodeServiceTable.setStatus("current")
_StatusCodeServiceEntry_Object = MibTableRow
statusCodeServiceEntry = _StatusCodeServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6, 1)
)
statusCodeServiceEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "interfaceTypeId"),
    (0, "TELESTE-LUMINATO-MIB", "scmModuleId"),
    (0, "TELESTE-LUMINATO-MIB", "sciInterfaceId"),
    (0, "TELESTE-LUMINATO-MIB", "sctsTransportStreamId"),
    (0, "TELESTE-LUMINATO-MIB", "scsSID"),
    (0, "TELESTE-LUMINATO-MIB", "scsObjectId"),
)
if mibBuilder.loadTexts:
    statusCodeServiceEntry.setStatus("current")


class _ScsSID_Type(Integer32):
    """Custom type scsSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ScsSID_Type.__name__ = "Integer32"
_ScsSID_Object = MibTableColumn
scsSID = _ScsSID_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6, 1, 1),
    _ScsSID_Type()
)
scsSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsSID.setStatus("current")
_ScsObjectId_Type = Unsigned32
_ScsObjectId_Object = MibTableColumn
scsObjectId = _ScsObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6, 1, 2),
    _ScsObjectId_Type()
)
scsObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsObjectId.setStatus("current")
_ScsObjectValue_Type = Integer32
_ScsObjectValue_Object = MibTableColumn
scsObjectValue = _ScsObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6, 1, 3),
    _ScsObjectValue_Type()
)
scsObjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsObjectValue.setStatus("current")
_ScsObjectDescriptor_Type = DisplayString
_ScsObjectDescriptor_Object = MibTableColumn
scsObjectDescriptor = _ScsObjectDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6, 1, 4),
    _ScsObjectDescriptor_Type()
)
scsObjectDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsObjectDescriptor.setStatus("current")
_ScsServiceName_Type = DisplayString
_ScsServiceName_Object = MibTableColumn
scsServiceName = _ScsServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6, 1, 5),
    _ScsServiceName_Type()
)
scsServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsServiceName.setStatus("current")
_ScsObjectAlarmValue_Type = Integer32
_ScsObjectAlarmValue_Object = MibTableColumn
scsObjectAlarmValue = _ScsObjectAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 6, 1, 6),
    _ScsObjectAlarmValue_Type()
)
scsObjectAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsObjectAlarmValue.setStatus("current")
_StatusCodePidTable_Object = MibTable
statusCodePidTable = _StatusCodePidTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 7)
)
if mibBuilder.loadTexts:
    statusCodePidTable.setStatus("current")
_StatusCodePidEntry_Object = MibTableRow
statusCodePidEntry = _StatusCodePidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 7, 1)
)
statusCodePidEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "interfaceTypeId"),
    (0, "TELESTE-LUMINATO-MIB", "scmModuleId"),
    (0, "TELESTE-LUMINATO-MIB", "sciInterfaceId"),
    (0, "TELESTE-LUMINATO-MIB", "sctsTransportStreamId"),
    (0, "TELESTE-LUMINATO-MIB", "scpPID"),
    (0, "TELESTE-LUMINATO-MIB", "scpObjectId"),
)
if mibBuilder.loadTexts:
    statusCodePidEntry.setStatus("current")


class _ScpPID_Type(Integer32):
    """Custom type scpPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ScpPID_Type.__name__ = "Integer32"
_ScpPID_Object = MibTableColumn
scpPID = _ScpPID_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 7, 1, 1),
    _ScpPID_Type()
)
scpPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpPID.setStatus("current")
_ScpObjectId_Type = Unsigned32
_ScpObjectId_Object = MibTableColumn
scpObjectId = _ScpObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 7, 1, 2),
    _ScpObjectId_Type()
)
scpObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpObjectId.setStatus("current")
_ScpObjectValue_Type = Integer32
_ScpObjectValue_Object = MibTableColumn
scpObjectValue = _ScpObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 7, 1, 3),
    _ScpObjectValue_Type()
)
scpObjectValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpObjectValue.setStatus("current")
_ScpObjectDescriptor_Type = DisplayString
_ScpObjectDescriptor_Object = MibTableColumn
scpObjectDescriptor = _ScpObjectDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 7, 1, 4),
    _ScpObjectDescriptor_Type()
)
scpObjectDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpObjectDescriptor.setStatus("current")
_ScpObjectAlarmValue_Type = Integer32
_ScpObjectAlarmValue_Object = MibTableColumn
scpObjectAlarmValue = _ScpObjectAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 2, 7, 1, 5),
    _ScpObjectAlarmValue_Type()
)
scpObjectAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scpObjectAlarmValue.setStatus("current")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3)
)
_IfExtTable_Object = MibTable
ifExtTable = _IfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1)
)
if mibBuilder.loadTexts:
    ifExtTable.setStatus("current")
_IfExtEntry_Object = MibTableRow
ifExtEntry = _IfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1)
)
ifExtEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    ifExtEntry.setStatus("current")
_IfExtIndex_Type = Integer32
_IfExtIndex_Object = MibTableColumn
ifExtIndex = _IfExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1, 1),
    _IfExtIndex_Type()
)
ifExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifExtIndex.setStatus("current")
_IfExtName_Type = DisplayString
_IfExtName_Object = MibTableColumn
ifExtName = _IfExtName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1, 2),
    _IfExtName_Type()
)
ifExtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtName.setStatus("current")
_IfExtModule_Type = Integer32
_IfExtModule_Object = MibTableColumn
ifExtModule = _IfExtModule_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1, 3),
    _IfExtModule_Type()
)
ifExtModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtModule.setStatus("current")
_IfExtPhysInterface_Type = Integer32
_IfExtPhysInterface_Object = MibTableColumn
ifExtPhysInterface = _IfExtPhysInterface_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1, 4),
    _IfExtPhysInterface_Type()
)
ifExtPhysInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtPhysInterface.setStatus("current")
_IfExtLogiInterface_Type = Integer32
_IfExtLogiInterface_Object = MibTableColumn
ifExtLogiInterface = _IfExtLogiInterface_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1, 5),
    _IfExtLogiInterface_Type()
)
ifExtLogiInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtLogiInterface.setStatus("current")


class _IfExtDirection_Type(Integer32):
    """Custom type ifExtDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2),
          ("both", 3))
    )


_IfExtDirection_Type.__name__ = "Integer32"
_IfExtDirection_Object = MibTableColumn
ifExtDirection = _IfExtDirection_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1, 6),
    _IfExtDirection_Type()
)
ifExtDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifExtDirection.setStatus("current")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 1, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_SignalPhysTable_Object = MibTable
signalPhysTable = _SignalPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2)
)
if mibBuilder.loadTexts:
    signalPhysTable.setStatus("current")
_SignalPhysEntry_Object = MibTableRow
signalPhysEntry = _SignalPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2, 1)
)
signalPhysEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "ifExtIndex"),
)
if mibBuilder.loadTexts:
    signalPhysEntry.setStatus("current")
_SignalSnr_Type = Integer32
_SignalSnr_Object = MibTableColumn
signalSnr = _SignalSnr_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2, 1, 2),
    _SignalSnr_Type()
)
signalSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalSnr.setStatus("current")
_SignalSnrMin_Type = Integer32
_SignalSnrMin_Object = MibTableColumn
signalSnrMin = _SignalSnrMin_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2, 1, 3),
    _SignalSnrMin_Type()
)
signalSnrMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalSnrMin.setStatus("current")
_SignalSnrMax_Type = Integer32
_SignalSnrMax_Object = MibTableColumn
signalSnrMax = _SignalSnrMax_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2, 1, 4),
    _SignalSnrMax_Type()
)
signalSnrMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalSnrMax.setStatus("current")
_SignalCcErrors_Type = Integer32
_SignalCcErrors_Object = MibTableColumn
signalCcErrors = _SignalCcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2, 1, 5),
    _SignalCcErrors_Type()
)
signalCcErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalCcErrors.setStatus("current")
_SignalBer_Type = Float
_SignalBer_Object = MibTableColumn
signalBer = _SignalBer_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2, 1, 6),
    _SignalBer_Type()
)
signalBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalBer.setStatus("current")
_SignalVber_Type = Float
_SignalVber_Object = MibTableColumn
signalVber = _SignalVber_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 2, 1, 7),
    _SignalVber_Type()
)
signalVber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalVber.setStatus("current")
_TransferTable_Object = MibTable
transferTable = _TransferTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 3)
)
if mibBuilder.loadTexts:
    transferTable.setStatus("current")
_TransferEntry_Object = MibTableRow
transferEntry = _TransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 3, 1)
)
transferEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "ifExtIndex"),
)
if mibBuilder.loadTexts:
    transferEntry.setStatus("current")
_TransBitrate_Type = Integer32
_TransBitrate_Object = MibTableColumn
transBitrate = _TransBitrate_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 3, 1, 2),
    _TransBitrate_Type()
)
transBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transBitrate.setStatus("current")
_TransBitrateMin_Type = Integer32
_TransBitrateMin_Object = MibTableColumn
transBitrateMin = _TransBitrateMin_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 3, 1, 3),
    _TransBitrateMin_Type()
)
transBitrateMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transBitrateMin.setStatus("current")
_TransBitrateMax_Type = Integer32
_TransBitrateMax_Object = MibTableColumn
transBitrateMax = _TransBitrateMax_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 3, 1, 4),
    _TransBitrateMax_Type()
)
transBitrateMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transBitrateMax.setStatus("current")
_InputServiceTable_Object = MibTable
inputServiceTable = _InputServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 4)
)
if mibBuilder.loadTexts:
    inputServiceTable.setStatus("current")
_InputServiceEntry_Object = MibTableRow
inputServiceEntry = _InputServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 4, 1)
)
inputServiceEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "ifExtIndex"),
)
if mibBuilder.loadTexts:
    inputServiceEntry.setStatus("current")


class _ISID_Type(Integer32):
    """Custom type iSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ISID_Type.__name__ = "Integer32"
_ISID_Object = MibTableColumn
iSID = _ISID_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 4, 1, 2),
    _ISID_Type()
)
iSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSID.setStatus("current")
_IServiceName_Type = DisplayString
_IServiceName_Object = MibTableColumn
iServiceName = _IServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 4, 1, 3),
    _IServiceName_Type()
)
iServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iServiceName.setStatus("current")


class _IServiceBitrate_Type(Integer32):
    """Custom type iServiceBitrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IServiceBitrate_Type.__name__ = "Integer32"
_IServiceBitrate_Object = MibTableColumn
iServiceBitrate = _IServiceBitrate_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 4, 1, 4),
    _IServiceBitrate_Type()
)
iServiceBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iServiceBitrate.setStatus("current")
_OutputServiceTable_Object = MibTable
outputServiceTable = _OutputServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 5)
)
if mibBuilder.loadTexts:
    outputServiceTable.setStatus("current")
_OutputServiceEntry_Object = MibTableRow
outputServiceEntry = _OutputServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 5, 1)
)
outputServiceEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "ifExtIndex"),
)
if mibBuilder.loadTexts:
    outputServiceEntry.setStatus("current")


class _OSID_Type(Integer32):
    """Custom type oSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OSID_Type.__name__ = "Integer32"
_OSID_Object = MibTableColumn
oSID = _OSID_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 5, 1, 2),
    _OSID_Type()
)
oSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oSID.setStatus("current")
_OServiceName_Type = DisplayString
_OServiceName_Object = MibTableColumn
oServiceName = _OServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 5, 1, 3),
    _OServiceName_Type()
)
oServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oServiceName.setStatus("current")


class _OServiceBitrate_Type(Integer32):
    """Custom type oServiceBitrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OServiceBitrate_Type.__name__ = "Integer32"
_OServiceBitrate_Object = MibTableColumn
oServiceBitrate = _OServiceBitrate_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 5, 1, 4),
    _OServiceBitrate_Type()
)
oServiceBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oServiceBitrate.setStatus("current")
_ProMpegFecTable_Object = MibTable
proMpegFecTable = _ProMpegFecTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20)
)
if mibBuilder.loadTexts:
    proMpegFecTable.setStatus("current")
_ProMpegFecEntry_Object = MibTableRow
proMpegFecEntry = _ProMpegFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1)
)
proMpegFecEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "ifExtIndex"),
)
if mibBuilder.loadTexts:
    proMpegFecEntry.setStatus("current")
_FecValidPkts_Type = Counter32
_FecValidPkts_Object = MibTableColumn
fecValidPkts = _FecValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1, 1),
    _FecValidPkts_Type()
)
fecValidPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecValidPkts.setStatus("current")
_FecUncorrectedPkts_Type = Counter32
_FecUncorrectedPkts_Object = MibTableColumn
fecUncorrectedPkts = _FecUncorrectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1, 2),
    _FecUncorrectedPkts_Type()
)
fecUncorrectedPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecUncorrectedPkts.setStatus("current")
_FecCorrectedPkts_Type = Counter32
_FecCorrectedPkts_Object = MibTableColumn
fecCorrectedPkts = _FecCorrectedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1, 3),
    _FecCorrectedPkts_Type()
)
fecCorrectedPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecCorrectedPkts.setStatus("current")
_FecDuplicatePkts_Type = Counter32
_FecDuplicatePkts_Object = MibTableColumn
fecDuplicatePkts = _FecDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1, 4),
    _FecDuplicatePkts_Type()
)
fecDuplicatePkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecDuplicatePkts.setStatus("current")
_FecReorderedPkts_Type = Counter32
_FecReorderedPkts_Object = MibTableColumn
fecReorderedPkts = _FecReorderedPkts_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1, 5),
    _FecReorderedPkts_Type()
)
fecReorderedPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecReorderedPkts.setStatus("current")
_FecIncorrectSeqNumbers_Type = Counter32
_FecIncorrectSeqNumbers_Object = MibTableColumn
fecIncorrectSeqNumbers = _FecIncorrectSeqNumbers_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1, 6),
    _FecIncorrectSeqNumbers_Type()
)
fecIncorrectSeqNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecIncorrectSeqNumbers.setStatus("current")
_FecDiscontinuities_Type = Counter32
_FecDiscontinuities_Object = MibTableColumn
fecDiscontinuities = _FecDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 3, 20, 1, 7),
    _FecDiscontinuities_Type()
)
fecDiscontinuities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fecDiscontinuities.setStatus("current")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 4)
)
_StatusFlags_ObjectIdentity = ObjectIdentity
statusFlags = _StatusFlags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5)
)
_ModuleStatusTable_Object = MibTable
moduleStatusTable = _ModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2)
)
if mibBuilder.loadTexts:
    moduleStatusTable.setStatus("current")
_ModuleStatusEntry_Object = MibTableRow
moduleStatusEntry = _ModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1)
)
moduleStatusEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "moduleId"),
)
if mibBuilder.loadTexts:
    moduleStatusEntry.setStatus("current")
_ModuleId_Type = Integer32
_ModuleId_Object = MibTableColumn
moduleId = _ModuleId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 1),
    _ModuleId_Type()
)
moduleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleId.setStatus("current")


class _ModulePidConflictStatus_Type(Integer32):
    """Custom type modulePidConflictStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pidOk", 1),
          ("pidConflict", 2))
    )


_ModulePidConflictStatus_Type.__name__ = "Integer32"
_ModulePidConflictStatus_Object = MibTableColumn
modulePidConflictStatus = _ModulePidConflictStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4),
    _ModulePidConflictStatus_Type()
)
modulePidConflictStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePidConflictStatus.setStatus("current")


class _ModuleTemperatureHigh_Type(Integer32):
    """Custom type moduleTemperatureHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureNominal", 1),
          ("temperatureHigh", 2))
    )


_ModuleTemperatureHigh_Type.__name__ = "Integer32"
_ModuleTemperatureHigh_Object = MibTableColumn
moduleTemperatureHigh = _ModuleTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 6),
    _ModuleTemperatureHigh_Type()
)
moduleTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperatureHigh.setStatus("current")


class _ModuleTemperatureLow_Type(Integer32):
    """Custom type moduleTemperatureLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureNominal", 1),
          ("temperatureLow", 2))
    )


_ModuleTemperatureLow_Type.__name__ = "Integer32"
_ModuleTemperatureLow_Object = MibTableColumn
moduleTemperatureLow = _ModuleTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 7),
    _ModuleTemperatureLow_Type()
)
moduleTemperatureLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperatureLow.setStatus("current")


class _ModulePidCapaStatus_Type(Integer32):
    """Custom type modulePidCapaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capacityNominal", 1),
          ("capacityExceeded", 2))
    )


_ModulePidCapaStatus_Type.__name__ = "Integer32"
_ModulePidCapaStatus_Object = MibTableColumn
modulePidCapaStatus = _ModulePidCapaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4104),
    _ModulePidCapaStatus_Type()
)
modulePidCapaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePidCapaStatus.setStatus("current")


class _ModulePsisiCaptureCapaStatus_Type(Integer32):
    """Custom type modulePsisiCaptureCapaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capacityNominal", 1),
          ("capacityExceeded", 2))
    )


_ModulePsisiCaptureCapaStatus_Type.__name__ = "Integer32"
_ModulePsisiCaptureCapaStatus_Object = MibTableColumn
modulePsisiCaptureCapaStatus = _ModulePsisiCaptureCapaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4105),
    _ModulePsisiCaptureCapaStatus_Type()
)
modulePsisiCaptureCapaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePsisiCaptureCapaStatus.setStatus("current")


class _ModuleSidAllocStatus_Type(Integer32):
    """Custom type moduleSidAllocStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sidAllocOk", 1),
          ("sidAllocCapaExceeded", 2))
    )


_ModuleSidAllocStatus_Type.__name__ = "Integer32"
_ModuleSidAllocStatus_Object = MibTableColumn
moduleSidAllocStatus = _ModuleSidAllocStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4106),
    _ModuleSidAllocStatus_Type()
)
moduleSidAllocStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSidAllocStatus.setStatus("current")


class _ModuleCaDetectStatus_Type(Integer32):
    """Custom type moduleCaDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleOk", 1),
          ("moduleMissing", 2))
    )


_ModuleCaDetectStatus_Type.__name__ = "Integer32"
_ModuleCaDetectStatus_Object = MibTableColumn
moduleCaDetectStatus = _ModuleCaDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4108),
    _ModuleCaDetectStatus_Type()
)
moduleCaDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCaDetectStatus.setStatus("current")


class _ModuleDetectStatus_Type(Integer32):
    """Custom type moduleDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleOk", 1),
          ("moduleUnknown", 2))
    )


_ModuleDetectStatus_Type.__name__ = "Integer32"
_ModuleDetectStatus_Object = MibTableColumn
moduleDetectStatus = _ModuleDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4111),
    _ModuleDetectStatus_Type()
)
moduleDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDetectStatus.setStatus("current")


class _ModuleVoltageHigh_Type(Integer32):
    """Custom type moduleVoltageHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voltageNominal", 1),
          ("voltageHigh", 2))
    )


_ModuleVoltageHigh_Type.__name__ = "Integer32"
_ModuleVoltageHigh_Object = MibTableColumn
moduleVoltageHigh = _ModuleVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4112),
    _ModuleVoltageHigh_Type()
)
moduleVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltageHigh.setStatus("current")


class _ModuleVoltageLow_Type(Integer32):
    """Custom type moduleVoltageLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voltageNominal", 1),
          ("voltageLow", 2))
    )


_ModuleVoltageLow_Type.__name__ = "Integer32"
_ModuleVoltageLow_Object = MibTableColumn
moduleVoltageLow = _ModuleVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4113),
    _ModuleVoltageLow_Type()
)
moduleVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleVoltageLow.setStatus("current")


class _ModuleCurrentHigh_Type(Integer32):
    """Custom type moduleCurrentHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentNominal", 1),
          ("currentHigh", 2))
    )


_ModuleCurrentHigh_Type.__name__ = "Integer32"
_ModuleCurrentHigh_Object = MibTableColumn
moduleCurrentHigh = _ModuleCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4114),
    _ModuleCurrentHigh_Type()
)
moduleCurrentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentHigh.setStatus("current")


class _ModuleCurrentLow_Type(Integer32):
    """Custom type moduleCurrentLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentNominal", 1),
          ("currentLow", 2))
    )


_ModuleCurrentLow_Type.__name__ = "Integer32"
_ModuleCurrentLow_Object = MibTableColumn
moduleCurrentLow = _ModuleCurrentLow_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4115),
    _ModuleCurrentLow_Type()
)
moduleCurrentLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCurrentLow.setStatus("current")


class _ModuleDaemonInitStatus_Type(Integer32):
    """Custom type moduleDaemonInitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daemonNominal", 1),
          ("daemonInitFailed", 2))
    )


_ModuleDaemonInitStatus_Type.__name__ = "Integer32"
_ModuleDaemonInitStatus_Object = MibTableColumn
moduleDaemonInitStatus = _ModuleDaemonInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4127),
    _ModuleDaemonInitStatus_Type()
)
moduleDaemonInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDaemonInitStatus.setStatus("current")


class _ModuleDriverStatus_Type(Integer32):
    """Custom type moduleDriverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("driverNominal", 1),
          ("driverFailure", 2))
    )


_ModuleDriverStatus_Type.__name__ = "Integer32"
_ModuleDriverStatus_Object = MibTableColumn
moduleDriverStatus = _ModuleDriverStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4129),
    _ModuleDriverStatus_Type()
)
moduleDriverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDriverStatus.setStatus("current")


class _ModuleHwStatus_Type(Integer32):
    """Custom type moduleHwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hwNominal", 1),
          ("hwFailure", 2))
    )


_ModuleHwStatus_Type.__name__ = "Integer32"
_ModuleHwStatus_Object = MibTableColumn
moduleHwStatus = _ModuleHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4130),
    _ModuleHwStatus_Type()
)
moduleHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwStatus.setStatus("current")


class _ModuleFanStatus_Type(Integer32):
    """Custom type moduleFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanNominal", 1),
          ("fanFailure", 2))
    )


_ModuleFanStatus_Type.__name__ = "Integer32"
_ModuleFanStatus_Object = MibTableColumn
moduleFanStatus = _ModuleFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4131),
    _ModuleFanStatus_Type()
)
moduleFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFanStatus.setStatus("current")


class _ModulePowerSourceStatus_Type(Integer32):
    """Custom type modulePowerSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("runningOnMainPower", 1),
          ("runningOnBackupPower", 2))
    )


_ModulePowerSourceStatus_Type.__name__ = "Integer32"
_ModulePowerSourceStatus_Object = MibTableColumn
modulePowerSourceStatus = _ModulePowerSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4132),
    _ModulePowerSourceStatus_Type()
)
modulePowerSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePowerSourceStatus.setStatus("current")


class _ModulePsuOverloadStatus_Type(Integer32):
    """Custom type modulePsuOverloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psuNominal", 1),
          ("psuOverloaded", 2))
    )


_ModulePsuOverloadStatus_Type.__name__ = "Integer32"
_ModulePsuOverloadStatus_Object = MibTableColumn
modulePsuOverloadStatus = _ModulePsuOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4133),
    _ModulePsuOverloadStatus_Type()
)
modulePsuOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePsuOverloadStatus.setStatus("current")


class _ModuleBootupProgressStatus_Type(Integer32):
    """Custom type moduleBootupProgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleBootingUp", 2))
    )


_ModuleBootupProgressStatus_Type.__name__ = "Integer32"
_ModuleBootupProgressStatus_Object = MibTableColumn
moduleBootupProgressStatus = _ModuleBootupProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4134),
    _ModuleBootupProgressStatus_Type()
)
moduleBootupProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBootupProgressStatus.setStatus("current")


class _ModuleBootupRetryStatus_Type(Integer32):
    """Custom type moduleBootupRetryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleBootingRetrying", 2))
    )


_ModuleBootupRetryStatus_Type.__name__ = "Integer32"
_ModuleBootupRetryStatus_Object = MibTableColumn
moduleBootupRetryStatus = _ModuleBootupRetryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4135),
    _ModuleBootupRetryStatus_Type()
)
moduleBootupRetryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBootupRetryStatus.setStatus("current")


class _ModuleBootupStatus_Type(Integer32):
    """Custom type moduleBootupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleBootFailure", 2))
    )


_ModuleBootupStatus_Type.__name__ = "Integer32"
_ModuleBootupStatus_Object = MibTableColumn
moduleBootupStatus = _ModuleBootupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4136),
    _ModuleBootupStatus_Type()
)
moduleBootupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBootupStatus.setStatus("current")


class _ModuleShutdownProgressStatus_Type(Integer32):
    """Custom type moduleShutdownProgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleShuttingDown", 2))
    )


_ModuleShutdownProgressStatus_Type.__name__ = "Integer32"
_ModuleShutdownProgressStatus_Object = MibTableColumn
moduleShutdownProgressStatus = _ModuleShutdownProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4137),
    _ModuleShutdownProgressStatus_Type()
)
moduleShutdownProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleShutdownProgressStatus.setStatus("current")


class _ModuleConnStatus_Type(Integer32):
    """Custom type moduleConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectionNominal", 1),
          ("connectionLost", 2))
    )


_ModuleConnStatus_Type.__name__ = "Integer32"
_ModuleConnStatus_Object = MibTableColumn
moduleConnStatus = _ModuleConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4138),
    _ModuleConnStatus_Type()
)
moduleConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleConnStatus.setStatus("current")


class _ModuleCompatStatus_Type(Integer32):
    """Custom type moduleCompatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleIncompatible", 2))
    )


_ModuleCompatStatus_Type.__name__ = "Integer32"
_ModuleCompatStatus_Object = MibTableColumn
moduleCompatStatus = _ModuleCompatStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4139),
    _ModuleCompatStatus_Type()
)
moduleCompatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCompatStatus.setStatus("current")


class _ModuleUpcPowerLow_Type(Integer32):
    """Custom type moduleUpcPowerLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ucpPowerNominal", 1),
          ("ucpPowerLow", 2))
    )


_ModuleUpcPowerLow_Type.__name__ = "Integer32"
_ModuleUpcPowerLow_Object = MibTableColumn
moduleUpcPowerLow = _ModuleUpcPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4147),
    _ModuleUpcPowerLow_Type()
)
moduleUpcPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleUpcPowerLow.setStatus("current")


class _ModuleUpcPowerHigh_Type(Integer32):
    """Custom type moduleUpcPowerHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ucpPowerNominal", 1),
          ("ucpPowerHigh", 2))
    )


_ModuleUpcPowerHigh_Type.__name__ = "Integer32"
_ModuleUpcPowerHigh_Object = MibTableColumn
moduleUpcPowerHigh = _ModuleUpcPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4148),
    _ModuleUpcPowerHigh_Type()
)
moduleUpcPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleUpcPowerHigh.setStatus("current")


class _ModuleCalibrDataStatus_Type(Integer32):
    """Custom type moduleCalibrDataStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("calibrationDataNominal", 1),
          ("calibrationDataMissing", 2))
    )


_ModuleCalibrDataStatus_Type.__name__ = "Integer32"
_ModuleCalibrDataStatus_Object = MibTableColumn
moduleCalibrDataStatus = _ModuleCalibrDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4149),
    _ModuleCalibrDataStatus_Type()
)
moduleCalibrDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCalibrDataStatus.setStatus("current")


class _ModuleCalibrDataCheckStatus_Type(Integer32):
    """Custom type moduleCalibrDataCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkOk", 1),
          ("checkSkipped", 2))
    )


_ModuleCalibrDataCheckStatus_Type.__name__ = "Integer32"
_ModuleCalibrDataCheckStatus_Object = MibTableColumn
moduleCalibrDataCheckStatus = _ModuleCalibrDataCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4150),
    _ModuleCalibrDataCheckStatus_Type()
)
moduleCalibrDataCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCalibrDataCheckStatus.setStatus("current")


class _ModuleDescrStatus_Type(Integer32):
    """Custom type moduleDescrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descramblingOk", 1),
          ("descramblingFailure", 2))
    )


_ModuleDescrStatus_Type.__name__ = "Integer32"
_ModuleDescrStatus_Object = MibTableColumn
moduleDescrStatus = _ModuleDescrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4151),
    _ModuleDescrStatus_Type()
)
moduleDescrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescrStatus.setStatus("current")


class _ModuleBackupStatus_Type(Integer32):
    """Custom type moduleBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleSwitchedToBackup", 2))
    )


_ModuleBackupStatus_Type.__name__ = "Integer32"
_ModuleBackupStatus_Object = MibTableColumn
moduleBackupStatus = _ModuleBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4153),
    _ModuleBackupStatus_Type()
)
moduleBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupStatus.setStatus("current")


class _ModuleNitOutputsStatus_Type(Integer32):
    """Custom type moduleNitOutputsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nitOutputsNominal", 1),
          ("noSupportedNitOutputs", 2))
    )


_ModuleNitOutputsStatus_Type.__name__ = "Integer32"
_ModuleNitOutputsStatus_Object = MibTableColumn
moduleNitOutputsStatus = _ModuleNitOutputsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4154),
    _ModuleNitOutputsStatus_Type()
)
moduleNitOutputsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNitOutputsStatus.setStatus("current")


class _ModuleNitSelectionStatus_Type(Integer32):
    """Custom type moduleNitSelectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nitSelectionNominal", 1),
          ("noSelectedNitOutputs", 2))
    )


_ModuleNitSelectionStatus_Type.__name__ = "Integer32"
_ModuleNitSelectionStatus_Object = MibTableColumn
moduleNitSelectionStatus = _ModuleNitSelectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4155),
    _ModuleNitSelectionStatus_Type()
)
moduleNitSelectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNitSelectionStatus.setStatus("current")


class _ModuleNitConfChangeStatus_Type(Integer32):
    """Custom type moduleNitConfChangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nitConfNominal", 1),
          ("nitConfChanged", 2))
    )


_ModuleNitConfChangeStatus_Type.__name__ = "Integer32"
_ModuleNitConfChangeStatus_Object = MibTableColumn
moduleNitConfChangeStatus = _ModuleNitConfChangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4156),
    _ModuleNitConfChangeStatus_Type()
)
moduleNitConfChangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNitConfChangeStatus.setStatus("current")


class _ModuleNitDataQueryStatus_Type(Integer32):
    """Custom type moduleNitDataQueryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nitDataQueryNominal", 1),
          ("nitDataQueryFailure", 2))
    )


_ModuleNitDataQueryStatus_Type.__name__ = "Integer32"
_ModuleNitDataQueryStatus_Object = MibTableColumn
moduleNitDataQueryStatus = _ModuleNitDataQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4157),
    _ModuleNitDataQueryStatus_Type()
)
moduleNitDataQueryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNitDataQueryStatus.setStatus("current")


class _ModuleNitWizardStatus_Type(Integer32):
    """Custom type moduleNitWizardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nitWizardNominal", 1),
          ("nitWizardFailure", 2))
    )


_ModuleNitWizardStatus_Type.__name__ = "Integer32"
_ModuleNitWizardStatus_Object = MibTableColumn
moduleNitWizardStatus = _ModuleNitWizardStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4158),
    _ModuleNitWizardStatus_Type()
)
moduleNitWizardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNitWizardStatus.setStatus("current")


class _ModuleQamFreqStatus_Type(Integer32):
    """Custom type moduleQamFreqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qamFreqUnique", 1),
          ("qamFreqDuplicate", 2))
    )


_ModuleQamFreqStatus_Type.__name__ = "Integer32"
_ModuleQamFreqStatus_Object = MibTableColumn
moduleQamFreqStatus = _ModuleQamFreqStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4159),
    _ModuleQamFreqStatus_Type()
)
moduleQamFreqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleQamFreqStatus.setStatus("current")


class _ModuleOutputSidStatus_Type(Integer32):
    """Custom type moduleOutputSidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sidOk", 1),
          ("sidConflict", 2))
    )


_ModuleOutputSidStatus_Type.__name__ = "Integer32"
_ModuleOutputSidStatus_Object = MibTableColumn
moduleOutputSidStatus = _ModuleOutputSidStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4173),
    _ModuleOutputSidStatus_Type()
)
moduleOutputSidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleOutputSidStatus.setStatus("current")


class _ModuleConfStatus_Type(Integer32):
    """Custom type moduleConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurationOk", 1),
          ("configurationUnsupported", 2))
    )


_ModuleConfStatus_Type.__name__ = "Integer32"
_ModuleConfStatus_Object = MibTableColumn
moduleConfStatus = _ModuleConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4175),
    _ModuleConfStatus_Type()
)
moduleConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleConfStatus.setStatus("current")


class _ModuleFreqStatus_Type(Integer32):
    """Custom type moduleFreqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freqOk", 1),
          ("freqOutOfRange", 2))
    )


_ModuleFreqStatus_Type.__name__ = "Integer32"
_ModuleFreqStatus_Object = MibTableColumn
moduleFreqStatus = _ModuleFreqStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4176),
    _ModuleFreqStatus_Type()
)
moduleFreqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFreqStatus.setStatus("current")


class _ModuleOutputPowerStatus_Type(Integer32):
    """Custom type moduleOutputPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerOk", 1),
          ("powerOutOfRange", 2))
    )


_ModuleOutputPowerStatus_Type.__name__ = "Integer32"
_ModuleOutputPowerStatus_Object = MibTableColumn
moduleOutputPowerStatus = _ModuleOutputPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4177),
    _ModuleOutputPowerStatus_Type()
)
moduleOutputPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleOutputPowerStatus.setStatus("current")


class _ModuleSymrateStatus_Type(Integer32):
    """Custom type moduleSymrateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("symbolRateOk", 1),
          ("symbolRateOutOfRange", 2))
    )


_ModuleSymrateStatus_Type.__name__ = "Integer32"
_ModuleSymrateStatus_Object = MibTableColumn
moduleSymrateStatus = _ModuleSymrateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4178),
    _ModuleSymrateStatus_Type()
)
moduleSymrateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSymrateStatus.setStatus("current")


class _ModuleChanDistStatus_Type(Integer32):
    """Custom type moduleChanDistStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chanDistOk", 1),
          ("chanDistTooNarrow", 2))
    )


_ModuleChanDistStatus_Type.__name__ = "Integer32"
_ModuleChanDistStatus_Object = MibTableColumn
moduleChanDistStatus = _ModuleChanDistStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4179),
    _ModuleChanDistStatus_Type()
)
moduleChanDistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleChanDistStatus.setStatus("current")


class _ModuleLnbVoltStatus_Type(Integer32):
    """Custom type moduleLnbVoltStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lnbVoltageOk", 1),
          ("lnbVoltageInvalid", 2))
    )


_ModuleLnbVoltStatus_Type.__name__ = "Integer32"
_ModuleLnbVoltStatus_Object = MibTableColumn
moduleLnbVoltStatus = _ModuleLnbVoltStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4180),
    _ModuleLnbVoltStatus_Type()
)
moduleLnbVoltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLnbVoltStatus.setStatus("current")


class _ModuleFecRateStatus_Type(Integer32):
    """Custom type moduleFecRateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fecRateOk", 1),
          ("fecRateInvalid", 2))
    )


_ModuleFecRateStatus_Type.__name__ = "Integer32"
_ModuleFecRateStatus_Object = MibTableColumn
moduleFecRateStatus = _ModuleFecRateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4181),
    _ModuleFecRateStatus_Type()
)
moduleFecRateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFecRateStatus.setStatus("current")


class _ModuleLnbCurrStatus_Type(Integer32):
    """Custom type moduleLnbCurrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lnbCurrentOk", 1),
          ("lnbCurrentInvalid", 2))
    )


_ModuleLnbCurrStatus_Type.__name__ = "Integer32"
_ModuleLnbCurrStatus_Object = MibTableColumn
moduleLnbCurrStatus = _ModuleLnbCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4182),
    _ModuleLnbCurrStatus_Type()
)
moduleLnbCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLnbCurrStatus.setStatus("current")


class _ModuleFreqOffsetStatus_Type(Integer32):
    """Custom type moduleFreqOffsetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freqOffsetOk", 1),
          ("freqOffsetInvalid", 2))
    )


_ModuleFreqOffsetStatus_Type.__name__ = "Integer32"
_ModuleFreqOffsetStatus_Object = MibTableColumn
moduleFreqOffsetStatus = _ModuleFreqOffsetStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4183),
    _ModuleFreqOffsetStatus_Type()
)
moduleFreqOffsetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFreqOffsetStatus.setStatus("current")


class _ModuleDescrRestartStatus_Type(Integer32):
    """Custom type moduleDescrRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descramblingNominal", 1),
          ("descramblingRestarting", 2))
    )


_ModuleDescrRestartStatus_Type.__name__ = "Integer32"
_ModuleDescrRestartStatus_Object = MibTableColumn
moduleDescrRestartStatus = _ModuleDescrRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4185),
    _ModuleDescrRestartStatus_Type()
)
moduleDescrRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescrRestartStatus.setStatus("current")


class _ModuleCamRestartStatus_Type(Integer32):
    """Custom type moduleCamRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("camNominal", 1),
          ("camRestarting", 2))
    )


_ModuleCamRestartStatus_Type.__name__ = "Integer32"
_ModuleCamRestartStatus_Object = MibTableColumn
moduleCamRestartStatus = _ModuleCamRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4186),
    _ModuleCamRestartStatus_Type()
)
moduleCamRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCamRestartStatus.setStatus("current")


class _ModuleEcmgStatus_Type(Integer32):
    """Custom type moduleEcmgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecmgNominal", 1),
          ("ecmgFailure", 2))
    )


_ModuleEcmgStatus_Type.__name__ = "Integer32"
_ModuleEcmgStatus_Object = MibTableColumn
moduleEcmgStatus = _ModuleEcmgStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4187),
    _ModuleEcmgStatus_Type()
)
moduleEcmgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEcmgStatus.setStatus("current")


class _ModuleEcmStreamStatus_Type(Integer32):
    """Custom type moduleEcmStreamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecmStreamNominal", 1),
          ("ecmStreamFailure", 2))
    )


_ModuleEcmStreamStatus_Type.__name__ = "Integer32"
_ModuleEcmStreamStatus_Object = MibTableColumn
moduleEcmStreamStatus = _ModuleEcmStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4188),
    _ModuleEcmStreamStatus_Type()
)
moduleEcmStreamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEcmStreamStatus.setStatus("current")


class _ModuleEmmStatus_Type(Integer32):
    """Custom type moduleEmmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emmNominal", 1),
          ("emmFailure", 2))
    )


_ModuleEmmStatus_Type.__name__ = "Integer32"
_ModuleEmmStatus_Object = MibTableColumn
moduleEmmStatus = _ModuleEmmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4189),
    _ModuleEmmStatus_Type()
)
moduleEmmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEmmStatus.setStatus("current")


class _ModuleEmmStreamStatus_Type(Integer32):
    """Custom type moduleEmmStreamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emmStreamNominal", 1),
          ("emmStreamFailure", 2))
    )


_ModuleEmmStreamStatus_Type.__name__ = "Integer32"
_ModuleEmmStreamStatus_Object = MibTableColumn
moduleEmmStreamStatus = _ModuleEmmStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4190),
    _ModuleEmmStreamStatus_Type()
)
moduleEmmStreamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEmmStreamStatus.setStatus("current")


class _ModuleEcmgConnStatus_Type(Integer32):
    """Custom type moduleEcmgConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecmgConnNominal", 1),
          ("ecmgNotConnected", 2))
    )


_ModuleEcmgConnStatus_Type.__name__ = "Integer32"
_ModuleEcmgConnStatus_Object = MibTableColumn
moduleEcmgConnStatus = _ModuleEcmgConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4191),
    _ModuleEcmgConnStatus_Type()
)
moduleEcmgConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEcmgConnStatus.setStatus("current")


class _ModuleEmmConnStatus_Type(Integer32):
    """Custom type moduleEmmConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emmConnNominal", 1),
          ("emmNotConnected", 2))
    )


_ModuleEmmConnStatus_Type.__name__ = "Integer32"
_ModuleEmmConnStatus_Object = MibTableColumn
moduleEmmConnStatus = _ModuleEmmConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4192),
    _ModuleEmmConnStatus_Type()
)
moduleEmmConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEmmConnStatus.setStatus("current")


class _ModuleEcmgSpareStatus_Type(Integer32):
    """Custom type moduleEcmgSpareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecmgNominal", 1),
          ("ecmgSwitchedToSpare", 2))
    )


_ModuleEcmgSpareStatus_Type.__name__ = "Integer32"
_ModuleEcmgSpareStatus_Object = MibTableColumn
moduleEcmgSpareStatus = _ModuleEcmgSpareStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4194),
    _ModuleEcmgSpareStatus_Type()
)
moduleEcmgSpareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEcmgSpareStatus.setStatus("current")


class _ModuleBootloaderAvailStatus_Type(Integer32):
    """Custom type moduleBootloaderAvailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootloaderOk", 1),
          ("bootloaderObsolete", 2))
    )


_ModuleBootloaderAvailStatus_Type.__name__ = "Integer32"
_ModuleBootloaderAvailStatus_Object = MibTableColumn
moduleBootloaderAvailStatus = _ModuleBootloaderAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4195),
    _ModuleBootloaderAvailStatus_Type()
)
moduleBootloaderAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBootloaderAvailStatus.setStatus("current")


class _ModuleBl1UpdateProgStatus_Type(Integer32):
    """Custom type moduleBl1UpdateProgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootloaderNominal", 1),
          ("bootloaderUpdating", 2))
    )


_ModuleBl1UpdateProgStatus_Type.__name__ = "Integer32"
_ModuleBl1UpdateProgStatus_Object = MibTableColumn
moduleBl1UpdateProgStatus = _ModuleBl1UpdateProgStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4196),
    _ModuleBl1UpdateProgStatus_Type()
)
moduleBl1UpdateProgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBl1UpdateProgStatus.setStatus("current")


class _ModuleBl2UpdateProgStatus_Type(Integer32):
    """Custom type moduleBl2UpdateProgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootloaderNominal", 1),
          ("bootloaderUpdating", 2))
    )


_ModuleBl2UpdateProgStatus_Type.__name__ = "Integer32"
_ModuleBl2UpdateProgStatus_Object = MibTableColumn
moduleBl2UpdateProgStatus = _ModuleBl2UpdateProgStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4197),
    _ModuleBl2UpdateProgStatus_Type()
)
moduleBl2UpdateProgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBl2UpdateProgStatus.setStatus("current")


class _ModuleBl1UpdateStatus_Type(Integer32):
    """Custom type moduleBl1UpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootloaderNominal", 1),
          ("bootloaderUpdateFailure", 2))
    )


_ModuleBl1UpdateStatus_Type.__name__ = "Integer32"
_ModuleBl1UpdateStatus_Object = MibTableColumn
moduleBl1UpdateStatus = _ModuleBl1UpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4198),
    _ModuleBl1UpdateStatus_Type()
)
moduleBl1UpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBl1UpdateStatus.setStatus("current")


class _ModuleBl2UpdateStatus_Type(Integer32):
    """Custom type moduleBl2UpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootloaderNominal", 1),
          ("bootloaderUpdateFailure", 2))
    )


_ModuleBl2UpdateStatus_Type.__name__ = "Integer32"
_ModuleBl2UpdateStatus_Object = MibTableColumn
moduleBl2UpdateStatus = _ModuleBl2UpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4199),
    _ModuleBl2UpdateStatus_Type()
)
moduleBl2UpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBl2UpdateStatus.setStatus("current")


class _ModuleActiveBackupStatus_Type(Integer32):
    """Custom type moduleActiveBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupPassive", 1),
          ("backupActive", 2))
    )


_ModuleActiveBackupStatus_Type.__name__ = "Integer32"
_ModuleActiveBackupStatus_Object = MibTableColumn
moduleActiveBackupStatus = _ModuleActiveBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4203),
    _ModuleActiveBackupStatus_Type()
)
moduleActiveBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleActiveBackupStatus.setStatus("current")


class _ModuleConfProgressStatus_Type(Integer32):
    """Custom type moduleConfProgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleConfiguring", 2))
    )


_ModuleConfProgressStatus_Type.__name__ = "Integer32"
_ModuleConfProgressStatus_Object = MibTableColumn
moduleConfProgressStatus = _ModuleConfProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4205),
    _ModuleConfProgressStatus_Type()
)
moduleConfProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleConfProgressStatus.setStatus("current")


class _ModulePresenceStatus_Type(Integer32):
    """Custom type modulePresenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("noModule", 2))
    )


_ModulePresenceStatus_Type.__name__ = "Integer32"
_ModulePresenceStatus_Object = MibTableColumn
modulePresenceStatus = _ModulePresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4206),
    _ModulePresenceStatus_Type()
)
modulePresenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePresenceStatus.setStatus("current")


class _ModuleProcessRestartStatus_Type(Integer32):
    """Custom type moduleProcessRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("processesNominal", 1),
          ("processRestarted", 2))
    )


_ModuleProcessRestartStatus_Type.__name__ = "Integer32"
_ModuleProcessRestartStatus_Object = MibTableColumn
moduleProcessRestartStatus = _ModuleProcessRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4208),
    _ModuleProcessRestartStatus_Type()
)
moduleProcessRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleProcessRestartStatus.setStatus("current")


class _ModuleBackupLicenseStatus_Type(Integer32):
    """Custom type moduleBackupLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModuleBackupLicenseStatus_Type.__name__ = "Integer32"
_ModuleBackupLicenseStatus_Object = MibTableColumn
moduleBackupLicenseStatus = _ModuleBackupLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4209),
    _ModuleBackupLicenseStatus_Type()
)
moduleBackupLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupLicenseStatus.setStatus("current")


class _ModulePsisiEditorLicenseStatus_Type(Integer32):
    """Custom type modulePsisiEditorLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModulePsisiEditorLicenseStatus_Type.__name__ = "Integer32"
_ModulePsisiEditorLicenseStatus_Object = MibTableColumn
modulePsisiEditorLicenseStatus = _ModulePsisiEditorLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4210),
    _ModulePsisiEditorLicenseStatus_Type()
)
modulePsisiEditorLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePsisiEditorLicenseStatus.setStatus("current")


class _ModuleMuxLicenseStatus_Type(Integer32):
    """Custom type moduleMuxLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModuleMuxLicenseStatus_Type.__name__ = "Integer32"
_ModuleMuxLicenseStatus_Object = MibTableColumn
moduleMuxLicenseStatus = _ModuleMuxLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4211),
    _ModuleMuxLicenseStatus_Type()
)
moduleMuxLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMuxLicenseStatus.setStatus("current")


class _ModuleDemuxLicenseStatus_Type(Integer32):
    """Custom type moduleDemuxLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModuleDemuxLicenseStatus_Type.__name__ = "Integer32"
_ModuleDemuxLicenseStatus_Object = MibTableColumn
moduleDemuxLicenseStatus = _ModuleDemuxLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4212),
    _ModuleDemuxLicenseStatus_Type()
)
moduleDemuxLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDemuxLicenseStatus.setStatus("current")


class _ModuleDvbLicenseStatus_Type(Integer32):
    """Custom type moduleDvbLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModuleDvbLicenseStatus_Type.__name__ = "Integer32"
_ModuleDvbLicenseStatus_Object = MibTableColumn
moduleDvbLicenseStatus = _ModuleDvbLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4213),
    _ModuleDvbLicenseStatus_Type()
)
moduleDvbLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDvbLicenseStatus.setStatus("current")


class _ModuleMsdLicenseStatus_Type(Integer32):
    """Custom type moduleMsdLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModuleMsdLicenseStatus_Type.__name__ = "Integer32"
_ModuleMsdLicenseStatus_Object = MibTableColumn
moduleMsdLicenseStatus = _ModuleMsdLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4214),
    _ModuleMsdLicenseStatus_Type()
)
moduleMsdLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMsdLicenseStatus.setStatus("current")


class _ModuleDvbs2LicenseStatus_Type(Integer32):
    """Custom type moduleDvbs2LicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModuleDvbs2LicenseStatus_Type.__name__ = "Integer32"
_ModuleDvbs2LicenseStatus_Object = MibTableColumn
moduleDvbs2LicenseStatus = _ModuleDvbs2LicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4215),
    _ModuleDvbs2LicenseStatus_Type()
)
moduleDvbs2LicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDvbs2LicenseStatus.setStatus("current")


class _ModuleDvbt2LicenseStatus_Type(Integer32):
    """Custom type moduleDvbt2LicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("notLicensed", 2))
    )


_ModuleDvbt2LicenseStatus_Type.__name__ = "Integer32"
_ModuleDvbt2LicenseStatus_Object = MibTableColumn
moduleDvbt2LicenseStatus = _ModuleDvbt2LicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4216),
    _ModuleDvbt2LicenseStatus_Type()
)
moduleDvbt2LicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDvbt2LicenseStatus.setStatus("current")


class _ModuleScsLicenseStatus_Type(Integer32):
    """Custom type moduleScsLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseValid", 1),
          ("notLicensed", 2))
    )


_ModuleScsLicenseStatus_Type.__name__ = "Integer32"
_ModuleScsLicenseStatus_Object = MibTableColumn
moduleScsLicenseStatus = _ModuleScsLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4217),
    _ModuleScsLicenseStatus_Type()
)
moduleScsLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleScsLicenseStatus.setStatus("current")


class _ModuleCliLoginStatus_Type(Integer32):
    """Custom type moduleCliLoginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cliNotLoggedIn", 1),
          ("cliLoggedIn", 2))
    )


_ModuleCliLoginStatus_Type.__name__ = "Integer32"
_ModuleCliLoginStatus_Object = MibTableColumn
moduleCliLoginStatus = _ModuleCliLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4218),
    _ModuleCliLoginStatus_Type()
)
moduleCliLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCliLoginStatus.setStatus("current")


class _ModuleRedunActivationStatus_Type(Integer32):
    """Custom type moduleRedunActivationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundancyPassive", 1),
          ("redundancyActivated", 2))
    )


_ModuleRedunActivationStatus_Type.__name__ = "Integer32"
_ModuleRedunActivationStatus_Object = MibTableColumn
moduleRedunActivationStatus = _ModuleRedunActivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4222),
    _ModuleRedunActivationStatus_Type()
)
moduleRedunActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleRedunActivationStatus.setStatus("current")


class _ModuleExtioPinSignalingStatus_Type(Integer32):
    """Custom type moduleExtioPinSignalingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extioPinNominal", 1),
          ("extioPinSignaled", 2))
    )


_ModuleExtioPinSignalingStatus_Type.__name__ = "Integer32"
_ModuleExtioPinSignalingStatus_Object = MibTableColumn
moduleExtioPinSignalingStatus = _ModuleExtioPinSignalingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4223),
    _ModuleExtioPinSignalingStatus_Type()
)
moduleExtioPinSignalingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleExtioPinSignalingStatus.setStatus("current")


class _ModuleBackupPsuStatus_Type(Integer32):
    """Custom type moduleBackupPsuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupPsuNominal", 1),
          ("backupPsuFailure", 2))
    )


_ModuleBackupPsuStatus_Type.__name__ = "Integer32"
_ModuleBackupPsuStatus_Object = MibTableColumn
moduleBackupPsuStatus = _ModuleBackupPsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4224),
    _ModuleBackupPsuStatus_Type()
)
moduleBackupPsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupPsuStatus.setStatus("current")


class _ModuleIntrusionStatus_Type(Integer32):
    """Custom type moduleIntrusionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intrusionNominal", 1),
          ("intrusionDetected", 2))
    )


_ModuleIntrusionStatus_Type.__name__ = "Integer32"
_ModuleIntrusionStatus_Object = MibTableColumn
moduleIntrusionStatus = _ModuleIntrusionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4225),
    _ModuleIntrusionStatus_Type()
)
moduleIntrusionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIntrusionStatus.setStatus("current")


class _ModuleRedunStatus_Type(Integer32):
    """Custom type moduleRedunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundancyOk", 1),
          ("redundancyFailure", 2))
    )


_ModuleRedunStatus_Type.__name__ = "Integer32"
_ModuleRedunStatus_Object = MibTableColumn
moduleRedunStatus = _ModuleRedunStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4227),
    _ModuleRedunStatus_Type()
)
moduleRedunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleRedunStatus.setStatus("current")


class _ModuleBackupHwStatus_Type(Integer32):
    """Custom type moduleBackupHwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupHwOk", 1),
          ("backupHwNotSupported", 2))
    )


_ModuleBackupHwStatus_Type.__name__ = "Integer32"
_ModuleBackupHwStatus_Object = MibTableColumn
moduleBackupHwStatus = _ModuleBackupHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4230),
    _ModuleBackupHwStatus_Type()
)
moduleBackupHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupHwStatus.setStatus("current")


class _ModuleSwUpdateProgress_Type(Integer32):
    """Custom type moduleSwUpdateProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swUpdateInactive", 1),
          ("swUpdateInProgress", 2))
    )


_ModuleSwUpdateProgress_Type.__name__ = "Integer32"
_ModuleSwUpdateProgress_Object = MibTableColumn
moduleSwUpdateProgress = _ModuleSwUpdateProgress_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4231),
    _ModuleSwUpdateProgress_Type()
)
moduleSwUpdateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwUpdateProgress.setStatus("current")


class _ModuleSwUpdateStatus_Type(Integer32):
    """Custom type moduleSwUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swNominal", 1),
          ("swUpdateFailure", 2))
    )


_ModuleSwUpdateStatus_Type.__name__ = "Integer32"
_ModuleSwUpdateStatus_Object = MibTableColumn
moduleSwUpdateStatus = _ModuleSwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4233),
    _ModuleSwUpdateStatus_Type()
)
moduleSwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwUpdateStatus.setStatus("current")


class _ModuleEitLicenseStatus_Type(Integer32):
    """Custom type moduleEitLicenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseValid", 1),
          ("notLicensed", 2))
    )


_ModuleEitLicenseStatus_Type.__name__ = "Integer32"
_ModuleEitLicenseStatus_Object = MibTableColumn
moduleEitLicenseStatus = _ModuleEitLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4235),
    _ModuleEitLicenseStatus_Type()
)
moduleEitLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEitLicenseStatus.setStatus("current")


class _ModuleDescramblingStatus_Type(Integer32):
    """Custom type moduleDescramblingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descramblingNominal", 1),
          ("descramblingFailure", 2))
    )


_ModuleDescramblingStatus_Type.__name__ = "Integer32"
_ModuleDescramblingStatus_Object = MibTableColumn
moduleDescramblingStatus = _ModuleDescramblingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4237),
    _ModuleDescramblingStatus_Type()
)
moduleDescramblingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescramblingStatus.setStatus("current")


class _ModuleDvbTimeStatus_Type(Integer32):
    """Custom type moduleDvbTimeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dvbTimeNominal", 1),
          ("dvbTimeMissing", 2))
    )


_ModuleDvbTimeStatus_Type.__name__ = "Integer32"
_ModuleDvbTimeStatus_Object = MibTableColumn
moduleDvbTimeStatus = _ModuleDvbTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4243),
    _ModuleDvbTimeStatus_Type()
)
moduleDvbTimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDvbTimeStatus.setStatus("current")


class _ModuleTunerDcFeedStatus_Type(Integer32):
    """Custom type moduleTunerDcFeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentNominal", 1),
          ("currentOutOfRange", 2))
    )


_ModuleTunerDcFeedStatus_Type.__name__ = "Integer32"
_ModuleTunerDcFeedStatus_Object = MibTableColumn
moduleTunerDcFeedStatus = _ModuleTunerDcFeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4245),
    _ModuleTunerDcFeedStatus_Type()
)
moduleTunerDcFeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTunerDcFeedStatus.setStatus("current")


class _ModuleTunerPlpSelectionReqStatus_Type(Integer32):
    """Custom type moduleTunerPlpSelectionReqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plpSelectionOk", 1),
          ("plpSelectionRequired", 2))
    )


_ModuleTunerPlpSelectionReqStatus_Type.__name__ = "Integer32"
_ModuleTunerPlpSelectionReqStatus_Object = MibTableColumn
moduleTunerPlpSelectionReqStatus = _ModuleTunerPlpSelectionReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4247),
    _ModuleTunerPlpSelectionReqStatus_Type()
)
moduleTunerPlpSelectionReqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTunerPlpSelectionReqStatus.setStatus("current")


class _ModuleTunerPlpStatus_Type(Integer32):
    """Custom type moduleTunerPlpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plpSelectionValid", 1),
          ("plpSelectionNotValid", 2))
    )


_ModuleTunerPlpStatus_Type.__name__ = "Integer32"
_ModuleTunerPlpStatus_Object = MibTableColumn
moduleTunerPlpStatus = _ModuleTunerPlpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4248),
    _ModuleTunerPlpStatus_Type()
)
moduleTunerPlpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTunerPlpStatus.setStatus("current")


class _ModuleTunerHierarchyStatus_Type(Integer32):
    """Custom type moduleTunerHierarchyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hierarchyOk", 1),
          ("hierarchyInvalid", 2))
    )


_ModuleTunerHierarchyStatus_Type.__name__ = "Integer32"
_ModuleTunerHierarchyStatus_Object = MibTableColumn
moduleTunerHierarchyStatus = _ModuleTunerHierarchyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4249),
    _ModuleTunerHierarchyStatus_Type()
)
moduleTunerHierarchyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTunerHierarchyStatus.setStatus("current")


class _ModuleEcmStatus_Type(Integer32):
    """Custom type moduleEcmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ecmNominal", 1),
          ("ecmMissing", 2))
    )


_ModuleEcmStatus_Type.__name__ = "Integer32"
_ModuleEcmStatus_Object = MibTableColumn
moduleEcmStatus = _ModuleEcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4250),
    _ModuleEcmStatus_Type()
)
moduleEcmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEcmStatus.setStatus("current")


class _ModuleScramConflictStatus_Type(Integer32):
    """Custom type moduleScramConflictStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scramblingNominal", 1),
          ("scramblingConflict", 2))
    )


_ModuleScramConflictStatus_Type.__name__ = "Integer32"
_ModuleScramConflictStatus_Object = MibTableColumn
moduleScramConflictStatus = _ModuleScramConflictStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4251),
    _ModuleScramConflictStatus_Type()
)
moduleScramConflictStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleScramConflictStatus.setStatus("current")


class _ModuleScramSharedStatus_Type(Integer32):
    """Custom type moduleScramSharedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scramblingNominal", 1),
          ("scramblingSharedComponent", 2))
    )


_ModuleScramSharedStatus_Type.__name__ = "Integer32"
_ModuleScramSharedStatus_Object = MibTableColumn
moduleScramSharedStatus = _ModuleScramSharedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4252),
    _ModuleScramSharedStatus_Type()
)
moduleScramSharedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleScramSharedStatus.setStatus("current")


class _ModuleBackupVoltageHigh_Type(Integer32):
    """Custom type moduleBackupVoltageHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voltageNominal", 1),
          ("voltageHigh", 2))
    )


_ModuleBackupVoltageHigh_Type.__name__ = "Integer32"
_ModuleBackupVoltageHigh_Object = MibTableColumn
moduleBackupVoltageHigh = _ModuleBackupVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4253),
    _ModuleBackupVoltageHigh_Type()
)
moduleBackupVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupVoltageHigh.setStatus("current")


class _ModuleBackupVoltageLow_Type(Integer32):
    """Custom type moduleBackupVoltageLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voltageNominal", 1),
          ("voltageLow", 2))
    )


_ModuleBackupVoltageLow_Type.__name__ = "Integer32"
_ModuleBackupVoltageLow_Object = MibTableColumn
moduleBackupVoltageLow = _ModuleBackupVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4254),
    _ModuleBackupVoltageLow_Type()
)
moduleBackupVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupVoltageLow.setStatus("current")


class _ModuleSdtTableStatus_Type(Integer32):
    """Custom type moduleSdtTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdtTableOk", 1),
          ("invalidSdtTableTemplate", 2))
    )


_ModuleSdtTableStatus_Type.__name__ = "Integer32"
_ModuleSdtTableStatus_Object = MibTableColumn
moduleSdtTableStatus = _ModuleSdtTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4255),
    _ModuleSdtTableStatus_Type()
)
moduleSdtTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSdtTableStatus.setStatus("current")


class _ModuleDescramblingRestart_Type(Integer32):
    """Custom type moduleDescramblingRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descramblingNominal", 1),
          ("descramblingRestarting", 2))
    )


_ModuleDescramblingRestart_Type.__name__ = "Integer32"
_ModuleDescramblingRestart_Object = MibTableColumn
moduleDescramblingRestart = _ModuleDescramblingRestart_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4256),
    _ModuleDescramblingRestart_Type()
)
moduleDescramblingRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDescramblingRestart.setStatus("current")


class _ModuleCaModuleRestart_Type(Integer32):
    """Custom type moduleCaModuleRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("caModuleNominal", 1),
          ("caModuleRestarting", 2))
    )


_ModuleCaModuleRestart_Type.__name__ = "Integer32"
_ModuleCaModuleRestart_Object = MibTableColumn
moduleCaModuleRestart = _ModuleCaModuleRestart_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4257),
    _ModuleCaModuleRestart_Type()
)
moduleCaModuleRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCaModuleRestart.setStatus("current")


class _ModuleCaMenuStatus_Type(Integer32):
    """Custom type moduleCaMenuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("caMenuNominal", 1),
          ("caMenuOpen", 2))
    )


_ModuleCaMenuStatus_Type.__name__ = "Integer32"
_ModuleCaMenuStatus_Object = MibTableColumn
moduleCaMenuStatus = _ModuleCaMenuStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4258),
    _ModuleCaMenuStatus_Type()
)
moduleCaMenuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCaMenuStatus.setStatus("current")


class _ModuleInvalidCamRouting_Type(Integer32):
    """Custom type moduleInvalidCamRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("camRoutingNominal", 1),
          ("camRoutingInvalid", 2))
    )


_ModuleInvalidCamRouting_Type.__name__ = "Integer32"
_ModuleInvalidCamRouting_Object = MibTableColumn
moduleInvalidCamRouting = _ModuleInvalidCamRouting_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4259),
    _ModuleInvalidCamRouting_Type()
)
moduleInvalidCamRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInvalidCamRouting.setStatus("current")


class _ModuleNitSidConflict_Type(Integer32):
    """Custom type moduleNitSidConflict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nitSidNominal", 1),
          ("nitSidConflict", 2))
    )


_ModuleNitSidConflict_Type.__name__ = "Integer32"
_ModuleNitSidConflict_Object = MibTableColumn
moduleNitSidConflict = _ModuleNitSidConflict_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4260),
    _ModuleNitSidConflict_Type()
)
moduleNitSidConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNitSidConflict.setStatus("current")


class _ModuleLicenseMissingFEC_Type(Integer32):
    """Custom type moduleLicenseMissingFEC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseOk", 1),
          ("licenseMissing", 2))
    )


_ModuleLicenseMissingFEC_Type.__name__ = "Integer32"
_ModuleLicenseMissingFEC_Object = MibTableColumn
moduleLicenseMissingFEC = _ModuleLicenseMissingFEC_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4262),
    _ModuleLicenseMissingFEC_Type()
)
moduleLicenseMissingFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLicenseMissingFEC.setStatus("current")


class _ModuleFecCorrectionStatus_Type(Integer32):
    """Custom type moduleFecCorrectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("correctionNominal", 1),
          ("correctionOverload", 2))
    )


_ModuleFecCorrectionStatus_Type.__name__ = "Integer32"
_ModuleFecCorrectionStatus_Object = MibTableColumn
moduleFecCorrectionStatus = _ModuleFecCorrectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4263),
    _ModuleFecCorrectionStatus_Type()
)
moduleFecCorrectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFecCorrectionStatus.setStatus("current")


class _ModuleFecPacketDropStatus_Type(Integer32):
    """Custom type moduleFecPacketDropStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packetsNominal", 1),
          ("packetsDropped", 2))
    )


_ModuleFecPacketDropStatus_Type.__name__ = "Integer32"
_ModuleFecPacketDropStatus_Object = MibTableColumn
moduleFecPacketDropStatus = _ModuleFecPacketDropStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4264),
    _ModuleFecPacketDropStatus_Type()
)
moduleFecPacketDropStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFecPacketDropStatus.setStatus("current")


class _ModuleFecMediaPktsStatus_Type(Integer32):
    """Custom type moduleFecMediaPktsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packetsNominal", 1),
          ("packetsDiscarded", 2))
    )


_ModuleFecMediaPktsStatus_Type.__name__ = "Integer32"
_ModuleFecMediaPktsStatus_Object = MibTableColumn
moduleFecMediaPktsStatus = _ModuleFecMediaPktsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4265),
    _ModuleFecMediaPktsStatus_Type()
)
moduleFecMediaPktsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFecMediaPktsStatus.setStatus("current")


class _ModuleSfpLinkStatus_Type(Integer32):
    """Custom type moduleSfpLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sfpLinkNominal", 1),
          ("sfpLinkDown", 2))
    )


_ModuleSfpLinkStatus_Type.__name__ = "Integer32"
_ModuleSfpLinkStatus_Object = MibTableColumn
moduleSfpLinkStatus = _ModuleSfpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4269),
    _ModuleSfpLinkStatus_Type()
)
moduleSfpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSfpLinkStatus.setStatus("current")


class _ModuleBackupSyncModeOff_Type(Integer32):
    """Custom type moduleBackupSyncModeOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modeNominal", 1),
          ("modeOff", 2))
    )


_ModuleBackupSyncModeOff_Type.__name__ = "Integer32"
_ModuleBackupSyncModeOff_Object = MibTableColumn
moduleBackupSyncModeOff = _ModuleBackupSyncModeOff_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4272),
    _ModuleBackupSyncModeOff_Type()
)
moduleBackupSyncModeOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncModeOff.setStatus("current")


class _ModuleBackupSyncModeManual_Type(Integer32):
    """Custom type moduleBackupSyncModeManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modeNominal", 1),
          ("modeManual", 2))
    )


_ModuleBackupSyncModeManual_Type.__name__ = "Integer32"
_ModuleBackupSyncModeManual_Object = MibTableColumn
moduleBackupSyncModeManual = _ModuleBackupSyncModeManual_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4273),
    _ModuleBackupSyncModeManual_Type()
)
moduleBackupSyncModeManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncModeManual.setStatus("current")


class _ModuleBackupSyncModeAuto_Type(Integer32):
    """Custom type moduleBackupSyncModeAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modeNominal", 1),
          ("modeAuto", 2))
    )


_ModuleBackupSyncModeAuto_Type.__name__ = "Integer32"
_ModuleBackupSyncModeAuto_Object = MibTableColumn
moduleBackupSyncModeAuto = _ModuleBackupSyncModeAuto_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4274),
    _ModuleBackupSyncModeAuto_Type()
)
moduleBackupSyncModeAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncModeAuto.setStatus("current")


class _ModuleBackupSyncConfStatus_Type(Integer32):
    """Custom type moduleBackupSyncConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurationNominal", 1),
          ("configurationChanged", 2))
    )


_ModuleBackupSyncConfStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncConfStatus_Object = MibTableColumn
moduleBackupSyncConfStatus = _ModuleBackupSyncConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4275),
    _ModuleBackupSyncConfStatus_Type()
)
moduleBackupSyncConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncConfStatus.setStatus("current")


class _ModuleBackupSyncStatus_Type(Integer32):
    """Custom type moduleBackupSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncNominal", 1),
          ("synchronizing", 2))
    )


_ModuleBackupSyncStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncStatus_Object = MibTableColumn
moduleBackupSyncStatus = _ModuleBackupSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4276),
    _ModuleBackupSyncStatus_Type()
)
moduleBackupSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncStatus.setStatus("current")


class _ModuleBackupSyncSwCompatibility_Type(Integer32):
    """Custom type moduleBackupSyncSwCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swCompatible", 1),
          ("swIncompatible", 2))
    )


_ModuleBackupSyncSwCompatibility_Type.__name__ = "Integer32"
_ModuleBackupSyncSwCompatibility_Object = MibTableColumn
moduleBackupSyncSwCompatibility = _ModuleBackupSyncSwCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4278),
    _ModuleBackupSyncSwCompatibility_Type()
)
moduleBackupSyncSwCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncSwCompatibility.setStatus("current")


class _ModuleBackupSyncHwCompatibility_Type(Integer32):
    """Custom type moduleBackupSyncHwCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hwCompatible", 1),
          ("hwIncompatible", 2))
    )


_ModuleBackupSyncHwCompatibility_Type.__name__ = "Integer32"
_ModuleBackupSyncHwCompatibility_Object = MibTableColumn
moduleBackupSyncHwCompatibility = _ModuleBackupSyncHwCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4279),
    _ModuleBackupSyncHwCompatibility_Type()
)
moduleBackupSyncHwCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncHwCompatibility.setStatus("current")


class _ModuleBackupSyncConfFaultStatus_Type(Integer32):
    """Custom type moduleBackupSyncConfFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurationNominal", 1),
          ("configurationFault", 2))
    )


_ModuleBackupSyncConfFaultStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncConfFaultStatus_Object = MibTableColumn
moduleBackupSyncConfFaultStatus = _ModuleBackupSyncConfFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4280),
    _ModuleBackupSyncConfFaultStatus_Type()
)
moduleBackupSyncConfFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncConfFaultStatus.setStatus("current")


class _ModuleBackupSyncConnectionStatus_Type(Integer32):
    """Custom type moduleBackupSyncConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectionNominal", 1),
          ("connectionLost", 2))
    )


_ModuleBackupSyncConnectionStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncConnectionStatus_Object = MibTableColumn
moduleBackupSyncConnectionStatus = _ModuleBackupSyncConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4281),
    _ModuleBackupSyncConnectionStatus_Type()
)
moduleBackupSyncConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncConnectionStatus.setStatus("current")


class _ModuleBackupSyncFromBackupStatus_Type(Integer32):
    """Custom type moduleBackupSyncFromBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncNominal", 1),
          ("syncNotPossible", 2))
    )


_ModuleBackupSyncFromBackupStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncFromBackupStatus_Object = MibTableColumn
moduleBackupSyncFromBackupStatus = _ModuleBackupSyncFromBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4283),
    _ModuleBackupSyncFromBackupStatus_Type()
)
moduleBackupSyncFromBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncFromBackupStatus.setStatus("current")


class _ModuleBackupSyncRebootStatus_Type(Integer32):
    """Custom type moduleBackupSyncRebootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pairDevNominal", 1),
          ("pairDevRebooting", 2))
    )


_ModuleBackupSyncRebootStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncRebootStatus_Object = MibTableColumn
moduleBackupSyncRebootStatus = _ModuleBackupSyncRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4284),
    _ModuleBackupSyncRebootStatus_Type()
)
moduleBackupSyncRebootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncRebootStatus.setStatus("current")


class _ModuleBackupSyncLicenseCompatStatus_Type(Integer32):
    """Custom type moduleBackupSyncLicenseCompatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licensesCompatible", 1),
          ("licensesIncompatible", 2))
    )


_ModuleBackupSyncLicenseCompatStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncLicenseCompatStatus_Object = MibTableColumn
moduleBackupSyncLicenseCompatStatus = _ModuleBackupSyncLicenseCompatStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4285),
    _ModuleBackupSyncLicenseCompatStatus_Type()
)
moduleBackupSyncLicenseCompatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncLicenseCompatStatus.setStatus("current")


class _ModuleBackupSyncLicenseCompareStatus_Type(Integer32):
    """Custom type moduleBackupSyncLicenseCompareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("licenseNominal", 1),
          ("licenseComparing", 2))
    )


_ModuleBackupSyncLicenseCompareStatus_Type.__name__ = "Integer32"
_ModuleBackupSyncLicenseCompareStatus_Object = MibTableColumn
moduleBackupSyncLicenseCompareStatus = _ModuleBackupSyncLicenseCompareStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4286),
    _ModuleBackupSyncLicenseCompareStatus_Type()
)
moduleBackupSyncLicenseCompareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleBackupSyncLicenseCompareStatus.setStatus("current")


class _ModuleDeviceFirstBootStatus_Type(Integer32):
    """Custom type moduleDeviceFirstBootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firstBootNominal", 1),
          ("firstBootInProgress", 2))
    )


_ModuleDeviceFirstBootStatus_Type.__name__ = "Integer32"
_ModuleDeviceFirstBootStatus_Object = MibTableColumn
moduleDeviceFirstBootStatus = _ModuleDeviceFirstBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4288),
    _ModuleDeviceFirstBootStatus_Type()
)
moduleDeviceFirstBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleDeviceFirstBootStatus.setStatus("current")


class _ModulePartitionConfigurationBackup_Type(Integer32):
    """Custom type modulePartitionConfigurationBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurationNominal", 1),
          ("configurationBackupInProgress", 2))
    )


_ModulePartitionConfigurationBackup_Type.__name__ = "Integer32"
_ModulePartitionConfigurationBackup_Object = MibTableColumn
modulePartitionConfigurationBackup = _ModulePartitionConfigurationBackup_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4289),
    _ModulePartitionConfigurationBackup_Type()
)
modulePartitionConfigurationBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePartitionConfigurationBackup.setStatus("current")


class _ModulePartitionConfigurationRestore_Type(Integer32):
    """Custom type modulePartitionConfigurationRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurationNominal", 1),
          ("configurationRestoreInProgress", 2))
    )


_ModulePartitionConfigurationRestore_Type.__name__ = "Integer32"
_ModulePartitionConfigurationRestore_Object = MibTableColumn
modulePartitionConfigurationRestore = _ModulePartitionConfigurationRestore_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4290),
    _ModulePartitionConfigurationRestore_Type()
)
modulePartitionConfigurationRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePartitionConfigurationRestore.setStatus("current")


class _ModuleSwRevertStatus_Type(Integer32):
    """Custom type moduleSwRevertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swNominal", 1),
          ("swRevertInProgress", 2))
    )


_ModuleSwRevertStatus_Type.__name__ = "Integer32"
_ModuleSwRevertStatus_Object = MibTableColumn
moduleSwRevertStatus = _ModuleSwRevertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4291),
    _ModuleSwRevertStatus_Type()
)
moduleSwRevertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwRevertStatus.setStatus("current")


class _ModuleMaxOutputPidsStatus_Type(Integer32):
    """Custom type moduleMaxOutputPidsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pidsNominal", 1),
          ("maxPidsUsed", 2))
    )


_ModuleMaxOutputPidsStatus_Type.__name__ = "Integer32"
_ModuleMaxOutputPidsStatus_Object = MibTableColumn
moduleMaxOutputPidsStatus = _ModuleMaxOutputPidsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4292),
    _ModuleMaxOutputPidsStatus_Type()
)
moduleMaxOutputPidsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleMaxOutputPidsStatus.setStatus("current")


class _ModuleUserRebootStatus_Type(Integer32):
    """Custom type moduleUserRebootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleRebootedByUser", 2))
    )


_ModuleUserRebootStatus_Type.__name__ = "Integer32"
_ModuleUserRebootStatus_Object = MibTableColumn
moduleUserRebootStatus = _ModuleUserRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4293),
    _ModuleUserRebootStatus_Type()
)
moduleUserRebootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleUserRebootStatus.setStatus("current")


class _ModuleRemovalStatus_Type(Integer32):
    """Custom type moduleRemovalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleRemoved", 2))
    )


_ModuleRemovalStatus_Type.__name__ = "Integer32"
_ModuleRemovalStatus_Object = MibTableColumn
moduleRemovalStatus = _ModuleRemovalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4294),
    _ModuleRemovalStatus_Type()
)
moduleRemovalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleRemovalStatus.setStatus("current")


class _ModuleInsertionStatus_Type(Integer32):
    """Custom type moduleInsertionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("moduleNominal", 1),
          ("moduleInserted", 2))
    )


_ModuleInsertionStatus_Type.__name__ = "Integer32"
_ModuleInsertionStatus_Object = MibTableColumn
moduleInsertionStatus = _ModuleInsertionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4295),
    _ModuleInsertionStatus_Type()
)
moduleInsertionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleInsertionStatus.setStatus("current")


class _ModuleSptsInputConfStatus_Type(Integer32):
    """Custom type moduleSptsInputConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sptsInputNominal", 1),
          ("inputNotSpts", 2))
    )


_ModuleSptsInputConfStatus_Type.__name__ = "Integer32"
_ModuleSptsInputConfStatus_Object = MibTableColumn
moduleSptsInputConfStatus = _ModuleSptsInputConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 2, 1, 4296),
    _ModuleSptsInputConfStatus_Type()
)
moduleSptsInputConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSptsInputConfStatus.setStatus("current")
_IfStatusTable_Object = MibTable
ifStatusTable = _IfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 3)
)
if mibBuilder.loadTexts:
    ifStatusTable.setStatus("current")
_IfStatusEntry_Object = MibTableRow
ifStatusEntry = _IfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 3, 1)
)
ifStatusEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "moduleId"),
    (0, "TELESTE-LUMINATO-MIB", "ifDirection"),
    (0, "TELESTE-LUMINATO-MIB", "ifId"),
)
if mibBuilder.loadTexts:
    ifStatusEntry.setStatus("current")
_IfId_Type = Integer32
_IfId_Object = MibTableColumn
ifId = _IfId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 3, 1, 1),
    _IfId_Type()
)
ifId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifId.setStatus("current")


class _IfDirection_Type(Integer32):
    """Custom type ifDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2),
          ("both", 3))
    )


_IfDirection_Type.__name__ = "Integer32"
_IfDirection_Object = MibTableColumn
ifDirection = _IfDirection_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 3, 1, 2),
    _IfDirection_Type()
)
ifDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifDirection.setStatus("current")


class _IfSignalStatus_Type(Integer32):
    """Custom type ifSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signalOk", 1),
          ("signalMissing", 2))
    )


_IfSignalStatus_Type.__name__ = "Integer32"
_IfSignalStatus_Object = MibTableColumn
ifSignalStatus = _IfSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 3, 1, 4097),
    _IfSignalStatus_Type()
)
ifSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSignalStatus.setStatus("current")


class _IfAsiLinkStatus_Type(Integer32):
    """Custom type ifAsiLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkOk", 1),
          ("linkDown", 2))
    )


_IfAsiLinkStatus_Type.__name__ = "Integer32"
_IfAsiLinkStatus_Object = MibTableColumn
ifAsiLinkStatus = _IfAsiLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 3, 1, 4102),
    _IfAsiLinkStatus_Type()
)
ifAsiLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAsiLinkStatus.setStatus("current")


class _IfLinkStatus_Type(Integer32):
    """Custom type ifLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkOk", 1),
          ("linkDown", 2))
    )


_IfLinkStatus_Type.__name__ = "Integer32"
_IfLinkStatus_Object = MibTableColumn
ifLinkStatus = _IfLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 3, 1, 4226),
    _IfLinkStatus_Type()
)
ifLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLinkStatus.setStatus("current")
_TsStatusTable_Object = MibTable
tsStatusTable = _TsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4)
)
if mibBuilder.loadTexts:
    tsStatusTable.setStatus("current")
_TsStatusEntry_Object = MibTableRow
tsStatusEntry = _TsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1)
)
tsStatusEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "moduleId"),
    (0, "TELESTE-LUMINATO-MIB", "ifDirection"),
    (0, "TELESTE-LUMINATO-MIB", "ifId"),
)
if mibBuilder.loadTexts:
    tsStatusEntry.setStatus("current")


class _TsPidRemappingStatus_Type(Integer32):
    """Custom type tsPidRemappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pidNominal", 1),
          ("pidRemapped", 2))
    )


_TsPidRemappingStatus_Type.__name__ = "Integer32"
_TsPidRemappingStatus_Object = MibTableColumn
tsPidRemappingStatus = _TsPidRemappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 5),
    _TsPidRemappingStatus_Type()
)
tsPidRemappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPidRemappingStatus.setStatus("current")


class _TsManualTableInsertStatus_Type(Integer32):
    """Custom type tsManualTableInsertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insertOk", 1),
          ("insertFailure", 2))
    )


_TsManualTableInsertStatus_Type.__name__ = "Integer32"
_TsManualTableInsertStatus_Object = MibTableColumn
tsManualTableInsertStatus = _TsManualTableInsertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 8),
    _TsManualTableInsertStatus_Type()
)
tsManualTableInsertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsManualTableInsertStatus.setStatus("current")


class _TsPassthruDupStatus_Type(Integer32):
    """Custom type tsPassthruDupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("servicesNominal", 1),
          ("servicesBlocked", 2))
    )


_TsPassthruDupStatus_Type.__name__ = "Integer32"
_TsPassthruDupStatus_Object = MibTableColumn
tsPassthruDupStatus = _TsPassthruDupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 11),
    _TsPassthruDupStatus_Type()
)
tsPassthruDupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPassthruDupStatus.setStatus("current")


class _TsSyncStatus_Type(Integer32):
    """Custom type tsSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncOk", 1),
          ("noSync", 2))
    )


_TsSyncStatus_Type.__name__ = "Integer32"
_TsSyncStatus_Object = MibTableColumn
tsSyncStatus = _TsSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4098),
    _TsSyncStatus_Type()
)
tsSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsSyncStatus.setStatus("current")


class _TsRxStatus_Type(Integer32):
    """Custom type tsRxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxNominal", 1),
          ("rxErrors", 2))
    )


_TsRxStatus_Type.__name__ = "Integer32"
_TsRxStatus_Object = MibTableColumn
tsRxStatus = _TsRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4099),
    _TsRxStatus_Type()
)
tsRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsRxStatus.setStatus("current")


class _TsInputBufferStatus_Type(Integer32):
    """Custom type tsInputBufferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bufferNominal", 1),
          ("bufferOverflow", 2))
    )


_TsInputBufferStatus_Type.__name__ = "Integer32"
_TsInputBufferStatus_Object = MibTableColumn
tsInputBufferStatus = _TsInputBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4100),
    _TsInputBufferStatus_Type()
)
tsInputBufferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsInputBufferStatus.setStatus("current")


class _TsNetworkStatus_Type(Integer32):
    """Custom type tsNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netOk", 1),
          ("netForbidden", 2))
    )


_TsNetworkStatus_Type.__name__ = "Integer32"
_TsNetworkStatus_Object = MibTableColumn
tsNetworkStatus = _TsNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4103),
    _TsNetworkStatus_Type()
)
tsNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsNetworkStatus.setStatus("current")


class _TsPsisiCapaStatus_Type(Integer32):
    """Custom type tsPsisiCapaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capacityNominal", 1),
          ("capacityExceeded", 2))
    )


_TsPsisiCapaStatus_Type.__name__ = "Integer32"
_TsPsisiCapaStatus_Object = MibTableColumn
tsPsisiCapaStatus = _TsPsisiCapaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4109),
    _TsPsisiCapaStatus_Type()
)
tsPsisiCapaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsPsisiCapaStatus.setStatus("current")


class _TsMultiplexDiscardStatus_Type(Integer32):
    """Custom type tsMultiplexDiscardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("muxNominal", 1),
          ("muxPacketsDiscarded", 2))
    )


_TsMultiplexDiscardStatus_Type.__name__ = "Integer32"
_TsMultiplexDiscardStatus_Object = MibTableColumn
tsMultiplexDiscardStatus = _TsMultiplexDiscardStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4110),
    _TsMultiplexDiscardStatus_Type()
)
tsMultiplexDiscardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsMultiplexDiscardStatus.setStatus("current")


class _TsMultiplexDelayStatus_Type(Integer32):
    """Custom type tsMultiplexDelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("muxNominal", 1),
          ("muxPacketsDelayed", 2))
    )


_TsMultiplexDelayStatus_Type.__name__ = "Integer32"
_TsMultiplexDelayStatus_Object = MibTableColumn
tsMultiplexDelayStatus = _TsMultiplexDelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4228),
    _TsMultiplexDelayStatus_Type()
)
tsMultiplexDelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsMultiplexDelayStatus.setStatus("current")


class _TsCbrOversubscriptionStatus_Type(Integer32):
    """Custom type tsCbrOversubscriptionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbrNominal", 1),
          ("cbrOversubscription", 2))
    )


_TsCbrOversubscriptionStatus_Type.__name__ = "Integer32"
_TsCbrOversubscriptionStatus_Object = MibTableColumn
tsCbrOversubscriptionStatus = _TsCbrOversubscriptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4229),
    _TsCbrOversubscriptionStatus_Type()
)
tsCbrOversubscriptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsCbrOversubscriptionStatus.setStatus("current")


class _TsCbrDiscardStatus_Type(Integer32):
    """Custom type tsCbrDiscardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbrNominal", 1),
          ("cbrPacketsDiscarded", 2))
    )


_TsCbrDiscardStatus_Type.__name__ = "Integer32"
_TsCbrDiscardStatus_Object = MibTableColumn
tsCbrDiscardStatus = _TsCbrDiscardStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4236),
    _TsCbrDiscardStatus_Type()
)
tsCbrDiscardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsCbrDiscardStatus.setStatus("current")


class _TsIpInputCapaStatus_Type(Integer32):
    """Custom type tsIpInputCapaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capacityNominal", 1),
          ("capacityExceeded", 2))
    )


_TsIpInputCapaStatus_Type.__name__ = "Integer32"
_TsIpInputCapaStatus_Object = MibTableColumn
tsIpInputCapaStatus = _TsIpInputCapaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4238),
    _TsIpInputCapaStatus_Type()
)
tsIpInputCapaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIpInputCapaStatus.setStatus("current")


class _TsEitReinsertCapaStatus_Type(Integer32):
    """Custom type tsEitReinsertCapaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capacityNominal", 1),
          ("capacityExceeded", 2))
    )


_TsEitReinsertCapaStatus_Type.__name__ = "Integer32"
_TsEitReinsertCapaStatus_Object = MibTableColumn
tsEitReinsertCapaStatus = _TsEitReinsertCapaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4239),
    _TsEitReinsertCapaStatus_Type()
)
tsEitReinsertCapaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsEitReinsertCapaStatus.setStatus("current")


class _TsSectionCapaStatus_Type(Integer32):
    """Custom type tsSectionCapaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capacityNominal", 1),
          ("capacityExceeded", 2))
    )


_TsSectionCapaStatus_Type.__name__ = "Integer32"
_TsSectionCapaStatus_Object = MibTableColumn
tsSectionCapaStatus = _TsSectionCapaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4240),
    _TsSectionCapaStatus_Type()
)
tsSectionCapaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsSectionCapaStatus.setStatus("current")


class _TsRtpInputStatus_Type(Integer32):
    """Custom type tsRtpInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inputOk", 1),
          ("inputPacketsDropped", 2))
    )


_TsRtpInputStatus_Type.__name__ = "Integer32"
_TsRtpInputStatus_Object = MibTableColumn
tsRtpInputStatus = _TsRtpInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4241),
    _TsRtpInputStatus_Type()
)
tsRtpInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsRtpInputStatus.setStatus("current")


class _TsRtpSeqStatus_Type(Integer32):
    """Custom type tsRtpSeqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seqOk", 1),
          ("seqAnomalies", 2))
    )


_TsRtpSeqStatus_Type.__name__ = "Integer32"
_TsRtpSeqStatus_Object = MibTableColumn
tsRtpSeqStatus = _TsRtpSeqStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4242),
    _TsRtpSeqStatus_Type()
)
tsRtpSeqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsRtpSeqStatus.setStatus("current")


class _TsTdtTotGenStatus_Type(Integer32):
    """Custom type tsTdtTotGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tdtTotOk", 1),
          ("tdtTotNotGenerated", 2))
    )


_TsTdtTotGenStatus_Type.__name__ = "Integer32"
_TsTdtTotGenStatus_Object = MibTableColumn
tsTdtTotGenStatus = _TsTdtTotGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4246),
    _TsTdtTotGenStatus_Type()
)
tsTdtTotGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsTdtTotGenStatus.setStatus("current")


class _TsSttGenStatus_Type(Integer32):
    """Custom type tsSttGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sttOk", 1),
          ("sttNotGenerated", 2))
    )


_TsSttGenStatus_Type.__name__ = "Integer32"
_TsSttGenStatus_Object = MibTableColumn
tsSttGenStatus = _TsSttGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4261),
    _TsSttGenStatus_Type()
)
tsSttGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsSttGenStatus.setStatus("current")


class _TsFecPacketCorrectionStatus_Type(Integer32):
    """Custom type tsFecPacketCorrectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packetsNominal", 1),
          ("fecCorrectedPackets", 2))
    )


_TsFecPacketCorrectionStatus_Type.__name__ = "Integer32"
_TsFecPacketCorrectionStatus_Object = MibTableColumn
tsFecPacketCorrectionStatus = _TsFecPacketCorrectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4266),
    _TsFecPacketCorrectionStatus_Type()
)
tsFecPacketCorrectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsFecPacketCorrectionStatus.setStatus("current")


class _TsFecInputAnomalyStatus_Type(Integer32):
    """Custom type tsFecInputAnomalyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fecInputNominal", 1),
          ("fecInputAnomalies", 2))
    )


_TsFecInputAnomalyStatus_Type.__name__ = "Integer32"
_TsFecInputAnomalyStatus_Object = MibTableColumn
tsFecInputAnomalyStatus = _TsFecInputAnomalyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4267),
    _TsFecInputAnomalyStatus_Type()
)
tsFecInputAnomalyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsFecInputAnomalyStatus.setStatus("current")


class _TsFecCorrectionCapacityStatus_Type(Integer32):
    """Custom type tsFecCorrectionCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("correctionCapacityNominal", 1),
          ("correctionCapacityExceeded", 2))
    )


_TsFecCorrectionCapacityStatus_Type.__name__ = "Integer32"
_TsFecCorrectionCapacityStatus_Object = MibTableColumn
tsFecCorrectionCapacityStatus = _TsFecCorrectionCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4268),
    _TsFecCorrectionCapacityStatus_Type()
)
tsFecCorrectionCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsFecCorrectionCapacityStatus.setStatus("current")


class _TsIpMirrorOutputPacketLossStatus_Type(Integer32):
    """Custom type tsIpMirrorOutputPacketLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipOutputNominal", 1),
          ("ipOutputPacketsDiscarded", 2))
    )


_TsIpMirrorOutputPacketLossStatus_Type.__name__ = "Integer32"
_TsIpMirrorOutputPacketLossStatus_Object = MibTableColumn
tsIpMirrorOutputPacketLossStatus = _TsIpMirrorOutputPacketLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 4, 1, 4297),
    _TsIpMirrorOutputPacketLossStatus_Type()
)
tsIpMirrorOutputPacketLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsIpMirrorOutputPacketLossStatus.setStatus("current")
_ServiceStatusTable_Object = MibTable
serviceStatusTable = _ServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 5)
)
if mibBuilder.loadTexts:
    serviceStatusTable.setStatus("current")
_ServiceStatusEntry_Object = MibTableRow
serviceStatusEntry = _ServiceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 5, 1)
)
serviceStatusEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "moduleId"),
    (0, "TELESTE-LUMINATO-MIB", "ifDirection"),
    (0, "TELESTE-LUMINATO-MIB", "ifId"),
    (0, "TELESTE-LUMINATO-MIB", "serviceId"),
)
if mibBuilder.loadTexts:
    serviceStatusEntry.setStatus("current")
_ServiceId_Type = Integer32
_ServiceId_Object = MibTableColumn
serviceId = _ServiceId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 5, 1, 1),
    _ServiceId_Type()
)
serviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serviceId.setStatus("current")


class _ServiceStatus_Type(Integer32):
    """Custom type serviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("servicePresent", 1),
          ("serviceMissing", 2))
    )


_ServiceStatus_Type.__name__ = "Integer32"
_ServiceStatus_Object = MibTableColumn
serviceStatus = _ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 5, 1, 3),
    _ServiceStatus_Type()
)
serviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceStatus.setStatus("current")
_PidStatusTable_Object = MibTable
pidStatusTable = _PidStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 6)
)
if mibBuilder.loadTexts:
    pidStatusTable.setStatus("current")
_PidStatusEntry_Object = MibTableRow
pidStatusEntry = _PidStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 6, 1)
)
pidStatusEntry.setIndexNames(
    (0, "TELESTE-LUMINATO-MIB", "moduleId"),
    (0, "TELESTE-LUMINATO-MIB", "ifDirection"),
    (0, "TELESTE-LUMINATO-MIB", "ifId"),
    (0, "TELESTE-LUMINATO-MIB", "pId"),
)
if mibBuilder.loadTexts:
    pidStatusEntry.setStatus("current")


class _PId_Type(Integer32):
    """Custom type pId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PId_Type.__name__ = "Integer32"
_PId_Object = MibTableColumn
pId = _PId_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 6, 1, 1),
    _PId_Type()
)
pId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pId.setStatus("current")


class _PidStatus_Type(Integer32):
    """Custom type pidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pidPresent", 1),
          ("pidMissing", 2))
    )


_PidStatus_Type.__name__ = "Integer32"
_PidStatus_Object = MibTableColumn
pidStatus = _PidStatus_Object(
    (1, 3, 6, 1, 4, 1, 3715, 17, 5, 6, 1, 2),
    _PidStatus_Type()
)
pidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TELESTE-LUMINATO-MIB",
    **{"general": general,
       "deviceName": deviceName,
       "generalStatus": generalStatus,
       "redundancyStatus": redundancyStatus,
       "hwSerialNumber": hwSerialNumber,
       "hwType": hwType,
       "hwVersion": hwVersion,
       "swVersion": swVersion,
       "upTime": upTime,
       "cumulativeUptime": cumulativeUptime,
       "statusCode": statusCode,
       "interfaceTypeTable": interfaceTypeTable,
       "interfaceTypeEntry": interfaceTypeEntry,
       "interfaceTypeId": interfaceTypeId,
       "statusCodeDeviceTable": statusCodeDeviceTable,
       "statusCodeDeviceEntry": statusCodeDeviceEntry,
       "scdObjectId": scdObjectId,
       "scdObjectValue": scdObjectValue,
       "scdObjectDescriptor": scdObjectDescriptor,
       "scdObjectAlarmValue": scdObjectAlarmValue,
       "statusCodeModuleTable": statusCodeModuleTable,
       "statusCodeModuleEntry": statusCodeModuleEntry,
       "scmModuleId": scmModuleId,
       "scmObjectId": scmObjectId,
       "scmObjectValue": scmObjectValue,
       "scmObjectDescriptor": scmObjectDescriptor,
       "scmObjectAlarmValue": scmObjectAlarmValue,
       "statusCodeInterfaceTable": statusCodeInterfaceTable,
       "statusCodeInterfaceEntry": statusCodeInterfaceEntry,
       "sciInterfaceId": sciInterfaceId,
       "sciObjectId": sciObjectId,
       "sciObjectValue": sciObjectValue,
       "sciObjectDescriptor": sciObjectDescriptor,
       "sciObjectAlarmValue": sciObjectAlarmValue,
       "statusCodeTransportStreamTable": statusCodeTransportStreamTable,
       "statusCodeTransportStreamEntry": statusCodeTransportStreamEntry,
       "sctsTransportStreamId": sctsTransportStreamId,
       "sctsObjectId": sctsObjectId,
       "sctsObjectValue": sctsObjectValue,
       "sctsObjectDescriptor": sctsObjectDescriptor,
       "sctsObjectAlarmValue": sctsObjectAlarmValue,
       "statusCodeServiceTable": statusCodeServiceTable,
       "statusCodeServiceEntry": statusCodeServiceEntry,
       "scsSID": scsSID,
       "scsObjectId": scsObjectId,
       "scsObjectValue": scsObjectValue,
       "scsObjectDescriptor": scsObjectDescriptor,
       "scsServiceName": scsServiceName,
       "scsObjectAlarmValue": scsObjectAlarmValue,
       "statusCodePidTable": statusCodePidTable,
       "statusCodePidEntry": statusCodePidEntry,
       "scpPID": scpPID,
       "scpObjectId": scpObjectId,
       "scpObjectValue": scpObjectValue,
       "scpObjectDescriptor": scpObjectDescriptor,
       "scpObjectAlarmValue": scpObjectAlarmValue,
       "interface": interface,
       "ifExtTable": ifExtTable,
       "ifExtEntry": ifExtEntry,
       "ifExtIndex": ifExtIndex,
       "ifExtName": ifExtName,
       "ifExtModule": ifExtModule,
       "ifExtPhysInterface": ifExtPhysInterface,
       "ifExtLogiInterface": ifExtLogiInterface,
       "ifExtDirection": ifExtDirection,
       "pysmiFakeCol1": pysmiFakeCol1,
       "signalPhysTable": signalPhysTable,
       "signalPhysEntry": signalPhysEntry,
       "signalSnr": signalSnr,
       "signalSnrMin": signalSnrMin,
       "signalSnrMax": signalSnrMax,
       "signalCcErrors": signalCcErrors,
       "signalBer": signalBer,
       "signalVber": signalVber,
       "transferTable": transferTable,
       "transferEntry": transferEntry,
       "transBitrate": transBitrate,
       "transBitrateMin": transBitrateMin,
       "transBitrateMax": transBitrateMax,
       "inputServiceTable": inputServiceTable,
       "inputServiceEntry": inputServiceEntry,
       "iSID": iSID,
       "iServiceName": iServiceName,
       "iServiceBitrate": iServiceBitrate,
       "outputServiceTable": outputServiceTable,
       "outputServiceEntry": outputServiceEntry,
       "oSID": oSID,
       "oServiceName": oServiceName,
       "oServiceBitrate": oServiceBitrate,
       "proMpegFecTable": proMpegFecTable,
       "proMpegFecEntry": proMpegFecEntry,
       "fecValidPkts": fecValidPkts,
       "fecUncorrectedPkts": fecUncorrectedPkts,
       "fecCorrectedPkts": fecCorrectedPkts,
       "fecDuplicatePkts": fecDuplicatePkts,
       "fecReorderedPkts": fecReorderedPkts,
       "fecIncorrectSeqNumbers": fecIncorrectSeqNumbers,
       "fecDiscontinuities": fecDiscontinuities,
       "notifications": notifications,
       "statusFlags": statusFlags,
       "moduleStatusTable": moduleStatusTable,
       "moduleStatusEntry": moduleStatusEntry,
       "moduleId": moduleId,
       "modulePidConflictStatus": modulePidConflictStatus,
       "moduleTemperatureHigh": moduleTemperatureHigh,
       "moduleTemperatureLow": moduleTemperatureLow,
       "modulePidCapaStatus": modulePidCapaStatus,
       "modulePsisiCaptureCapaStatus": modulePsisiCaptureCapaStatus,
       "moduleSidAllocStatus": moduleSidAllocStatus,
       "moduleCaDetectStatus": moduleCaDetectStatus,
       "moduleDetectStatus": moduleDetectStatus,
       "moduleVoltageHigh": moduleVoltageHigh,
       "moduleVoltageLow": moduleVoltageLow,
       "moduleCurrentHigh": moduleCurrentHigh,
       "moduleCurrentLow": moduleCurrentLow,
       "moduleDaemonInitStatus": moduleDaemonInitStatus,
       "moduleDriverStatus": moduleDriverStatus,
       "moduleHwStatus": moduleHwStatus,
       "moduleFanStatus": moduleFanStatus,
       "modulePowerSourceStatus": modulePowerSourceStatus,
       "modulePsuOverloadStatus": modulePsuOverloadStatus,
       "moduleBootupProgressStatus": moduleBootupProgressStatus,
       "moduleBootupRetryStatus": moduleBootupRetryStatus,
       "moduleBootupStatus": moduleBootupStatus,
       "moduleShutdownProgressStatus": moduleShutdownProgressStatus,
       "moduleConnStatus": moduleConnStatus,
       "moduleCompatStatus": moduleCompatStatus,
       "moduleUpcPowerLow": moduleUpcPowerLow,
       "moduleUpcPowerHigh": moduleUpcPowerHigh,
       "moduleCalibrDataStatus": moduleCalibrDataStatus,
       "moduleCalibrDataCheckStatus": moduleCalibrDataCheckStatus,
       "moduleDescrStatus": moduleDescrStatus,
       "moduleBackupStatus": moduleBackupStatus,
       "moduleNitOutputsStatus": moduleNitOutputsStatus,
       "moduleNitSelectionStatus": moduleNitSelectionStatus,
       "moduleNitConfChangeStatus": moduleNitConfChangeStatus,
       "moduleNitDataQueryStatus": moduleNitDataQueryStatus,
       "moduleNitWizardStatus": moduleNitWizardStatus,
       "moduleQamFreqStatus": moduleQamFreqStatus,
       "moduleOutputSidStatus": moduleOutputSidStatus,
       "moduleConfStatus": moduleConfStatus,
       "moduleFreqStatus": moduleFreqStatus,
       "moduleOutputPowerStatus": moduleOutputPowerStatus,
       "moduleSymrateStatus": moduleSymrateStatus,
       "moduleChanDistStatus": moduleChanDistStatus,
       "moduleLnbVoltStatus": moduleLnbVoltStatus,
       "moduleFecRateStatus": moduleFecRateStatus,
       "moduleLnbCurrStatus": moduleLnbCurrStatus,
       "moduleFreqOffsetStatus": moduleFreqOffsetStatus,
       "moduleDescrRestartStatus": moduleDescrRestartStatus,
       "moduleCamRestartStatus": moduleCamRestartStatus,
       "moduleEcmgStatus": moduleEcmgStatus,
       "moduleEcmStreamStatus": moduleEcmStreamStatus,
       "moduleEmmStatus": moduleEmmStatus,
       "moduleEmmStreamStatus": moduleEmmStreamStatus,
       "moduleEcmgConnStatus": moduleEcmgConnStatus,
       "moduleEmmConnStatus": moduleEmmConnStatus,
       "moduleEcmgSpareStatus": moduleEcmgSpareStatus,
       "moduleBootloaderAvailStatus": moduleBootloaderAvailStatus,
       "moduleBl1UpdateProgStatus": moduleBl1UpdateProgStatus,
       "moduleBl2UpdateProgStatus": moduleBl2UpdateProgStatus,
       "moduleBl1UpdateStatus": moduleBl1UpdateStatus,
       "moduleBl2UpdateStatus": moduleBl2UpdateStatus,
       "moduleActiveBackupStatus": moduleActiveBackupStatus,
       "moduleConfProgressStatus": moduleConfProgressStatus,
       "modulePresenceStatus": modulePresenceStatus,
       "moduleProcessRestartStatus": moduleProcessRestartStatus,
       "moduleBackupLicenseStatus": moduleBackupLicenseStatus,
       "modulePsisiEditorLicenseStatus": modulePsisiEditorLicenseStatus,
       "moduleMuxLicenseStatus": moduleMuxLicenseStatus,
       "moduleDemuxLicenseStatus": moduleDemuxLicenseStatus,
       "moduleDvbLicenseStatus": moduleDvbLicenseStatus,
       "moduleMsdLicenseStatus": moduleMsdLicenseStatus,
       "moduleDvbs2LicenseStatus": moduleDvbs2LicenseStatus,
       "moduleDvbt2LicenseStatus": moduleDvbt2LicenseStatus,
       "moduleScsLicenseStatus": moduleScsLicenseStatus,
       "moduleCliLoginStatus": moduleCliLoginStatus,
       "moduleRedunActivationStatus": moduleRedunActivationStatus,
       "moduleExtioPinSignalingStatus": moduleExtioPinSignalingStatus,
       "moduleBackupPsuStatus": moduleBackupPsuStatus,
       "moduleIntrusionStatus": moduleIntrusionStatus,
       "moduleRedunStatus": moduleRedunStatus,
       "moduleBackupHwStatus": moduleBackupHwStatus,
       "moduleSwUpdateProgress": moduleSwUpdateProgress,
       "moduleSwUpdateStatus": moduleSwUpdateStatus,
       "moduleEitLicenseStatus": moduleEitLicenseStatus,
       "moduleDescramblingStatus": moduleDescramblingStatus,
       "moduleDvbTimeStatus": moduleDvbTimeStatus,
       "moduleTunerDcFeedStatus": moduleTunerDcFeedStatus,
       "moduleTunerPlpSelectionReqStatus": moduleTunerPlpSelectionReqStatus,
       "moduleTunerPlpStatus": moduleTunerPlpStatus,
       "moduleTunerHierarchyStatus": moduleTunerHierarchyStatus,
       "moduleEcmStatus": moduleEcmStatus,
       "moduleScramConflictStatus": moduleScramConflictStatus,
       "moduleScramSharedStatus": moduleScramSharedStatus,
       "moduleBackupVoltageHigh": moduleBackupVoltageHigh,
       "moduleBackupVoltageLow": moduleBackupVoltageLow,
       "moduleSdtTableStatus": moduleSdtTableStatus,
       "moduleDescramblingRestart": moduleDescramblingRestart,
       "moduleCaModuleRestart": moduleCaModuleRestart,
       "moduleCaMenuStatus": moduleCaMenuStatus,
       "moduleInvalidCamRouting": moduleInvalidCamRouting,
       "moduleNitSidConflict": moduleNitSidConflict,
       "moduleLicenseMissingFEC": moduleLicenseMissingFEC,
       "moduleFecCorrectionStatus": moduleFecCorrectionStatus,
       "moduleFecPacketDropStatus": moduleFecPacketDropStatus,
       "moduleFecMediaPktsStatus": moduleFecMediaPktsStatus,
       "moduleSfpLinkStatus": moduleSfpLinkStatus,
       "moduleBackupSyncModeOff": moduleBackupSyncModeOff,
       "moduleBackupSyncModeManual": moduleBackupSyncModeManual,
       "moduleBackupSyncModeAuto": moduleBackupSyncModeAuto,
       "moduleBackupSyncConfStatus": moduleBackupSyncConfStatus,
       "moduleBackupSyncStatus": moduleBackupSyncStatus,
       "moduleBackupSyncSwCompatibility": moduleBackupSyncSwCompatibility,
       "moduleBackupSyncHwCompatibility": moduleBackupSyncHwCompatibility,
       "moduleBackupSyncConfFaultStatus": moduleBackupSyncConfFaultStatus,
       "moduleBackupSyncConnectionStatus": moduleBackupSyncConnectionStatus,
       "moduleBackupSyncFromBackupStatus": moduleBackupSyncFromBackupStatus,
       "moduleBackupSyncRebootStatus": moduleBackupSyncRebootStatus,
       "moduleBackupSyncLicenseCompatStatus": moduleBackupSyncLicenseCompatStatus,
       "moduleBackupSyncLicenseCompareStatus": moduleBackupSyncLicenseCompareStatus,
       "moduleDeviceFirstBootStatus": moduleDeviceFirstBootStatus,
       "modulePartitionConfigurationBackup": modulePartitionConfigurationBackup,
       "modulePartitionConfigurationRestore": modulePartitionConfigurationRestore,
       "moduleSwRevertStatus": moduleSwRevertStatus,
       "moduleMaxOutputPidsStatus": moduleMaxOutputPidsStatus,
       "moduleUserRebootStatus": moduleUserRebootStatus,
       "moduleRemovalStatus": moduleRemovalStatus,
       "moduleInsertionStatus": moduleInsertionStatus,
       "moduleSptsInputConfStatus": moduleSptsInputConfStatus,
       "ifStatusTable": ifStatusTable,
       "ifStatusEntry": ifStatusEntry,
       "ifId": ifId,
       "ifDirection": ifDirection,
       "ifSignalStatus": ifSignalStatus,
       "ifAsiLinkStatus": ifAsiLinkStatus,
       "ifLinkStatus": ifLinkStatus,
       "tsStatusTable": tsStatusTable,
       "tsStatusEntry": tsStatusEntry,
       "tsPidRemappingStatus": tsPidRemappingStatus,
       "tsManualTableInsertStatus": tsManualTableInsertStatus,
       "tsPassthruDupStatus": tsPassthruDupStatus,
       "tsSyncStatus": tsSyncStatus,
       "tsRxStatus": tsRxStatus,
       "tsInputBufferStatus": tsInputBufferStatus,
       "tsNetworkStatus": tsNetworkStatus,
       "tsPsisiCapaStatus": tsPsisiCapaStatus,
       "tsMultiplexDiscardStatus": tsMultiplexDiscardStatus,
       "tsMultiplexDelayStatus": tsMultiplexDelayStatus,
       "tsCbrOversubscriptionStatus": tsCbrOversubscriptionStatus,
       "tsCbrDiscardStatus": tsCbrDiscardStatus,
       "tsIpInputCapaStatus": tsIpInputCapaStatus,
       "tsEitReinsertCapaStatus": tsEitReinsertCapaStatus,
       "tsSectionCapaStatus": tsSectionCapaStatus,
       "tsRtpInputStatus": tsRtpInputStatus,
       "tsRtpSeqStatus": tsRtpSeqStatus,
       "tsTdtTotGenStatus": tsTdtTotGenStatus,
       "tsSttGenStatus": tsSttGenStatus,
       "tsFecPacketCorrectionStatus": tsFecPacketCorrectionStatus,
       "tsFecInputAnomalyStatus": tsFecInputAnomalyStatus,
       "tsFecCorrectionCapacityStatus": tsFecCorrectionCapacityStatus,
       "tsIpMirrorOutputPacketLossStatus": tsIpMirrorOutputPacketLossStatus,
       "serviceStatusTable": serviceStatusTable,
       "serviceStatusEntry": serviceStatusEntry,
       "serviceId": serviceId,
       "serviceStatus": serviceStatus,
       "pidStatusTable": pidStatusTable,
       "pidStatusEntry": pidStatusEntry,
       "pId": pId,
       "pidStatus": pidStatus}
)
