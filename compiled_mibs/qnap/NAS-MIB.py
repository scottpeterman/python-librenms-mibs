# SNMP MIB module (NAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\qnap\NAS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:36 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681)
)
_StorageSystem_ObjectIdentity = ObjectIdentity
storageSystem = _StorageSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1)
)
_SystemEventMsg_ObjectIdentity = ObjectIdentity
systemEventMsg = _SystemEventMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 1)
)
_EventInformMsg_Type = DisplayString
_EventInformMsg_Object = MibScalar
eventInformMsg = _EventInformMsg_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 1, 101),
    _EventInformMsg_Type()
)
eventInformMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInformMsg.setStatus("current")
_EventWarningMsg_Type = DisplayString
_EventWarningMsg_Object = MibScalar
eventWarningMsg = _EventWarningMsg_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 1, 102),
    _EventWarningMsg_Type()
)
eventWarningMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventWarningMsg.setStatus("current")
_EventErrorMsg_Type = DisplayString
_EventErrorMsg_Object = MibScalar
eventErrorMsg = _EventErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 1, 103),
    _EventErrorMsg_Type()
)
eventErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventErrorMsg.setStatus("current")
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2)
)
_SystemCPU_Usage_Type = DisplayString
_SystemCPU_Usage_Object = MibScalar
systemCPU_Usage = _SystemCPU_Usage_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 1),
    _SystemCPU_Usage_Type()
)
systemCPU_Usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPU_Usage.setStatus("current")
_SystemTotalMem_Type = DisplayString
_SystemTotalMem_Object = MibScalar
systemTotalMem = _SystemTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 2),
    _SystemTotalMem_Type()
)
systemTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTotalMem.setStatus("current")
_SystemFreeMem_Type = DisplayString
_SystemFreeMem_Object = MibScalar
systemFreeMem = _SystemFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 3),
    _SystemFreeMem_Type()
)
systemFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFreeMem.setStatus("current")
_SystemUptime_Type = TimeTicks
_SystemUptime_Object = MibScalar
systemUptime = _SystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 4),
    _SystemUptime_Type()
)
systemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptime.setStatus("current")
_Cpu_Temperature_Type = DisplayString
_Cpu_Temperature_Object = MibScalar
cpu_Temperature = _Cpu_Temperature_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 5),
    _Cpu_Temperature_Type()
)
cpu_Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu_Temperature.setStatus("current")
_SystemTemperature_Type = DisplayString
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 6),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")
_IfNumber_Type = Integer32
_IfNumber_Object = MibScalar
ifNumber = _IfNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 8),
    _IfNumber_Type()
)
ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumber.setStatus("current")
_SystemIfTable_Object = MibTable
systemIfTable = _SystemIfTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 9)
)
if mibBuilder.loadTexts:
    systemIfTable.setStatus("current")
_IfEntry_Object = MibTableRow
ifEntry = _IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 9, 1)
)
ifEntry.setIndexNames(
    (0, "NAS-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifEntry.setStatus("current")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 9, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")


class _IfDescr_Type(DisplayString):
    """Custom type ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfDescr_Type.__name__ = "DisplayString"
_IfDescr_Object = MibTableColumn
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 9, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("current")
_IfPacketsReceived_Type = Counter32
_IfPacketsReceived_Object = MibTableColumn
ifPacketsReceived = _IfPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 9, 1, 3),
    _IfPacketsReceived_Type()
)
ifPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPacketsReceived.setStatus("current")
_IfPacketsSent_Type = Counter32
_IfPacketsSent_Object = MibTableColumn
ifPacketsSent = _IfPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 9, 1, 4),
    _IfPacketsSent_Type()
)
ifPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPacketsSent.setStatus("current")
_IfErrorPackets_Type = Counter32
_IfErrorPackets_Object = MibTableColumn
ifErrorPackets = _IfErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 9, 1, 5),
    _IfErrorPackets_Type()
)
ifErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrorPackets.setStatus("current")
_HdNumber_Type = Integer32
_HdNumber_Object = MibScalar
hdNumber = _HdNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 10),
    _HdNumber_Type()
)
hdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdNumber.setStatus("current")
_SystemHdTable_Object = MibTable
systemHdTable = _SystemHdTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11)
)
if mibBuilder.loadTexts:
    systemHdTable.setStatus("current")
_HdEntry_Object = MibTableRow
hdEntry = _HdEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1)
)
hdEntry.setIndexNames(
    (0, "NAS-MIB", "hdIndex"),
)
if mibBuilder.loadTexts:
    hdEntry.setStatus("current")
_HdIndex_Type = Integer32
_HdIndex_Object = MibTableColumn
hdIndex = _HdIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1, 1),
    _HdIndex_Type()
)
hdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdIndex.setStatus("current")


class _HdDescr_Type(DisplayString):
    """Custom type hdDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HdDescr_Type.__name__ = "DisplayString"
_HdDescr_Object = MibTableColumn
hdDescr = _HdDescr_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1, 2),
    _HdDescr_Type()
)
hdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdDescr.setStatus("current")
_HdTemperature_Type = DisplayString
_HdTemperature_Object = MibTableColumn
hdTemperature = _HdTemperature_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1, 3),
    _HdTemperature_Type()
)
hdTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdTemperature.setStatus("current")


class _HdStatus_Type(Integer32):
    """Custom type hdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_HdStatus_Type.__name__ = "Integer32"
_HdStatus_Object = MibTableColumn
hdStatus = _HdStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1, 4),
    _HdStatus_Type()
)
hdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdStatus.setStatus("current")
_HdModel_Type = DisplayString
_HdModel_Object = MibTableColumn
hdModel = _HdModel_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1, 5),
    _HdModel_Type()
)
hdModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdModel.setStatus("current")
_HdCapacity_Type = DisplayString
_HdCapacity_Object = MibTableColumn
hdCapacity = _HdCapacity_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1, 6),
    _HdCapacity_Type()
)
hdCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdCapacity.setStatus("current")
_HdSmartInfo_Type = DisplayString
_HdSmartInfo_Object = MibTableColumn
hdSmartInfo = _HdSmartInfo_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 11, 1, 7),
    _HdSmartInfo_Type()
)
hdSmartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdSmartInfo.setStatus("current")
_ModelName_Type = DisplayString
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 12),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")
_HostName_Type = DisplayString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 13),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_SysFanNumber_Type = Integer32
_SysFanNumber_Object = MibScalar
sysFanNumber = _SysFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 14),
    _SysFanNumber_Type()
)
sysFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanNumber.setStatus("current")
_SystemFanTable_Object = MibTable
systemFanTable = _SystemFanTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 15)
)
if mibBuilder.loadTexts:
    systemFanTable.setStatus("current")
_SysFanEntry_Object = MibTableRow
sysFanEntry = _SysFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 15, 1)
)
sysFanEntry.setIndexNames(
    (0, "NAS-MIB", "sysFanIndex"),
)
if mibBuilder.loadTexts:
    sysFanEntry.setStatus("current")
_SysFanIndex_Type = Integer32
_SysFanIndex_Object = MibTableColumn
sysFanIndex = _SysFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 15, 1, 1),
    _SysFanIndex_Type()
)
sysFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanIndex.setStatus("current")


class _SysFanDescr_Type(DisplayString):
    """Custom type sysFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysFanDescr_Type.__name__ = "DisplayString"
_SysFanDescr_Object = MibTableColumn
sysFanDescr = _SysFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 15, 1, 2),
    _SysFanDescr_Type()
)
sysFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanDescr.setStatus("current")


class _SysFanSpeed_Type(DisplayString):
    """Custom type sysFanSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysFanSpeed_Type.__name__ = "DisplayString"
_SysFanSpeed_Object = MibTableColumn
sysFanSpeed = _SysFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 15, 1, 3),
    _SysFanSpeed_Type()
)
sysFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanSpeed.setStatus("current")
_SysVolumeNumber_Type = Integer32
_SysVolumeNumber_Object = MibScalar
sysVolumeNumber = _SysVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 16),
    _SysVolumeNumber_Type()
)
sysVolumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeNumber.setStatus("current")
_SystemVolumeTable_Object = MibTable
systemVolumeTable = _SystemVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17)
)
if mibBuilder.loadTexts:
    systemVolumeTable.setStatus("current")
_SysVolumeEntry_Object = MibTableRow
sysVolumeEntry = _SysVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17, 1)
)
sysVolumeEntry.setIndexNames(
    (0, "NAS-MIB", "sysVolumeIndex"),
)
if mibBuilder.loadTexts:
    sysVolumeEntry.setStatus("current")
_SysVolumeIndex_Type = Integer32
_SysVolumeIndex_Object = MibTableColumn
sysVolumeIndex = _SysVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17, 1, 1),
    _SysVolumeIndex_Type()
)
sysVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeIndex.setStatus("current")


class _SysVolumeDescr_Type(DisplayString):
    """Custom type sysVolumeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysVolumeDescr_Type.__name__ = "DisplayString"
_SysVolumeDescr_Object = MibTableColumn
sysVolumeDescr = _SysVolumeDescr_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17, 1, 2),
    _SysVolumeDescr_Type()
)
sysVolumeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeDescr.setStatus("current")


class _SysVolumeFS_Type(DisplayString):
    """Custom type sysVolumeFS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysVolumeFS_Type.__name__ = "DisplayString"
_SysVolumeFS_Object = MibTableColumn
sysVolumeFS = _SysVolumeFS_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17, 1, 3),
    _SysVolumeFS_Type()
)
sysVolumeFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeFS.setStatus("current")


class _SysVolumeTotalSize_Type(DisplayString):
    """Custom type sysVolumeTotalSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysVolumeTotalSize_Type.__name__ = "DisplayString"
_SysVolumeTotalSize_Object = MibTableColumn
sysVolumeTotalSize = _SysVolumeTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17, 1, 4),
    _SysVolumeTotalSize_Type()
)
sysVolumeTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeTotalSize.setStatus("current")


class _SysVolumeFreeSize_Type(DisplayString):
    """Custom type sysVolumeFreeSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysVolumeFreeSize_Type.__name__ = "DisplayString"
_SysVolumeFreeSize_Object = MibTableColumn
sysVolumeFreeSize = _SysVolumeFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17, 1, 5),
    _SysVolumeFreeSize_Type()
)
sysVolumeFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeFreeSize.setStatus("current")


class _SysVolumeStatus_Type(DisplayString):
    """Custom type sysVolumeStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysVolumeStatus_Type.__name__ = "DisplayString"
_SysVolumeStatus_Object = MibTableColumn
sysVolumeStatus = _SysVolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 17, 1, 6),
    _SysVolumeStatus_Type()
)
sysVolumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeStatus.setStatus("current")
_JBODInfo_Type = DisplayString
_JBODInfo_Object = MibScalar
jBODInfo = _JBODInfo_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18),
    _JBODInfo_Type()
)
jBODInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODInfo.setStatus("current")
_JBODBitmap_Type = DisplayString
_JBODBitmap_Object = MibScalar
jBODBitmap = _JBODBitmap_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 1),
    _JBODBitmap_Type()
)
jBODBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODBitmap.setStatus("current")
_JBODInfos_Object = MibTable
jBODInfos = _JBODInfos_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 2)
)
if mibBuilder.loadTexts:
    jBODInfos.setStatus("current")
_JBODInfosEntry_Object = MibTableRow
jBODInfosEntry = _JBODInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 2, 1)
)
jBODInfosEntry.setIndexNames(
    (0, "NAS-MIB", "jBODid"),
)
if mibBuilder.loadTexts:
    jBODInfosEntry.setStatus("current")
_JBODid_Type = Integer32
_JBODid_Object = MibTableColumn
jBODid = _JBODid_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 2, 1, 1),
    _JBODid_Type()
)
jBODid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODid.setStatus("current")
_JBODHdNumber_Type = Integer32
_JBODHdNumber_Object = MibTableColumn
jBODHdNumber = _JBODHdNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 2, 1, 2),
    _JBODHdNumber_Type()
)
jBODHdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdNumber.setStatus("current")
_JBODHdTable1_Object = MibTable
jBODHdTable1 = _JBODHdTable1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3)
)
if mibBuilder.loadTexts:
    jBODHdTable1.setStatus("current")
_JBODHdEntry1_Object = MibTableRow
jBODHdEntry1 = _JBODHdEntry1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1)
)
jBODHdEntry1.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex1"),
)
if mibBuilder.loadTexts:
    jBODHdEntry1.setStatus("current")
_JBODHdIndex1_Type = Integer32
_JBODHdIndex1_Object = MibTableColumn
jBODHdIndex1 = _JBODHdIndex1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1, 1),
    _JBODHdIndex1_Type()
)
jBODHdIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex1.setStatus("current")


class _JBODHdDescr1_Type(DisplayString):
    """Custom type jBODHdDescr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr1_Type.__name__ = "DisplayString"
_JBODHdDescr1_Object = MibTableColumn
jBODHdDescr1 = _JBODHdDescr1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1, 2),
    _JBODHdDescr1_Type()
)
jBODHdDescr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr1.setStatus("current")
_JBODHdTemperature1_Type = DisplayString
_JBODHdTemperature1_Object = MibTableColumn
jBODHdTemperature1 = _JBODHdTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1, 3),
    _JBODHdTemperature1_Type()
)
jBODHdTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature1.setStatus("current")


class _JBODHdStatus1_Type(Integer32):
    """Custom type jBODHdStatus1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus1_Type.__name__ = "Integer32"
_JBODHdStatus1_Object = MibTableColumn
jBODHdStatus1 = _JBODHdStatus1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1, 4),
    _JBODHdStatus1_Type()
)
jBODHdStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus1.setStatus("current")
_JBODHdModel1_Type = DisplayString
_JBODHdModel1_Object = MibTableColumn
jBODHdModel1 = _JBODHdModel1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1, 5),
    _JBODHdModel1_Type()
)
jBODHdModel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel1.setStatus("current")
_JBODHdCapacity1_Type = DisplayString
_JBODHdCapacity1_Object = MibTableColumn
jBODHdCapacity1 = _JBODHdCapacity1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1, 6),
    _JBODHdCapacity1_Type()
)
jBODHdCapacity1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity1.setStatus("current")
_JBODHdSmartInfo1_Type = DisplayString
_JBODHdSmartInfo1_Object = MibTableColumn
jBODHdSmartInfo1 = _JBODHdSmartInfo1_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 3, 1, 7),
    _JBODHdSmartInfo1_Type()
)
jBODHdSmartInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo1.setStatus("current")
_JBODHdTable2_Object = MibTable
jBODHdTable2 = _JBODHdTable2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4)
)
if mibBuilder.loadTexts:
    jBODHdTable2.setStatus("current")
_JBODHdEntry2_Object = MibTableRow
jBODHdEntry2 = _JBODHdEntry2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1)
)
jBODHdEntry2.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex2"),
)
if mibBuilder.loadTexts:
    jBODHdEntry2.setStatus("current")
_JBODHdIndex2_Type = Integer32
_JBODHdIndex2_Object = MibTableColumn
jBODHdIndex2 = _JBODHdIndex2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1, 1),
    _JBODHdIndex2_Type()
)
jBODHdIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex2.setStatus("current")


class _JBODHdDescr2_Type(DisplayString):
    """Custom type jBODHdDescr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr2_Type.__name__ = "DisplayString"
_JBODHdDescr2_Object = MibTableColumn
jBODHdDescr2 = _JBODHdDescr2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1, 2),
    _JBODHdDescr2_Type()
)
jBODHdDescr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr2.setStatus("current")
_JBODHdTemperature2_Type = DisplayString
_JBODHdTemperature2_Object = MibTableColumn
jBODHdTemperature2 = _JBODHdTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1, 3),
    _JBODHdTemperature2_Type()
)
jBODHdTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature2.setStatus("current")


class _JBODHdStatus2_Type(Integer32):
    """Custom type jBODHdStatus2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus2_Type.__name__ = "Integer32"
_JBODHdStatus2_Object = MibTableColumn
jBODHdStatus2 = _JBODHdStatus2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1, 4),
    _JBODHdStatus2_Type()
)
jBODHdStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus2.setStatus("current")
_JBODHdModel2_Type = DisplayString
_JBODHdModel2_Object = MibTableColumn
jBODHdModel2 = _JBODHdModel2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1, 5),
    _JBODHdModel2_Type()
)
jBODHdModel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel2.setStatus("current")
_JBODHdCapacity2_Type = DisplayString
_JBODHdCapacity2_Object = MibTableColumn
jBODHdCapacity2 = _JBODHdCapacity2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1, 6),
    _JBODHdCapacity2_Type()
)
jBODHdCapacity2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity2.setStatus("current")
_JBODHdSmartInfo2_Type = DisplayString
_JBODHdSmartInfo2_Object = MibTableColumn
jBODHdSmartInfo2 = _JBODHdSmartInfo2_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 4, 1, 7),
    _JBODHdSmartInfo2_Type()
)
jBODHdSmartInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo2.setStatus("current")
_JBODHdTable3_Object = MibTable
jBODHdTable3 = _JBODHdTable3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5)
)
if mibBuilder.loadTexts:
    jBODHdTable3.setStatus("current")
_JBODHdEntry3_Object = MibTableRow
jBODHdEntry3 = _JBODHdEntry3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1)
)
jBODHdEntry3.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex3"),
)
if mibBuilder.loadTexts:
    jBODHdEntry3.setStatus("current")
_JBODHdIndex3_Type = Integer32
_JBODHdIndex3_Object = MibTableColumn
jBODHdIndex3 = _JBODHdIndex3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1, 1),
    _JBODHdIndex3_Type()
)
jBODHdIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex3.setStatus("current")


class _JBODHdDescr3_Type(DisplayString):
    """Custom type jBODHdDescr3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr3_Type.__name__ = "DisplayString"
_JBODHdDescr3_Object = MibTableColumn
jBODHdDescr3 = _JBODHdDescr3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1, 2),
    _JBODHdDescr3_Type()
)
jBODHdDescr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr3.setStatus("current")
_JBODHdTemperature3_Type = DisplayString
_JBODHdTemperature3_Object = MibTableColumn
jBODHdTemperature3 = _JBODHdTemperature3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1, 3),
    _JBODHdTemperature3_Type()
)
jBODHdTemperature3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature3.setStatus("current")


class _JBODHdStatus3_Type(Integer32):
    """Custom type jBODHdStatus3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus3_Type.__name__ = "Integer32"
_JBODHdStatus3_Object = MibTableColumn
jBODHdStatus3 = _JBODHdStatus3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1, 4),
    _JBODHdStatus3_Type()
)
jBODHdStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus3.setStatus("current")
_JBODHdModel3_Type = DisplayString
_JBODHdModel3_Object = MibTableColumn
jBODHdModel3 = _JBODHdModel3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1, 5),
    _JBODHdModel3_Type()
)
jBODHdModel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel3.setStatus("current")
_JBODHdCapacity3_Type = DisplayString
_JBODHdCapacity3_Object = MibTableColumn
jBODHdCapacity3 = _JBODHdCapacity3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1, 6),
    _JBODHdCapacity3_Type()
)
jBODHdCapacity3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity3.setStatus("current")
_JBODHdSmartInfo3_Type = DisplayString
_JBODHdSmartInfo3_Object = MibTableColumn
jBODHdSmartInfo3 = _JBODHdSmartInfo3_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 5, 1, 7),
    _JBODHdSmartInfo3_Type()
)
jBODHdSmartInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo3.setStatus("current")
_JBODHdTable4_Object = MibTable
jBODHdTable4 = _JBODHdTable4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6)
)
if mibBuilder.loadTexts:
    jBODHdTable4.setStatus("current")
_JBODHdEntry4_Object = MibTableRow
jBODHdEntry4 = _JBODHdEntry4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1)
)
jBODHdEntry4.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex4"),
)
if mibBuilder.loadTexts:
    jBODHdEntry4.setStatus("current")
_JBODHdIndex4_Type = Integer32
_JBODHdIndex4_Object = MibTableColumn
jBODHdIndex4 = _JBODHdIndex4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1, 1),
    _JBODHdIndex4_Type()
)
jBODHdIndex4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex4.setStatus("current")


class _JBODHdDescr4_Type(DisplayString):
    """Custom type jBODHdDescr4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr4_Type.__name__ = "DisplayString"
_JBODHdDescr4_Object = MibTableColumn
jBODHdDescr4 = _JBODHdDescr4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1, 2),
    _JBODHdDescr4_Type()
)
jBODHdDescr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr4.setStatus("current")
_JBODHdTemperature4_Type = DisplayString
_JBODHdTemperature4_Object = MibTableColumn
jBODHdTemperature4 = _JBODHdTemperature4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1, 3),
    _JBODHdTemperature4_Type()
)
jBODHdTemperature4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature4.setStatus("current")


class _JBODHdStatus4_Type(Integer32):
    """Custom type jBODHdStatus4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus4_Type.__name__ = "Integer32"
_JBODHdStatus4_Object = MibTableColumn
jBODHdStatus4 = _JBODHdStatus4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1, 4),
    _JBODHdStatus4_Type()
)
jBODHdStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus4.setStatus("current")
_JBODHdModel4_Type = DisplayString
_JBODHdModel4_Object = MibTableColumn
jBODHdModel4 = _JBODHdModel4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1, 5),
    _JBODHdModel4_Type()
)
jBODHdModel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel4.setStatus("current")
_JBODHdCapacity4_Type = DisplayString
_JBODHdCapacity4_Object = MibTableColumn
jBODHdCapacity4 = _JBODHdCapacity4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1, 6),
    _JBODHdCapacity4_Type()
)
jBODHdCapacity4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity4.setStatus("current")
_JBODHdSmartInfo4_Type = DisplayString
_JBODHdSmartInfo4_Object = MibTableColumn
jBODHdSmartInfo4 = _JBODHdSmartInfo4_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 6, 1, 7),
    _JBODHdSmartInfo4_Type()
)
jBODHdSmartInfo4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo4.setStatus("current")
_JBODHdTable5_Object = MibTable
jBODHdTable5 = _JBODHdTable5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7)
)
if mibBuilder.loadTexts:
    jBODHdTable5.setStatus("current")
_JBODHdEntry5_Object = MibTableRow
jBODHdEntry5 = _JBODHdEntry5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1)
)
jBODHdEntry5.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex5"),
)
if mibBuilder.loadTexts:
    jBODHdEntry5.setStatus("current")
_JBODHdIndex5_Type = Integer32
_JBODHdIndex5_Object = MibTableColumn
jBODHdIndex5 = _JBODHdIndex5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1, 1),
    _JBODHdIndex5_Type()
)
jBODHdIndex5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex5.setStatus("current")


class _JBODHdDescr5_Type(DisplayString):
    """Custom type jBODHdDescr5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr5_Type.__name__ = "DisplayString"
_JBODHdDescr5_Object = MibTableColumn
jBODHdDescr5 = _JBODHdDescr5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1, 2),
    _JBODHdDescr5_Type()
)
jBODHdDescr5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr5.setStatus("current")
_JBODHdTemperature5_Type = DisplayString
_JBODHdTemperature5_Object = MibTableColumn
jBODHdTemperature5 = _JBODHdTemperature5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1, 3),
    _JBODHdTemperature5_Type()
)
jBODHdTemperature5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature5.setStatus("current")


class _JBODHdStatus5_Type(Integer32):
    """Custom type jBODHdStatus5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus5_Type.__name__ = "Integer32"
_JBODHdStatus5_Object = MibTableColumn
jBODHdStatus5 = _JBODHdStatus5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1, 4),
    _JBODHdStatus5_Type()
)
jBODHdStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus5.setStatus("current")
_JBODHdModel5_Type = DisplayString
_JBODHdModel5_Object = MibTableColumn
jBODHdModel5 = _JBODHdModel5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1, 5),
    _JBODHdModel5_Type()
)
jBODHdModel5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel5.setStatus("current")
_JBODHdCapacity5_Type = DisplayString
_JBODHdCapacity5_Object = MibTableColumn
jBODHdCapacity5 = _JBODHdCapacity5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1, 6),
    _JBODHdCapacity5_Type()
)
jBODHdCapacity5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity5.setStatus("current")
_JBODHdSmartInfo5_Type = DisplayString
_JBODHdSmartInfo5_Object = MibTableColumn
jBODHdSmartInfo5 = _JBODHdSmartInfo5_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 7, 1, 7),
    _JBODHdSmartInfo5_Type()
)
jBODHdSmartInfo5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo5.setStatus("current")
_JBODHdTable6_Object = MibTable
jBODHdTable6 = _JBODHdTable6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8)
)
if mibBuilder.loadTexts:
    jBODHdTable6.setStatus("current")
_JBODHdEntry6_Object = MibTableRow
jBODHdEntry6 = _JBODHdEntry6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1)
)
jBODHdEntry6.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex6"),
)
if mibBuilder.loadTexts:
    jBODHdEntry6.setStatus("current")
_JBODHdIndex6_Type = Integer32
_JBODHdIndex6_Object = MibTableColumn
jBODHdIndex6 = _JBODHdIndex6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1, 1),
    _JBODHdIndex6_Type()
)
jBODHdIndex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex6.setStatus("current")


class _JBODHdDescr6_Type(DisplayString):
    """Custom type jBODHdDescr6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr6_Type.__name__ = "DisplayString"
_JBODHdDescr6_Object = MibTableColumn
jBODHdDescr6 = _JBODHdDescr6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1, 2),
    _JBODHdDescr6_Type()
)
jBODHdDescr6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr6.setStatus("current")
_JBODHdTemperature6_Type = DisplayString
_JBODHdTemperature6_Object = MibTableColumn
jBODHdTemperature6 = _JBODHdTemperature6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1, 3),
    _JBODHdTemperature6_Type()
)
jBODHdTemperature6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature6.setStatus("current")


class _JBODHdStatus6_Type(Integer32):
    """Custom type jBODHdStatus6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus6_Type.__name__ = "Integer32"
_JBODHdStatus6_Object = MibTableColumn
jBODHdStatus6 = _JBODHdStatus6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1, 4),
    _JBODHdStatus6_Type()
)
jBODHdStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus6.setStatus("current")
_JBODHdModel6_Type = DisplayString
_JBODHdModel6_Object = MibTableColumn
jBODHdModel6 = _JBODHdModel6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1, 5),
    _JBODHdModel6_Type()
)
jBODHdModel6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel6.setStatus("current")
_JBODHdCapacity6_Type = DisplayString
_JBODHdCapacity6_Object = MibTableColumn
jBODHdCapacity6 = _JBODHdCapacity6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1, 6),
    _JBODHdCapacity6_Type()
)
jBODHdCapacity6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity6.setStatus("current")
_JBODHdSmartInfo6_Type = DisplayString
_JBODHdSmartInfo6_Object = MibTableColumn
jBODHdSmartInfo6 = _JBODHdSmartInfo6_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 8, 1, 7),
    _JBODHdSmartInfo6_Type()
)
jBODHdSmartInfo6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo6.setStatus("current")
_JBODHdTable7_Object = MibTable
jBODHdTable7 = _JBODHdTable7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9)
)
if mibBuilder.loadTexts:
    jBODHdTable7.setStatus("current")
_JBODHdEntry7_Object = MibTableRow
jBODHdEntry7 = _JBODHdEntry7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1)
)
jBODHdEntry7.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex7"),
)
if mibBuilder.loadTexts:
    jBODHdEntry7.setStatus("current")
_JBODHdIndex7_Type = Integer32
_JBODHdIndex7_Object = MibTableColumn
jBODHdIndex7 = _JBODHdIndex7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1, 1),
    _JBODHdIndex7_Type()
)
jBODHdIndex7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex7.setStatus("current")


class _JBODHdDescr7_Type(DisplayString):
    """Custom type jBODHdDescr7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr7_Type.__name__ = "DisplayString"
_JBODHdDescr7_Object = MibTableColumn
jBODHdDescr7 = _JBODHdDescr7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1, 2),
    _JBODHdDescr7_Type()
)
jBODHdDescr7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr7.setStatus("current")
_JBODHdTemperature7_Type = DisplayString
_JBODHdTemperature7_Object = MibTableColumn
jBODHdTemperature7 = _JBODHdTemperature7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1, 3),
    _JBODHdTemperature7_Type()
)
jBODHdTemperature7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature7.setStatus("current")


class _JBODHdStatus7_Type(Integer32):
    """Custom type jBODHdStatus7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus7_Type.__name__ = "Integer32"
_JBODHdStatus7_Object = MibTableColumn
jBODHdStatus7 = _JBODHdStatus7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1, 4),
    _JBODHdStatus7_Type()
)
jBODHdStatus7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus7.setStatus("current")
_JBODHdModel7_Type = DisplayString
_JBODHdModel7_Object = MibTableColumn
jBODHdModel7 = _JBODHdModel7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1, 5),
    _JBODHdModel7_Type()
)
jBODHdModel7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel7.setStatus("current")
_JBODHdCapacity7_Type = DisplayString
_JBODHdCapacity7_Object = MibTableColumn
jBODHdCapacity7 = _JBODHdCapacity7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1, 6),
    _JBODHdCapacity7_Type()
)
jBODHdCapacity7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity7.setStatus("current")
_JBODHdSmartInfo7_Type = DisplayString
_JBODHdSmartInfo7_Object = MibTableColumn
jBODHdSmartInfo7 = _JBODHdSmartInfo7_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 9, 1, 7),
    _JBODHdSmartInfo7_Type()
)
jBODHdSmartInfo7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo7.setStatus("current")
_JBODHdTable8_Object = MibTable
jBODHdTable8 = _JBODHdTable8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10)
)
if mibBuilder.loadTexts:
    jBODHdTable8.setStatus("current")
_JBODHdEntry8_Object = MibTableRow
jBODHdEntry8 = _JBODHdEntry8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1)
)
jBODHdEntry8.setIndexNames(
    (0, "NAS-MIB", "jBODHdIndex8"),
)
if mibBuilder.loadTexts:
    jBODHdEntry8.setStatus("current")
_JBODHdIndex8_Type = Integer32
_JBODHdIndex8_Object = MibTableColumn
jBODHdIndex8 = _JBODHdIndex8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1, 1),
    _JBODHdIndex8_Type()
)
jBODHdIndex8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdIndex8.setStatus("current")


class _JBODHdDescr8_Type(DisplayString):
    """Custom type jBODHdDescr8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JBODHdDescr8_Type.__name__ = "DisplayString"
_JBODHdDescr8_Object = MibTableColumn
jBODHdDescr8 = _JBODHdDescr8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1, 2),
    _JBODHdDescr8_Type()
)
jBODHdDescr8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdDescr8.setStatus("current")
_JBODHdTemperature8_Type = DisplayString
_JBODHdTemperature8_Object = MibTableColumn
jBODHdTemperature8 = _JBODHdTemperature8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1, 3),
    _JBODHdTemperature8_Type()
)
jBODHdTemperature8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdTemperature8.setStatus("current")


class _JBODHdStatus8_Type(Integer32):
    """Custom type jBODHdStatus8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_JBODHdStatus8_Type.__name__ = "Integer32"
_JBODHdStatus8_Object = MibTableColumn
jBODHdStatus8 = _JBODHdStatus8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1, 4),
    _JBODHdStatus8_Type()
)
jBODHdStatus8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdStatus8.setStatus("current")
_JBODHdModel8_Type = DisplayString
_JBODHdModel8_Object = MibTableColumn
jBODHdModel8 = _JBODHdModel8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1, 5),
    _JBODHdModel8_Type()
)
jBODHdModel8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdModel8.setStatus("current")
_JBODHdCapacity8_Type = DisplayString
_JBODHdCapacity8_Object = MibTableColumn
jBODHdCapacity8 = _JBODHdCapacity8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1, 6),
    _JBODHdCapacity8_Type()
)
jBODHdCapacity8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdCapacity8.setStatus("current")
_JBODHdSmartInfo8_Type = DisplayString
_JBODHdSmartInfo8_Object = MibTableColumn
jBODHdSmartInfo8 = _JBODHdSmartInfo8_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 2, 18, 10, 1, 7),
    _JBODHdSmartInfo8_Type()
)
jBODHdSmartInfo8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jBODHdSmartInfo8.setStatus("current")
_SystemInfoEx_ObjectIdentity = ObjectIdentity
systemInfoEx = _SystemInfoEx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3)
)
_SystemCPU_UsageEX_Type = Integer32
_SystemCPU_UsageEX_Object = MibScalar
systemCPU_UsageEX = _SystemCPU_UsageEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 1),
    _SystemCPU_UsageEX_Type()
)
systemCPU_UsageEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPU_UsageEX.setStatus("current")
_SystemTotalMemEX_Type = Counter64
_SystemTotalMemEX_Object = MibScalar
systemTotalMemEX = _SystemTotalMemEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 2),
    _SystemTotalMemEX_Type()
)
systemTotalMemEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTotalMemEX.setStatus("current")
_SystemFreeMemEX_Type = Counter64
_SystemFreeMemEX_Object = MibScalar
systemFreeMemEX = _SystemFreeMemEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 3),
    _SystemFreeMemEX_Type()
)
systemFreeMemEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFreeMemEX.setStatus("current")
_SystemUptimeEX_Type = TimeTicks
_SystemUptimeEX_Object = MibScalar
systemUptimeEX = _SystemUptimeEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 4),
    _SystemUptimeEX_Type()
)
systemUptimeEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUptimeEX.setStatus("current")
_Cpu_TemperatureEX_Type = Integer32
_Cpu_TemperatureEX_Object = MibScalar
cpu_TemperatureEX = _Cpu_TemperatureEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 5),
    _Cpu_TemperatureEX_Type()
)
cpu_TemperatureEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu_TemperatureEX.setStatus("current")
_SystemTemperatureEX_Type = Integer32
_SystemTemperatureEX_Object = MibScalar
systemTemperatureEX = _SystemTemperatureEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 6),
    _SystemTemperatureEX_Type()
)
systemTemperatureEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperatureEX.setStatus("current")
_IfNumberEX_Type = Integer32
_IfNumberEX_Object = MibScalar
ifNumberEX = _IfNumberEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 8),
    _IfNumberEX_Type()
)
ifNumberEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumberEX.setStatus("current")
_SystemIfTableEx_Object = MibTable
systemIfTableEx = _SystemIfTableEx_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 9)
)
if mibBuilder.loadTexts:
    systemIfTableEx.setStatus("current")
_IfEntryEx_Object = MibTableRow
ifEntryEx = _IfEntryEx_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 9, 1)
)
ifEntryEx.setIndexNames(
    (0, "NAS-MIB", "ifIndexEX"),
)
if mibBuilder.loadTexts:
    ifEntryEx.setStatus("current")
_IfIndexEX_Type = Integer32
_IfIndexEX_Object = MibTableColumn
ifIndexEX = _IfIndexEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 9, 1, 1),
    _IfIndexEX_Type()
)
ifIndexEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndexEX.setStatus("current")


class _IfDescrEX_Type(DisplayString):
    """Custom type ifDescrEX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfDescrEX_Type.__name__ = "DisplayString"
_IfDescrEX_Object = MibTableColumn
ifDescrEX = _IfDescrEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 9, 1, 2),
    _IfDescrEX_Type()
)
ifDescrEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescrEX.setStatus("current")
_IfPacketsReceivedEX_Type = Counter32
_IfPacketsReceivedEX_Object = MibTableColumn
ifPacketsReceivedEX = _IfPacketsReceivedEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 9, 1, 3),
    _IfPacketsReceivedEX_Type()
)
ifPacketsReceivedEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPacketsReceivedEX.setStatus("current")
_IfPacketsSentEX_Type = Counter32
_IfPacketsSentEX_Object = MibTableColumn
ifPacketsSentEX = _IfPacketsSentEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 9, 1, 4),
    _IfPacketsSentEX_Type()
)
ifPacketsSentEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPacketsSentEX.setStatus("current")
_IfErrorPacketsEX_Type = Counter32
_IfErrorPacketsEX_Object = MibTableColumn
ifErrorPacketsEX = _IfErrorPacketsEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 9, 1, 5),
    _IfErrorPacketsEX_Type()
)
ifErrorPacketsEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifErrorPacketsEX.setStatus("current")
_HdNumberEX_Type = Integer32
_HdNumberEX_Object = MibScalar
hdNumberEX = _HdNumberEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 10),
    _HdNumberEX_Type()
)
hdNumberEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdNumberEX.setStatus("current")
_SystemHdTableEX_Object = MibTable
systemHdTableEX = _SystemHdTableEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11)
)
if mibBuilder.loadTexts:
    systemHdTableEX.setStatus("current")
_HdEntryEx_Object = MibTableRow
hdEntryEx = _HdEntryEx_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1)
)
hdEntryEx.setIndexNames(
    (0, "NAS-MIB", "hdIndex"),
)
if mibBuilder.loadTexts:
    hdEntryEx.setStatus("current")
_HdIndexEX_Type = Integer32
_HdIndexEX_Object = MibTableColumn
hdIndexEX = _HdIndexEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1, 1),
    _HdIndexEX_Type()
)
hdIndexEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdIndexEX.setStatus("current")


class _HdDescrEX_Type(DisplayString):
    """Custom type hdDescrEX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HdDescrEX_Type.__name__ = "DisplayString"
_HdDescrEX_Object = MibTableColumn
hdDescrEX = _HdDescrEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1, 2),
    _HdDescrEX_Type()
)
hdDescrEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdDescrEX.setStatus("current")
_HdTemperatureEX_Type = Integer32
_HdTemperatureEX_Object = MibTableColumn
hdTemperatureEX = _HdTemperatureEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1, 3),
    _HdTemperatureEX_Type()
)
hdTemperatureEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdTemperatureEX.setStatus("current")


class _HdStatusEX_Type(Integer32):
    """Custom type hdStatusEX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-9,
              -6,
              -5,
              -4,
              0)
        )
    )
    namedValues = NamedValues(
        *(("rwError", -9),
          ("invalid", -6),
          ("noDisk", -5),
          ("unknown", -4),
          ("ready", 0))
    )


_HdStatusEX_Type.__name__ = "Integer32"
_HdStatusEX_Object = MibTableColumn
hdStatusEX = _HdStatusEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1, 4),
    _HdStatusEX_Type()
)
hdStatusEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdStatusEX.setStatus("current")
_HdModelEX_Type = DisplayString
_HdModelEX_Object = MibTableColumn
hdModelEX = _HdModelEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1, 5),
    _HdModelEX_Type()
)
hdModelEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdModelEX.setStatus("current")
_HdCapacityEX_Type = Counter64
_HdCapacityEX_Object = MibTableColumn
hdCapacityEX = _HdCapacityEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1, 6),
    _HdCapacityEX_Type()
)
hdCapacityEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdCapacityEX.setStatus("current")
_HdSmartInfoEX_Type = DisplayString
_HdSmartInfoEX_Object = MibTableColumn
hdSmartInfoEX = _HdSmartInfoEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 11, 1, 7),
    _HdSmartInfoEX_Type()
)
hdSmartInfoEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdSmartInfoEX.setStatus("current")
_ModelNameEX_Type = DisplayString
_ModelNameEX_Object = MibScalar
modelNameEX = _ModelNameEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 12),
    _ModelNameEX_Type()
)
modelNameEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelNameEX.setStatus("current")
_HostNameEX_Type = DisplayString
_HostNameEX_Object = MibScalar
hostNameEX = _HostNameEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 13),
    _HostNameEX_Type()
)
hostNameEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostNameEX.setStatus("current")
_SysFanNumberEX_Type = Integer32
_SysFanNumberEX_Object = MibScalar
sysFanNumberEX = _SysFanNumberEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 14),
    _SysFanNumberEX_Type()
)
sysFanNumberEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanNumberEX.setStatus("current")
_SystemFanTableEx_Object = MibTable
systemFanTableEx = _SystemFanTableEx_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 15)
)
if mibBuilder.loadTexts:
    systemFanTableEx.setStatus("current")
_SysFanEntryEx_Object = MibTableRow
sysFanEntryEx = _SysFanEntryEx_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 15, 1)
)
sysFanEntryEx.setIndexNames(
    (0, "NAS-MIB", "sysFanIndexEX"),
)
if mibBuilder.loadTexts:
    sysFanEntryEx.setStatus("current")
_SysFanIndexEX_Type = Integer32
_SysFanIndexEX_Object = MibTableColumn
sysFanIndexEX = _SysFanIndexEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 15, 1, 1),
    _SysFanIndexEX_Type()
)
sysFanIndexEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanIndexEX.setStatus("current")


class _SysFanDescrEX_Type(DisplayString):
    """Custom type sysFanDescrEX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysFanDescrEX_Type.__name__ = "DisplayString"
_SysFanDescrEX_Object = MibTableColumn
sysFanDescrEX = _SysFanDescrEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 15, 1, 2),
    _SysFanDescrEX_Type()
)
sysFanDescrEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanDescrEX.setStatus("current")
_SysFanSpeedEX_Type = Integer32
_SysFanSpeedEX_Object = MibTableColumn
sysFanSpeedEX = _SysFanSpeedEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 15, 1, 3),
    _SysFanSpeedEX_Type()
)
sysFanSpeedEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanSpeedEX.setStatus("current")
_SysVolumeNumberEX_Type = Integer32
_SysVolumeNumberEX_Object = MibScalar
sysVolumeNumberEX = _SysVolumeNumberEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 16),
    _SysVolumeNumberEX_Type()
)
sysVolumeNumberEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeNumberEX.setStatus("current")
_SystemVolumeTableEx_Object = MibTable
systemVolumeTableEx = _SystemVolumeTableEx_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17)
)
if mibBuilder.loadTexts:
    systemVolumeTableEx.setStatus("current")
_SysVolumeEntryEx_Object = MibTableRow
sysVolumeEntryEx = _SysVolumeEntryEx_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17, 1)
)
sysVolumeEntryEx.setIndexNames(
    (0, "NAS-MIB", "sysVolumeIndexEX"),
)
if mibBuilder.loadTexts:
    sysVolumeEntryEx.setStatus("current")
_SysVolumeIndexEX_Type = Integer32
_SysVolumeIndexEX_Object = MibTableColumn
sysVolumeIndexEX = _SysVolumeIndexEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17, 1, 1),
    _SysVolumeIndexEX_Type()
)
sysVolumeIndexEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeIndexEX.setStatus("current")


class _SysVolumeDescrEX_Type(DisplayString):
    """Custom type sysVolumeDescrEX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysVolumeDescrEX_Type.__name__ = "DisplayString"
_SysVolumeDescrEX_Object = MibTableColumn
sysVolumeDescrEX = _SysVolumeDescrEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17, 1, 2),
    _SysVolumeDescrEX_Type()
)
sysVolumeDescrEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeDescrEX.setStatus("current")


class _SysVolumeFSEX_Type(DisplayString):
    """Custom type sysVolumeFSEX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysVolumeFSEX_Type.__name__ = "DisplayString"
_SysVolumeFSEX_Object = MibTableColumn
sysVolumeFSEX = _SysVolumeFSEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17, 1, 3),
    _SysVolumeFSEX_Type()
)
sysVolumeFSEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeFSEX.setStatus("current")
_SysVolumeTotalSizeEX_Type = Counter64
_SysVolumeTotalSizeEX_Object = MibTableColumn
sysVolumeTotalSizeEX = _SysVolumeTotalSizeEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17, 1, 4),
    _SysVolumeTotalSizeEX_Type()
)
sysVolumeTotalSizeEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeTotalSizeEX.setStatus("current")
_SysVolumeFreeSizeEX_Type = Counter64
_SysVolumeFreeSizeEX_Object = MibTableColumn
sysVolumeFreeSizeEX = _SysVolumeFreeSizeEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17, 1, 5),
    _SysVolumeFreeSizeEX_Type()
)
sysVolumeFreeSizeEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeFreeSizeEX.setStatus("current")


class _SysVolumeStatusEX_Type(DisplayString):
    """Custom type sysVolumeStatusEX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysVolumeStatusEX_Type.__name__ = "DisplayString"
_SysVolumeStatusEX_Object = MibTableColumn
sysVolumeStatusEX = _SysVolumeStatusEX_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 3, 17, 1, 6),
    _SysVolumeStatusEX_Type()
)
sysVolumeStatusEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVolumeStatusEX.setStatus("current")
_StorageSystemEx_ObjectIdentity = ObjectIdentity
storageSystemEx = _StorageSystemEx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4)
)
_SystemSettings_ObjectIdentity = ObjectIdentity
systemSettings = _SystemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1)
)
_StorageManager_ObjectIdentity = ObjectIdentity
storageManager = _StorageManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1)
)
_NasStorage_ObjectIdentity = ObjectIdentity
nasStorage = _NasStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1)
)
_Components_ObjectIdentity = ObjectIdentity
components = _Components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1)
)
_Enclosure_ObjectIdentity = ObjectIdentity
enclosure = _Enclosure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1)
)
_EnclosurelNumber_Type = Integer32
_EnclosurelNumber_Object = MibScalar
enclosurelNumber = _EnclosurelNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 1),
    _EnclosurelNumber_Type()
)
enclosurelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosurelNumber.setStatus("current")
_EnclosureTable_Object = MibTable
enclosureTable = _EnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    enclosureTable.setStatus("current")
_EnclosureTableEntry_Object = MibTableRow
enclosureTableEntry = _EnclosureTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1)
)
enclosureTableEntry.setIndexNames(
    (0, "NAS-MIB", "enclosureIndex"),
)
if mibBuilder.loadTexts:
    enclosureTableEntry.setStatus("current")
_EnclosureIndex_Type = Integer32
_EnclosureIndex_Object = MibTableColumn
enclosureIndex = _EnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1, 1),
    _EnclosureIndex_Type()
)
enclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureIndex.setStatus("current")
_EnclosureID_Type = Integer32
_EnclosureID_Object = MibTableColumn
enclosureID = _EnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1, 2),
    _EnclosureID_Type()
)
enclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureID.setStatus("current")


class _EnclosureModel_Type(DisplayString):
    """Custom type enclosureModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EnclosureModel_Type.__name__ = "DisplayString"
_EnclosureModel_Object = MibTableColumn
enclosureModel = _EnclosureModel_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1, 3),
    _EnclosureModel_Type()
)
enclosureModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureModel.setStatus("current")


class _EnclosureSerialNum_Type(DisplayString):
    """Custom type enclosureSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EnclosureSerialNum_Type.__name__ = "DisplayString"
_EnclosureSerialNum_Object = MibTableColumn
enclosureSerialNum = _EnclosureSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1, 4),
    _EnclosureSerialNum_Type()
)
enclosureSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSerialNum.setStatus("current")
_EnclosureSlot_Type = Integer32
_EnclosureSlot_Object = MibTableColumn
enclosureSlot = _EnclosureSlot_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1, 5),
    _EnclosureSlot_Type()
)
enclosureSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSlot.setStatus("current")
_EnclosureName_Type = DisplayString
_EnclosureName_Object = MibTableColumn
enclosureName = _EnclosureName_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1, 6),
    _EnclosureName_Type()
)
enclosureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureName.setStatus("current")
_EnclosureSystemTemp_Type = Integer32
_EnclosureSystemTemp_Object = MibTableColumn
enclosureSystemTemp = _EnclosureSystemTemp_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 1, 2, 1, 7),
    _EnclosureSystemTemp_Type()
)
enclosureSystemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSystemTemp.setStatus("current")
_SystemFan_ObjectIdentity = ObjectIdentity
systemFan = _SystemFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2)
)
_SystemFanNumber_Type = Integer32
_SystemFanNumber_Object = MibScalar
systemFanNumber = _SystemFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 1),
    _SystemFanNumber_Type()
)
systemFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanNumber.setStatus("current")
_SystemFan2Table_Object = MibTable
systemFan2Table = _SystemFan2Table_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    systemFan2Table.setStatus("current")
_SystemFan2TableEntry_Object = MibTableRow
systemFan2TableEntry = _SystemFan2TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 2, 1)
)
systemFan2TableEntry.setIndexNames(
    (0, "NAS-MIB", "systemFanIndex"),
)
if mibBuilder.loadTexts:
    systemFan2TableEntry.setStatus("current")
_SystemFanIndex_Type = Integer32
_SystemFanIndex_Object = MibTableColumn
systemFanIndex = _SystemFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 2, 1, 1),
    _SystemFanIndex_Type()
)
systemFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanIndex.setStatus("current")
_SystemFanID_Type = Integer32
_SystemFanID_Object = MibTableColumn
systemFanID = _SystemFanID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 2, 1, 2),
    _SystemFanID_Type()
)
systemFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanID.setStatus("current")
_SystemFanEnclosureID_Type = Integer32
_SystemFanEnclosureID_Object = MibTableColumn
systemFanEnclosureID = _SystemFanEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 2, 1, 3),
    _SystemFanEnclosureID_Type()
)
systemFanEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanEnclosureID.setStatus("current")


class _SystemFanStatus_Type(Integer32):
    """Custom type systemFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("fail", -1),
          ("ok", 0))
    )


_SystemFanStatus_Type.__name__ = "Integer32"
_SystemFanStatus_Object = MibTableColumn
systemFanStatus = _SystemFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 2, 1, 4),
    _SystemFanStatus_Type()
)
systemFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanStatus.setStatus("current")
_SystemFanSpeed_Type = Integer32
_SystemFanSpeed_Object = MibTableColumn
systemFanSpeed = _SystemFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 2, 2, 1, 5),
    _SystemFanSpeed_Type()
)
systemFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanSpeed.setStatus("current")
_SystemPower_ObjectIdentity = ObjectIdentity
systemPower = _SystemPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3)
)
_SystemPowerNumber_Type = Integer32
_SystemPowerNumber_Object = MibScalar
systemPowerNumber = _SystemPowerNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 1),
    _SystemPowerNumber_Type()
)
systemPowerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerNumber.setStatus("current")
_SystemPowerTable_Object = MibTable
systemPowerTable = _SystemPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    systemPowerTable.setStatus("current")
_SystemPowerTableEntry_Object = MibTableRow
systemPowerTableEntry = _SystemPowerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2, 1)
)
systemPowerTableEntry.setIndexNames(
    (0, "NAS-MIB", "systemPowerIndex"),
)
if mibBuilder.loadTexts:
    systemPowerTableEntry.setStatus("current")
_SystemPowerIndex_Type = Integer32
_SystemPowerIndex_Object = MibTableColumn
systemPowerIndex = _SystemPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2, 1, 1),
    _SystemPowerIndex_Type()
)
systemPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerIndex.setStatus("current")
_SystemPowerID_Type = Integer32
_SystemPowerID_Object = MibTableColumn
systemPowerID = _SystemPowerID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2, 1, 2),
    _SystemPowerID_Type()
)
systemPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerID.setStatus("current")
_SystemPowerEnclosureID_Type = Integer32
_SystemPowerEnclosureID_Object = MibTableColumn
systemPowerEnclosureID = _SystemPowerEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2, 1, 3),
    _SystemPowerEnclosureID_Type()
)
systemPowerEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerEnclosureID.setStatus("current")


class _SystemPowerStatus_Type(Integer32):
    """Custom type systemPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("fail", -1),
          ("ok", 0))
    )


_SystemPowerStatus_Type.__name__ = "Integer32"
_SystemPowerStatus_Object = MibTableColumn
systemPowerStatus = _SystemPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2, 1, 4),
    _SystemPowerStatus_Type()
)
systemPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerStatus.setStatus("current")
_SystemPowerFanSpeed_Type = Integer32
_SystemPowerFanSpeed_Object = MibTableColumn
systemPowerFanSpeed = _SystemPowerFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2, 1, 5),
    _SystemPowerFanSpeed_Type()
)
systemPowerFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerFanSpeed.setStatus("current")
_SystemPowerTemp_Type = Integer32
_SystemPowerTemp_Object = MibTableColumn
systemPowerTemp = _SystemPowerTemp_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 3, 2, 1, 6),
    _SystemPowerTemp_Type()
)
systemPowerTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPowerTemp.setStatus("current")
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4)
)
_CpuNumber_Type = Integer32
_CpuNumber_Object = MibScalar
cpuNumber = _CpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4, 1),
    _CpuNumber_Type()
)
cpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuNumber.setStatus("current")
_CpuTemp_Type = Integer32
_CpuTemp_Object = MibTableColumn
cpuTemp = _CpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4, 2),
    _CpuTemp_Type()
)
cpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemp.setStatus("current")
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("current")
_CpuTableEntry_Object = MibTableRow
cpuTableEntry = _CpuTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4, 3, 1)
)
cpuTableEntry.setIndexNames(
    (0, "NAS-MIB", "cpuIndex"),
)
if mibBuilder.loadTexts:
    cpuTableEntry.setStatus("current")
_CpuIndex_Type = Integer32
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4, 3, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")
_CpuID_Type = Integer32
_CpuID_Object = MibTableColumn
cpuID = _CpuID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4, 3, 1, 2),
    _CpuID_Type()
)
cpuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuID.setStatus("current")
_CpuUsage_Type = Integer32
_CpuUsage_Object = MibTableColumn
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 4, 3, 1, 3),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_Disk_ObjectIdentity = ObjectIdentity
disk = _Disk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5)
)
_DiskNumber_Type = Integer32
_DiskNumber_Object = MibScalar
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 1),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskTableEntry_Object = MibTableRow
diskTableEntry = _DiskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1)
)
diskTableEntry.setIndexNames(
    (0, "NAS-MIB", "diskIndex"),
)
if mibBuilder.loadTexts:
    diskTableEntry.setStatus("current")
_DiskIndex_Type = Integer32
_DiskIndex_Object = MibTableColumn
diskIndex = _DiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 1),
    _DiskIndex_Type()
)
diskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskIndex.setStatus("current")
_DiskID_Type = Integer32
_DiskID_Object = MibTableColumn
diskID = _DiskID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 2),
    _DiskID_Type()
)
diskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskID.setStatus("current")
_DiskEnclosureID_Type = Integer32
_DiskEnclosureID_Object = MibTableColumn
diskEnclosureID = _DiskEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 3),
    _DiskEnclosureID_Type()
)
diskEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskEnclosureID.setStatus("current")


class _DiskSummary_Type(DisplayString):
    """Custom type diskSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskSummary_Type.__name__ = "DisplayString"
_DiskSummary_Object = MibTableColumn
diskSummary = _DiskSummary_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 4),
    _DiskSummary_Type()
)
diskSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSummary.setStatus("current")


class _DiskSmartInfo_Type(Integer32):
    """Custom type diskSmartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", -1),
          ("good", 0),
          ("warning", 1),
          ("abnormal", 2))
    )


_DiskSmartInfo_Type.__name__ = "Integer32"
_DiskSmartInfo_Object = MibTableColumn
diskSmartInfo = _DiskSmartInfo_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 5),
    _DiskSmartInfo_Type()
)
diskSmartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSmartInfo.setStatus("current")
_DiskTemperture_Type = Integer32
_DiskTemperture_Object = MibTableColumn
diskTemperture = _DiskTemperture_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 6),
    _DiskTemperture_Type()
)
diskTemperture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskTemperture.setStatus("current")


class _DiskGlobalSpare_Type(Integer32):
    """Custom type diskGlobalSpare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_DiskGlobalSpare_Type.__name__ = "Integer32"
_DiskGlobalSpare_Object = MibTableColumn
diskGlobalSpare = _DiskGlobalSpare_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 7),
    _DiskGlobalSpare_Type()
)
diskGlobalSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskGlobalSpare.setStatus("current")


class _DiskModel_Type(DisplayString):
    """Custom type diskModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiskModel_Type.__name__ = "DisplayString"
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 8),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")
_DiskCapacity_Type = Counter64
_DiskCapacity_Object = MibTableColumn
diskCapacity = _DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 5, 2, 1, 9),
    _DiskCapacity_Type()
)
diskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskCapacity.setStatus("current")
_MsataDisk_ObjectIdentity = ObjectIdentity
msataDisk = _MsataDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6)
)
_MsataDiskNumber_Type = Integer32
_MsataDiskNumber_Object = MibScalar
msataDiskNumber = _MsataDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 1),
    _MsataDiskNumber_Type()
)
msataDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskNumber.setStatus("current")
_MsataDiskTable_Object = MibTable
msataDiskTable = _MsataDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    msataDiskTable.setStatus("current")
_MsataDiskTableEntry_Object = MibTableRow
msataDiskTableEntry = _MsataDiskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1)
)
msataDiskTableEntry.setIndexNames(
    (0, "NAS-MIB", "msataDiskIndex"),
)
if mibBuilder.loadTexts:
    msataDiskTableEntry.setStatus("current")
_MsataDiskIndex_Type = Integer32
_MsataDiskIndex_Object = MibTableColumn
msataDiskIndex = _MsataDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 1),
    _MsataDiskIndex_Type()
)
msataDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskIndex.setStatus("current")
_MsataDiskID_Type = Integer32
_MsataDiskID_Object = MibTableColumn
msataDiskID = _MsataDiskID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 2),
    _MsataDiskID_Type()
)
msataDiskID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskID.setStatus("current")
_MsataDiskEnclosureID_Type = Integer32
_MsataDiskEnclosureID_Object = MibTableColumn
msataDiskEnclosureID = _MsataDiskEnclosureID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 3),
    _MsataDiskEnclosureID_Type()
)
msataDiskEnclosureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskEnclosureID.setStatus("current")


class _MsataDiskSummary_Type(DisplayString):
    """Custom type msataDiskSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsataDiskSummary_Type.__name__ = "DisplayString"
_MsataDiskSummary_Object = MibTableColumn
msataDiskSummary = _MsataDiskSummary_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 4),
    _MsataDiskSummary_Type()
)
msataDiskSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskSummary.setStatus("current")


class _MsataDiskSmartInfo_Type(Integer32):
    """Custom type msataDiskSmartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", -1),
          ("good", 0),
          ("warning", 1),
          ("abnormal", 2))
    )


_MsataDiskSmartInfo_Type.__name__ = "Integer32"
_MsataDiskSmartInfo_Object = MibTableColumn
msataDiskSmartInfo = _MsataDiskSmartInfo_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 5),
    _MsataDiskSmartInfo_Type()
)
msataDiskSmartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskSmartInfo.setStatus("current")
_MsataDiskTemperture_Type = Integer32
_MsataDiskTemperture_Object = MibTableColumn
msataDiskTemperture = _MsataDiskTemperture_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 6),
    _MsataDiskTemperture_Type()
)
msataDiskTemperture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskTemperture.setStatus("current")


class _MsataDiskGlobalSpare_Type(Integer32):
    """Custom type msataDiskGlobalSpare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsataDiskGlobalSpare_Type.__name__ = "Integer32"
_MsataDiskGlobalSpare_Object = MibTableColumn
msataDiskGlobalSpare = _MsataDiskGlobalSpare_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 7),
    _MsataDiskGlobalSpare_Type()
)
msataDiskGlobalSpare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskGlobalSpare.setStatus("current")


class _MsataDiskModel_Type(DisplayString):
    """Custom type msataDiskModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsataDiskModel_Type.__name__ = "DisplayString"
_MsataDiskModel_Object = MibTableColumn
msataDiskModel = _MsataDiskModel_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 8),
    _MsataDiskModel_Type()
)
msataDiskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskModel.setStatus("current")
_MsataDiskCapacity_Type = Counter64
_MsataDiskCapacity_Object = MibTableColumn
msataDiskCapacity = _MsataDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 1, 6, 2, 1, 9),
    _MsataDiskCapacity_Type()
)
msataDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msataDiskCapacity.setStatus("current")
_StorageSpace_ObjectIdentity = ObjectIdentity
storageSpace = _StorageSpace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2)
)
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1)
)
_RaidNumber_Type = Integer32
_RaidNumber_Object = MibScalar
raidNumber = _RaidNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 1),
    _RaidNumber_Type()
)
raidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidNumber.setStatus("current")
_RaidGroupTable_Object = MibTable
raidGroupTable = _RaidGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    raidGroupTable.setStatus("current")
_RaidGroupTableEntry_Object = MibTableRow
raidGroupTableEntry = _RaidGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1)
)
raidGroupTableEntry.setIndexNames(
    (0, "NAS-MIB", "raidIndex"),
)
if mibBuilder.loadTexts:
    raidGroupTableEntry.setStatus("current")
_RaidIndex_Type = Integer32
_RaidIndex_Object = MibTableColumn
raidIndex = _RaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1, 1),
    _RaidIndex_Type()
)
raidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidIndex.setStatus("current")
_RaidID_Type = Integer32
_RaidID_Object = MibTableColumn
raidID = _RaidID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1, 2),
    _RaidID_Type()
)
raidID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidID.setStatus("current")
_RaidCapacity_Type = Counter64
_RaidCapacity_Object = MibTableColumn
raidCapacity = _RaidCapacity_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1, 3),
    _RaidCapacity_Type()
)
raidCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidCapacity.setStatus("current")
_RaidFreeSize_Type = Counter64
_RaidFreeSize_Object = MibTableColumn
raidFreeSize = _RaidFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1, 4),
    _RaidFreeSize_Type()
)
raidFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidFreeSize.setStatus("current")


class _RaidStatus_Type(DisplayString):
    """Custom type raidStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RaidStatus_Type.__name__ = "DisplayString"
_RaidStatus_Object = MibTableColumn
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1, 5),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatus.setStatus("current")


class _RaidBitmap_Type(Integer32):
    """Custom type raidBitmap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RaidBitmap_Type.__name__ = "Integer32"
_RaidBitmap_Object = MibTableColumn
raidBitmap = _RaidBitmap_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1, 6),
    _RaidBitmap_Type()
)
raidBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidBitmap.setStatus("current")


class _RaidLevel_Type(DisplayString):
    """Custom type raidLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RaidLevel_Type.__name__ = "DisplayString"
_RaidLevel_Object = MibTableColumn
raidLevel = _RaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 1, 2, 1, 7),
    _RaidLevel_Type()
)
raidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidLevel.setStatus("current")
_Pool_ObjectIdentity = ObjectIdentity
pool = _Pool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2)
)
_PoolNumber_Type = Integer32
_PoolNumber_Object = MibScalar
poolNumber = _PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 1),
    _PoolNumber_Type()
)
poolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumber.setStatus("current")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("current")
_PoolTableEntry_Object = MibTableRow
poolTableEntry = _PoolTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 2, 1)
)
poolTableEntry.setIndexNames(
    (0, "NAS-MIB", "poolIndex"),
)
if mibBuilder.loadTexts:
    poolTableEntry.setStatus("current")
_PoolIndex_Type = Integer32
_PoolIndex_Object = MibTableColumn
poolIndex = _PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 2, 1, 1),
    _PoolIndex_Type()
)
poolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolIndex.setStatus("current")
_PoolID_Type = Integer32
_PoolID_Object = MibTableColumn
poolID = _PoolID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 2, 1, 2),
    _PoolID_Type()
)
poolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolID.setStatus("current")
_PoolCapacity_Type = Counter64
_PoolCapacity_Object = MibTableColumn
poolCapacity = _PoolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 2, 1, 3),
    _PoolCapacity_Type()
)
poolCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCapacity.setStatus("current")
_PoolFreeSize_Type = Counter64
_PoolFreeSize_Object = MibTableColumn
poolFreeSize = _PoolFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 2, 1, 4),
    _PoolFreeSize_Type()
)
poolFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolFreeSize.setStatus("current")


class _PoolStatus_Type(Integer32):
    """Custom type poolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-3,
              -2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("error", -3),
          ("notReady", -2),
          ("warning", -1),
          ("ready", 0))
    )


_PoolStatus_Type.__name__ = "Integer32"
_PoolStatus_Object = MibTableColumn
poolStatus = _PoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 2, 2, 1, 5),
    _PoolStatus_Type()
)
poolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolStatus.setStatus("current")
_Volume_ObjectIdentity = ObjectIdentity
volume = _Volume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3)
)
_VolumeNumber_Type = Integer32
_VolumeNumber_Object = MibScalar
volumeNumber = _VolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 1),
    _VolumeNumber_Type()
)
volumeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeNumber.setStatus("current")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("current")
_VolumeTableEntry_Object = MibTableRow
volumeTableEntry = _VolumeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1)
)
volumeTableEntry.setIndexNames(
    (0, "NAS-MIB", "volumeIndex"),
)
if mibBuilder.loadTexts:
    volumeTableEntry.setStatus("current")
_VolumeIndex_Type = Integer32
_VolumeIndex_Object = MibTableColumn
volumeIndex = _VolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 1),
    _VolumeIndex_Type()
)
volumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeIndex.setStatus("current")
_VolumeID_Type = Integer32
_VolumeID_Object = MibTableColumn
volumeID = _VolumeID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 2),
    _VolumeID_Type()
)
volumeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeID.setStatus("current")
_VolumeCapacity_Type = Counter64
_VolumeCapacity_Object = MibTableColumn
volumeCapacity = _VolumeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 3),
    _VolumeCapacity_Type()
)
volumeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeCapacity.setStatus("current")
_VolumeFreeSize_Type = Counter64
_VolumeFreeSize_Object = MibTableColumn
volumeFreeSize = _VolumeFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 4),
    _VolumeFreeSize_Type()
)
volumeFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFreeSize.setStatus("current")


class _VolumeStatus_Type(DisplayString):
    """Custom type volumeStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VolumeStatus_Type.__name__ = "DisplayString"
_VolumeStatus_Object = MibTableColumn
volumeStatus = _VolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 5),
    _VolumeStatus_Type()
)
volumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeStatus.setStatus("current")


class _VolumeSSDCache_Type(Integer32):
    """Custom type volumeSSDCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VolumeSSDCache_Type.__name__ = "Integer32"
_VolumeSSDCache_Object = MibTableColumn
volumeSSDCache = _VolumeSSDCache_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 6),
    _VolumeSSDCache_Type()
)
volumeSSDCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSSDCache.setStatus("current")


class _VolumeThin_Type(Integer32):
    """Custom type volumeThin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VolumeThin_Type.__name__ = "Integer32"
_VolumeThin_Object = MibTableColumn
volumeThin = _VolumeThin_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 7),
    _VolumeThin_Type()
)
volumeThin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeThin.setStatus("current")


class _VolumeName_Type(DisplayString):
    """Custom type volumeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VolumeName_Type.__name__ = "DisplayString"
_VolumeName_Object = MibTableColumn
volumeName = _VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 2, 3, 2, 1, 8),
    _VolumeName_Type()
)
volumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeName.setStatus("current")
_CacheAcceleration_ObjectIdentity = ObjectIdentity
cacheAcceleration = _CacheAcceleration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 3)
)


class _Service_Type(Integer32):
    """Custom type service based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Service_Type.__name__ = "Integer32"
_Service_Object = MibScalar
service = _Service_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 3, 1),
    _Service_Type()
)
service.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    service.setStatus("current")
_AvailablePercent_Type = Integer32
_AvailablePercent_Object = MibScalar
availablePercent = _AvailablePercent_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 3, 2),
    _AvailablePercent_Type()
)
availablePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availablePercent.setStatus("current")
_ReadHitRate_Type = Integer32
_ReadHitRate_Object = MibScalar
readHitRate = _ReadHitRate_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 3, 3),
    _ReadHitRate_Type()
)
readHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readHitRate.setStatus("current")
_WriteHitRate_Type = Integer32
_WriteHitRate_Object = MibScalar
writeHitRate = _WriteHitRate_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 3, 4),
    _WriteHitRate_Type()
)
writeHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeHitRate.setStatus("current")


class _Status_Type(DisplayString):
    """Custom type status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Status_Type.__name__ = "DisplayString"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 1, 3, 5),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")
_ISCSI_ObjectIdentity = ObjectIdentity
iSCSI = _ISCSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2)
)
_ISCSIStorage_ObjectIdentity = ObjectIdentity
iSCSIStorage = _ISCSIStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1)
)


class _ISCSIService_Type(Integer32):
    """Custom type iSCSIService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ISCSIService_Type.__name__ = "Integer32"
_ISCSIService_Object = MibScalar
iSCSIService = _ISCSIService_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 1),
    _ISCSIService_Type()
)
iSCSIService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSIService.setStatus("current")
_ISCSIServicePort_Type = Integer32
_ISCSIServicePort_Object = MibScalar
iSCSIServicePort = _ISCSIServicePort_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 2),
    _ISCSIServicePort_Type()
)
iSCSIServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSCSIServicePort.setStatus("current")


class _ISNSService_Type(Integer32):
    """Custom type iSNSService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ISNSService_Type.__name__ = "Integer32"
_ISNSService_Object = MibScalar
iSNSService = _ISNSService_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 3),
    _ISNSService_Type()
)
iSNSService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSNSService.setStatus("current")
_ISNSIP_Type = IpAddress
_ISNSIP_Object = MibScalar
iSNSIP = _ISNSIP_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 4),
    _ISNSIP_Type()
)
iSNSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iSNSIP.setStatus("current")
_Lun_ObjectIdentity = ObjectIdentity
lun = _Lun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10)
)
_LunNumber_Type = Integer32
_LunNumber_Object = MibScalar
lunNumber = _LunNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 1),
    _LunNumber_Type()
)
lunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunNumber.setStatus("current")
_LunTable_Object = MibTable
lunTable = _LunTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    lunTable.setStatus("current")
_LunTableEntry_Object = MibTableRow
lunTableEntry = _LunTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1)
)
lunTableEntry.setIndexNames(
    (0, "NAS-MIB", "lunIndex"),
)
if mibBuilder.loadTexts:
    lunTableEntry.setStatus("current")
_LunIndex_Type = Integer32
_LunIndex_Object = MibTableColumn
lunIndex = _LunIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 1),
    _LunIndex_Type()
)
lunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunIndex.setStatus("current")
_LunID_Type = Integer32
_LunID_Object = MibTableColumn
lunID = _LunID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 2),
    _LunID_Type()
)
lunID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunID.setStatus("current")
_LunCapacity_Type = Counter64
_LunCapacity_Object = MibTableColumn
lunCapacity = _LunCapacity_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 3),
    _LunCapacity_Type()
)
lunCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunCapacity.setStatus("current")
_LunUsedPercent_Type = Integer32
_LunUsedPercent_Object = MibTableColumn
lunUsedPercent = _LunUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 4),
    _LunUsedPercent_Type()
)
lunUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunUsedPercent.setStatus("current")


class _LunStatus_Type(DisplayString):
    """Custom type lunStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LunStatus_Type.__name__ = "DisplayString"
_LunStatus_Object = MibTableColumn
lunStatus = _LunStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 5),
    _LunStatus_Type()
)
lunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunStatus.setStatus("current")


class _LunName_Type(DisplayString):
    """Custom type lunName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LunName_Type.__name__ = "DisplayString"
_LunName_Object = MibTableColumn
lunName = _LunName_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 6),
    _LunName_Type()
)
lunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunName.setStatus("current")


class _LunBackupStatus_Type(Integer32):
    """Custom type lunBackupStatus based on Integer32"""
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
        *(("none", 0),
          ("backup", 1),
          ("restore", 2),
          ("snapshot", 3))
    )


_LunBackupStatus_Type.__name__ = "Integer32"
_LunBackupStatus_Object = MibTableColumn
lunBackupStatus = _LunBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 7),
    _LunBackupStatus_Type()
)
lunBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunBackupStatus.setStatus("current")


class _LunIsMap_Type(Integer32):
    """Custom type lunIsMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unmapped", 0),
          ("mapped", 1))
    )


_LunIsMap_Type.__name__ = "Integer32"
_LunIsMap_Object = MibTableColumn
lunIsMap = _LunIsMap_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 10, 2, 1, 8),
    _LunIsMap_Type()
)
lunIsMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunIsMap.setStatus("current")
_Target_ObjectIdentity = ObjectIdentity
target = _Target_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11)
)
_TargetNumber_Type = Integer32
_TargetNumber_Object = MibScalar
targetNumber = _TargetNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 1),
    _TargetNumber_Type()
)
targetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetNumber.setStatus("current")
_TargeTable_Object = MibTable
targeTable = _TargeTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    targeTable.setStatus("current")
_TargeTableEntry_Object = MibTableRow
targeTableEntry = _TargeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 2, 1)
)
targeTableEntry.setIndexNames(
    (0, "NAS-MIB", "targetIndex"),
)
if mibBuilder.loadTexts:
    targeTableEntry.setStatus("current")
_TargetIndex_Type = Integer32
_TargetIndex_Object = MibTableColumn
targetIndex = _TargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 2, 1, 1),
    _TargetIndex_Type()
)
targetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetIndex.setStatus("current")
_TargetID_Type = Integer32
_TargetID_Object = MibTableColumn
targetID = _TargetID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 2, 1, 2),
    _TargetID_Type()
)
targetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetID.setStatus("current")


class _TargetName_Type(DisplayString):
    """Custom type targetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TargetName_Type.__name__ = "DisplayString"
_TargetName_Object = MibTableColumn
targetName = _TargetName_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 2, 1, 3),
    _TargetName_Type()
)
targetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetName.setStatus("current")


class _TargetIQN_Type(DisplayString):
    """Custom type targetIQN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TargetIQN_Type.__name__ = "DisplayString"
_TargetIQN_Object = MibTableColumn
targetIQN = _TargetIQN_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 2, 1, 4),
    _TargetIQN_Type()
)
targetIQN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetIQN.setStatus("current")


class _TargetStatus_Type(Integer32):
    """Custom type targetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", -1),
          ("ready", 0),
          ("connected", 1))
    )


_TargetStatus_Type.__name__ = "Integer32"
_TargetStatus_Object = MibTableColumn
targetStatus = _TargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 1, 2, 1, 11, 2, 1, 5),
    _TargetStatus_Type()
)
targetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetStatus.setStatus("current")
_SystemStatus_ObjectIdentity = ObjectIdentity
systemStatus = _SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11)
)
_ResourceMonitor_ObjectIdentity = ObjectIdentity
resourceMonitor = _ResourceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5)
)
_DiskPerformance_ObjectIdentity = ObjectIdentity
diskPerformance = _DiskPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6)
)
_DiskPerformanceNumber_Type = Integer32
_DiskPerformanceNumber_Object = MibScalar
diskPerformanceNumber = _DiskPerformanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6, 1),
    _DiskPerformanceNumber_Type()
)
diskPerformanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerformanceNumber.setStatus("current")
_DiskPerformanceTable_Object = MibTable
diskPerformanceTable = _DiskPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6, 2)
)
if mibBuilder.loadTexts:
    diskPerformanceTable.setStatus("current")
_DiskPerformanceTableEntry_Object = MibTableRow
diskPerformanceTableEntry = _DiskPerformanceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6, 2, 1)
)
diskPerformanceTableEntry.setIndexNames(
    (0, "NAS-MIB", "diskPerformanceIndex"),
)
if mibBuilder.loadTexts:
    diskPerformanceTableEntry.setStatus("current")
_DiskPerformanceIndex_Type = Integer32
_DiskPerformanceIndex_Object = MibTableColumn
diskPerformanceIndex = _DiskPerformanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6, 2, 1, 1),
    _DiskPerformanceIndex_Type()
)
diskPerformanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerformanceIndex.setStatus("current")
_BlvID_Type = Integer32
_BlvID_Object = MibTableColumn
blvID = _BlvID_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6, 2, 1, 2),
    _BlvID_Type()
)
blvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blvID.setStatus("current")
_Iops_Type = Integer32
_Iops_Object = MibTableColumn
iops = _Iops_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6, 2, 1, 3),
    _Iops_Type()
)
iops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iops.setStatus("current")
_Latency_Type = Integer32
_Latency_Object = MibTableColumn
latency = _Latency_Object(
    (1, 3, 6, 1, 4, 1, 24681, 1, 4, 1, 11, 5, 6, 2, 1, 4),
    _Latency_Type()
)
latency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency.setStatus("current")
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24681, 1, 10)
)

# Managed Objects groups


# Notification objects

eventInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 24681, 1, 10, 1)
)
eventInform.setObjects(
    ("NAS-MIB", "eventInformMsg")
)
if mibBuilder.loadTexts:
    eventInform.setStatus(
        "current"
    )

eventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 24681, 1, 10, 2)
)
eventWarning.setObjects(
    ("NAS-MIB", "eventWarningMsg")
)
if mibBuilder.loadTexts:
    eventWarning.setStatus(
        "current"
    )

eventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 24681, 1, 10, 4)
)
eventError.setObjects(
    ("NAS-MIB", "eventErrorMsg")
)
if mibBuilder.loadTexts:
    eventError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NAS-MIB",
    **{"DisplayString": DisplayString,
       "storage": storage,
       "storageSystem": storageSystem,
       "systemEventMsg": systemEventMsg,
       "eventInformMsg": eventInformMsg,
       "eventWarningMsg": eventWarningMsg,
       "eventErrorMsg": eventErrorMsg,
       "systemInfo": systemInfo,
       "systemCPU-Usage": systemCPU_Usage,
       "systemTotalMem": systemTotalMem,
       "systemFreeMem": systemFreeMem,
       "systemUptime": systemUptime,
       "cpu-Temperature": cpu_Temperature,
       "systemTemperature": systemTemperature,
       "ifNumber": ifNumber,
       "systemIfTable": systemIfTable,
       "ifEntry": ifEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "ifPacketsReceived": ifPacketsReceived,
       "ifPacketsSent": ifPacketsSent,
       "ifErrorPackets": ifErrorPackets,
       "hdNumber": hdNumber,
       "systemHdTable": systemHdTable,
       "hdEntry": hdEntry,
       "hdIndex": hdIndex,
       "hdDescr": hdDescr,
       "hdTemperature": hdTemperature,
       "hdStatus": hdStatus,
       "hdModel": hdModel,
       "hdCapacity": hdCapacity,
       "hdSmartInfo": hdSmartInfo,
       "modelName": modelName,
       "hostName": hostName,
       "sysFanNumber": sysFanNumber,
       "systemFanTable": systemFanTable,
       "sysFanEntry": sysFanEntry,
       "sysFanIndex": sysFanIndex,
       "sysFanDescr": sysFanDescr,
       "sysFanSpeed": sysFanSpeed,
       "sysVolumeNumber": sysVolumeNumber,
       "systemVolumeTable": systemVolumeTable,
       "sysVolumeEntry": sysVolumeEntry,
       "sysVolumeIndex": sysVolumeIndex,
       "sysVolumeDescr": sysVolumeDescr,
       "sysVolumeFS": sysVolumeFS,
       "sysVolumeTotalSize": sysVolumeTotalSize,
       "sysVolumeFreeSize": sysVolumeFreeSize,
       "sysVolumeStatus": sysVolumeStatus,
       "jBODInfo": jBODInfo,
       "jBODBitmap": jBODBitmap,
       "jBODInfos": jBODInfos,
       "jBODInfosEntry": jBODInfosEntry,
       "jBODid": jBODid,
       "jBODHdNumber": jBODHdNumber,
       "jBODHdTable1": jBODHdTable1,
       "jBODHdEntry1": jBODHdEntry1,
       "jBODHdIndex1": jBODHdIndex1,
       "jBODHdDescr1": jBODHdDescr1,
       "jBODHdTemperature1": jBODHdTemperature1,
       "jBODHdStatus1": jBODHdStatus1,
       "jBODHdModel1": jBODHdModel1,
       "jBODHdCapacity1": jBODHdCapacity1,
       "jBODHdSmartInfo1": jBODHdSmartInfo1,
       "jBODHdTable2": jBODHdTable2,
       "jBODHdEntry2": jBODHdEntry2,
       "jBODHdIndex2": jBODHdIndex2,
       "jBODHdDescr2": jBODHdDescr2,
       "jBODHdTemperature2": jBODHdTemperature2,
       "jBODHdStatus2": jBODHdStatus2,
       "jBODHdModel2": jBODHdModel2,
       "jBODHdCapacity2": jBODHdCapacity2,
       "jBODHdSmartInfo2": jBODHdSmartInfo2,
       "jBODHdTable3": jBODHdTable3,
       "jBODHdEntry3": jBODHdEntry3,
       "jBODHdIndex3": jBODHdIndex3,
       "jBODHdDescr3": jBODHdDescr3,
       "jBODHdTemperature3": jBODHdTemperature3,
       "jBODHdStatus3": jBODHdStatus3,
       "jBODHdModel3": jBODHdModel3,
       "jBODHdCapacity3": jBODHdCapacity3,
       "jBODHdSmartInfo3": jBODHdSmartInfo3,
       "jBODHdTable4": jBODHdTable4,
       "jBODHdEntry4": jBODHdEntry4,
       "jBODHdIndex4": jBODHdIndex4,
       "jBODHdDescr4": jBODHdDescr4,
       "jBODHdTemperature4": jBODHdTemperature4,
       "jBODHdStatus4": jBODHdStatus4,
       "jBODHdModel4": jBODHdModel4,
       "jBODHdCapacity4": jBODHdCapacity4,
       "jBODHdSmartInfo4": jBODHdSmartInfo4,
       "jBODHdTable5": jBODHdTable5,
       "jBODHdEntry5": jBODHdEntry5,
       "jBODHdIndex5": jBODHdIndex5,
       "jBODHdDescr5": jBODHdDescr5,
       "jBODHdTemperature5": jBODHdTemperature5,
       "jBODHdStatus5": jBODHdStatus5,
       "jBODHdModel5": jBODHdModel5,
       "jBODHdCapacity5": jBODHdCapacity5,
       "jBODHdSmartInfo5": jBODHdSmartInfo5,
       "jBODHdTable6": jBODHdTable6,
       "jBODHdEntry6": jBODHdEntry6,
       "jBODHdIndex6": jBODHdIndex6,
       "jBODHdDescr6": jBODHdDescr6,
       "jBODHdTemperature6": jBODHdTemperature6,
       "jBODHdStatus6": jBODHdStatus6,
       "jBODHdModel6": jBODHdModel6,
       "jBODHdCapacity6": jBODHdCapacity6,
       "jBODHdSmartInfo6": jBODHdSmartInfo6,
       "jBODHdTable7": jBODHdTable7,
       "jBODHdEntry7": jBODHdEntry7,
       "jBODHdIndex7": jBODHdIndex7,
       "jBODHdDescr7": jBODHdDescr7,
       "jBODHdTemperature7": jBODHdTemperature7,
       "jBODHdStatus7": jBODHdStatus7,
       "jBODHdModel7": jBODHdModel7,
       "jBODHdCapacity7": jBODHdCapacity7,
       "jBODHdSmartInfo7": jBODHdSmartInfo7,
       "jBODHdTable8": jBODHdTable8,
       "jBODHdEntry8": jBODHdEntry8,
       "jBODHdIndex8": jBODHdIndex8,
       "jBODHdDescr8": jBODHdDescr8,
       "jBODHdTemperature8": jBODHdTemperature8,
       "jBODHdStatus8": jBODHdStatus8,
       "jBODHdModel8": jBODHdModel8,
       "jBODHdCapacity8": jBODHdCapacity8,
       "jBODHdSmartInfo8": jBODHdSmartInfo8,
       "systemInfoEx": systemInfoEx,
       "systemCPU-UsageEX": systemCPU_UsageEX,
       "systemTotalMemEX": systemTotalMemEX,
       "systemFreeMemEX": systemFreeMemEX,
       "systemUptimeEX": systemUptimeEX,
       "cpu-TemperatureEX": cpu_TemperatureEX,
       "systemTemperatureEX": systemTemperatureEX,
       "ifNumberEX": ifNumberEX,
       "systemIfTableEx": systemIfTableEx,
       "ifEntryEx": ifEntryEx,
       "ifIndexEX": ifIndexEX,
       "ifDescrEX": ifDescrEX,
       "ifPacketsReceivedEX": ifPacketsReceivedEX,
       "ifPacketsSentEX": ifPacketsSentEX,
       "ifErrorPacketsEX": ifErrorPacketsEX,
       "hdNumberEX": hdNumberEX,
       "systemHdTableEX": systemHdTableEX,
       "hdEntryEx": hdEntryEx,
       "hdIndexEX": hdIndexEX,
       "hdDescrEX": hdDescrEX,
       "hdTemperatureEX": hdTemperatureEX,
       "hdStatusEX": hdStatusEX,
       "hdModelEX": hdModelEX,
       "hdCapacityEX": hdCapacityEX,
       "hdSmartInfoEX": hdSmartInfoEX,
       "modelNameEX": modelNameEX,
       "hostNameEX": hostNameEX,
       "sysFanNumberEX": sysFanNumberEX,
       "systemFanTableEx": systemFanTableEx,
       "sysFanEntryEx": sysFanEntryEx,
       "sysFanIndexEX": sysFanIndexEX,
       "sysFanDescrEX": sysFanDescrEX,
       "sysFanSpeedEX": sysFanSpeedEX,
       "sysVolumeNumberEX": sysVolumeNumberEX,
       "systemVolumeTableEx": systemVolumeTableEx,
       "sysVolumeEntryEx": sysVolumeEntryEx,
       "sysVolumeIndexEX": sysVolumeIndexEX,
       "sysVolumeDescrEX": sysVolumeDescrEX,
       "sysVolumeFSEX": sysVolumeFSEX,
       "sysVolumeTotalSizeEX": sysVolumeTotalSizeEX,
       "sysVolumeFreeSizeEX": sysVolumeFreeSizeEX,
       "sysVolumeStatusEX": sysVolumeStatusEX,
       "storageSystemEx": storageSystemEx,
       "systemSettings": systemSettings,
       "storageManager": storageManager,
       "nasStorage": nasStorage,
       "components": components,
       "enclosure": enclosure,
       "enclosurelNumber": enclosurelNumber,
       "enclosureTable": enclosureTable,
       "enclosureTableEntry": enclosureTableEntry,
       "enclosureIndex": enclosureIndex,
       "enclosureID": enclosureID,
       "enclosureModel": enclosureModel,
       "enclosureSerialNum": enclosureSerialNum,
       "enclosureSlot": enclosureSlot,
       "enclosureName": enclosureName,
       "enclosureSystemTemp": enclosureSystemTemp,
       "systemFan": systemFan,
       "systemFanNumber": systemFanNumber,
       "systemFan2Table": systemFan2Table,
       "systemFan2TableEntry": systemFan2TableEntry,
       "systemFanIndex": systemFanIndex,
       "systemFanID": systemFanID,
       "systemFanEnclosureID": systemFanEnclosureID,
       "systemFanStatus": systemFanStatus,
       "systemFanSpeed": systemFanSpeed,
       "systemPower": systemPower,
       "systemPowerNumber": systemPowerNumber,
       "systemPowerTable": systemPowerTable,
       "systemPowerTableEntry": systemPowerTableEntry,
       "systemPowerIndex": systemPowerIndex,
       "systemPowerID": systemPowerID,
       "systemPowerEnclosureID": systemPowerEnclosureID,
       "systemPowerStatus": systemPowerStatus,
       "systemPowerFanSpeed": systemPowerFanSpeed,
       "systemPowerTemp": systemPowerTemp,
       "cpu": cpu,
       "cpuNumber": cpuNumber,
       "cpuTemp": cpuTemp,
       "cpuTable": cpuTable,
       "cpuTableEntry": cpuTableEntry,
       "cpuIndex": cpuIndex,
       "cpuID": cpuID,
       "cpuUsage": cpuUsage,
       "disk": disk,
       "diskNumber": diskNumber,
       "diskTable": diskTable,
       "diskTableEntry": diskTableEntry,
       "diskIndex": diskIndex,
       "diskID": diskID,
       "diskEnclosureID": diskEnclosureID,
       "diskSummary": diskSummary,
       "diskSmartInfo": diskSmartInfo,
       "diskTemperture": diskTemperture,
       "diskGlobalSpare": diskGlobalSpare,
       "diskModel": diskModel,
       "diskCapacity": diskCapacity,
       "msataDisk": msataDisk,
       "msataDiskNumber": msataDiskNumber,
       "msataDiskTable": msataDiskTable,
       "msataDiskTableEntry": msataDiskTableEntry,
       "msataDiskIndex": msataDiskIndex,
       "msataDiskID": msataDiskID,
       "msataDiskEnclosureID": msataDiskEnclosureID,
       "msataDiskSummary": msataDiskSummary,
       "msataDiskSmartInfo": msataDiskSmartInfo,
       "msataDiskTemperture": msataDiskTemperture,
       "msataDiskGlobalSpare": msataDiskGlobalSpare,
       "msataDiskModel": msataDiskModel,
       "msataDiskCapacity": msataDiskCapacity,
       "storageSpace": storageSpace,
       "raid": raid,
       "raidNumber": raidNumber,
       "raidGroupTable": raidGroupTable,
       "raidGroupTableEntry": raidGroupTableEntry,
       "raidIndex": raidIndex,
       "raidID": raidID,
       "raidCapacity": raidCapacity,
       "raidFreeSize": raidFreeSize,
       "raidStatus": raidStatus,
       "raidBitmap": raidBitmap,
       "raidLevel": raidLevel,
       "pool": pool,
       "poolNumber": poolNumber,
       "poolTable": poolTable,
       "poolTableEntry": poolTableEntry,
       "poolIndex": poolIndex,
       "poolID": poolID,
       "poolCapacity": poolCapacity,
       "poolFreeSize": poolFreeSize,
       "poolStatus": poolStatus,
       "volume": volume,
       "volumeNumber": volumeNumber,
       "volumeTable": volumeTable,
       "volumeTableEntry": volumeTableEntry,
       "volumeIndex": volumeIndex,
       "volumeID": volumeID,
       "volumeCapacity": volumeCapacity,
       "volumeFreeSize": volumeFreeSize,
       "volumeStatus": volumeStatus,
       "volumeSSDCache": volumeSSDCache,
       "volumeThin": volumeThin,
       "volumeName": volumeName,
       "cacheAcceleration": cacheAcceleration,
       "service": service,
       "availablePercent": availablePercent,
       "readHitRate": readHitRate,
       "writeHitRate": writeHitRate,
       "status": status,
       "iSCSI": iSCSI,
       "iSCSIStorage": iSCSIStorage,
       "iSCSIService": iSCSIService,
       "iSCSIServicePort": iSCSIServicePort,
       "iSNSService": iSNSService,
       "iSNSIP": iSNSIP,
       "lun": lun,
       "lunNumber": lunNumber,
       "lunTable": lunTable,
       "lunTableEntry": lunTableEntry,
       "lunIndex": lunIndex,
       "lunID": lunID,
       "lunCapacity": lunCapacity,
       "lunUsedPercent": lunUsedPercent,
       "lunStatus": lunStatus,
       "lunName": lunName,
       "lunBackupStatus": lunBackupStatus,
       "lunIsMap": lunIsMap,
       "target": target,
       "targetNumber": targetNumber,
       "targeTable": targeTable,
       "targeTableEntry": targeTableEntry,
       "targetIndex": targetIndex,
       "targetID": targetID,
       "targetName": targetName,
       "targetIQN": targetIQN,
       "targetStatus": targetStatus,
       "systemStatus": systemStatus,
       "resourceMonitor": resourceMonitor,
       "diskPerformance": diskPerformance,
       "diskPerformanceNumber": diskPerformanceNumber,
       "diskPerformanceTable": diskPerformanceTable,
       "diskPerformanceTableEntry": diskPerformanceTableEntry,
       "diskPerformanceIndex": diskPerformanceIndex,
       "blvID": blvID,
       "iops": iops,
       "latency": latency,
       "systemTraps": systemTraps,
       "eventInform": eventInform,
       "eventWarning": eventWarning,
       "eventError": eventError}
)
