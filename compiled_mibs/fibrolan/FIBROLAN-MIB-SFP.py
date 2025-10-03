# SNMP MIB module (FIBROLAN-MIB-SFP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-SFP
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:30 2025
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

(flMsChassisModuleMvIndex,
 flMsChassisMvIndex) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    "flMsChassisModuleMvIndex",
    "flMsChassisMvIndex")

(flMsModuleMvChannelIndex,) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-MSMODULE",
    "flMsModuleMvChannelIndex")

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

flSfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibrolan_ObjectIdentity = ObjectIdentity
fibrolan = _Fibrolan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467)
)
_FibrolanSNMP_ObjectIdentity = ObjectIdentity
fibrolanSNMP = _FibrolanSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100)
)
_FlMetroStarMv_ObjectIdentity = ObjectIdentity
flMetroStarMv = _FlMetroStarMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500)
)
_FlSfpMIBConformance_ObjectIdentity = ObjectIdentity
flSfpMIBConformance = _FlSfpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 1)
)
_FlSfpMIBCompliances_ObjectIdentity = ObjectIdentity
flSfpMIBCompliances = _FlSfpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 1, 1)
)
_FlSfpMIBGroups_ObjectIdentity = ObjectIdentity
flSfpMIBGroups = _FlSfpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 1, 2)
)
_FlSfpDevice_ObjectIdentity = ObjectIdentity
flSfpDevice = _FlSfpDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10)
)
_FlSfpDeviceTable_Object = MibTable
flSfpDeviceTable = _FlSfpDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1)
)
if mibBuilder.loadTexts:
    flSfpDeviceTable.setStatus("current")
_FlSfpDeviceEntry_Object = MibTableRow
flSfpDeviceEntry = _FlSfpDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1)
)
flSfpDeviceEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDevicePortIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceLocalRemoteIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceRemoteChannelIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceRemotePortIndex"),
)
if mibBuilder.loadTexts:
    flSfpDeviceEntry.setStatus("current")


class _FlSfpDevicePortIndex_Type(Integer32):
    """Custom type flSfpDevicePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlSfpDevicePortIndex_Type.__name__ = "Integer32"
_FlSfpDevicePortIndex_Object = MibTableColumn
flSfpDevicePortIndex = _FlSfpDevicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 1),
    _FlSfpDevicePortIndex_Type()
)
flSfpDevicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDevicePortIndex.setStatus("current")


class _FlSfpDeviceLocalRemoteIndex_Type(Integer32):
    """Custom type flSfpDeviceLocalRemoteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_FlSfpDeviceLocalRemoteIndex_Type.__name__ = "Integer32"
_FlSfpDeviceLocalRemoteIndex_Object = MibTableColumn
flSfpDeviceLocalRemoteIndex = _FlSfpDeviceLocalRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 2),
    _FlSfpDeviceLocalRemoteIndex_Type()
)
flSfpDeviceLocalRemoteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceLocalRemoteIndex.setStatus("current")


class _FlSfpDeviceRemoteChannelIndex_Type(Integer32):
    """Custom type flSfpDeviceRemoteChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlSfpDeviceRemoteChannelIndex_Type.__name__ = "Integer32"
_FlSfpDeviceRemoteChannelIndex_Object = MibTableColumn
flSfpDeviceRemoteChannelIndex = _FlSfpDeviceRemoteChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 3),
    _FlSfpDeviceRemoteChannelIndex_Type()
)
flSfpDeviceRemoteChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceRemoteChannelIndex.setStatus("current")


class _FlSfpDeviceRemotePortIndex_Type(Integer32):
    """Custom type flSfpDeviceRemotePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlSfpDeviceRemotePortIndex_Type.__name__ = "Integer32"
_FlSfpDeviceRemotePortIndex_Object = MibTableColumn
flSfpDeviceRemotePortIndex = _FlSfpDeviceRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 4),
    _FlSfpDeviceRemotePortIndex_Type()
)
flSfpDeviceRemotePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceRemotePortIndex.setStatus("current")
_FlSfpDeviceSerialNumber_Type = DisplayString
_FlSfpDeviceSerialNumber_Object = MibTableColumn
flSfpDeviceSerialNumber = _FlSfpDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 5),
    _FlSfpDeviceSerialNumber_Type()
)
flSfpDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceSerialNumber.setStatus("current")
_FlSfpDevicePartNumber_Type = DisplayString
_FlSfpDevicePartNumber_Object = MibTableColumn
flSfpDevicePartNumber = _FlSfpDevicePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 6),
    _FlSfpDevicePartNumber_Type()
)
flSfpDevicePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDevicePartNumber.setStatus("current")
_FlSfpDevicePortName_Type = DisplayString
_FlSfpDevicePortName_Object = MibTableColumn
flSfpDevicePortName = _FlSfpDevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 7),
    _FlSfpDevicePortName_Type()
)
flSfpDevicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDevicePortName.setStatus("current")
_FlSfpDeviceType_Type = DisplayString
_FlSfpDeviceType_Object = MibTableColumn
flSfpDeviceType = _FlSfpDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 8),
    _FlSfpDeviceType_Type()
)
flSfpDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceType.setStatus("current")
_FlSfpDeviceRange_Type = Integer32
_FlSfpDeviceRange_Object = MibTableColumn
flSfpDeviceRange = _FlSfpDeviceRange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 9),
    _FlSfpDeviceRange_Type()
)
flSfpDeviceRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceRange.setStatus("current")
_FlSfpDeviceTxWl_Type = Integer32
_FlSfpDeviceTxWl_Object = MibTableColumn
flSfpDeviceTxWl = _FlSfpDeviceTxWl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 10),
    _FlSfpDeviceTxWl_Type()
)
flSfpDeviceTxWl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceTxWl.setStatus("current")
_FlSfpDeviceRxwl_Type = Integer32
_FlSfpDeviceRxwl_Object = MibTableColumn
flSfpDeviceRxwl = _FlSfpDeviceRxwl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 11),
    _FlSfpDeviceRxwl_Type()
)
flSfpDeviceRxwl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceRxwl.setStatus("current")


class _FlSfpDeviceState_Type(Integer32):
    """Custom type flSfpDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unplugged", 1),
          ("invalid", 2),
          ("authenticated", 3),
          ("unknown", 4))
    )


_FlSfpDeviceState_Type.__name__ = "Integer32"
_FlSfpDeviceState_Object = MibTableColumn
flSfpDeviceState = _FlSfpDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 1, 1, 12),
    _FlSfpDeviceState_Type()
)
flSfpDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceState.setStatus("current")
_FlSfpPortsTable_Object = MibTable
flSfpPortsTable = _FlSfpPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 2)
)
if mibBuilder.loadTexts:
    flSfpPortsTable.setStatus("current")
_FlSfpPortsEntry_Object = MibTableRow
flSfpPortsEntry = _FlSfpPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 2, 1)
)
flSfpPortsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDevicePortIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceLocalRemoteIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceRemoteChannelIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceRemotePortIndex"),
)
if mibBuilder.loadTexts:
    flSfpPortsEntry.setStatus("current")


class _FlSfpPortSignalDetect_Type(Integer32):
    """Custom type flSfpPortSignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlSfpPortSignalDetect_Type.__name__ = "Integer32"
_FlSfpPortSignalDetect_Object = MibTableColumn
flSfpPortSignalDetect = _FlSfpPortSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 2, 1, 5),
    _FlSfpPortSignalDetect_Type()
)
flSfpPortSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpPortSignalDetect.setStatus("current")


class _FlSfpPortLink_Type(Integer32):
    """Custom type flSfpPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("kld", 3))
    )


_FlSfpPortLink_Type.__name__ = "Integer32"
_FlSfpPortLink_Object = MibTableColumn
flSfpPortLink = _FlSfpPortLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 2, 1, 6),
    _FlSfpPortLink_Type()
)
flSfpPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpPortLink.setStatus("current")


class _FlSfpPortEnable_Type(Integer32):
    """Custom type flSfpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("n-a", 3))
    )


_FlSfpPortEnable_Type.__name__ = "Integer32"
_FlSfpPortEnable_Object = MibTableColumn
flSfpPortEnable = _FlSfpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 2, 1, 7),
    _FlSfpPortEnable_Type()
)
flSfpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flSfpPortEnable.setStatus("current")
_FlSfpDeviceMonitoringTable_Object = MibTable
flSfpDeviceMonitoringTable = _FlSfpDeviceMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 3)
)
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringTable.setStatus("current")
_FlSfpDeviceMonitoringEntry_Object = MibTableRow
flSfpDeviceMonitoringEntry = _FlSfpDeviceMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 3, 1)
)
flSfpDeviceMonitoringEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDevicePortIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceLocalRemoteIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceRemoteChannelIndex"),
    (0, "FIBROLAN-MIB-SFP", "flSfpDeviceRemotePortIndex"),
)
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringEntry.setStatus("current")
_FlSfpDeviceMonitoringRxPower_Type = Integer32
_FlSfpDeviceMonitoringRxPower_Object = MibTableColumn
flSfpDeviceMonitoringRxPower = _FlSfpDeviceMonitoringRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 3, 1, 1),
    _FlSfpDeviceMonitoringRxPower_Type()
)
flSfpDeviceMonitoringRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringRxPower.setStatus("current")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringRxPower.setUnits("0.01dBm")
_FlSfpDeviceMonitoringTxPower_Type = Integer32
_FlSfpDeviceMonitoringTxPower_Object = MibTableColumn
flSfpDeviceMonitoringTxPower = _FlSfpDeviceMonitoringTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 3, 1, 2),
    _FlSfpDeviceMonitoringTxPower_Type()
)
flSfpDeviceMonitoringTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringTxPower.setStatus("current")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringTxPower.setUnits("0.01dBm")
_FlSfpDeviceMonitoringTemperature_Type = Integer32
_FlSfpDeviceMonitoringTemperature_Object = MibTableColumn
flSfpDeviceMonitoringTemperature = _FlSfpDeviceMonitoringTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 3, 1, 3),
    _FlSfpDeviceMonitoringTemperature_Type()
)
flSfpDeviceMonitoringTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringTemperature.setStatus("current")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringTemperature.setUnits("0.1 degrees Celsius (oC)")
_FlSfpDeviceMonitoringTxBias_Type = Integer32
_FlSfpDeviceMonitoringTxBias_Object = MibTableColumn
flSfpDeviceMonitoringTxBias = _FlSfpDeviceMonitoringTxBias_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 3, 1, 4),
    _FlSfpDeviceMonitoringTxBias_Type()
)
flSfpDeviceMonitoringTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringTxBias.setStatus("current")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringTxBias.setUnits("micro Ampere (uA)")
_FlSfpDeviceMonitoringSupplyVoltage_Type = Integer32
_FlSfpDeviceMonitoringSupplyVoltage_Object = MibTableColumn
flSfpDeviceMonitoringSupplyVoltage = _FlSfpDeviceMonitoringSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 10, 3, 1, 5),
    _FlSfpDeviceMonitoringSupplyVoltage_Type()
)
flSfpDeviceMonitoringSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    flSfpDeviceMonitoringSupplyVoltage.setUnits("100 micro Volt (100uV)")

# Managed Objects groups

flSfpDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 1, 2, 1)
)
flSfpDeviceGroup.setObjects(
      *(("FIBROLAN-MIB-SFP", "flSfpDevicePortIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceLocalRemoteIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRemoteChannelIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRemotePortIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceSerialNumber"),
        ("FIBROLAN-MIB-SFP", "flSfpDevicePartNumber"),
        ("FIBROLAN-MIB-SFP", "flSfpDevicePortName"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceType"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRange"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceTxWl"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRxwl"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceState"))
)
if mibBuilder.loadTexts:
    flSfpDeviceGroup.setStatus("current")

flSfpPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 1, 2, 2)
)
flSfpPortsGroup.setObjects(
      *(("FIBROLAN-MIB-SFP", "flSfpDevicePortIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceLocalRemoteIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRemoteChannelIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRemotePortIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpPortSignalDetect"),
        ("FIBROLAN-MIB-SFP", "flSfpPortLink"),
        ("FIBROLAN-MIB-SFP", "flSfpPortEnable"))
)
if mibBuilder.loadTexts:
    flSfpPortsGroup.setStatus("current")

flSfpMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 1, 2, 3)
)
flSfpMonitoringGroup.setObjects(
      *(("FIBROLAN-MIB-SFP", "flSfpDevicePortIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceLocalRemoteIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRemoteChannelIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceRemotePortIndex"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceMonitoringRxPower"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceMonitoringTxPower"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceMonitoringTemperature"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceMonitoringTxBias"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceMonitoringSupplyVoltage"))
)
if mibBuilder.loadTexts:
    flSfpMonitoringGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flSfpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 100, 1, 1, 1)
)
flSfpMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModulesGroup"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelsGroup"),
        ("FIBROLAN-MIB-SFP", "flSfpDeviceGroup"),
        ("FIBROLAN-MIB-SFP", "flSfpPortsGroup"),
        ("FIBROLAN-MIB-SFP", "flSfpMonitoringGroup"))
)
if mibBuilder.loadTexts:
    flSfpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-SFP",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flSfp": flSfp,
       "flSfpMIBConformance": flSfpMIBConformance,
       "flSfpMIBCompliances": flSfpMIBCompliances,
       "flSfpMIBCompliance": flSfpMIBCompliance,
       "flSfpMIBGroups": flSfpMIBGroups,
       "flSfpDeviceGroup": flSfpDeviceGroup,
       "flSfpPortsGroup": flSfpPortsGroup,
       "flSfpMonitoringGroup": flSfpMonitoringGroup,
       "flSfpDevice": flSfpDevice,
       "flSfpDeviceTable": flSfpDeviceTable,
       "flSfpDeviceEntry": flSfpDeviceEntry,
       "flSfpDevicePortIndex": flSfpDevicePortIndex,
       "flSfpDeviceLocalRemoteIndex": flSfpDeviceLocalRemoteIndex,
       "flSfpDeviceRemoteChannelIndex": flSfpDeviceRemoteChannelIndex,
       "flSfpDeviceRemotePortIndex": flSfpDeviceRemotePortIndex,
       "flSfpDeviceSerialNumber": flSfpDeviceSerialNumber,
       "flSfpDevicePartNumber": flSfpDevicePartNumber,
       "flSfpDevicePortName": flSfpDevicePortName,
       "flSfpDeviceType": flSfpDeviceType,
       "flSfpDeviceRange": flSfpDeviceRange,
       "flSfpDeviceTxWl": flSfpDeviceTxWl,
       "flSfpDeviceRxwl": flSfpDeviceRxwl,
       "flSfpDeviceState": flSfpDeviceState,
       "flSfpPortsTable": flSfpPortsTable,
       "flSfpPortsEntry": flSfpPortsEntry,
       "flSfpPortSignalDetect": flSfpPortSignalDetect,
       "flSfpPortLink": flSfpPortLink,
       "flSfpPortEnable": flSfpPortEnable,
       "flSfpDeviceMonitoringTable": flSfpDeviceMonitoringTable,
       "flSfpDeviceMonitoringEntry": flSfpDeviceMonitoringEntry,
       "flSfpDeviceMonitoringRxPower": flSfpDeviceMonitoringRxPower,
       "flSfpDeviceMonitoringTxPower": flSfpDeviceMonitoringTxPower,
       "flSfpDeviceMonitoringTemperature": flSfpDeviceMonitoringTemperature,
       "flSfpDeviceMonitoringTxBias": flSfpDeviceMonitoringTxBias,
       "flSfpDeviceMonitoringSupplyVoltage": flSfpDeviceMonitoringSupplyVoltage}
)
