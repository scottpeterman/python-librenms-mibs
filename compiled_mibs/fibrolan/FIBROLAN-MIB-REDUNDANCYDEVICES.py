# SNMP MIB module (FIBROLAN-MIB-REDUNDANCYDEVICES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-REDUNDANCYDEVICES
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:29 2025
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

flRedundantDev = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40)
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
_FlMaRemoteDevice_ObjectIdentity = ObjectIdentity
flMaRemoteDevice = _FlMaRemoteDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50)
)
_FlRedundantDevMIBConformance_ObjectIdentity = ObjectIdentity
flRedundantDevMIBConformance = _FlRedundantDevMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 1)
)
_FlRedundantDevMIBCompliances_ObjectIdentity = ObjectIdentity
flRedundantDevMIBCompliances = _FlRedundantDevMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 1, 1)
)
_FlRedundantDevMIBGroups_ObjectIdentity = ObjectIdentity
flRedundantDevMIBGroups = _FlRedundantDevMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 1, 2)
)
_FlRedundantDevice_ObjectIdentity = ObjectIdentity
flRedundantDevice = _FlRedundantDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10)
)
_FlRedundantDeviceConfigTable_Object = MibTable
flRedundantDeviceConfigTable = _FlRedundantDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1)
)
if mibBuilder.loadTexts:
    flRedundantDeviceConfigTable.setStatus("current")
_FlRedundantDeviceConfigEntry_Object = MibTableRow
flRedundantDeviceConfigEntry = _FlRedundantDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1, 1)
)
flRedundantDeviceConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flRedundantDeviceConfigEntry.setStatus("current")


class _FlRedundantDeviceReset_Type(Integer32):
    """Custom type flRedundantDeviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_FlRedundantDeviceReset_Type.__name__ = "Integer32"
_FlRedundantDeviceReset_Object = MibTableColumn
flRedundantDeviceReset = _FlRedundantDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1, 1, 2),
    _FlRedundantDeviceReset_Type()
)
flRedundantDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDeviceReset.setStatus("current")


class _FlRedundantDeviceRestoreDefaults_Type(Integer32):
    """Custom type flRedundantDeviceRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("restore", 2))
    )


_FlRedundantDeviceRestoreDefaults_Type.__name__ = "Integer32"
_FlRedundantDeviceRestoreDefaults_Object = MibTableColumn
flRedundantDeviceRestoreDefaults = _FlRedundantDeviceRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1, 1, 3),
    _FlRedundantDeviceRestoreDefaults_Type()
)
flRedundantDeviceRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDeviceRestoreDefaults.setStatus("current")
_FlRedundantDeviceFirmRevision_Type = DisplayString
_FlRedundantDeviceFirmRevision_Object = MibTableColumn
flRedundantDeviceFirmRevision = _FlRedundantDeviceFirmRevision_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1, 1, 4),
    _FlRedundantDeviceFirmRevision_Type()
)
flRedundantDeviceFirmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDeviceFirmRevision.setStatus("current")


class _FlRedundantDeviceRedundancyMode_Type(Integer32):
    """Custom type flRedundantDeviceRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 1),
          ("redundant", 2),
          ("hybrid", 3))
    )


_FlRedundantDeviceRedundancyMode_Type.__name__ = "Integer32"
_FlRedundantDeviceRedundancyMode_Object = MibTableColumn
flRedundantDeviceRedundancyMode = _FlRedundantDeviceRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1, 1, 5),
    _FlRedundantDeviceRedundancyMode_Type()
)
flRedundantDeviceRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDeviceRedundancyMode.setStatus("current")
_FlRedundantTemperature_Type = Integer32
_FlRedundantTemperature_Object = MibTableColumn
flRedundantTemperature = _FlRedundantTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1, 1, 6),
    _FlRedundantTemperature_Type()
)
flRedundantTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantTemperature.setStatus("current")
_FlRedundantSerialNumber_Type = DisplayString
_FlRedundantSerialNumber_Object = MibTableColumn
flRedundantSerialNumber = _FlRedundantSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 1, 1, 7),
    _FlRedundantSerialNumber_Type()
)
flRedundantSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantSerialNumber.setStatus("current")
_FlRedundantDeviceStatusTable_Object = MibTable
flRedundantDeviceStatusTable = _FlRedundantDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2)
)
if mibBuilder.loadTexts:
    flRedundantDeviceStatusTable.setStatus("current")
_FlRedundantDeviceStatusEntry_Object = MibTableRow
flRedundantDeviceStatusEntry = _FlRedundantDeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1)
)
flRedundantDeviceStatusEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flRedundantDeviceStatusEntry.setStatus("current")


class _FlRedundantDevActiveFoLink_Type(Integer32):
    """Custom type flRedundantDevActiveFoLink based on Integer32"""
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
        *(("down", 1),
          ("bckp", 2),
          ("fBckp", 3),
          ("main", 4))
    )


_FlRedundantDevActiveFoLink_Type.__name__ = "Integer32"
_FlRedundantDevActiveFoLink_Object = MibTableColumn
flRedundantDevActiveFoLink = _FlRedundantDevActiveFoLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 1),
    _FlRedundantDevActiveFoLink_Type()
)
flRedundantDevActiveFoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevActiveFoLink.setStatus("current")


class _FlRedundantDevActiveTpLink_Type(Integer32):
    """Custom type flRedundantDevActiveTpLink based on Integer32"""
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
        *(("down", 1),
          ("killed", 2),
          ("bckp", 3),
          ("fBckp", 4),
          ("main", 5))
    )


_FlRedundantDevActiveTpLink_Type.__name__ = "Integer32"
_FlRedundantDevActiveTpLink_Object = MibTableColumn
flRedundantDevActiveTpLink = _FlRedundantDevActiveTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 2),
    _FlRedundantDevActiveTpLink_Type()
)
flRedundantDevActiveTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevActiveTpLink.setStatus("current")


class _FlRedundantDevStbyFoLink_Type(Integer32):
    """Custom type flRedundantDevStbyFoLink based on Integer32"""
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
        *(("mainDown", 1),
          ("bckpDown", 2),
          ("bckpUnused", 3),
          ("mainUp", 4),
          ("bckpUp", 5))
    )


_FlRedundantDevStbyFoLink_Type.__name__ = "Integer32"
_FlRedundantDevStbyFoLink_Object = MibTableColumn
flRedundantDevStbyFoLink = _FlRedundantDevStbyFoLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 3),
    _FlRedundantDevStbyFoLink_Type()
)
flRedundantDevStbyFoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevStbyFoLink.setStatus("current")


class _FlRedundantDevStbyTpLink_Type(Integer32):
    """Custom type flRedundantDevStbyTpLink based on Integer32"""
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
        *(("mainDown", 1),
          ("bckpDown", 2),
          ("bckpUnused", 3),
          ("mainUp", 4),
          ("bckpUp", 5))
    )


_FlRedundantDevStbyTpLink_Type.__name__ = "Integer32"
_FlRedundantDevStbyTpLink_Object = MibTableColumn
flRedundantDevStbyTpLink = _FlRedundantDevStbyTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 4),
    _FlRedundantDevStbyTpLink_Type()
)
flRedundantDevStbyTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevStbyTpLink.setStatus("current")


class _FlRedundantDevMainFoInuse_Type(Integer32):
    """Custom type flRedundantDevMainFoInuse based on Integer32"""
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


_FlRedundantDevMainFoInuse_Type.__name__ = "Integer32"
_FlRedundantDevMainFoInuse_Object = MibTableColumn
flRedundantDevMainFoInuse = _FlRedundantDevMainFoInuse_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 5),
    _FlRedundantDevMainFoInuse_Type()
)
flRedundantDevMainFoInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevMainFoInuse.setStatus("current")


class _FlRedundantDevMainTpInuse_Type(Integer32):
    """Custom type flRedundantDevMainTpInuse based on Integer32"""
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


_FlRedundantDevMainTpInuse_Type.__name__ = "Integer32"
_FlRedundantDevMainTpInuse_Object = MibTableColumn
flRedundantDevMainTpInuse = _FlRedundantDevMainTpInuse_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 6),
    _FlRedundantDevMainTpInuse_Type()
)
flRedundantDevMainTpInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevMainTpInuse.setStatus("current")


class _FlRedundantDevBckpFoInuse_Type(Integer32):
    """Custom type flRedundantDevBckpFoInuse based on Integer32"""
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


_FlRedundantDevBckpFoInuse_Type.__name__ = "Integer32"
_FlRedundantDevBckpFoInuse_Object = MibTableColumn
flRedundantDevBckpFoInuse = _FlRedundantDevBckpFoInuse_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 7),
    _FlRedundantDevBckpFoInuse_Type()
)
flRedundantDevBckpFoInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevBckpFoInuse.setStatus("current")


class _FlRedundantDevBckpTpInuse_Type(Integer32):
    """Custom type flRedundantDevBckpTpInuse based on Integer32"""
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


_FlRedundantDevBckpTpInuse_Type.__name__ = "Integer32"
_FlRedundantDevBckpTpInuse_Object = MibTableColumn
flRedundantDevBckpTpInuse = _FlRedundantDevBckpTpInuse_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 10, 2, 1, 8),
    _FlRedundantDevBckpTpInuse_Type()
)
flRedundantDevBckpTpInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevBckpTpInuse.setStatus("current")
_FlRedundantDevChannel_ObjectIdentity = ObjectIdentity
flRedundantDevChannel = _FlRedundantDevChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20)
)
_FlRedundantDevChannelConfigTable_Object = MibTable
flRedundantDevChannelConfigTable = _FlRedundantDevChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1)
)
if mibBuilder.loadTexts:
    flRedundantDevChannelConfigTable.setStatus("current")
_FlRedundantDevChannelConfigEntry_Object = MibTableRow
flRedundantDevChannelConfigEntry = _FlRedundantDevChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1)
)
flRedundantDevChannelConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevChannelConfigIndex"),
)
if mibBuilder.loadTexts:
    flRedundantDevChannelConfigEntry.setStatus("current")


class _FlRedundantDevChannelConfigIndex_Type(Integer32):
    """Custom type flRedundantDevChannelConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlRedundantDevChannelConfigIndex_Type.__name__ = "Integer32"
_FlRedundantDevChannelConfigIndex_Object = MibTableColumn
flRedundantDevChannelConfigIndex = _FlRedundantDevChannelConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 1),
    _FlRedundantDevChannelConfigIndex_Type()
)
flRedundantDevChannelConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flRedundantDevChannelConfigIndex.setStatus("current")


class _FlRedundantDevUpstreamBw_Type(Integer32):
    """Custom type flRedundantDevUpstreamBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FlRedundantDevUpstreamBw_Type.__name__ = "Integer32"
_FlRedundantDevUpstreamBw_Object = MibTableColumn
flRedundantDevUpstreamBw = _FlRedundantDevUpstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 2),
    _FlRedundantDevUpstreamBw_Type()
)
flRedundantDevUpstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevUpstreamBw.setStatus("current")


class _FlRedundantDevEnableTpPort_Type(Integer32):
    """Custom type flRedundantDevEnableTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlRedundantDevEnableTpPort_Type.__name__ = "Integer32"
_FlRedundantDevEnableTpPort_Object = MibTableColumn
flRedundantDevEnableTpPort = _FlRedundantDevEnableTpPort_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 3),
    _FlRedundantDevEnableTpPort_Type()
)
flRedundantDevEnableTpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevEnableTpPort.setStatus("current")


class _FlRedundantDevPause_Type(Integer32):
    """Custom type flRedundantDevPause based on Integer32"""
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


_FlRedundantDevPause_Type.__name__ = "Integer32"
_FlRedundantDevPause_Object = MibTableColumn
flRedundantDevPause = _FlRedundantDevPause_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 4),
    _FlRedundantDevPause_Type()
)
flRedundantDevPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevPause.setStatus("current")


class _FlRedundantDevFo2TpFp_Type(Integer32):
    """Custom type flRedundantDevFo2TpFp based on Integer32"""
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


_FlRedundantDevFo2TpFp_Type.__name__ = "Integer32"
_FlRedundantDevFo2TpFp_Object = MibTableColumn
flRedundantDevFo2TpFp = _FlRedundantDevFo2TpFp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 5),
    _FlRedundantDevFo2TpFp_Type()
)
flRedundantDevFo2TpFp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevFo2TpFp.setStatus("current")


class _FlRedundantDevFoLb_Type(Integer32):
    """Custom type flRedundantDevFoLb based on Integer32"""
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


_FlRedundantDevFoLb_Type.__name__ = "Integer32"
_FlRedundantDevFoLb_Object = MibTableColumn
flRedundantDevFoLb = _FlRedundantDevFoLb_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 6),
    _FlRedundantDevFoLb_Type()
)
flRedundantDevFoLb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevFoLb.setStatus("current")


class _FlRedundantDevTpLb_Type(Integer32):
    """Custom type flRedundantDevTpLb based on Integer32"""
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


_FlRedundantDevTpLb_Type.__name__ = "Integer32"
_FlRedundantDevTpLb_Object = MibTableColumn
flRedundantDevTpLb = _FlRedundantDevTpLb_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 7),
    _FlRedundantDevTpLb_Type()
)
flRedundantDevTpLb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevTpLb.setStatus("current")


class _FlRedundantDevFo2TpLst_Type(Integer32):
    """Custom type flRedundantDevFo2TpLst based on Integer32"""
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


_FlRedundantDevFo2TpLst_Type.__name__ = "Integer32"
_FlRedundantDevFo2TpLst_Object = MibTableColumn
flRedundantDevFo2TpLst = _FlRedundantDevFo2TpLst_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 8),
    _FlRedundantDevFo2TpLst_Type()
)
flRedundantDevFo2TpLst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevFo2TpLst.setStatus("current")


class _FlRedundantDevFoBckp2Main_Type(Integer32):
    """Custom type flRedundantDevFoBckp2Main based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sec0", 1),
          ("sec1", 2),
          ("sec5", 3),
          ("sec10", 4),
          ("sec20", 5),
          ("never", 6))
    )


_FlRedundantDevFoBckp2Main_Type.__name__ = "Integer32"
_FlRedundantDevFoBckp2Main_Object = MibTableColumn
flRedundantDevFoBckp2Main = _FlRedundantDevFoBckp2Main_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 9),
    _FlRedundantDevFoBckp2Main_Type()
)
flRedundantDevFoBckp2Main.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevFoBckp2Main.setStatus("current")


class _FlRedundantDevTpBckp2Main_Type(Integer32):
    """Custom type flRedundantDevTpBckp2Main based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sec0", 1),
          ("sec1", 2),
          ("sec5", 3),
          ("sec10", 4),
          ("sec20", 5),
          ("never", 6))
    )


_FlRedundantDevTpBckp2Main_Type.__name__ = "Integer32"
_FlRedundantDevTpBckp2Main_Object = MibTableColumn
flRedundantDevTpBckp2Main = _FlRedundantDevTpBckp2Main_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 10),
    _FlRedundantDevTpBckp2Main_Type()
)
flRedundantDevTpBckp2Main.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevTpBckp2Main.setStatus("current")


class _FlRedundantDevForceFo_Type(Integer32):
    """Custom type flRedundantDevForceFo based on Integer32"""
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


_FlRedundantDevForceFo_Type.__name__ = "Integer32"
_FlRedundantDevForceFo_Object = MibTableColumn
flRedundantDevForceFo = _FlRedundantDevForceFo_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 11),
    _FlRedundantDevForceFo_Type()
)
flRedundantDevForceFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevForceFo.setStatus("current")


class _FlRedundantDevForceTp_Type(Integer32):
    """Custom type flRedundantDevForceTp based on Integer32"""
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


_FlRedundantDevForceTp_Type.__name__ = "Integer32"
_FlRedundantDevForceTp_Object = MibTableColumn
flRedundantDevForceTp = _FlRedundantDevForceTp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 12),
    _FlRedundantDevForceTp_Type()
)
flRedundantDevForceTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevForceTp.setStatus("current")


class _FlRedundantDevBckpFoUnused_Type(Integer32):
    """Custom type flRedundantDevBckpFoUnused based on Integer32"""
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


_FlRedundantDevBckpFoUnused_Type.__name__ = "Integer32"
_FlRedundantDevBckpFoUnused_Object = MibTableColumn
flRedundantDevBckpFoUnused = _FlRedundantDevBckpFoUnused_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 13),
    _FlRedundantDevBckpFoUnused_Type()
)
flRedundantDevBckpFoUnused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevBckpFoUnused.setStatus("current")


class _FlRedundantDevBckpTpUnused_Type(Integer32):
    """Custom type flRedundantDevBckpTpUnused based on Integer32"""
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


_FlRedundantDevBckpTpUnused_Type.__name__ = "Integer32"
_FlRedundantDevBckpTpUnused_Object = MibTableColumn
flRedundantDevBckpTpUnused = _FlRedundantDevBckpTpUnused_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 14),
    _FlRedundantDevBckpTpUnused_Type()
)
flRedundantDevBckpTpUnused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevBckpTpUnused.setStatus("current")
_FlRedundantDevPortDescription_Type = DisplayString
_FlRedundantDevPortDescription_Object = MibTableColumn
flRedundantDevPortDescription = _FlRedundantDevPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 15),
    _FlRedundantDevPortDescription_Type()
)
flRedundantDevPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevPortDescription.setStatus("current")


class _FlRedundantDevTpFailOver_Type(Integer32):
    """Custom type flRedundantDevTpFailOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fast", 2))
    )


_FlRedundantDevTpFailOver_Type.__name__ = "Integer32"
_FlRedundantDevTpFailOver_Object = MibTableColumn
flRedundantDevTpFailOver = _FlRedundantDevTpFailOver_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 16),
    _FlRedundantDevTpFailOver_Type()
)
flRedundantDevTpFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevTpFailOver.setStatus("current")


class _FlRedundantDevAutoNego_Type(Integer32):
    """Custom type flRedundantDevAutoNego based on Integer32"""
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


_FlRedundantDevAutoNego_Type.__name__ = "Integer32"
_FlRedundantDevAutoNego_Object = MibTableColumn
flRedundantDevAutoNego = _FlRedundantDevAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 20, 1, 1, 17),
    _FlRedundantDevAutoNego_Type()
)
flRedundantDevAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flRedundantDevAutoNego.setStatus("current")

# Managed Objects groups

flRedundantDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 1, 2, 1)
)
flRedundantDeviceGroup.setObjects(
      *(("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDeviceReset"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDeviceRestoreDefaults"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDeviceFirmRevision"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDeviceRedundancyMode"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantTemperature"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantSerialNumber"))
)
if mibBuilder.loadTexts:
    flRedundantDeviceGroup.setStatus("current")

flRedundantDeviceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 1, 2, 2)
)
flRedundantDeviceStatusGroup.setObjects(
      *(("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevActiveFoLink"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevActiveTpLink"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevStbyFoLink"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevStbyTpLink"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevMainFoInuse"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevMainTpInuse"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevBckpFoInuse"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevBckpTpInuse"))
)
if mibBuilder.loadTexts:
    flRedundantDeviceStatusGroup.setStatus("current")

flRedundantDevChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 1, 2, 3)
)
flRedundantDevChannelGroup.setObjects(
      *(("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevChannelConfigIndex"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevUpstreamBw"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevEnableTpPort"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevPause"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevFo2TpFp"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevFoLb"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevTpLb"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevFo2TpLst"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevFoBckp2Main"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevTpBckp2Main"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevForceFo"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevForceTp"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevBckpFoUnused"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevBckpTpUnused"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevPortDescription"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevTpFailOver"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevAutoNego"))
)
if mibBuilder.loadTexts:
    flRedundantDevChannelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flRedundantDevMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 40, 1, 1, 1)
)
flRedundantDevMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDeviceGroup"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDeviceStatusGroup"),
        ("FIBROLAN-MIB-REDUNDANCYDEVICES", "flRedundantDevChannelGroup"))
)
if mibBuilder.loadTexts:
    flRedundantDevMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-REDUNDANCYDEVICES",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMaRemoteDevice": flMaRemoteDevice,
       "flRedundantDev": flRedundantDev,
       "flRedundantDevMIBConformance": flRedundantDevMIBConformance,
       "flRedundantDevMIBCompliances": flRedundantDevMIBCompliances,
       "flRedundantDevMIBCompliance": flRedundantDevMIBCompliance,
       "flRedundantDevMIBGroups": flRedundantDevMIBGroups,
       "flRedundantDeviceGroup": flRedundantDeviceGroup,
       "flRedundantDeviceStatusGroup": flRedundantDeviceStatusGroup,
       "flRedundantDevChannelGroup": flRedundantDevChannelGroup,
       "flRedundantDevice": flRedundantDevice,
       "flRedundantDeviceConfigTable": flRedundantDeviceConfigTable,
       "flRedundantDeviceConfigEntry": flRedundantDeviceConfigEntry,
       "flRedundantDeviceReset": flRedundantDeviceReset,
       "flRedundantDeviceRestoreDefaults": flRedundantDeviceRestoreDefaults,
       "flRedundantDeviceFirmRevision": flRedundantDeviceFirmRevision,
       "flRedundantDeviceRedundancyMode": flRedundantDeviceRedundancyMode,
       "flRedundantTemperature": flRedundantTemperature,
       "flRedundantSerialNumber": flRedundantSerialNumber,
       "flRedundantDeviceStatusTable": flRedundantDeviceStatusTable,
       "flRedundantDeviceStatusEntry": flRedundantDeviceStatusEntry,
       "flRedundantDevActiveFoLink": flRedundantDevActiveFoLink,
       "flRedundantDevActiveTpLink": flRedundantDevActiveTpLink,
       "flRedundantDevStbyFoLink": flRedundantDevStbyFoLink,
       "flRedundantDevStbyTpLink": flRedundantDevStbyTpLink,
       "flRedundantDevMainFoInuse": flRedundantDevMainFoInuse,
       "flRedundantDevMainTpInuse": flRedundantDevMainTpInuse,
       "flRedundantDevBckpFoInuse": flRedundantDevBckpFoInuse,
       "flRedundantDevBckpTpInuse": flRedundantDevBckpTpInuse,
       "flRedundantDevChannel": flRedundantDevChannel,
       "flRedundantDevChannelConfigTable": flRedundantDevChannelConfigTable,
       "flRedundantDevChannelConfigEntry": flRedundantDevChannelConfigEntry,
       "flRedundantDevChannelConfigIndex": flRedundantDevChannelConfigIndex,
       "flRedundantDevUpstreamBw": flRedundantDevUpstreamBw,
       "flRedundantDevEnableTpPort": flRedundantDevEnableTpPort,
       "flRedundantDevPause": flRedundantDevPause,
       "flRedundantDevFo2TpFp": flRedundantDevFo2TpFp,
       "flRedundantDevFoLb": flRedundantDevFoLb,
       "flRedundantDevTpLb": flRedundantDevTpLb,
       "flRedundantDevFo2TpLst": flRedundantDevFo2TpLst,
       "flRedundantDevFoBckp2Main": flRedundantDevFoBckp2Main,
       "flRedundantDevTpBckp2Main": flRedundantDevTpBckp2Main,
       "flRedundantDevForceFo": flRedundantDevForceFo,
       "flRedundantDevForceTp": flRedundantDevForceTp,
       "flRedundantDevBckpFoUnused": flRedundantDevBckpFoUnused,
       "flRedundantDevBckpTpUnused": flRedundantDevBckpTpUnused,
       "flRedundantDevPortDescription": flRedundantDevPortDescription,
       "flRedundantDevTpFailOver": flRedundantDevTpFailOver,
       "flRedundantDevAutoNego": flRedundantDevAutoNego}
)
