# SNMP MIB module (MWR-RADIO-MC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\MWR-RADIO-MC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:34 2025
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

(mwr,) = mibBuilder.importSymbols(
    "DWI-HARMONY-PRIVATE-MIB",
    "mwr")

(EnableType,
 equipmentAlarmActiveConditionId,
 equipmentOutTrapsCounter,
 equipmentTrapInfo) = mibBuilder.importSymbols(
    "EQUIPMENT-COMMON-MIB",
    "EnableType",
    "equipmentAlarmActiveConditionId",
    "equipmentOutTrapsCounter",
    "equipmentTrapInfo")

(RadioInstanceType,
 mwrEventConfigSeverity) = mibBuilder.importSymbols(
    "MWR-ETHERNET-MIB",
    "RadioInstanceType",
    "mwrEventConfigSeverity")

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


# MODULE-IDENTITY

mwrRadioMcModIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 1003)
)
if mibBuilder.loadTexts:
    mwrRadioMcModIdentity.setRevisions(
        ("2014-06-23 11:09",
         "2014-09-23 17:22")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwrRadio_ObjectIdentity = ObjectIdentity
mwrRadio = _MwrRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12)
)
_MwrEmcRadioConfigurations_ObjectIdentity = ObjectIdentity
mwrEmcRadioConfigurations = _MwrEmcRadioConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201)
)
_MwrEmcRadioConfigurationsTable_Object = MibTable
mwrEmcRadioConfigurationsTable = _MwrEmcRadioConfigurationsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1)
)
if mibBuilder.loadTexts:
    mwrEmcRadioConfigurationsTable.setStatus("current")
_MwrEmcRadioConfigurationsEntry_Object = MibTableRow
mwrEmcRadioConfigurationsEntry = _MwrEmcRadioConfigurationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1, 1)
)
mwrEmcRadioConfigurationsEntry.setIndexNames(
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioConfigIndex"),
)
if mibBuilder.loadTexts:
    mwrEmcRadioConfigurationsEntry.setStatus("current")
_MwrEmcRadioConfigIndex_Type = RadioInstanceType
_MwrEmcRadioConfigIndex_Object = MibTableColumn
mwrEmcRadioConfigIndex = _MwrEmcRadioConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1, 1, 1),
    _MwrEmcRadioConfigIndex_Type()
)
mwrEmcRadioConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEmcRadioConfigIndex.setStatus("current")
_MwrEmcRadioTxState_Type = EnableType
_MwrEmcRadioTxState_Object = MibTableColumn
mwrEmcRadioTxState = _MwrEmcRadioTxState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1, 1, 2),
    _MwrEmcRadioTxState_Type()
)
mwrEmcRadioTxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioTxState.setStatus("current")
_MwrEmcRadioTxPower_Type = Integer32
_MwrEmcRadioTxPower_Object = MibTableColumn
mwrEmcRadioTxPower = _MwrEmcRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1, 1, 3),
    _MwrEmcRadioTxPower_Type()
)
mwrEmcRadioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioTxPower.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTxPower.setUnits("dB")
_MwrEmcRadioTxDownTime_Type = Integer32
_MwrEmcRadioTxDownTime_Object = MibTableColumn
mwrEmcRadioTxDownTime = _MwrEmcRadioTxDownTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1, 1, 4),
    _MwrEmcRadioTxDownTime_Type()
)
mwrEmcRadioTxDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioTxDownTime.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTxDownTime.setUnits("sec")
_MwrEmcRadioRxFrequency_Type = Integer32
_MwrEmcRadioRxFrequency_Object = MibTableColumn
mwrEmcRadioRxFrequency = _MwrEmcRadioRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1, 1, 5),
    _MwrEmcRadioRxFrequency_Type()
)
mwrEmcRadioRxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioRxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioRxFrequency.setUnits("kHz")
_MwrEmcRadioTxFrequency_Type = Integer32
_MwrEmcRadioTxFrequency_Object = MibTableColumn
mwrEmcRadioTxFrequency = _MwrEmcRadioTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 1, 1, 6),
    _MwrEmcRadioTxFrequency_Type()
)
mwrEmcRadioTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFrequency.setUnits("kHz")
_MwrEmcRadioProfileTable_Object = MibTable
mwrEmcRadioProfileTable = _MwrEmcRadioProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 2)
)
if mibBuilder.loadTexts:
    mwrEmcRadioProfileTable.setStatus("current")
_MwrEmcRadioProfileEntry_Object = MibTableRow
mwrEmcRadioProfileEntry = _MwrEmcRadioProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 2, 1)
)
mwrEmcRadioProfileEntry.setIndexNames(
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioStandardMode"),
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioChannelBw"),
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioStaticTxProfile"),
)
if mibBuilder.loadTexts:
    mwrEmcRadioProfileEntry.setStatus("current")
_MwrEmcRadioStandardMode_Type = DisplayString
_MwrEmcRadioStandardMode_Object = MibTableColumn
mwrEmcRadioStandardMode = _MwrEmcRadioStandardMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 2, 1, 1),
    _MwrEmcRadioStandardMode_Type()
)
mwrEmcRadioStandardMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEmcRadioStandardMode.setStatus("current")
_MwrEmcRadioChannelBw_Type = DisplayString
_MwrEmcRadioChannelBw_Object = MibTableColumn
mwrEmcRadioChannelBw = _MwrEmcRadioChannelBw_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 2, 1, 2),
    _MwrEmcRadioChannelBw_Type()
)
mwrEmcRadioChannelBw.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEmcRadioChannelBw.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioChannelBw.setUnits("MHz")
_MwrEmcRadioStaticTxProfile_Type = DisplayString
_MwrEmcRadioStaticTxProfile_Object = MibTableColumn
mwrEmcRadioStaticTxProfile = _MwrEmcRadioStaticTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 2, 1, 3),
    _MwrEmcRadioStaticTxProfile_Type()
)
mwrEmcRadioStaticTxProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEmcRadioStaticTxProfile.setStatus("current")
_MwrEmcRadioProgrammedProfile_Type = EnableType
_MwrEmcRadioProgrammedProfile_Object = MibTableColumn
mwrEmcRadioProgrammedProfile = _MwrEmcRadioProgrammedProfile_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 2, 1, 4),
    _MwrEmcRadioProgrammedProfile_Type()
)
mwrEmcRadioProgrammedProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioProgrammedProfile.setStatus("current")
_MwrEmcRadioThresholdAlarmTable_Object = MibTable
mwrEmcRadioThresholdAlarmTable = _MwrEmcRadioThresholdAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 3)
)
if mibBuilder.loadTexts:
    mwrEmcRadioThresholdAlarmTable.setStatus("current")
_MwrEmcRadioThresholdAlarmEntry_Object = MibTableRow
mwrEmcRadioThresholdAlarmEntry = _MwrEmcRadioThresholdAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 3, 1)
)
mwrEmcRadioThresholdAlarmEntry.setIndexNames(
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioThresholdIndex"),
)
if mibBuilder.loadTexts:
    mwrEmcRadioThresholdAlarmEntry.setStatus("current")
_MwrEmcRadioThresholdIndex_Type = RadioInstanceType
_MwrEmcRadioThresholdIndex_Object = MibTableColumn
mwrEmcRadioThresholdIndex = _MwrEmcRadioThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 3, 1, 1),
    _MwrEmcRadioThresholdIndex_Type()
)
mwrEmcRadioThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEmcRadioThresholdIndex.setStatus("current")
_MwrEmcRadioRslBelowThresholdParams_Type = DisplayString
_MwrEmcRadioRslBelowThresholdParams_Object = MibTableColumn
mwrEmcRadioRslBelowThresholdParams = _MwrEmcRadioRslBelowThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 3, 1, 2),
    _MwrEmcRadioRslBelowThresholdParams_Type()
)
mwrEmcRadioRslBelowThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioRslBelowThresholdParams.setStatus("current")
_MwrEmcRadioTxAboveThresholdParams_Type = DisplayString
_MwrEmcRadioTxAboveThresholdParams_Object = MibTableColumn
mwrEmcRadioTxAboveThresholdParams = _MwrEmcRadioTxAboveThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 3, 1, 3),
    _MwrEmcRadioTxAboveThresholdParams_Type()
)
mwrEmcRadioTxAboveThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioTxAboveThresholdParams.setStatus("current")
_MwrEmcRadioChCfgSynchEnable_Type = EnableType
_MwrEmcRadioChCfgSynchEnable_Object = MibScalar
mwrEmcRadioChCfgSynchEnable = _MwrEmcRadioChCfgSynchEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 201, 4),
    _MwrEmcRadioChCfgSynchEnable_Type()
)
mwrEmcRadioChCfgSynchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwrEmcRadioChCfgSynchEnable.setStatus("current")
_MwrEmcRadioStatus_ObjectIdentity = ObjectIdentity
mwrEmcRadioStatus = _MwrEmcRadioStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202)
)
_MwrEmcRadioStatusTable_Object = MibTable
mwrEmcRadioStatusTable = _MwrEmcRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1)
)
if mibBuilder.loadTexts:
    mwrEmcRadioStatusTable.setStatus("current")
_MwrEmcRadioStatusEntry_Object = MibTableRow
mwrEmcRadioStatusEntry = _MwrEmcRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1)
)
mwrEmcRadioStatusEntry.setIndexNames(
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioStatusIndex"),
)
if mibBuilder.loadTexts:
    mwrEmcRadioStatusEntry.setStatus("current")
_MwrEmcRadioStatusIndex_Type = RadioInstanceType
_MwrEmcRadioStatusIndex_Object = MibTableColumn
mwrEmcRadioStatusIndex = _MwrEmcRadioStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 1),
    _MwrEmcRadioStatusIndex_Type()
)
mwrEmcRadioStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioStatusIndex.setStatus("current")


class _MwrEmcRadioOperStatus_Type(Integer32):
    """Custom type mwrEmcRadioOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MwrEmcRadioOperStatus_Type.__name__ = "Integer32"
_MwrEmcRadioOperStatus_Object = MibTableColumn
mwrEmcRadioOperStatus = _MwrEmcRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 2),
    _MwrEmcRadioOperStatus_Type()
)
mwrEmcRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioOperStatus.setStatus("current")
_MwrEmcRadioTRSpacing_Type = Integer32
_MwrEmcRadioTRSpacing_Object = MibTableColumn
mwrEmcRadioTRSpacing = _MwrEmcRadioTRSpacing_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 3),
    _MwrEmcRadioTRSpacing_Type()
)
mwrEmcRadioTRSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioTRSpacing.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTRSpacing.setUnits("kHz")
_MwrEmcRadioActualTxStatus_Type = EnableType
_MwrEmcRadioActualTxStatus_Object = MibTableColumn
mwrEmcRadioActualTxStatus = _MwrEmcRadioActualTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 4),
    _MwrEmcRadioActualTxStatus_Type()
)
mwrEmcRadioActualTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioActualTxStatus.setStatus("current")
_MwrEmcRadioRxFreqMin_Type = Integer32
_MwrEmcRadioRxFreqMin_Object = MibTableColumn
mwrEmcRadioRxFreqMin = _MwrEmcRadioRxFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 5),
    _MwrEmcRadioRxFreqMin_Type()
)
mwrEmcRadioRxFreqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioRxFreqMin.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioRxFreqMin.setUnits("kHz")
_MwrEmcRadioRxFreqMax_Type = Integer32
_MwrEmcRadioRxFreqMax_Object = MibTableColumn
mwrEmcRadioRxFreqMax = _MwrEmcRadioRxFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 6),
    _MwrEmcRadioRxFreqMax_Type()
)
mwrEmcRadioRxFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioRxFreqMax.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioRxFreqMax.setUnits("kHz")
_MwrEmcRadioTxFreqMin_Type = Integer32
_MwrEmcRadioTxFreqMin_Object = MibTableColumn
mwrEmcRadioTxFreqMin = _MwrEmcRadioTxFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 7),
    _MwrEmcRadioTxFreqMin_Type()
)
mwrEmcRadioTxFreqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFreqMin.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFreqMin.setUnits("kHz")
_MwrEmcRadioTxFreqMax_Type = Integer32
_MwrEmcRadioTxFreqMax_Object = MibTableColumn
mwrEmcRadioTxFreqMax = _MwrEmcRadioTxFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 8),
    _MwrEmcRadioTxFreqMax_Type()
)
mwrEmcRadioTxFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFreqMax.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFreqMax.setUnits("kHz")
_MwrEmcRadioTxPowerMin_Type = Integer32
_MwrEmcRadioTxPowerMin_Object = MibTableColumn
mwrEmcRadioTxPowerMin = _MwrEmcRadioTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 9),
    _MwrEmcRadioTxPowerMin_Type()
)
mwrEmcRadioTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTxPowerMin.setUnits("dB")
_MwrEmcRadioTxPowerMax_Type = Integer32
_MwrEmcRadioTxPowerMax_Object = MibTableColumn
mwrEmcRadioTxPowerMax = _MwrEmcRadioTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 10),
    _MwrEmcRadioTxPowerMax_Type()
)
mwrEmcRadioTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioTxPowerMax.setUnits("dB")


class _MwrEmcRadioLinkStatus_Type(Integer32):
    """Custom type mwrEmcRadioLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MwrEmcRadioLinkStatus_Type.__name__ = "Integer32"
_MwrEmcRadioLinkStatus_Object = MibTableColumn
mwrEmcRadioLinkStatus = _MwrEmcRadioLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 202, 1, 1, 11),
    _MwrEmcRadioLinkStatus_Type()
)
mwrEmcRadioLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioLinkStatus.setStatus("current")
_MwrEmcRadioPerformance_ObjectIdentity = ObjectIdentity
mwrEmcRadioPerformance = _MwrEmcRadioPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203)
)
_MwrEmcRadioPerfStatsTable_Object = MibTable
mwrEmcRadioPerfStatsTable = _MwrEmcRadioPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1)
)
if mibBuilder.loadTexts:
    mwrEmcRadioPerfStatsTable.setStatus("current")
_MwrEmcRadioPerfStatsEntry_Object = MibTableRow
mwrEmcRadioPerfStatsEntry = _MwrEmcRadioPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1)
)
mwrEmcRadioPerfStatsEntry.setIndexNames(
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioStatsIndex"),
)
if mibBuilder.loadTexts:
    mwrEmcRadioPerfStatsEntry.setStatus("current")
_MwrEmcRadioStatsIndex_Type = RadioInstanceType
_MwrEmcRadioStatsIndex_Object = MibTableColumn
mwrEmcRadioStatsIndex = _MwrEmcRadioStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 1),
    _MwrEmcRadioStatsIndex_Type()
)
mwrEmcRadioStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEmcRadioStatsIndex.setStatus("current")
_MwrEmcRadioTxFrames_Type = Counter64
_MwrEmcRadioTxFrames_Object = MibTableColumn
mwrEmcRadioTxFrames = _MwrEmcRadioTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 2),
    _MwrEmcRadioTxFrames_Type()
)
mwrEmcRadioTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFrames.setStatus("current")
_MwrEmcRadioRxGoodFrames_Type = Counter64
_MwrEmcRadioRxGoodFrames_Object = MibTableColumn
mwrEmcRadioRxGoodFrames = _MwrEmcRadioRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 3),
    _MwrEmcRadioRxGoodFrames_Type()
)
mwrEmcRadioRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioRxGoodFrames.setStatus("current")
_MwrEmcRadioRxErrsFrames_Type = Counter64
_MwrEmcRadioRxErrsFrames_Object = MibTableColumn
mwrEmcRadioRxErrsFrames = _MwrEmcRadioRxErrsFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 4),
    _MwrEmcRadioRxErrsFrames_Type()
)
mwrEmcRadioRxErrsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioRxErrsFrames.setStatus("current")
_MwrEmcRadioRSL_Type = Integer32
_MwrEmcRadioRSL_Object = MibTableColumn
mwrEmcRadioRSL = _MwrEmcRadioRSL_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 5),
    _MwrEmcRadioRSL_Type()
)
mwrEmcRadioRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioRSL.setStatus("current")
_MwrEmcRadioEqualizerStress_Type = Integer32
_MwrEmcRadioEqualizerStress_Object = MibTableColumn
mwrEmcRadioEqualizerStress = _MwrEmcRadioEqualizerStress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 6),
    _MwrEmcRadioEqualizerStress_Type()
)
mwrEmcRadioEqualizerStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioEqualizerStress.setStatus("current")
_MwrEmcRadioSNR_Type = Integer32
_MwrEmcRadioSNR_Object = MibTableColumn
mwrEmcRadioSNR = _MwrEmcRadioSNR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 7),
    _MwrEmcRadioSNR_Type()
)
mwrEmcRadioSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioSNR.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioSNR.setUnits("dB")
_MwrEmcRadioLinkAvailability_Type = Counter32
_MwrEmcRadioLinkAvailability_Object = MibTableColumn
mwrEmcRadioLinkAvailability = _MwrEmcRadioLinkAvailability_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 8),
    _MwrEmcRadioLinkAvailability_Type()
)
mwrEmcRadioLinkAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioLinkAvailability.setStatus("current")
if mibBuilder.loadTexts:
    mwrEmcRadioLinkAvailability.setUnits("sec")
_MwrEmcRadioActualTxPower_Type = Integer32
_MwrEmcRadioActualTxPower_Object = MibTableColumn
mwrEmcRadioActualTxPower = _MwrEmcRadioActualTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 9),
    _MwrEmcRadioActualTxPower_Type()
)
mwrEmcRadioActualTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioActualTxPower.setStatus("current")
_MwrEmcRadioActualTxProfile_Type = DisplayString
_MwrEmcRadioActualTxProfile_Object = MibTableColumn
mwrEmcRadioActualTxProfile = _MwrEmcRadioActualTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 1, 1, 10),
    _MwrEmcRadioActualTxProfile_Type()
)
mwrEmcRadioActualTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioActualTxProfile.setStatus("current")
_MwrEmcRadioPerfStats32BitTable_Object = MibTable
mwrEmcRadioPerfStats32BitTable = _MwrEmcRadioPerfStats32BitTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 2)
)
if mibBuilder.loadTexts:
    mwrEmcRadioPerfStats32BitTable.setStatus("current")
_MwrEmcRadioPerfStats32BitEntry_Object = MibTableRow
mwrEmcRadioPerfStats32BitEntry = _MwrEmcRadioPerfStats32BitEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 2, 1)
)
mwrEmcRadioPerfStats32BitEntry.setIndexNames(
    (0, "MWR-RADIO-MC-MIB", "mwrEmcRadioStats32BitIndex"),
)
if mibBuilder.loadTexts:
    mwrEmcRadioPerfStats32BitEntry.setStatus("current")
_MwrEmcRadioStats32BitIndex_Type = RadioInstanceType
_MwrEmcRadioStats32BitIndex_Object = MibTableColumn
mwrEmcRadioStats32BitIndex = _MwrEmcRadioStats32BitIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 2, 1, 1),
    _MwrEmcRadioStats32BitIndex_Type()
)
mwrEmcRadioStats32BitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwrEmcRadioStats32BitIndex.setStatus("current")
_MwrEmcRadioTxFrames32Bit_Type = Counter32
_MwrEmcRadioTxFrames32Bit_Object = MibTableColumn
mwrEmcRadioTxFrames32Bit = _MwrEmcRadioTxFrames32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 2, 1, 2),
    _MwrEmcRadioTxFrames32Bit_Type()
)
mwrEmcRadioTxFrames32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioTxFrames32Bit.setStatus("current")
_MwrEmcRadioRxGoodFrames32Bit_Type = Counter32
_MwrEmcRadioRxGoodFrames32Bit_Object = MibTableColumn
mwrEmcRadioRxGoodFrames32Bit = _MwrEmcRadioRxGoodFrames32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 2, 1, 3),
    _MwrEmcRadioRxGoodFrames32Bit_Type()
)
mwrEmcRadioRxGoodFrames32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioRxGoodFrames32Bit.setStatus("current")
_MwrEmcRadioRxErrsFrames32Bit_Type = Counter32
_MwrEmcRadioRxErrsFrames32Bit_Object = MibTableColumn
mwrEmcRadioRxErrsFrames32Bit = _MwrEmcRadioRxErrsFrames32Bit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 203, 2, 1, 4),
    _MwrEmcRadioRxErrsFrames32Bit_Type()
)
mwrEmcRadioRxErrsFrames32Bit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwrEmcRadioRxErrsFrames32Bit.setStatus("current")
_MwrEmcRadioNotifications_ObjectIdentity = ObjectIdentity
mwrEmcRadioNotifications = _MwrEmcRadioNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 204)
)

# Managed Objects groups


# Notification objects

mwrEmcRadioRxLossOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 204, 1)
)
mwrEmcRadioRxLossOfSync.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-RADIO-MC-MIB", "mwrEmcRadioStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrEmcRadioRxLossOfSync.setStatus(
        "current"
    )

mwrEmcRadioFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 204, 2)
)
mwrEmcRadioFailure.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-RADIO-MC-MIB", "mwrEmcRadioStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrEmcRadioFailure.setStatus(
        "current"
    )

mwrEmcRadioCalUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 204, 3)
)
mwrEmcRadioCalUnavailable.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrEmcRadioCalUnavailable.setStatus(
        "current"
    )

mwrEmcRadioRslBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 204, 4)
)
mwrEmcRadioRslBelowThreshold.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-RADIO-MC-MIB", "mwrEmcRadioStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrEmcRadioRslBelowThreshold.setStatus(
        "current"
    )

mwrEmcRadioTxlAboveThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 204, 5)
)
mwrEmcRadioTxlAboveThreshold.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-RADIO-MC-MIB", "mwrEmcRadioStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrEmcRadioTxlAboveThreshold.setStatus(
        "current"
    )

mwrEmcRadioConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 4, 5, 12, 204, 6)
)
mwrEmcRadioConfigMismatch.setObjects(
      *(("MWR-ETHERNET-MIB", "mwrEventConfigSeverity"),
        ("MWR-RADIO-MC-MIB", "mwrEmcRadioStatusIndex"),
        ("EQUIPMENT-COMMON-MIB", "equipmentAlarmActiveConditionId"),
        ("EQUIPMENT-COMMON-MIB", "equipmentTrapInfo"),
        ("EQUIPMENT-COMMON-MIB", "equipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    mwrEmcRadioConfigMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MWR-RADIO-MC-MIB",
    **{"mwrRadio": mwrRadio,
       "mwrEmcRadioConfigurations": mwrEmcRadioConfigurations,
       "mwrEmcRadioConfigurationsTable": mwrEmcRadioConfigurationsTable,
       "mwrEmcRadioConfigurationsEntry": mwrEmcRadioConfigurationsEntry,
       "mwrEmcRadioConfigIndex": mwrEmcRadioConfigIndex,
       "mwrEmcRadioTxState": mwrEmcRadioTxState,
       "mwrEmcRadioTxPower": mwrEmcRadioTxPower,
       "mwrEmcRadioTxDownTime": mwrEmcRadioTxDownTime,
       "mwrEmcRadioRxFrequency": mwrEmcRadioRxFrequency,
       "mwrEmcRadioTxFrequency": mwrEmcRadioTxFrequency,
       "mwrEmcRadioProfileTable": mwrEmcRadioProfileTable,
       "mwrEmcRadioProfileEntry": mwrEmcRadioProfileEntry,
       "mwrEmcRadioStandardMode": mwrEmcRadioStandardMode,
       "mwrEmcRadioChannelBw": mwrEmcRadioChannelBw,
       "mwrEmcRadioStaticTxProfile": mwrEmcRadioStaticTxProfile,
       "mwrEmcRadioProgrammedProfile": mwrEmcRadioProgrammedProfile,
       "mwrEmcRadioThresholdAlarmTable": mwrEmcRadioThresholdAlarmTable,
       "mwrEmcRadioThresholdAlarmEntry": mwrEmcRadioThresholdAlarmEntry,
       "mwrEmcRadioThresholdIndex": mwrEmcRadioThresholdIndex,
       "mwrEmcRadioRslBelowThresholdParams": mwrEmcRadioRslBelowThresholdParams,
       "mwrEmcRadioTxAboveThresholdParams": mwrEmcRadioTxAboveThresholdParams,
       "mwrEmcRadioChCfgSynchEnable": mwrEmcRadioChCfgSynchEnable,
       "mwrEmcRadioStatus": mwrEmcRadioStatus,
       "mwrEmcRadioStatusTable": mwrEmcRadioStatusTable,
       "mwrEmcRadioStatusEntry": mwrEmcRadioStatusEntry,
       "mwrEmcRadioStatusIndex": mwrEmcRadioStatusIndex,
       "mwrEmcRadioOperStatus": mwrEmcRadioOperStatus,
       "mwrEmcRadioTRSpacing": mwrEmcRadioTRSpacing,
       "mwrEmcRadioActualTxStatus": mwrEmcRadioActualTxStatus,
       "mwrEmcRadioRxFreqMin": mwrEmcRadioRxFreqMin,
       "mwrEmcRadioRxFreqMax": mwrEmcRadioRxFreqMax,
       "mwrEmcRadioTxFreqMin": mwrEmcRadioTxFreqMin,
       "mwrEmcRadioTxFreqMax": mwrEmcRadioTxFreqMax,
       "mwrEmcRadioTxPowerMin": mwrEmcRadioTxPowerMin,
       "mwrEmcRadioTxPowerMax": mwrEmcRadioTxPowerMax,
       "mwrEmcRadioLinkStatus": mwrEmcRadioLinkStatus,
       "mwrEmcRadioPerformance": mwrEmcRadioPerformance,
       "mwrEmcRadioPerfStatsTable": mwrEmcRadioPerfStatsTable,
       "mwrEmcRadioPerfStatsEntry": mwrEmcRadioPerfStatsEntry,
       "mwrEmcRadioStatsIndex": mwrEmcRadioStatsIndex,
       "mwrEmcRadioTxFrames": mwrEmcRadioTxFrames,
       "mwrEmcRadioRxGoodFrames": mwrEmcRadioRxGoodFrames,
       "mwrEmcRadioRxErrsFrames": mwrEmcRadioRxErrsFrames,
       "mwrEmcRadioRSL": mwrEmcRadioRSL,
       "mwrEmcRadioEqualizerStress": mwrEmcRadioEqualizerStress,
       "mwrEmcRadioSNR": mwrEmcRadioSNR,
       "mwrEmcRadioLinkAvailability": mwrEmcRadioLinkAvailability,
       "mwrEmcRadioActualTxPower": mwrEmcRadioActualTxPower,
       "mwrEmcRadioActualTxProfile": mwrEmcRadioActualTxProfile,
       "mwrEmcRadioPerfStats32BitTable": mwrEmcRadioPerfStats32BitTable,
       "mwrEmcRadioPerfStats32BitEntry": mwrEmcRadioPerfStats32BitEntry,
       "mwrEmcRadioStats32BitIndex": mwrEmcRadioStats32BitIndex,
       "mwrEmcRadioTxFrames32Bit": mwrEmcRadioTxFrames32Bit,
       "mwrEmcRadioRxGoodFrames32Bit": mwrEmcRadioRxGoodFrames32Bit,
       "mwrEmcRadioRxErrsFrames32Bit": mwrEmcRadioRxErrsFrames32Bit,
       "mwrEmcRadioNotifications": mwrEmcRadioNotifications,
       "mwrEmcRadioRxLossOfSync": mwrEmcRadioRxLossOfSync,
       "mwrEmcRadioFailure": mwrEmcRadioFailure,
       "mwrEmcRadioCalUnavailable": mwrEmcRadioCalUnavailable,
       "mwrEmcRadioRslBelowThreshold": mwrEmcRadioRslBelowThreshold,
       "mwrEmcRadioTxlAboveThreshold": mwrEmcRadioTxlAboveThreshold,
       "mwrEmcRadioConfigMismatch": mwrEmcRadioConfigMismatch,
       "mwrRadioMcModIdentity": mwrRadioMcModIdentity}
)
