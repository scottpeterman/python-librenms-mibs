# SNMP MIB module (VENTURI-SERVER-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\venturi\VENTURI-SERVER-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:51 2025
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

(vServerMgmt,) = mibBuilder.importSymbols(
    "VENTURI-SERVER-MIB",
    "vServerMgmt")

(VenturiBooleanType,
 VenturiConditionState,
 VenturiConditionType) = mibBuilder.importSymbols(
    "VENTURI-TC",
    "VenturiBooleanType",
    "VenturiConditionState",
    "VenturiConditionType")


# MODULE-IDENTITY

vServerSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2)
)
if mibBuilder.loadTexts:
    vServerSystem.setRevisions(
        ("2013-02-22 00:00",
         "2013-01-27 00:00",
         "2011-01-03 00:00",
         "2010-01-06 00:00",
         "2008-04-29 00:00",
         "2008-03-11 00:00",
         "2005-02-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VServerGeneral_ObjectIdentity = ObjectIdentity
vServerGeneral = _VServerGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1)
)
_VServerGeneralScalars_ObjectIdentity = ObjectIdentity
vServerGeneralScalars = _VServerGeneralScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1)
)


class _VServerType_Type(Bits):
    """Custom type vServerType based on Bits"""
    namedValues = NamedValues(
        *(("vServer", 0),
          ("client", 1))
    )

_VServerType_Type.__name__ = "Bits"
_VServerType_Object = MibScalar
vServerType = _VServerType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 1),
    _VServerType_Type()
)
vServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerType.setStatus("current")


class _VServerVersion_Type(OctetString):
    """Custom type vServerVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_VServerVersion_Type.__name__ = "OctetString"
_VServerVersion_Object = MibScalar
vServerVersion = _VServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 2),
    _VServerVersion_Type()
)
vServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerVersion.setStatus("current")
_VServerStartTime_Type = Integer32
_VServerStartTime_Object = MibScalar
vServerStartTime = _VServerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 3),
    _VServerStartTime_Type()
)
vServerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStartTime.setStatus("current")
_VServerUpTime_Type = TimeTicks
_VServerUpTime_Object = MibScalar
vServerUpTime = _VServerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 4),
    _VServerUpTime_Type()
)
vServerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerUpTime.setStatus("current")


class _VServerBuildId_Type(OctetString):
    """Custom type vServerBuildId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_VServerBuildId_Type.__name__ = "OctetString"
_VServerBuildId_Object = MibScalar
vServerBuildId = _VServerBuildId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 5),
    _VServerBuildId_Type()
)
vServerBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerBuildId.setStatus("current")
_VServerMaxClients_Type = Integer32
_VServerMaxClients_Object = MibScalar
vServerMaxClients = _VServerMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 6),
    _VServerMaxClients_Type()
)
vServerMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerMaxClients.setStatus("current")
_VServerMaxClientless_Type = Integer32
_VServerMaxClientless_Object = MibScalar
vServerMaxClientless = _VServerMaxClientless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 7),
    _VServerMaxClientless_Type()
)
vServerMaxClientless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerMaxClientless.setStatus("current")


class _VServerSerialNumber_Type(OctetString):
    """Custom type vServerSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_VServerSerialNumber_Type.__name__ = "OctetString"
_VServerSerialNumber_Object = MibScalar
vServerSerialNumber = _VServerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 8),
    _VServerSerialNumber_Type()
)
vServerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSerialNumber.setStatus("current")
_VServerNumCPUs_Type = Integer32
_VServerNumCPUs_Object = MibScalar
vServerNumCPUs = _VServerNumCPUs_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 9),
    _VServerNumCPUs_Type()
)
vServerNumCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerNumCPUs.setStatus("current")
_VServerMaxTcpBandwidth_Type = Integer32
_VServerMaxTcpBandwidth_Object = MibScalar
vServerMaxTcpBandwidth = _VServerMaxTcpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 10),
    _VServerMaxTcpBandwidth_Type()
)
vServerMaxTcpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerMaxTcpBandwidth.setStatus("current")
_VServerClientUpdateVersion_Type = DisplayString
_VServerClientUpdateVersion_Object = MibScalar
vServerClientUpdateVersion = _VServerClientUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 11),
    _VServerClientUpdateVersion_Type()
)
vServerClientUpdateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientUpdateVersion.setStatus("current")
_VServerMemoryRAM_Type = Integer32
_VServerMemoryRAM_Object = MibScalar
vServerMemoryRAM = _VServerMemoryRAM_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 12),
    _VServerMemoryRAM_Type()
)
vServerMemoryRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerMemoryRAM.setStatus("current")
if mibBuilder.loadTexts:
    vServerMemoryRAM.setUnits("KBytes")
_VServerMemorySwap_Type = Integer32
_VServerMemorySwap_Object = MibScalar
vServerMemorySwap = _VServerMemorySwap_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 1, 13),
    _VServerMemorySwap_Type()
)
vServerMemorySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerMemorySwap.setStatus("current")
if mibBuilder.loadTexts:
    vServerMemorySwap.setUnits("KBytes")
_VServerGeneralTables_ObjectIdentity = ObjectIdentity
vServerGeneralTables = _VServerGeneralTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2)
)
_VServerCPUTable_Object = MibTable
vServerCPUTable = _VServerCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vServerCPUTable.setStatus("current")
_VServerCPUEntry_Object = MibTableRow
vServerCPUEntry = _VServerCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 1, 1)
)
vServerCPUEntry.setIndexNames(
    (0, "VENTURI-SERVER-SYSTEM-MIB", "vServerCPUId"),
)
if mibBuilder.loadTexts:
    vServerCPUEntry.setStatus("current")


class _VServerCPUId_Type(Integer32):
    """Custom type vServerCPUId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VServerCPUId_Type.__name__ = "Integer32"
_VServerCPUId_Object = MibTableColumn
vServerCPUId = _VServerCPUId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 1, 1, 1),
    _VServerCPUId_Type()
)
vServerCPUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCPUId.setStatus("current")
_VServerCPUClockSpeed_Type = Integer32
_VServerCPUClockSpeed_Object = MibTableColumn
vServerCPUClockSpeed = _VServerCPUClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 1, 1, 2),
    _VServerCPUClockSpeed_Type()
)
vServerCPUClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCPUClockSpeed.setStatus("current")
if mibBuilder.loadTexts:
    vServerCPUClockSpeed.setUnits("Hz")
_VServerCPUCacheSize_Type = Integer32
_VServerCPUCacheSize_Object = MibTableColumn
vServerCPUCacheSize = _VServerCPUCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 1, 1, 3),
    _VServerCPUCacheSize_Type()
)
vServerCPUCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCPUCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    vServerCPUCacheSize.setUnits("KBytes")


class _VServerCPUVendorName_Type(OctetString):
    """Custom type vServerCPUVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VServerCPUVendorName_Type.__name__ = "OctetString"
_VServerCPUVendorName_Object = MibTableColumn
vServerCPUVendorName = _VServerCPUVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 1, 1, 4),
    _VServerCPUVendorName_Type()
)
vServerCPUVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCPUVendorName.setStatus("current")


class _VServerCPUModelName_Type(OctetString):
    """Custom type vServerCPUModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VServerCPUModelName_Type.__name__ = "OctetString"
_VServerCPUModelName_Object = MibTableColumn
vServerCPUModelName = _VServerCPUModelName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 1, 1, 5),
    _VServerCPUModelName_Type()
)
vServerCPUModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCPUModelName.setStatus("current")
_VServerStorageTable_Object = MibTable
vServerStorageTable = _VServerStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    vServerStorageTable.setStatus("current")
_VServerStorageEntry_Object = MibTableRow
vServerStorageEntry = _VServerStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 2, 1)
)
vServerStorageEntry.setIndexNames(
    (0, "VENTURI-SERVER-SYSTEM-MIB", "vServerStorageId"),
)
if mibBuilder.loadTexts:
    vServerStorageEntry.setStatus("current")


class _VServerStorageId_Type(Integer32):
    """Custom type vServerStorageId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VServerStorageId_Type.__name__ = "Integer32"
_VServerStorageId_Object = MibTableColumn
vServerStorageId = _VServerStorageId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 2, 1, 1),
    _VServerStorageId_Type()
)
vServerStorageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStorageId.setStatus("current")


class _VServerStorageDeviceName_Type(OctetString):
    """Custom type vServerStorageDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VServerStorageDeviceName_Type.__name__ = "OctetString"
_VServerStorageDeviceName_Object = MibTableColumn
vServerStorageDeviceName = _VServerStorageDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 2, 1, 2),
    _VServerStorageDeviceName_Type()
)
vServerStorageDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStorageDeviceName.setStatus("current")


class _VServerStorageModelName_Type(OctetString):
    """Custom type vServerStorageModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VServerStorageModelName_Type.__name__ = "OctetString"
_VServerStorageModelName_Object = MibTableColumn
vServerStorageModelName = _VServerStorageModelName_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 2, 1, 3),
    _VServerStorageModelName_Type()
)
vServerStorageModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStorageModelName.setStatus("current")
_VServerStorageSize_Type = Integer32
_VServerStorageSize_Object = MibTableColumn
vServerStorageSize = _VServerStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 1, 2, 2, 1, 4),
    _VServerStorageSize_Type()
)
vServerStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    vServerStorageSize.setUnits("KBytes")
_VServerAlarms_ObjectIdentity = ObjectIdentity
vServerAlarms = _VServerAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2)
)
_VServerAlarmScalars_ObjectIdentity = ObjectIdentity
vServerAlarmScalars = _VServerAlarmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 1)
)
_VServerAlarmTables_ObjectIdentity = ObjectIdentity
vServerAlarmTables = _VServerAlarmTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2)
)
_VServerConditionTable_Object = MibTable
vServerConditionTable = _VServerConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vServerConditionTable.setStatus("current")
_VServerConditionEntry_Object = MibTableRow
vServerConditionEntry = _VServerConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1)
)
vServerConditionEntry.setIndexNames(
    (0, "VENTURI-SERVER-SYSTEM-MIB", "vServerConditionType"),
)
if mibBuilder.loadTexts:
    vServerConditionEntry.setStatus("current")
_VServerConditionType_Type = VenturiConditionType
_VServerConditionType_Object = MibTableColumn
vServerConditionType = _VServerConditionType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 1),
    _VServerConditionType_Type()
)
vServerConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConditionType.setStatus("current")
_VServerConditionSetTrapNum_Type = Unsigned32
_VServerConditionSetTrapNum_Object = MibTableColumn
vServerConditionSetTrapNum = _VServerConditionSetTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 2),
    _VServerConditionSetTrapNum_Type()
)
vServerConditionSetTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConditionSetTrapNum.setStatus("current")
_VServerConditionClearTrapNum_Type = Unsigned32
_VServerConditionClearTrapNum_Object = MibTableColumn
vServerConditionClearTrapNum = _VServerConditionClearTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 3),
    _VServerConditionClearTrapNum_Type()
)
vServerConditionClearTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConditionClearTrapNum.setStatus("current")
_VServerConditionState_Type = VenturiConditionState
_VServerConditionState_Object = MibTableColumn
vServerConditionState = _VServerConditionState_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 4),
    _VServerConditionState_Type()
)
vServerConditionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConditionState.setStatus("current")
_VServerConditionThresholdApplicable_Type = VenturiBooleanType
_VServerConditionThresholdApplicable_Object = MibTableColumn
vServerConditionThresholdApplicable = _VServerConditionThresholdApplicable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 5),
    _VServerConditionThresholdApplicable_Type()
)
vServerConditionThresholdApplicable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConditionThresholdApplicable.setStatus("current")
_VServerConditionHighThreshold_Type = Unsigned32
_VServerConditionHighThreshold_Object = MibTableColumn
vServerConditionHighThreshold = _VServerConditionHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 6),
    _VServerConditionHighThreshold_Type()
)
vServerConditionHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConditionHighThreshold.setStatus("current")
_VServerConditionLowThreshold_Type = Unsigned32
_VServerConditionLowThreshold_Object = MibTableColumn
vServerConditionLowThreshold = _VServerConditionLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 7),
    _VServerConditionLowThreshold_Type()
)
vServerConditionLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConditionLowThreshold.setStatus("current")
_VServerConditionCurValue_Type = Unsigned32
_VServerConditionCurValue_Object = MibTableColumn
vServerConditionCurValue = _VServerConditionCurValue_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 8),
    _VServerConditionCurValue_Type()
)
vServerConditionCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerConditionCurValue.setStatus("current")
_VServerConditionSetSeverity_Type = Unsigned32
_VServerConditionSetSeverity_Object = MibTableColumn
vServerConditionSetSeverity = _VServerConditionSetSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 2, 2, 1, 1, 9),
    _VServerConditionSetSeverity_Type()
)
vServerConditionSetSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerConditionSetSeverity.setStatus("current")
_VServerActions_ObjectIdentity = ObjectIdentity
vServerActions = _VServerActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3)
)
_VServerActionScalars_ObjectIdentity = ObjectIdentity
vServerActionScalars = _VServerActionScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 1)
)
_VServerActionReboot_Type = VenturiBooleanType
_VServerActionReboot_Object = MibScalar
vServerActionReboot = _VServerActionReboot_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 1, 1),
    _VServerActionReboot_Type()
)
vServerActionReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerActionReboot.setStatus("current")
_VServerActionPushNow_Type = VenturiBooleanType
_VServerActionPushNow_Object = MibScalar
vServerActionPushNow = _VServerActionPushNow_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 1, 2),
    _VServerActionPushNow_Type()
)
vServerActionPushNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerActionPushNow.setStatus("current")
_VServerActionSendTestTrap_Type = VenturiBooleanType
_VServerActionSendTestTrap_Object = MibScalar
vServerActionSendTestTrap = _VServerActionSendTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 1, 3),
    _VServerActionSendTestTrap_Type()
)
vServerActionSendTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerActionSendTestTrap.setStatus("current")
_VServerActionSendAllTraps_Type = VenturiBooleanType
_VServerActionSendAllTraps_Object = MibScalar
vServerActionSendAllTraps = _VServerActionSendAllTraps_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 1, 4),
    _VServerActionSendAllTraps_Type()
)
vServerActionSendAllTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerActionSendAllTraps.setStatus("current")
_VServerActionSendEnabledTraps_Type = VenturiBooleanType
_VServerActionSendEnabledTraps_Object = MibScalar
vServerActionSendEnabledTraps = _VServerActionSendEnabledTraps_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 1, 5),
    _VServerActionSendEnabledTraps_Type()
)
vServerActionSendEnabledTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerActionSendEnabledTraps.setStatus("current")
_VServerActionTables_ObjectIdentity = ObjectIdentity
vServerActionTables = _VServerActionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 2)
)
_VServerFscOverrideTable_Object = MibTable
vServerFscOverrideTable = _VServerFscOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vServerFscOverrideTable.setStatus("current")
_VServerFscOverrideEntry_Object = MibTableRow
vServerFscOverrideEntry = _VServerFscOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 2, 1, 1)
)
vServerFscOverrideEntry.setIndexNames(
    (0, "VENTURI-SERVER-SYSTEM-MIB", "vServerFscOverrideRowId"),
)
if mibBuilder.loadTexts:
    vServerFscOverrideEntry.setStatus("current")
_VServerFscOverrideRowId_Type = Unsigned32
_VServerFscOverrideRowId_Object = MibTableColumn
vServerFscOverrideRowId = _VServerFscOverrideRowId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 2, 1, 1, 1),
    _VServerFscOverrideRowId_Type()
)
vServerFscOverrideRowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vServerFscOverrideRowId.setStatus("current")


class _VServerFscOverrideClientId_Type(DisplayString):
    """Custom type vServerFscOverrideClientId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VServerFscOverrideClientId_Type.__name__ = "DisplayString"
_VServerFscOverrideClientId_Object = MibTableColumn
vServerFscOverrideClientId = _VServerFscOverrideClientId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 2, 1, 1, 2),
    _VServerFscOverrideClientId_Type()
)
vServerFscOverrideClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFscOverrideClientId.setStatus("current")


class _VServerFscOverrideFsc_Type(DisplayString):
    """Custom type vServerFscOverrideFsc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VServerFscOverrideFsc_Type.__name__ = "DisplayString"
_VServerFscOverrideFsc_Object = MibTableColumn
vServerFscOverrideFsc = _VServerFscOverrideFsc_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 2, 3, 2, 1, 1, 3),
    _VServerFscOverrideFsc_Type()
)
vServerFscOverrideFsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vServerFscOverrideFsc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VENTURI-SERVER-SYSTEM-MIB",
    **{"vServerSystem": vServerSystem,
       "vServerGeneral": vServerGeneral,
       "vServerGeneralScalars": vServerGeneralScalars,
       "vServerType": vServerType,
       "vServerVersion": vServerVersion,
       "vServerStartTime": vServerStartTime,
       "vServerUpTime": vServerUpTime,
       "vServerBuildId": vServerBuildId,
       "vServerMaxClients": vServerMaxClients,
       "vServerMaxClientless": vServerMaxClientless,
       "vServerSerialNumber": vServerSerialNumber,
       "vServerNumCPUs": vServerNumCPUs,
       "vServerMaxTcpBandwidth": vServerMaxTcpBandwidth,
       "vServerClientUpdateVersion": vServerClientUpdateVersion,
       "vServerMemoryRAM": vServerMemoryRAM,
       "vServerMemorySwap": vServerMemorySwap,
       "vServerGeneralTables": vServerGeneralTables,
       "vServerCPUTable": vServerCPUTable,
       "vServerCPUEntry": vServerCPUEntry,
       "vServerCPUId": vServerCPUId,
       "vServerCPUClockSpeed": vServerCPUClockSpeed,
       "vServerCPUCacheSize": vServerCPUCacheSize,
       "vServerCPUVendorName": vServerCPUVendorName,
       "vServerCPUModelName": vServerCPUModelName,
       "vServerStorageTable": vServerStorageTable,
       "vServerStorageEntry": vServerStorageEntry,
       "vServerStorageId": vServerStorageId,
       "vServerStorageDeviceName": vServerStorageDeviceName,
       "vServerStorageModelName": vServerStorageModelName,
       "vServerStorageSize": vServerStorageSize,
       "vServerAlarms": vServerAlarms,
       "vServerAlarmScalars": vServerAlarmScalars,
       "vServerAlarmTables": vServerAlarmTables,
       "vServerConditionTable": vServerConditionTable,
       "vServerConditionEntry": vServerConditionEntry,
       "vServerConditionType": vServerConditionType,
       "vServerConditionSetTrapNum": vServerConditionSetTrapNum,
       "vServerConditionClearTrapNum": vServerConditionClearTrapNum,
       "vServerConditionState": vServerConditionState,
       "vServerConditionThresholdApplicable": vServerConditionThresholdApplicable,
       "vServerConditionHighThreshold": vServerConditionHighThreshold,
       "vServerConditionLowThreshold": vServerConditionLowThreshold,
       "vServerConditionCurValue": vServerConditionCurValue,
       "vServerConditionSetSeverity": vServerConditionSetSeverity,
       "vServerActions": vServerActions,
       "vServerActionScalars": vServerActionScalars,
       "vServerActionReboot": vServerActionReboot,
       "vServerActionPushNow": vServerActionPushNow,
       "vServerActionSendTestTrap": vServerActionSendTestTrap,
       "vServerActionSendAllTraps": vServerActionSendAllTraps,
       "vServerActionSendEnabledTraps": vServerActionSendEnabledTraps,
       "vServerActionTables": vServerActionTables,
       "vServerFscOverrideTable": vServerFscOverrideTable,
       "vServerFscOverrideEntry": vServerFscOverrideEntry,
       "vServerFscOverrideRowId": vServerFscOverrideRowId,
       "vServerFscOverrideClientId": vServerFscOverrideClientId,
       "vServerFscOverrideFsc": vServerFscOverrideFsc}
)
