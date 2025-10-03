# SNMP MIB module (FIBROLAN-MIB-GBECONVERTERS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-GBECONVERTERS
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:23 2025
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

flGbeConverter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30)
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
_FlGbeConverterMIBConformance_ObjectIdentity = ObjectIdentity
flGbeConverterMIBConformance = _FlGbeConverterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 1)
)
_FlGbeConverterMIBCompliances_ObjectIdentity = ObjectIdentity
flGbeConverterMIBCompliances = _FlGbeConverterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 1, 1)
)
_FlGbeConverterMIBGroups_ObjectIdentity = ObjectIdentity
flGbeConverterMIBGroups = _FlGbeConverterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 1, 2)
)
_FlGbeConverterDevice_ObjectIdentity = ObjectIdentity
flGbeConverterDevice = _FlGbeConverterDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 10)
)
_FlGbeConverterDeviceConfigTable_Object = MibTable
flGbeConverterDeviceConfigTable = _FlGbeConverterDeviceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 10, 1)
)
if mibBuilder.loadTexts:
    flGbeConverterDeviceConfigTable.setStatus("current")
_FlGbeConverterDeviceConfigEntry_Object = MibTableRow
flGbeConverterDeviceConfigEntry = _FlGbeConverterDeviceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 10, 1, 1)
)
flGbeConverterDeviceConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flGbeConverterDeviceConfigEntry.setStatus("current")


class _FlGbeConverterRestoreDefaults_Type(Integer32):
    """Custom type flGbeConverterRestoreDefaults based on Integer32"""
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


_FlGbeConverterRestoreDefaults_Type.__name__ = "Integer32"
_FlGbeConverterRestoreDefaults_Object = MibTableColumn
flGbeConverterRestoreDefaults = _FlGbeConverterRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 10, 1, 1, 2),
    _FlGbeConverterRestoreDefaults_Type()
)
flGbeConverterRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterRestoreDefaults.setStatus("current")
_FlGbeConverterDeviceFirmRevision_Type = DisplayString
_FlGbeConverterDeviceFirmRevision_Object = MibTableColumn
flGbeConverterDeviceFirmRevision = _FlGbeConverterDeviceFirmRevision_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 10, 1, 1, 3),
    _FlGbeConverterDeviceFirmRevision_Type()
)
flGbeConverterDeviceFirmRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterDeviceFirmRevision.setStatus("current")
_FlGbeConverterDeviceTemperature_Type = Integer32
_FlGbeConverterDeviceTemperature_Object = MibTableColumn
flGbeConverterDeviceTemperature = _FlGbeConverterDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 10, 1, 1, 4),
    _FlGbeConverterDeviceTemperature_Type()
)
flGbeConverterDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterDeviceTemperature.setStatus("current")
_FlGbeConverterPorts_ObjectIdentity = ObjectIdentity
flGbeConverterPorts = _FlGbeConverterPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20)
)
_FlGbeConverterPortConfigTable_Object = MibTable
flGbeConverterPortConfigTable = _FlGbeConverterPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1)
)
if mibBuilder.loadTexts:
    flGbeConverterPortConfigTable.setStatus("current")
_FlGbeConverterPortConfigEntry_Object = MibTableRow
flGbeConverterPortConfigEntry = _FlGbeConverterPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1)
)
flGbeConverterPortConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterPortIndex"),
)
if mibBuilder.loadTexts:
    flGbeConverterPortConfigEntry.setStatus("current")
_FlGbeConverterPortIndex_Type = Integer32
_FlGbeConverterPortIndex_Object = MibTableColumn
flGbeConverterPortIndex = _FlGbeConverterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 1),
    _FlGbeConverterPortIndex_Type()
)
flGbeConverterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterPortIndex.setStatus("current")


class _FlGbeConverterP1Link_Type(Integer32):
    """Custom type flGbeConverterP1Link based on Integer32"""
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


_FlGbeConverterP1Link_Type.__name__ = "Integer32"
_FlGbeConverterP1Link_Object = MibTableColumn
flGbeConverterP1Link = _FlGbeConverterP1Link_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 2),
    _FlGbeConverterP1Link_Type()
)
flGbeConverterP1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterP1Link.setStatus("current")


class _FlGbeConverterP2Link_Type(Integer32):
    """Custom type flGbeConverterP2Link based on Integer32"""
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


_FlGbeConverterP2Link_Type.__name__ = "Integer32"
_FlGbeConverterP2Link_Object = MibTableColumn
flGbeConverterP2Link = _FlGbeConverterP2Link_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 3),
    _FlGbeConverterP2Link_Type()
)
flGbeConverterP2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterP2Link.setStatus("current")
_FlGbeConverterPortDescription_Type = DisplayString
_FlGbeConverterPortDescription_Object = MibTableColumn
flGbeConverterPortDescription = _FlGbeConverterPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 4),
    _FlGbeConverterPortDescription_Type()
)
flGbeConverterPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterPortDescription.setStatus("current")


class _FlGbeConverterP1SignalDetect_Type(Integer32):
    """Custom type flGbeConverterP1SignalDetect based on Integer32"""
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


_FlGbeConverterP1SignalDetect_Type.__name__ = "Integer32"
_FlGbeConverterP1SignalDetect_Object = MibTableColumn
flGbeConverterP1SignalDetect = _FlGbeConverterP1SignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 5),
    _FlGbeConverterP1SignalDetect_Type()
)
flGbeConverterP1SignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterP1SignalDetect.setStatus("current")


class _FlGbeConverterP2SignalDetect_Type(Integer32):
    """Custom type flGbeConverterP2SignalDetect based on Integer32"""
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


_FlGbeConverterP2SignalDetect_Type.__name__ = "Integer32"
_FlGbeConverterP2SignalDetect_Object = MibTableColumn
flGbeConverterP2SignalDetect = _FlGbeConverterP2SignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 6),
    _FlGbeConverterP2SignalDetect_Type()
)
flGbeConverterP2SignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterP2SignalDetect.setStatus("current")


class _FlGbeConverterChannelEnable_Type(Integer32):
    """Custom type flGbeConverterChannelEnable based on Integer32"""
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


_FlGbeConverterChannelEnable_Type.__name__ = "Integer32"
_FlGbeConverterChannelEnable_Object = MibTableColumn
flGbeConverterChannelEnable = _FlGbeConverterChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 7),
    _FlGbeConverterChannelEnable_Type()
)
flGbeConverterChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterChannelEnable.setStatus("current")


class _FlGbeConverterP2LoopBack_Type(Integer32):
    """Custom type flGbeConverterP2LoopBack based on Integer32"""
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


_FlGbeConverterP2LoopBack_Type.__name__ = "Integer32"
_FlGbeConverterP2LoopBack_Object = MibTableColumn
flGbeConverterP2LoopBack = _FlGbeConverterP2LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 8),
    _FlGbeConverterP2LoopBack_Type()
)
flGbeConverterP2LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterP2LoopBack.setStatus("current")


class _FlGbeConverterLstP1_P2_Type(Integer32):
    """Custom type flGbeConverterLstP1_P2 based on Integer32"""
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


_FlGbeConverterLstP1_P2_Type.__name__ = "Integer32"
_FlGbeConverterLstP1_P2_Object = MibTableColumn
flGbeConverterLstP1_P2 = _FlGbeConverterLstP1_P2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 9),
    _FlGbeConverterLstP1_P2_Type()
)
flGbeConverterLstP1_P2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterLstP1_P2.setStatus("current")


class _FlGbeConverterLstP2_P1_Type(Integer32):
    """Custom type flGbeConverterLstP2_P1 based on Integer32"""
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


_FlGbeConverterLstP2_P1_Type.__name__ = "Integer32"
_FlGbeConverterLstP2_P1_Object = MibTableColumn
flGbeConverterLstP2_P1 = _FlGbeConverterLstP2_P1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 10),
    _FlGbeConverterLstP2_P1_Type()
)
flGbeConverterLstP2_P1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterLstP2_P1.setStatus("current")


class _FlGbeConverterUpstreamBW_Type(Integer32):
    """Custom type flGbeConverterUpstreamBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FlGbeConverterUpstreamBW_Type.__name__ = "Integer32"
_FlGbeConverterUpstreamBW_Object = MibTableColumn
flGbeConverterUpstreamBW = _FlGbeConverterUpstreamBW_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 11),
    _FlGbeConverterUpstreamBW_Type()
)
flGbeConverterUpstreamBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterUpstreamBW.setStatus("current")


class _FlGbeConverterP1LoopBack_Type(Integer32):
    """Custom type flGbeConverterP1LoopBack based on Integer32"""
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


_FlGbeConverterP1LoopBack_Type.__name__ = "Integer32"
_FlGbeConverterP1LoopBack_Object = MibTableColumn
flGbeConverterP1LoopBack = _FlGbeConverterP1LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 12),
    _FlGbeConverterP1LoopBack_Type()
)
flGbeConverterP1LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterP1LoopBack.setStatus("current")


class _FlGbeConverterP1Type_Type(Integer32):
    """Custom type flGbeConverterP1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tp", 1),
          ("fo", 2),
          ("n-a", 3))
    )


_FlGbeConverterP1Type_Type.__name__ = "Integer32"
_FlGbeConverterP1Type_Object = MibTableColumn
flGbeConverterP1Type = _FlGbeConverterP1Type_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 13),
    _FlGbeConverterP1Type_Type()
)
flGbeConverterP1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterP1Type.setStatus("current")


class _FlGbeConverterP2Type_Type(Integer32):
    """Custom type flGbeConverterP2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tp", 1),
          ("fo", 2),
          ("n-a", 3))
    )


_FlGbeConverterP2Type_Type.__name__ = "Integer32"
_FlGbeConverterP2Type_Object = MibTableColumn
flGbeConverterP2Type = _FlGbeConverterP2Type_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 14),
    _FlGbeConverterP2Type_Type()
)
flGbeConverterP2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterP2Type.setStatus("current")


class _FlGbeConverterPause_Type(Integer32):
    """Custom type flGbeConverterPause based on Integer32"""
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


_FlGbeConverterPause_Type.__name__ = "Integer32"
_FlGbeConverterPause_Object = MibTableColumn
flGbeConverterPause = _FlGbeConverterPause_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 15),
    _FlGbeConverterPause_Type()
)
flGbeConverterPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterPause.setStatus("current")


class _FlGbeConverterAutoNego_Type(Integer32):
    """Custom type flGbeConverterAutoNego based on Integer32"""
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


_FlGbeConverterAutoNego_Type.__name__ = "Integer32"
_FlGbeConverterAutoNego_Object = MibTableColumn
flGbeConverterAutoNego = _FlGbeConverterAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 20, 1, 1, 16),
    _FlGbeConverterAutoNego_Type()
)
flGbeConverterAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterAutoNego.setStatus("current")
_FlGbeConverterStatistics_ObjectIdentity = ObjectIdentity
flGbeConverterStatistics = _FlGbeConverterStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30)
)
_FlGbeConverterStatisticsTable_Object = MibTable
flGbeConverterStatisticsTable = _FlGbeConverterStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1)
)
if mibBuilder.loadTexts:
    flGbeConverterStatisticsTable.setStatus("current")
_FlGbeConverterStatisticsEntry_Object = MibTableRow
flGbeConverterStatisticsEntry = _FlGbeConverterStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1)
)
flGbeConverterStatisticsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
    (0, "FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterPortIndex"),
)
if mibBuilder.loadTexts:
    flGbeConverterStatisticsEntry.setStatus("current")
_FlGbeConverterRxDropEvents_Type = Counter64
_FlGbeConverterRxDropEvents_Object = MibTableColumn
flGbeConverterRxDropEvents = _FlGbeConverterRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 1),
    _FlGbeConverterRxDropEvents_Type()
)
flGbeConverterRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxDropEvents.setStatus("current")
_FlGbeConverterRxOctets_Type = Counter64
_FlGbeConverterRxOctets_Object = MibTableColumn
flGbeConverterRxOctets = _FlGbeConverterRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 2),
    _FlGbeConverterRxOctets_Type()
)
flGbeConverterRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxOctets.setStatus("current")
_FlGbeConverterRxPackets_Type = Counter64
_FlGbeConverterRxPackets_Object = MibTableColumn
flGbeConverterRxPackets = _FlGbeConverterRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 3),
    _FlGbeConverterRxPackets_Type()
)
flGbeConverterRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPackets.setStatus("current")
_FlGbeConverterRxBroadcastPackets_Type = Counter64
_FlGbeConverterRxBroadcastPackets_Object = MibTableColumn
flGbeConverterRxBroadcastPackets = _FlGbeConverterRxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 4),
    _FlGbeConverterRxBroadcastPackets_Type()
)
flGbeConverterRxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxBroadcastPackets.setStatus("current")
_FlGbeConverterRxMulticastPackets_Type = Counter64
_FlGbeConverterRxMulticastPackets_Object = MibTableColumn
flGbeConverterRxMulticastPackets = _FlGbeConverterRxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 5),
    _FlGbeConverterRxMulticastPackets_Type()
)
flGbeConverterRxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxMulticastPackets.setStatus("current")
_FlGbeConverterRxCrcAlignmentErrors_Type = Counter64
_FlGbeConverterRxCrcAlignmentErrors_Object = MibTableColumn
flGbeConverterRxCrcAlignmentErrors = _FlGbeConverterRxCrcAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 6),
    _FlGbeConverterRxCrcAlignmentErrors_Type()
)
flGbeConverterRxCrcAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxCrcAlignmentErrors.setStatus("current")
_FlGbeConverterRxUndersizePackets_Type = Counter64
_FlGbeConverterRxUndersizePackets_Object = MibTableColumn
flGbeConverterRxUndersizePackets = _FlGbeConverterRxUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 7),
    _FlGbeConverterRxUndersizePackets_Type()
)
flGbeConverterRxUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxUndersizePackets.setStatus("current")
_FlGbeConverterRxOversizePackets_Type = Counter64
_FlGbeConverterRxOversizePackets_Object = MibTableColumn
flGbeConverterRxOversizePackets = _FlGbeConverterRxOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 8),
    _FlGbeConverterRxOversizePackets_Type()
)
flGbeConverterRxOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxOversizePackets.setStatus("current")
_FlGbeConverterRxFragments_Type = Counter64
_FlGbeConverterRxFragments_Object = MibTableColumn
flGbeConverterRxFragments = _FlGbeConverterRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 9),
    _FlGbeConverterRxFragments_Type()
)
flGbeConverterRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxFragments.setStatus("current")
_FlGbeConverterRxJabbers_Type = Counter64
_FlGbeConverterRxJabbers_Object = MibTableColumn
flGbeConverterRxJabbers = _FlGbeConverterRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 10),
    _FlGbeConverterRxJabbers_Type()
)
flGbeConverterRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxJabbers.setStatus("current")
_FlGbeConverterRxCollisions_Type = Counter64
_FlGbeConverterRxCollisions_Object = MibTableColumn
flGbeConverterRxCollisions = _FlGbeConverterRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 11),
    _FlGbeConverterRxCollisions_Type()
)
flGbeConverterRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxCollisions.setStatus("current")
_FlGbeConverterRxPackets64Octets_Type = Counter64
_FlGbeConverterRxPackets64Octets_Object = MibTableColumn
flGbeConverterRxPackets64Octets = _FlGbeConverterRxPackets64Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 12),
    _FlGbeConverterRxPackets64Octets_Type()
)
flGbeConverterRxPackets64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPackets64Octets.setStatus("current")
_FlGbeConverterRxPackets65to127Octets_Type = Counter64
_FlGbeConverterRxPackets65to127Octets_Object = MibTableColumn
flGbeConverterRxPackets65to127Octets = _FlGbeConverterRxPackets65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 13),
    _FlGbeConverterRxPackets65to127Octets_Type()
)
flGbeConverterRxPackets65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPackets65to127Octets.setStatus("current")
_FlGbeConverterRxPackets128to255Octets_Type = Counter64
_FlGbeConverterRxPackets128to255Octets_Object = MibTableColumn
flGbeConverterRxPackets128to255Octets = _FlGbeConverterRxPackets128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 14),
    _FlGbeConverterRxPackets128to255Octets_Type()
)
flGbeConverterRxPackets128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPackets128to255Octets.setStatus("current")
_FlGbeConverterRxPackets256to511Octets_Type = Counter64
_FlGbeConverterRxPackets256to511Octets_Object = MibTableColumn
flGbeConverterRxPackets256to511Octets = _FlGbeConverterRxPackets256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 15),
    _FlGbeConverterRxPackets256to511Octets_Type()
)
flGbeConverterRxPackets256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPackets256to511Octets.setStatus("current")
_FlGbeConverterRxPackets512to1023Octets_Type = Counter64
_FlGbeConverterRxPackets512to1023Octets_Object = MibTableColumn
flGbeConverterRxPackets512to1023Octets = _FlGbeConverterRxPackets512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 16),
    _FlGbeConverterRxPackets512to1023Octets_Type()
)
flGbeConverterRxPackets512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPackets512to1023Octets.setStatus("current")
_FlGbeConverterRxPackets1024toMaxOctets_Type = Counter64
_FlGbeConverterRxPackets1024toMaxOctets_Object = MibTableColumn
flGbeConverterRxPackets1024toMaxOctets = _FlGbeConverterRxPackets1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 17),
    _FlGbeConverterRxPackets1024toMaxOctets_Type()
)
flGbeConverterRxPackets1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPackets1024toMaxOctets.setStatus("current")
_FlGbeConverterRxFibroLANProprietryFrames_Type = Counter64
_FlGbeConverterRxFibroLANProprietryFrames_Object = MibTableColumn
flGbeConverterRxFibroLANProprietryFrames = _FlGbeConverterRxFibroLANProprietryFrames_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 18),
    _FlGbeConverterRxFibroLANProprietryFrames_Type()
)
flGbeConverterRxFibroLANProprietryFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxFibroLANProprietryFrames.setStatus("current")


class _FlGbeConverterClearCounters_Type(Integer32):
    """Custom type flGbeConverterClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlGbeConverterClearCounters_Type.__name__ = "Integer32"
_FlGbeConverterClearCounters_Object = MibTableColumn
flGbeConverterClearCounters = _FlGbeConverterClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 19),
    _FlGbeConverterClearCounters_Type()
)
flGbeConverterClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flGbeConverterClearCounters.setStatus("current")
_FlGbeConverterRxOctetsRate_Type = Counter64
_FlGbeConverterRxOctetsRate_Object = MibTableColumn
flGbeConverterRxOctetsRate = _FlGbeConverterRxOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 20),
    _FlGbeConverterRxOctetsRate_Type()
)
flGbeConverterRxOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxOctetsRate.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterRxOctetsRate.setUnits("bytes/sec")
_FlGbeConverterRxBitsRate_Type = Counter64
_FlGbeConverterRxBitsRate_Object = MibTableColumn
flGbeConverterRxBitsRate = _FlGbeConverterRxBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 21),
    _FlGbeConverterRxBitsRate_Type()
)
flGbeConverterRxBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxBitsRate.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterRxBitsRate.setUnits("bits/sec")
_FlGbeConverterRxPacketsRate_Type = Counter64
_FlGbeConverterRxPacketsRate_Object = MibTableColumn
flGbeConverterRxPacketsRate = _FlGbeConverterRxPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 22),
    _FlGbeConverterRxPacketsRate_Type()
)
flGbeConverterRxPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterRxPacketsRate.setUnits("frames/sec")
_FlGbeConverterRxUtilization_Type = DisplayString
_FlGbeConverterRxUtilization_Object = MibTableColumn
flGbeConverterRxUtilization = _FlGbeConverterRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 23),
    _FlGbeConverterRxUtilization_Type()
)
flGbeConverterRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterRxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterRxUtilization.setUnits("%")
_FlGbeConverterTxOctets_Type = Counter64
_FlGbeConverterTxOctets_Object = MibTableColumn
flGbeConverterTxOctets = _FlGbeConverterTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 24),
    _FlGbeConverterTxOctets_Type()
)
flGbeConverterTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxOctets.setStatus("current")
_FlGbeConverterTxPackets_Type = Counter64
_FlGbeConverterTxPackets_Object = MibTableColumn
flGbeConverterTxPackets = _FlGbeConverterTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 25),
    _FlGbeConverterTxPackets_Type()
)
flGbeConverterTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxPackets.setStatus("current")
_FlGbeConverterTxBroadcastPackets_Type = Counter64
_FlGbeConverterTxBroadcastPackets_Object = MibTableColumn
flGbeConverterTxBroadcastPackets = _FlGbeConverterTxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 26),
    _FlGbeConverterTxBroadcastPackets_Type()
)
flGbeConverterTxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxBroadcastPackets.setStatus("current")
_FlGbeConverterTxMulticastPackets_Type = Counter64
_FlGbeConverterTxMulticastPackets_Object = MibTableColumn
flGbeConverterTxMulticastPackets = _FlGbeConverterTxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 27),
    _FlGbeConverterTxMulticastPackets_Type()
)
flGbeConverterTxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxMulticastPackets.setStatus("current")
_FlGbeConverterTxFibroLANProprietryFrames_Type = Counter64
_FlGbeConverterTxFibroLANProprietryFrames_Object = MibTableColumn
flGbeConverterTxFibroLANProprietryFrames = _FlGbeConverterTxFibroLANProprietryFrames_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 28),
    _FlGbeConverterTxFibroLANProprietryFrames_Type()
)
flGbeConverterTxFibroLANProprietryFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxFibroLANProprietryFrames.setStatus("current")
_FlGbeConverterTxOctetsRate_Type = Counter64
_FlGbeConverterTxOctetsRate_Object = MibTableColumn
flGbeConverterTxOctetsRate = _FlGbeConverterTxOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 29),
    _FlGbeConverterTxOctetsRate_Type()
)
flGbeConverterTxOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxOctetsRate.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterTxOctetsRate.setUnits("bytes/sec")
_FlGbeConverterTxBitsRate_Type = Counter64
_FlGbeConverterTxBitsRate_Object = MibTableColumn
flGbeConverterTxBitsRate = _FlGbeConverterTxBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 30),
    _FlGbeConverterTxBitsRate_Type()
)
flGbeConverterTxBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxBitsRate.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterTxBitsRate.setUnits("bits/sec")
_FlGbeConverterTxPacketsRate_Type = Counter64
_FlGbeConverterTxPacketsRate_Object = MibTableColumn
flGbeConverterTxPacketsRate = _FlGbeConverterTxPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 31),
    _FlGbeConverterTxPacketsRate_Type()
)
flGbeConverterTxPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterTxPacketsRate.setUnits("frames/sec")
_FlGbeConverterTxUtilization_Type = DisplayString
_FlGbeConverterTxUtilization_Object = MibTableColumn
flGbeConverterTxUtilization = _FlGbeConverterTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 30, 1, 1, 32),
    _FlGbeConverterTxUtilization_Type()
)
flGbeConverterTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGbeConverterTxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    flGbeConverterTxUtilization.setUnits("%")

# Managed Objects groups

flGbeConverterDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 1, 2, 1)
)
flGbeConverterDeviceGroup.setObjects(
      *(("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRestoreDefaults"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterDeviceFirmRevision"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterDeviceTemperature"))
)
if mibBuilder.loadTexts:
    flGbeConverterDeviceGroup.setStatus("current")

flGbeConverterPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 1, 2, 2)
)
flGbeConverterPortsGroup.setObjects(
      *(("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterPortIndex"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP1Link"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP2Link"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterPortDescription"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP1SignalDetect"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP2SignalDetect"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterChannelEnable"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP2LoopBack"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterLstP1-P2"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterLstP2-P1"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterUpstreamBW"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP1LoopBack"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP1Type"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterP2Type"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterPause"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterAutoNego"))
)
if mibBuilder.loadTexts:
    flGbeConverterPortsGroup.setStatus("current")

flGbeConverterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 1, 2, 3)
)
flGbeConverterStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxDropEvents"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxOctets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxBroadcastPackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxMulticastPackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxCrcAlignmentErrors"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxUndersizePackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxOversizePackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxFragments"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxJabbers"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxCollisions"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPackets64Octets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPackets65to127Octets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPackets128to255Octets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPackets256to511Octets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPackets512to1023Octets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPackets1024toMaxOctets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxFibroLANProprietryFrames"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterClearCounters"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxOctetsRate"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxBitsRate"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxPacketsRate"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterRxUtilization"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxOctets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxPackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxBroadcastPackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxMulticastPackets"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxFibroLANProprietryFrames"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxOctetsRate"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxBitsRate"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxPacketsRate"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterTxUtilization"))
)
if mibBuilder.loadTexts:
    flGbeConverterStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flGbeConverterMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 50, 30, 1, 1, 1)
)
flGbeConverterMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterDeviceGroup"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterPortsGroup"),
        ("FIBROLAN-MIB-GBECONVERTERS", "flGbeConverterStatisticsGroup"))
)
if mibBuilder.loadTexts:
    flGbeConverterMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-GBECONVERTERS",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMaRemoteDevice": flMaRemoteDevice,
       "flGbeConverter": flGbeConverter,
       "flGbeConverterMIBConformance": flGbeConverterMIBConformance,
       "flGbeConverterMIBCompliances": flGbeConverterMIBCompliances,
       "flGbeConverterMIBCompliance": flGbeConverterMIBCompliance,
       "flGbeConverterMIBGroups": flGbeConverterMIBGroups,
       "flGbeConverterDeviceGroup": flGbeConverterDeviceGroup,
       "flGbeConverterPortsGroup": flGbeConverterPortsGroup,
       "flGbeConverterStatisticsGroup": flGbeConverterStatisticsGroup,
       "flGbeConverterDevice": flGbeConverterDevice,
       "flGbeConverterDeviceConfigTable": flGbeConverterDeviceConfigTable,
       "flGbeConverterDeviceConfigEntry": flGbeConverterDeviceConfigEntry,
       "flGbeConverterRestoreDefaults": flGbeConverterRestoreDefaults,
       "flGbeConverterDeviceFirmRevision": flGbeConverterDeviceFirmRevision,
       "flGbeConverterDeviceTemperature": flGbeConverterDeviceTemperature,
       "flGbeConverterPorts": flGbeConverterPorts,
       "flGbeConverterPortConfigTable": flGbeConverterPortConfigTable,
       "flGbeConverterPortConfigEntry": flGbeConverterPortConfigEntry,
       "flGbeConverterPortIndex": flGbeConverterPortIndex,
       "flGbeConverterP1Link": flGbeConverterP1Link,
       "flGbeConverterP2Link": flGbeConverterP2Link,
       "flGbeConverterPortDescription": flGbeConverterPortDescription,
       "flGbeConverterP1SignalDetect": flGbeConverterP1SignalDetect,
       "flGbeConverterP2SignalDetect": flGbeConverterP2SignalDetect,
       "flGbeConverterChannelEnable": flGbeConverterChannelEnable,
       "flGbeConverterP2LoopBack": flGbeConverterP2LoopBack,
       "flGbeConverterLstP1-P2": flGbeConverterLstP1_P2,
       "flGbeConverterLstP2-P1": flGbeConverterLstP2_P1,
       "flGbeConverterUpstreamBW": flGbeConverterUpstreamBW,
       "flGbeConverterP1LoopBack": flGbeConverterP1LoopBack,
       "flGbeConverterP1Type": flGbeConverterP1Type,
       "flGbeConverterP2Type": flGbeConverterP2Type,
       "flGbeConverterPause": flGbeConverterPause,
       "flGbeConverterAutoNego": flGbeConverterAutoNego,
       "flGbeConverterStatistics": flGbeConverterStatistics,
       "flGbeConverterStatisticsTable": flGbeConverterStatisticsTable,
       "flGbeConverterStatisticsEntry": flGbeConverterStatisticsEntry,
       "flGbeConverterRxDropEvents": flGbeConverterRxDropEvents,
       "flGbeConverterRxOctets": flGbeConverterRxOctets,
       "flGbeConverterRxPackets": flGbeConverterRxPackets,
       "flGbeConverterRxBroadcastPackets": flGbeConverterRxBroadcastPackets,
       "flGbeConverterRxMulticastPackets": flGbeConverterRxMulticastPackets,
       "flGbeConverterRxCrcAlignmentErrors": flGbeConverterRxCrcAlignmentErrors,
       "flGbeConverterRxUndersizePackets": flGbeConverterRxUndersizePackets,
       "flGbeConverterRxOversizePackets": flGbeConverterRxOversizePackets,
       "flGbeConverterRxFragments": flGbeConverterRxFragments,
       "flGbeConverterRxJabbers": flGbeConverterRxJabbers,
       "flGbeConverterRxCollisions": flGbeConverterRxCollisions,
       "flGbeConverterRxPackets64Octets": flGbeConverterRxPackets64Octets,
       "flGbeConverterRxPackets65to127Octets": flGbeConverterRxPackets65to127Octets,
       "flGbeConverterRxPackets128to255Octets": flGbeConverterRxPackets128to255Octets,
       "flGbeConverterRxPackets256to511Octets": flGbeConverterRxPackets256to511Octets,
       "flGbeConverterRxPackets512to1023Octets": flGbeConverterRxPackets512to1023Octets,
       "flGbeConverterRxPackets1024toMaxOctets": flGbeConverterRxPackets1024toMaxOctets,
       "flGbeConverterRxFibroLANProprietryFrames": flGbeConverterRxFibroLANProprietryFrames,
       "flGbeConverterClearCounters": flGbeConverterClearCounters,
       "flGbeConverterRxOctetsRate": flGbeConverterRxOctetsRate,
       "flGbeConverterRxBitsRate": flGbeConverterRxBitsRate,
       "flGbeConverterRxPacketsRate": flGbeConverterRxPacketsRate,
       "flGbeConverterRxUtilization": flGbeConverterRxUtilization,
       "flGbeConverterTxOctets": flGbeConverterTxOctets,
       "flGbeConverterTxPackets": flGbeConverterTxPackets,
       "flGbeConverterTxBroadcastPackets": flGbeConverterTxBroadcastPackets,
       "flGbeConverterTxMulticastPackets": flGbeConverterTxMulticastPackets,
       "flGbeConverterTxFibroLANProprietryFrames": flGbeConverterTxFibroLANProprietryFrames,
       "flGbeConverterTxOctetsRate": flGbeConverterTxOctetsRate,
       "flGbeConverterTxBitsRate": flGbeConverterTxBitsRate,
       "flGbeConverterTxPacketsRate": flGbeConverterTxPacketsRate,
       "flGbeConverterTxUtilization": flGbeConverterTxUtilization}
)
