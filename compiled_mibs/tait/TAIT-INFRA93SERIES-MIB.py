# SNMP MIB module (TAIT-INFRA93SERIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\tait\TAIT-INFRA93SERIES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:36 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(taitGeneric,) = mibBuilder.importSymbols(
    "TAIT-COMMON-MIB",
    "taitGeneric")

(infra93_94MibModule,) = mibBuilder.importSymbols(
    "TAIT-INFRA93-94SERIES-COMMON-MIB",
    "infra93-94MibModule")

(AlarmState,
 BaseStationMode,
 ChannelGroupStatus,
 Condition,
 CurrentmA,
 FrequencyHz,
 GateState,
 Milliseconds,
 OptionState,
 PowerW,
 TimingControlType,
 TransmitterStatus,
 VoltageV) = mibBuilder.importSymbols(
    "TAIT-INFRA93-94SERIES-TC-MIB",
    "AlarmState",
    "BaseStationMode",
    "ChannelGroupStatus",
    "Condition",
    "CurrentmA",
    "FrequencyHz",
    "GateState",
    "Milliseconds",
    "OptionState",
    "PowerW",
    "TimingControlType",
    "TransmitterStatus",
    "VoltageV")

(ColourCode,
 ControlProtocolStatus,
 DcsCode,
 FallbackNodeStatus,
 FrequencydHz,
 LeveldBm,
 LogicalChannelState,
 MPTControlProtocolStatus,
 OperationalMode,
 Ratio,
 ReceiverSyncStatus,
 RxFrequencyResponse,
 SINADLevel,
 StandaloneNodeStatus,
 SubAudibleType,
 Temperature,
 TransmitterSyncStatus,
 TxFrequencyResponse) = mibBuilder.importSymbols(
    "TAIT-INFRA93SERIES-TC-MIB",
    "ColourCode",
    "ControlProtocolStatus",
    "DcsCode",
    "FallbackNodeStatus",
    "FrequencydHz",
    "LeveldBm",
    "LogicalChannelState",
    "MPTControlProtocolStatus",
    "OperationalMode",
    "Ratio",
    "ReceiverSyncStatus",
    "RxFrequencyResponse",
    "SINADLevel",
    "StandaloneNodeStatus",
    "SubAudibleType",
    "Temperature",
    "TransmitterSyncStatus",
    "TxFrequencyResponse")


# MODULE-IDENTITY

infra93MibMonitored = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    infra93MibMonitored.setRevisions(
        ("2019-08-30 15:38",
         "2019-05-29 00:00",
         "2019-03-30 00:00",
         "2018-08-30 00:00",
         "2018-07-30 00:00",
         "2018-05-22 00:26",
         "2017-09-14 01:30",
         "2017-08-24 14:00",
         "2017-05-05 15:00",
         "2017-03-07 00:00",
         "2017-02-03 00:00",
         "2016-12-05 00:00",
         "2016-07-01 00:00",
         "2016-02-18 00:00",
         "2015-11-03 04:00",
         "2015-03-23 04:00",
         "2014-10-30 15:00",
         "2014-07-29 00:00",
         "2014-07-10 00:00",
         "2014-04-14 00:00",
         "2014-04-13 00:00",
         "2014-03-14 00:00",
         "2014-01-26 00:00",
         "2014-01-14 11:00",
         "2014-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Infra93MIB_ObjectIdentity = ObjectIdentity
infra93MIB = _Infra93MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2)
)
_Monitored_ObjectIdentity = ObjectIdentity
monitored = _Monitored_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2)
)
_MibObjects_ObjectIdentity = ObjectIdentity
mibObjects = _MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1)
)
_ProductInfo_ObjectIdentity = ObjectIdentity
productInfo = _ProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1)
)
_ProductSummary_ObjectIdentity = ObjectIdentity
productSummary = _ProductSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 1)
)
_InfoTransmitterStatus_Type = TransmitterStatus
_InfoTransmitterStatus_Object = MibScalar
infoTransmitterStatus = _InfoTransmitterStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 1, 1),
    _InfoTransmitterStatus_Type()
)
infoTransmitterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTransmitterStatus.setStatus("current")
_InfoStandaloneNodeStatus_Type = StandaloneNodeStatus
_InfoStandaloneNodeStatus_Object = MibScalar
infoStandaloneNodeStatus = _InfoStandaloneNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 1, 2),
    _InfoStandaloneNodeStatus_Type()
)
infoStandaloneNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoStandaloneNodeStatus.setStatus("deprecated")
_InfoMPTFallbackNodeStatus_Type = FallbackNodeStatus
_InfoMPTFallbackNodeStatus_Object = MibScalar
infoMPTFallbackNodeStatus = _InfoMPTFallbackNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 1, 3),
    _InfoMPTFallbackNodeStatus_Type()
)
infoMPTFallbackNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMPTFallbackNodeStatus.setStatus("current")
_InfoDMRFallbackNodeStatus_Type = FallbackNodeStatus
_InfoDMRFallbackNodeStatus_Object = MibScalar
infoDMRFallbackNodeStatus = _InfoDMRFallbackNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 1, 4),
    _InfoDMRFallbackNodeStatus_Type()
)
infoDMRFallbackNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDMRFallbackNodeStatus.setStatus("current")
_Health_ObjectIdentity = ObjectIdentity
health = _Health_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 2)
)
_HealthRunMode_Type = BaseStationMode
_HealthRunMode_Object = MibScalar
healthRunMode = _HealthRunMode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 2, 2),
    _HealthRunMode_Type()
)
healthRunMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthRunMode.setStatus("current")
_HealthNetworkConnLogChan1State_Type = LogicalChannelState
_HealthNetworkConnLogChan1State_Object = MibScalar
healthNetworkConnLogChan1State = _HealthNetworkConnLogChan1State_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 2, 3),
    _HealthNetworkConnLogChan1State_Type()
)
healthNetworkConnLogChan1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthNetworkConnLogChan1State.setStatus("current")
_HealthNetworkConnLogChan2State_Type = LogicalChannelState
_HealthNetworkConnLogChan2State_Object = MibScalar
healthNetworkConnLogChan2State = _HealthNetworkConnLogChan2State_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 2, 4),
    _HealthNetworkConnLogChan2State_Type()
)
healthNetworkConnLogChan2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthNetworkConnLogChan2State.setStatus("current")
_HealthSecureShellRunning_Type = TruthValue
_HealthSecureShellRunning_Object = MibScalar
healthSecureShellRunning = _HealthSecureShellRunning_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 1, 2, 5),
    _HealthSecureShellRunning_Type()
)
healthSecureShellRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthSecureShellRunning.setStatus("current")
_ProductEnabledFeatures_ObjectIdentity = ObjectIdentity
productEnabledFeatures = _ProductEnabledFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2)
)
_LicenceDmrFull_Type = TruthValue
_LicenceDmrFull_Object = MibScalar
licenceDmrFull = _LicenceDmrFull_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 300),
    _LicenceDmrFull_Type()
)
licenceDmrFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDmrFull.setStatus("current")
_LicenceAnalogConventional_Type = TruthValue
_LicenceAnalogConventional_Object = MibScalar
licenceAnalogConventional = _LicenceAnalogConventional_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 301),
    _LicenceAnalogConventional_Type()
)
licenceAnalogConventional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceAnalogConventional.setStatus("current")
_LicenceDmrExpress_Type = TruthValue
_LicenceDmrExpress_Object = MibScalar
licenceDmrExpress = _LicenceDmrExpress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 302),
    _LicenceDmrExpress_Type()
)
licenceDmrExpress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDmrExpress.setStatus("current")
_LicenceDmrAccess_Type = TruthValue
_LicenceDmrAccess_Object = MibScalar
licenceDmrAccess = _LicenceDmrAccess_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 303),
    _LicenceDmrAccess_Type()
)
licenceDmrAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDmrAccess.setStatus("current")
_LicenceDmrConventional_Type = TruthValue
_LicenceDmrConventional_Object = MibScalar
licenceDmrConventional = _LicenceDmrConventional_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 304),
    _LicenceDmrConventional_Type()
)
licenceDmrConventional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDmrConventional.setStatus("current")
_LicenceDmrExpress20_Type = TruthValue
_LicenceDmrExpress20_Object = MibScalar
licenceDmrExpress20 = _LicenceDmrExpress20_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 305),
    _LicenceDmrExpress20_Type()
)
licenceDmrExpress20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDmrExpress20.setStatus("current")
_LicenceDmrCentralVoter_Type = TruthValue
_LicenceDmrCentralVoter_Object = MibScalar
licenceDmrCentralVoter = _LicenceDmrCentralVoter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 306),
    _LicenceDmrCentralVoter_Type()
)
licenceDmrCentralVoter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDmrCentralVoter.setStatus("current")
_LicenceDmrNetworkSatellite_Type = TruthValue
_LicenceDmrNetworkSatellite_Object = MibScalar
licenceDmrNetworkSatellite = _LicenceDmrNetworkSatellite_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 1, 2, 307),
    _LicenceDmrNetworkSatellite_Type()
)
licenceDmrNetworkSatellite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenceDmrNetworkSatellite.setStatus("current")
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2)
)
_Reciter_ObjectIdentity = ObjectIdentity
reciter = _Reciter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2)
)
_RctSummary_ObjectIdentity = ObjectIdentity
rctSummary = _RctSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 1)
)
_RctInfo_ObjectIdentity = ObjectIdentity
rctInfo = _RctInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 1, 1)
)
_RctInfoProductCode_Type = SnmpAdminString
_RctInfoProductCode_Object = MibScalar
rctInfoProductCode = _RctInfoProductCode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 1, 1, 1),
    _RctInfoProductCode_Type()
)
rctInfoProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctInfoProductCode.setStatus("current")
_RctInfoSerialNumber_Type = SnmpAdminString
_RctInfoSerialNumber_Object = MibScalar
rctInfoSerialNumber = _RctInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 1, 1, 2),
    _RctInfoSerialNumber_Type()
)
rctInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctInfoSerialNumber.setStatus("current")
_RctInfoHardwareVersion_Type = SnmpAdminString
_RctInfoHardwareVersion_Object = MibScalar
rctInfoHardwareVersion = _RctInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 1, 1, 3),
    _RctInfoHardwareVersion_Type()
)
rctInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctInfoHardwareVersion.setStatus("current")
_RctInfoFirmwareVersion_Type = SnmpAdminString
_RctInfoFirmwareVersion_Object = MibScalar
rctInfoFirmwareVersion = _RctInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 1, 1, 4),
    _RctInfoFirmwareVersion_Type()
)
rctInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctInfoFirmwareVersion.setStatus("current")
_RctHealth_ObjectIdentity = ObjectIdentity
rctHealth = _RctHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 1, 2)
)
_RctSelectedChannel_ObjectIdentity = ObjectIdentity
rctSelectedChannel = _RctSelectedChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2)
)
_RctSelectedChannelNumber_Type = Unsigned32
_RctSelectedChannelNumber_Object = MibScalar
rctSelectedChannelNumber = _RctSelectedChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 1),
    _RctSelectedChannelNumber_Type()
)
rctSelectedChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelNumber.setStatus("current")
_RctSelectedChannelName_Type = SnmpAdminString
_RctSelectedChannelName_Object = MibScalar
rctSelectedChannelName = _RctSelectedChannelName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 2),
    _RctSelectedChannelName_Type()
)
rctSelectedChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelName.setStatus("current")
_RctSelectedChannelProfileName_Type = SnmpAdminString
_RctSelectedChannelProfileName_Object = MibScalar
rctSelectedChannelProfileName = _RctSelectedChannelProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 3),
    _RctSelectedChannelProfileName_Type()
)
rctSelectedChannelProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelProfileName.setStatus("current")
_RctSelectedChannelSigProfileName_Type = SnmpAdminString
_RctSelectedChannelSigProfileName_Object = MibScalar
rctSelectedChannelSigProfileName = _RctSelectedChannelSigProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 4),
    _RctSelectedChannelSigProfileName_Type()
)
rctSelectedChannelSigProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelSigProfileName.setStatus("current")
_RctSelectedChannelTransmitPower_Type = PowerW
_RctSelectedChannelTransmitPower_Object = MibScalar
rctSelectedChannelTransmitPower = _RctSelectedChannelTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 5),
    _RctSelectedChannelTransmitPower_Type()
)
rctSelectedChannelTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelTransmitPower.setStatus("current")
_RctSelectedChannelTxFreq_Type = FrequencyHz
_RctSelectedChannelTxFreq_Object = MibScalar
rctSelectedChannelTxFreq = _RctSelectedChannelTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 6),
    _RctSelectedChannelTxFreq_Type()
)
rctSelectedChannelTxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelTxFreq.setStatus("current")
_RctSelectedChannelRxFreq_Type = FrequencyHz
_RctSelectedChannelRxFreq_Object = MibScalar
rctSelectedChannelRxFreq = _RctSelectedChannelRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 7),
    _RctSelectedChannelRxFreq_Type()
)
rctSelectedChannelRxFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelRxFreq.setStatus("current")
_RctSelectedChannelSystemType_Type = OperationalMode
_RctSelectedChannelSystemType_Object = MibScalar
rctSelectedChannelSystemType = _RctSelectedChannelSystemType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 10),
    _RctSelectedChannelSystemType_Type()
)
rctSelectedChannelSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelSystemType.setStatus("current")
_RctSelectedChannelColourCode_Type = ColourCode
_RctSelectedChannelColourCode_Object = MibScalar
rctSelectedChannelColourCode = _RctSelectedChannelColourCode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 11),
    _RctSelectedChannelColourCode_Type()
)
rctSelectedChannelColourCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelColourCode.setStatus("current")
_RctSelectedChannelGroupName_Type = SnmpAdminString
_RctSelectedChannelGroupName_Object = MibScalar
rctSelectedChannelGroupName = _RctSelectedChannelGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 2, 12),
    _RctSelectedChannelGroupName_Type()
)
rctSelectedChannelGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSelectedChannelGroupName.setStatus("current")
_RctRfReceiveQuality_ObjectIdentity = ObjectIdentity
rctRfReceiveQuality = _RctRfReceiveQuality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 3)
)
_RctRfRcvInterference_Type = TruthValue
_RctRfRcvInterference_Object = MibScalar
rctRfRcvInterference = _RctRfRcvInterference_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 3, 2),
    _RctRfRcvInterference_Type()
)
rctRfRcvInterference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfRcvInterference.setStatus("current")
_RctRfInterferenceCounter_Type = Counter32
_RctRfInterferenceCounter_Object = MibScalar
rctRfInterferenceCounter = _RctRfInterferenceCounter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 3, 3),
    _RctRfInterferenceCounter_Type()
)
rctRfInterferenceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfInterferenceCounter.setStatus("current")
_RctRfInterferenceEvents_Type = Counter32
_RctRfInterferenceEvents_Object = MibScalar
rctRfInterferenceEvents = _RctRfInterferenceEvents_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 3, 4),
    _RctRfInterferenceEvents_Type()
)
rctRfInterferenceEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfInterferenceEvents.setStatus("current")
_RctRfReceiver_ObjectIdentity = ObjectIdentity
rctRfReceiver = _RctRfReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4)
)
_RctRfReceiverRSSI_Type = LeveldBm
_RctRfReceiverRSSI_Object = MibScalar
rctRfReceiverRSSI = _RctRfReceiverRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 1),
    _RctRfReceiverRSSI_Type()
)
rctRfReceiverRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverRSSI.setStatus("current")
_RctRfReceiverLC1RSSI_Type = LeveldBm
_RctRfReceiverLC1RSSI_Object = MibScalar
rctRfReceiverLC1RSSI = _RctRfReceiverLC1RSSI_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 2),
    _RctRfReceiverLC1RSSI_Type()
)
rctRfReceiverLC1RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverLC1RSSI.setStatus("current")
_RctRfReceiverLC2RSSI_Type = LeveldBm
_RctRfReceiverLC2RSSI_Object = MibScalar
rctRfReceiverLC2RSSI = _RctRfReceiverLC2RSSI_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 3),
    _RctRfReceiverLC2RSSI_Type()
)
rctRfReceiverLC2RSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverLC2RSSI.setStatus("current")
_RctRfReceiverLC1RxGateState_Type = TruthValue
_RctRfReceiverLC1RxGateState_Object = MibScalar
rctRfReceiverLC1RxGateState = _RctRfReceiverLC1RxGateState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 4),
    _RctRfReceiverLC1RxGateState_Type()
)
rctRfReceiverLC1RxGateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverLC1RxGateState.setStatus("current")
_RctRfReceiverLC2RxGateState_Type = TruthValue
_RctRfReceiverLC2RxGateState_Object = MibScalar
rctRfReceiverLC2RxGateState = _RctRfReceiverLC2RxGateState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 5),
    _RctRfReceiverLC2RxGateState_Type()
)
rctRfReceiverLC2RxGateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverLC2RxGateState.setStatus("current")
_RctRfReceiverSelectedDecodeCTCSS_Type = FrequencydHz
_RctRfReceiverSelectedDecodeCTCSS_Object = MibScalar
rctRfReceiverSelectedDecodeCTCSS = _RctRfReceiverSelectedDecodeCTCSS_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 8),
    _RctRfReceiverSelectedDecodeCTCSS_Type()
)
rctRfReceiverSelectedDecodeCTCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverSelectedDecodeCTCSS.setStatus("current")
_RctRfReceiverSelectedDecodeSubAudibleType_Type = SubAudibleType
_RctRfReceiverSelectedDecodeSubAudibleType_Object = MibScalar
rctRfReceiverSelectedDecodeSubAudibleType = _RctRfReceiverSelectedDecodeSubAudibleType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 9),
    _RctRfReceiverSelectedDecodeSubAudibleType_Type()
)
rctRfReceiverSelectedDecodeSubAudibleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverSelectedDecodeSubAudibleType.setStatus("current")
_RctRfReceiverSelectedSINADGatingLevel_Type = SINADLevel
_RctRfReceiverSelectedSINADGatingLevel_Object = MibScalar
rctRfReceiverSelectedSINADGatingLevel = _RctRfReceiverSelectedSINADGatingLevel_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 10),
    _RctRfReceiverSelectedSINADGatingLevel_Type()
)
rctRfReceiverSelectedSINADGatingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverSelectedSINADGatingLevel.setStatus("current")
_RctRfReceiverSelectedDecodeDCS_Type = DcsCode
_RctRfReceiverSelectedDecodeDCS_Object = MibScalar
rctRfReceiverSelectedDecodeDCS = _RctRfReceiverSelectedDecodeDCS_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 11),
    _RctRfReceiverSelectedDecodeDCS_Type()
)
rctRfReceiverSelectedDecodeDCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverSelectedDecodeDCS.setStatus("current")
_RctRfReceiverSelectedFrequencyResponse_Type = RxFrequencyResponse
_RctRfReceiverSelectedFrequencyResponse_Object = MibScalar
rctRfReceiverSelectedFrequencyResponse = _RctRfReceiverSelectedFrequencyResponse_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 12),
    _RctRfReceiverSelectedFrequencyResponse_Type()
)
rctRfReceiverSelectedFrequencyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverSelectedFrequencyResponse.setStatus("current")
_RctRfReceiverAnalogGateState_Type = TruthValue
_RctRfReceiverAnalogGateState_Object = MibScalar
rctRfReceiverAnalogGateState = _RctRfReceiverAnalogGateState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 13),
    _RctRfReceiverAnalogGateState_Type()
)
rctRfReceiverAnalogGateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverAnalogGateState.setStatus("current")
_RctRfReceiverIsDisabled_Type = TruthValue
_RctRfReceiverIsDisabled_Object = MibScalar
rctRfReceiverIsDisabled = _RctRfReceiverIsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 4, 14),
    _RctRfReceiverIsDisabled_Type()
)
rctRfReceiverIsDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfReceiverIsDisabled.setStatus("current")
_RctRfTransmitter_ObjectIdentity = ObjectIdentity
rctRfTransmitter = _RctRfTransmitter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 5)
)
_RctRfTxSelectedEncodeCTCSS_Type = FrequencydHz
_RctRfTxSelectedEncodeCTCSS_Object = MibScalar
rctRfTxSelectedEncodeCTCSS = _RctRfTxSelectedEncodeCTCSS_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 5, 10),
    _RctRfTxSelectedEncodeCTCSS_Type()
)
rctRfTxSelectedEncodeCTCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfTxSelectedEncodeCTCSS.setStatus("current")
_RctRfTxSelectedEncodeSubAudibleType_Type = SubAudibleType
_RctRfTxSelectedEncodeSubAudibleType_Object = MibScalar
rctRfTxSelectedEncodeSubAudibleType = _RctRfTxSelectedEncodeSubAudibleType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 5, 11),
    _RctRfTxSelectedEncodeSubAudibleType_Type()
)
rctRfTxSelectedEncodeSubAudibleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfTxSelectedEncodeSubAudibleType.setStatus("current")
_RctRfTxSelectFrequencyResponse_Type = TxFrequencyResponse
_RctRfTxSelectFrequencyResponse_Object = MibScalar
rctRfTxSelectFrequencyResponse = _RctRfTxSelectFrequencyResponse_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 5, 12),
    _RctRfTxSelectFrequencyResponse_Type()
)
rctRfTxSelectFrequencyResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfTxSelectFrequencyResponse.setStatus("current")
_RctRfTxSelectedEncodeDCS_Type = DcsCode
_RctRfTxSelectedEncodeDCS_Object = MibScalar
rctRfTxSelectedEncodeDCS = _RctRfTxSelectedEncodeDCS_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 5, 13),
    _RctRfTxSelectedEncodeDCS_Type()
)
rctRfTxSelectedEncodeDCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfTxSelectedEncodeDCS.setStatus("current")
_RctRfTxSelectedEncodeSubAudibleDeviation_Type = Unsigned32
_RctRfTxSelectedEncodeSubAudibleDeviation_Object = MibScalar
rctRfTxSelectedEncodeSubAudibleDeviation = _RctRfTxSelectedEncodeSubAudibleDeviation_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 5, 14),
    _RctRfTxSelectedEncodeSubAudibleDeviation_Type()
)
rctRfTxSelectedEncodeSubAudibleDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfTxSelectedEncodeSubAudibleDeviation.setStatus("current")
_RctRfTxRfRepeatState_Type = OptionState
_RctRfTxRfRepeatState_Object = MibScalar
rctRfTxRfRepeatState = _RctRfTxRfRepeatState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 5, 16),
    _RctRfTxRfRepeatState_Type()
)
rctRfTxRfRepeatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctRfTxRfRepeatState.setStatus("current")
_RctTemperature_ObjectIdentity = ObjectIdentity
rctTemperature = _RctTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 6)
)
_RctTemperatureBoard_Type = Temperature
_RctTemperatureBoard_Object = MibScalar
rctTemperatureBoard = _RctTemperatureBoard_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 6, 1),
    _RctTemperatureBoard_Type()
)
rctTemperatureBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctTemperatureBoard.setStatus("current")
_RctSystemInterface_ObjectIdentity = ObjectIdentity
rctSystemInterface = _RctSystemInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 7)
)
_RctSiConfiguredBalancedLineInLevel_Type = LeveldBm
_RctSiConfiguredBalancedLineInLevel_Object = MibScalar
rctSiConfiguredBalancedLineInLevel = _RctSiConfiguredBalancedLineInLevel_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 7, 1),
    _RctSiConfiguredBalancedLineInLevel_Type()
)
rctSiConfiguredBalancedLineInLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSiConfiguredBalancedLineInLevel.setStatus("current")
_RctSiConfiguredBalancedLineOutLevel_Type = LeveldBm
_RctSiConfiguredBalancedLineOutLevel_Object = MibScalar
rctSiConfiguredBalancedLineOutLevel = _RctSiConfiguredBalancedLineOutLevel_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 7, 2),
    _RctSiConfiguredBalancedLineOutLevel_Type()
)
rctSiConfiguredBalancedLineOutLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSiConfiguredBalancedLineOutLevel.setStatus("current")
_RctSiTxKey_Type = GateState
_RctSiTxKey_Object = MibScalar
rctSiTxKey = _RctSiTxKey_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 7, 3),
    _RctSiTxKey_Type()
)
rctSiTxKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSiTxKey.setStatus("current")
_RctSiRxGate_Type = GateState
_RctSiRxGate_Object = MibScalar
rctSiRxGate = _RctSiRxGate_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 2, 7, 4),
    _RctSiRxGate_Type()
)
rctSiRxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctSiRxGate.setStatus("current")
_PowerAmplifier_ObjectIdentity = ObjectIdentity
powerAmplifier = _PowerAmplifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3)
)
_PaSummary_ObjectIdentity = ObjectIdentity
paSummary = _PaSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 1)
)
_PaInfo_ObjectIdentity = ObjectIdentity
paInfo = _PaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 1, 1)
)
_PaInfoProductCode_Type = SnmpAdminString
_PaInfoProductCode_Object = MibScalar
paInfoProductCode = _PaInfoProductCode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 1, 1, 1),
    _PaInfoProductCode_Type()
)
paInfoProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paInfoProductCode.setStatus("current")
_PaInfoSerialNumber_Type = SnmpAdminString
_PaInfoSerialNumber_Object = MibScalar
paInfoSerialNumber = _PaInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 1, 1, 2),
    _PaInfoSerialNumber_Type()
)
paInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paInfoSerialNumber.setStatus("current")
_PaInfoHardwareVersion_Type = SnmpAdminString
_PaInfoHardwareVersion_Object = MibScalar
paInfoHardwareVersion = _PaInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 1, 1, 3),
    _PaInfoHardwareVersion_Type()
)
paInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paInfoHardwareVersion.setStatus("current")
_PaInfoFirmwareVersion_Type = SnmpAdminString
_PaInfoFirmwareVersion_Object = MibScalar
paInfoFirmwareVersion = _PaInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 1, 1, 4),
    _PaInfoFirmwareVersion_Type()
)
paInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paInfoFirmwareVersion.setStatus("current")
_PaHealth_ObjectIdentity = ObjectIdentity
paHealth = _PaHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 1, 2)
)
_PaTxOutput_ObjectIdentity = ObjectIdentity
paTxOutput = _PaTxOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 2)
)
_PaTxOutputForwardPower_Type = PowerW
_PaTxOutputForwardPower_Object = MibScalar
paTxOutputForwardPower = _PaTxOutputForwardPower_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 2, 1),
    _PaTxOutputForwardPower_Type()
)
paTxOutputForwardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paTxOutputForwardPower.setStatus("current")
_PaTxOutputVSWR_Type = Ratio
_PaTxOutputVSWR_Object = MibScalar
paTxOutputVSWR = _PaTxOutputVSWR_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 2, 2),
    _PaTxOutputVSWR_Type()
)
paTxOutputVSWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paTxOutputVSWR.setStatus("current")
_PaTemperature_ObjectIdentity = ObjectIdentity
paTemperature = _PaTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 4)
)
_PaGeneral_ObjectIdentity = ObjectIdentity
paGeneral = _PaGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 3, 5)
)
_PowerManagementUnit_ObjectIdentity = ObjectIdentity
powerManagementUnit = _PowerManagementUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4)
)
_PmuSummary_ObjectIdentity = ObjectIdentity
pmuSummary = _PmuSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1)
)
_PmuInfo_ObjectIdentity = ObjectIdentity
pmuInfo = _PmuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 1)
)
_PmuInfoProductCode_Type = SnmpAdminString
_PmuInfoProductCode_Object = MibScalar
pmuInfoProductCode = _PmuInfoProductCode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 1, 1),
    _PmuInfoProductCode_Type()
)
pmuInfoProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuInfoProductCode.setStatus("current")
_PmuInfoSerialNumber_Type = SnmpAdminString
_PmuInfoSerialNumber_Object = MibScalar
pmuInfoSerialNumber = _PmuInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 1, 2),
    _PmuInfoSerialNumber_Type()
)
pmuInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuInfoSerialNumber.setStatus("current")
_PmuInfoHardwareVersion_Type = SnmpAdminString
_PmuInfoHardwareVersion_Object = MibScalar
pmuInfoHardwareVersion = _PmuInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 1, 3),
    _PmuInfoHardwareVersion_Type()
)
pmuInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuInfoHardwareVersion.setStatus("current")
_PmuInfoFirmwareVersion_Type = SnmpAdminString
_PmuInfoFirmwareVersion_Object = MibScalar
pmuInfoFirmwareVersion = _PmuInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 1, 4),
    _PmuInfoFirmwareVersion_Type()
)
pmuInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuInfoFirmwareVersion.setStatus("current")
_PmuInfoCalibrationUpdateDate_Type = SnmpAdminString
_PmuInfoCalibrationUpdateDate_Object = MibScalar
pmuInfoCalibrationUpdateDate = _PmuInfoCalibrationUpdateDate_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 1, 5),
    _PmuInfoCalibrationUpdateDate_Type()
)
pmuInfoCalibrationUpdateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuInfoCalibrationUpdateDate.setStatus("current")
_PmuHealth_ObjectIdentity = ObjectIdentity
pmuHealth = _PmuHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 2)
)
_PmuSubmodules_ObjectIdentity = ObjectIdentity
pmuSubmodules = _PmuSubmodules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 1, 3)
)
_PmuState_ObjectIdentity = ObjectIdentity
pmuState = _PmuState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2)
)
_PmuStateMainsInState_Type = Condition
_PmuStateMainsInState_Object = MibScalar
pmuStateMainsInState = _PmuStateMainsInState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 1),
    _PmuStateMainsInState_Type()
)
pmuStateMainsInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateMainsInState.setStatus("current")
_PmuStateBatteryInState_Type = Condition
_PmuStateBatteryInState_Object = MibScalar
pmuStateBatteryInState = _PmuStateBatteryInState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 2),
    _PmuStateBatteryInState_Type()
)
pmuStateBatteryInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateBatteryInState.setStatus("current")
_PmuStateBatteryInVoltage_Type = VoltageV
_PmuStateBatteryInVoltage_Object = MibScalar
pmuStateBatteryInVoltage = _PmuStateBatteryInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 3),
    _PmuStateBatteryInVoltage_Type()
)
pmuStateBatteryInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateBatteryInVoltage.setStatus("current")
_PmuStateOutCurrent_Type = CurrentmA
_PmuStateOutCurrent_Object = MibScalar
pmuStateOutCurrent = _PmuStateOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 4),
    _PmuStateOutCurrent_Type()
)
pmuStateOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateOutCurrent.setStatus("current")
_PmuStateOutVoltage_Type = VoltageV
_PmuStateOutVoltage_Object = MibScalar
pmuStateOutVoltage = _PmuStateOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 5),
    _PmuStateOutVoltage_Type()
)
pmuStateOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateOutVoltage.setStatus("current")
_PmuStateOutStatus_Type = Condition
_PmuStateOutStatus_Object = MibScalar
pmuStateOutStatus = _PmuStateOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 6),
    _PmuStateOutStatus_Type()
)
pmuStateOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateOutStatus.setStatus("current")
_PmuStateAuxOutState_Type = Condition
_PmuStateAuxOutState_Object = MibScalar
pmuStateAuxOutState = _PmuStateAuxOutState_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 7),
    _PmuStateAuxOutState_Type()
)
pmuStateAuxOutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateAuxOutState.setStatus("current")
_PmuStateBusConnect_Type = TruthValue
_PmuStateBusConnect_Object = MibScalar
pmuStateBusConnect = _PmuStateBusConnect_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 4, 2, 9),
    _PmuStateBusConnect_Type()
)
pmuStateBusConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuStateBusConnect.setStatus("current")
_FrontPanel_ObjectIdentity = ObjectIdentity
frontPanel = _FrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5)
)
_FpSummary_ObjectIdentity = ObjectIdentity
fpSummary = _FpSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5, 1)
)
_FpInfo_ObjectIdentity = ObjectIdentity
fpInfo = _FpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5, 1, 1)
)
_FpInfoProductCode_Type = SnmpAdminString
_FpInfoProductCode_Object = MibScalar
fpInfoProductCode = _FpInfoProductCode_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5, 1, 1, 1),
    _FpInfoProductCode_Type()
)
fpInfoProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpInfoProductCode.setStatus("current")
_FpInfoSerialNumber_Type = SnmpAdminString
_FpInfoSerialNumber_Object = MibScalar
fpInfoSerialNumber = _FpInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5, 1, 1, 2),
    _FpInfoSerialNumber_Type()
)
fpInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpInfoSerialNumber.setStatus("current")
_FpInfoHardwareVersion_Type = SnmpAdminString
_FpInfoHardwareVersion_Object = MibScalar
fpInfoHardwareVersion = _FpInfoHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5, 1, 1, 3),
    _FpInfoHardwareVersion_Type()
)
fpInfoHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpInfoHardwareVersion.setStatus("current")
_FpInfoFirmwareVersion_Type = SnmpAdminString
_FpInfoFirmwareVersion_Object = MibScalar
fpInfoFirmwareVersion = _FpInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5, 1, 1, 4),
    _FpInfoFirmwareVersion_Type()
)
fpInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpInfoFirmwareVersion.setStatus("current")
_FpHealth_ObjectIdentity = ObjectIdentity
fpHealth = _FpHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 2, 5, 1, 2)
)
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3)
)
_AlarmSummary_ObjectIdentity = ObjectIdentity
alarmSummary = _AlarmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1)
)
_AlarmSummaryBaseStation_Type = AlarmState
_AlarmSummaryBaseStation_Object = MibScalar
alarmSummaryBaseStation = _AlarmSummaryBaseStation_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 1),
    _AlarmSummaryBaseStation_Type()
)
alarmSummaryBaseStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryBaseStation.setStatus("current")
_AlarmSummaryReciter_Type = AlarmState
_AlarmSummaryReciter_Object = MibScalar
alarmSummaryReciter = _AlarmSummaryReciter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 2),
    _AlarmSummaryReciter_Type()
)
alarmSummaryReciter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryReciter.setStatus("current")
_AlarmSummaryPowerAmplifier_Type = AlarmState
_AlarmSummaryPowerAmplifier_Object = MibScalar
alarmSummaryPowerAmplifier = _AlarmSummaryPowerAmplifier_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 3),
    _AlarmSummaryPowerAmplifier_Type()
)
alarmSummaryPowerAmplifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryPowerAmplifier.setStatus("current")
_AlarmSummaryPowerManagementUnit_Type = AlarmState
_AlarmSummaryPowerManagementUnit_Object = MibScalar
alarmSummaryPowerManagementUnit = _AlarmSummaryPowerManagementUnit_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 4),
    _AlarmSummaryPowerManagementUnit_Type()
)
alarmSummaryPowerManagementUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryPowerManagementUnit.setStatus("current")
_AlarmSummaryCustomAlarms_Type = AlarmState
_AlarmSummaryCustomAlarms_Object = MibScalar
alarmSummaryCustomAlarms = _AlarmSummaryCustomAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 5),
    _AlarmSummaryCustomAlarms_Type()
)
alarmSummaryCustomAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryCustomAlarms.setStatus("current")
_AlarmSummaryFrontPanel_Type = AlarmState
_AlarmSummaryFrontPanel_Object = MibScalar
alarmSummaryFrontPanel = _AlarmSummaryFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 6),
    _AlarmSummaryFrontPanel_Type()
)
alarmSummaryFrontPanel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryFrontPanel.setStatus("current")
_AlarmSummarySystem_Type = AlarmState
_AlarmSummarySystem_Object = MibScalar
alarmSummarySystem = _AlarmSummarySystem_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 7),
    _AlarmSummarySystem_Type()
)
alarmSummarySystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummarySystem.setStatus("current")
_AlarmSummaryMinor_Type = AlarmState
_AlarmSummaryMinor_Object = MibScalar
alarmSummaryMinor = _AlarmSummaryMinor_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 8),
    _AlarmSummaryMinor_Type()
)
alarmSummaryMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryMinor.setStatus("current")
_AlarmSummaryMajor_Type = AlarmState
_AlarmSummaryMajor_Object = MibScalar
alarmSummaryMajor = _AlarmSummaryMajor_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 1, 9),
    _AlarmSummaryMajor_Type()
)
alarmSummaryMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSummaryMajor.setStatus("current")
_ReciterAlarms_ObjectIdentity = ObjectIdentity
reciterAlarms = _ReciterAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3)
)
_RctAlarmRxSynthOutOfLock_Type = AlarmState
_RctAlarmRxSynthOutOfLock_Object = MibScalar
rctAlarmRxSynthOutOfLock = _RctAlarmRxSynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 2),
    _RctAlarmRxSynthOutOfLock_Type()
)
rctAlarmRxSynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmRxSynthOutOfLock.setStatus("current")
_RctAlarmInvalidChannelSelected_Type = AlarmState
_RctAlarmInvalidChannelSelected_Object = MibScalar
rctAlarmInvalidChannelSelected = _RctAlarmInvalidChannelSelected_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 3),
    _RctAlarmInvalidChannelSelected_Type()
)
rctAlarmInvalidChannelSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmInvalidChannelSelected.setStatus("current")
_RctAlarmOverTemperature_Type = AlarmState
_RctAlarmOverTemperature_Object = MibScalar
rctAlarmOverTemperature = _RctAlarmOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 10),
    _RctAlarmOverTemperature_Type()
)
rctAlarmOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmOverTemperature.setStatus("current")
_RctAlarmTxCalibrationInvalid_Type = AlarmState
_RctAlarmTxCalibrationInvalid_Object = MibScalar
rctAlarmTxCalibrationInvalid = _RctAlarmTxCalibrationInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 13),
    _RctAlarmTxCalibrationInvalid_Type()
)
rctAlarmTxCalibrationInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmTxCalibrationInvalid.setStatus("current")
_RctAlarmRxCalibrationInvalid_Type = AlarmState
_RctAlarmRxCalibrationInvalid_Object = MibScalar
rctAlarmRxCalibrationInvalid = _RctAlarmRxCalibrationInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 14),
    _RctAlarmRxCalibrationInvalid_Type()
)
rctAlarmRxCalibrationInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmRxCalibrationInvalid.setStatus("current")
_RctAlarmInvalidConfiguration_Type = AlarmState
_RctAlarmInvalidConfiguration_Object = MibScalar
rctAlarmInvalidConfiguration = _RctAlarmInvalidConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 15),
    _RctAlarmInvalidConfiguration_Type()
)
rctAlarmInvalidConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmInvalidConfiguration.setStatus("current")
_RctAlarm25MHzSynthOutOfLock_Type = AlarmState
_RctAlarm25MHzSynthOutOfLock_Object = MibScalar
rctAlarm25MHzSynthOutOfLock = _RctAlarm25MHzSynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 16),
    _RctAlarm25MHzSynthOutOfLock_Type()
)
rctAlarm25MHzSynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarm25MHzSynthOutOfLock.setStatus("current")
_RctAlarm6144MHzSynthOutOfLock_Type = AlarmState
_RctAlarm6144MHzSynthOutOfLock_Object = MibScalar
rctAlarm6144MHzSynthOutOfLock = _RctAlarm6144MHzSynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 17),
    _RctAlarm6144MHzSynthOutOfLock_Type()
)
rctAlarm6144MHzSynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarm6144MHzSynthOutOfLock.setStatus("current")
_RctAlarmTxFSynthOutOfLock_Type = AlarmState
_RctAlarmTxFSynthOutOfLock_Object = MibScalar
rctAlarmTxFSynthOutOfLock = _RctAlarmTxFSynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 18),
    _RctAlarmTxFSynthOutOfLock_Type()
)
rctAlarmTxFSynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmTxFSynthOutOfLock.setStatus("current")
_RctAlarmSimulcastSynch_Type = AlarmState
_RctAlarmSimulcastSynch_Object = MibScalar
rctAlarmSimulcastSynch = _RctAlarmSimulcastSynch_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 19),
    _RctAlarmSimulcastSynch_Type()
)
rctAlarmSimulcastSynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmSimulcastSynch.setStatus("current")
_RctAlarmReceiverSynch_Type = AlarmState
_RctAlarmReceiverSynch_Object = MibScalar
rctAlarmReceiverSynch = _RctAlarmReceiverSynch_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 20),
    _RctAlarmReceiverSynch_Type()
)
rctAlarmReceiverSynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmReceiverSynch.setStatus("current")
_RctAlarmTxRSynthOutOfLock_Type = AlarmState
_RctAlarmTxRSynthOutOfLock_Object = MibScalar
rctAlarmTxRSynthOutOfLock = _RctAlarmTxRSynthOutOfLock_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 3, 21),
    _RctAlarmTxRSynthOutOfLock_Type()
)
rctAlarmTxRSynthOutOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rctAlarmTxRSynthOutOfLock.setStatus("current")
_PaAlarms_ObjectIdentity = ObjectIdentity
paAlarms = _PaAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4)
)
_PaAlarmNoPADetected_Type = AlarmState
_PaAlarmNoPADetected_Object = MibScalar
paAlarmNoPADetected = _PaAlarmNoPADetected_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 1),
    _PaAlarmNoPADetected_Type()
)
paAlarmNoPADetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmNoPADetected.setStatus("current")
_PaAlarmInvalidFirmware_Type = AlarmState
_PaAlarmInvalidFirmware_Object = MibScalar
paAlarmInvalidFirmware = _PaAlarmInvalidFirmware_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 2),
    _PaAlarmInvalidFirmware_Type()
)
paAlarmInvalidFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmInvalidFirmware.setStatus("current")
_PaAlarmInvalidCalibration_Type = AlarmState
_PaAlarmInvalidCalibration_Object = MibScalar
paAlarmInvalidCalibration = _PaAlarmInvalidCalibration_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 3),
    _PaAlarmInvalidCalibration_Type()
)
paAlarmInvalidCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmInvalidCalibration.setStatus("current")
_PaAlarmForwardPowerLow_Type = AlarmState
_PaAlarmForwardPowerLow_Object = MibScalar
paAlarmForwardPowerLow = _PaAlarmForwardPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 5),
    _PaAlarmForwardPowerLow_Type()
)
paAlarmForwardPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmForwardPowerLow.setStatus("current")
_PaAlarmPowerFoldback_Type = AlarmState
_PaAlarmPowerFoldback_Object = MibScalar
paAlarmPowerFoldback = _PaAlarmPowerFoldback_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 7),
    _PaAlarmPowerFoldback_Type()
)
paAlarmPowerFoldback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmPowerFoldback.setStatus("current")
_PaAlarmReversePowerHigh_Type = AlarmState
_PaAlarmReversePowerHigh_Object = MibScalar
paAlarmReversePowerHigh = _PaAlarmReversePowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 8),
    _PaAlarmReversePowerHigh_Type()
)
paAlarmReversePowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmReversePowerHigh.setStatus("current")
_PaAlarmShutdownImminent_Type = AlarmState
_PaAlarmShutdownImminent_Object = MibScalar
paAlarmShutdownImminent = _PaAlarmShutdownImminent_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 9),
    _PaAlarmShutdownImminent_Type()
)
paAlarmShutdownImminent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmShutdownImminent.setStatus("current")
_PaAlarmVSWRFault_Type = AlarmState
_PaAlarmVSWRFault_Object = MibScalar
paAlarmVSWRFault = _PaAlarmVSWRFault_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 10),
    _PaAlarmVSWRFault_Type()
)
paAlarmVSWRFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmVSWRFault.setStatus("current")
_PaAlarmDriverCurrentHigh_Type = AlarmState
_PaAlarmDriverCurrentHigh_Object = MibScalar
paAlarmDriverCurrentHigh = _PaAlarmDriverCurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 11),
    _PaAlarmDriverCurrentHigh_Type()
)
paAlarmDriverCurrentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmDriverCurrentHigh.setStatus("current")
_PaAlarmFinal1CurrentHigh_Type = AlarmState
_PaAlarmFinal1CurrentHigh_Object = MibScalar
paAlarmFinal1CurrentHigh = _PaAlarmFinal1CurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 12),
    _PaAlarmFinal1CurrentHigh_Type()
)
paAlarmFinal1CurrentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmFinal1CurrentHigh.setStatus("current")
_PaAlarmFinal2CurrentHigh_Type = AlarmState
_PaAlarmFinal2CurrentHigh_Object = MibScalar
paAlarmFinal2CurrentHigh = _PaAlarmFinal2CurrentHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 13),
    _PaAlarmFinal2CurrentHigh_Type()
)
paAlarmFinal2CurrentHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmFinal2CurrentHigh.setStatus("current")
_PaAlarmCurrentImbalance_Type = AlarmState
_PaAlarmCurrentImbalance_Object = MibScalar
paAlarmCurrentImbalance = _PaAlarmCurrentImbalance_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 14),
    _PaAlarmCurrentImbalance_Type()
)
paAlarmCurrentImbalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmCurrentImbalance.setStatus("current")
_PaAlarmSupplyVoltageLow_Type = AlarmState
_PaAlarmSupplyVoltageLow_Object = MibScalar
paAlarmSupplyVoltageLow = _PaAlarmSupplyVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 15),
    _PaAlarmSupplyVoltageLow_Type()
)
paAlarmSupplyVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmSupplyVoltageLow.setStatus("current")
_PaAlarmSupplyVoltageHigh_Type = AlarmState
_PaAlarmSupplyVoltageHigh_Object = MibScalar
paAlarmSupplyVoltageHigh = _PaAlarmSupplyVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 16),
    _PaAlarmSupplyVoltageHigh_Type()
)
paAlarmSupplyVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmSupplyVoltageHigh.setStatus("current")
_PaAlarmDriverTemperatureHigh_Type = AlarmState
_PaAlarmDriverTemperatureHigh_Object = MibScalar
paAlarmDriverTemperatureHigh = _PaAlarmDriverTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 17),
    _PaAlarmDriverTemperatureHigh_Type()
)
paAlarmDriverTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmDriverTemperatureHigh.setStatus("current")
_PaAlarmFinal1TemperatureHigh_Type = AlarmState
_PaAlarmFinal1TemperatureHigh_Object = MibScalar
paAlarmFinal1TemperatureHigh = _PaAlarmFinal1TemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 18),
    _PaAlarmFinal1TemperatureHigh_Type()
)
paAlarmFinal1TemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmFinal1TemperatureHigh.setStatus("current")
_PaAlarmFinal2TemperatureHigh_Type = AlarmState
_PaAlarmFinal2TemperatureHigh_Object = MibScalar
paAlarmFinal2TemperatureHigh = _PaAlarmFinal2TemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 4, 19),
    _PaAlarmFinal2TemperatureHigh_Type()
)
paAlarmFinal2TemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paAlarmFinal2TemperatureHigh.setStatus("current")
_PmuAlarms_ObjectIdentity = ObjectIdentity
pmuAlarms = _PmuAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5)
)
_PmuAlarmNoPMUDetected_Type = AlarmState
_PmuAlarmNoPMUDetected_Object = MibScalar
pmuAlarmNoPMUDetected = _PmuAlarmNoPMUDetected_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 1),
    _PmuAlarmNoPMUDetected_Type()
)
pmuAlarmNoPMUDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmNoPMUDetected.setStatus("current")
_PmuAlarmInvalidFirmware_Type = AlarmState
_PmuAlarmInvalidFirmware_Object = MibScalar
pmuAlarmInvalidFirmware = _PmuAlarmInvalidFirmware_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 2),
    _PmuAlarmInvalidFirmware_Type()
)
pmuAlarmInvalidFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmInvalidFirmware.setStatus("current")
_PmuAlarmMainsFailure_Type = AlarmState
_PmuAlarmMainsFailure_Object = MibScalar
pmuAlarmMainsFailure = _PmuAlarmMainsFailure_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 4),
    _PmuAlarmMainsFailure_Type()
)
pmuAlarmMainsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmMainsFailure.setStatus("current")
_PmuAlarmSelfTestFailure_Type = AlarmState
_PmuAlarmSelfTestFailure_Object = MibScalar
pmuAlarmSelfTestFailure = _PmuAlarmSelfTestFailure_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 5),
    _PmuAlarmSelfTestFailure_Type()
)
pmuAlarmSelfTestFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmSelfTestFailure.setStatus("current")
_PmuAlarmShutdownImminent_Type = AlarmState
_PmuAlarmShutdownImminent_Object = MibScalar
pmuAlarmShutdownImminent = _PmuAlarmShutdownImminent_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 6),
    _PmuAlarmShutdownImminent_Type()
)
pmuAlarmShutdownImminent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmShutdownImminent.setStatus("current")
_PmuAlarmTemperatureHigh_Type = AlarmState
_PmuAlarmTemperatureHigh_Object = MibScalar
pmuAlarmTemperatureHigh = _PmuAlarmTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 7),
    _PmuAlarmTemperatureHigh_Type()
)
pmuAlarmTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmTemperatureHigh.setStatus("current")
_PmuAlarmBatteryProtect_Type = AlarmState
_PmuAlarmBatteryProtect_Object = MibScalar
pmuAlarmBatteryProtect = _PmuAlarmBatteryProtect_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 8),
    _PmuAlarmBatteryProtect_Type()
)
pmuAlarmBatteryProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmBatteryProtect.setStatus("current")
_PmuAlarmBatteryVoltageLow_Type = AlarmState
_PmuAlarmBatteryVoltageLow_Object = MibScalar
pmuAlarmBatteryVoltageLow = _PmuAlarmBatteryVoltageLow_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 9),
    _PmuAlarmBatteryVoltageLow_Type()
)
pmuAlarmBatteryVoltageLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmBatteryVoltageLow.setStatus("current")
_PmuAlarmBatteryVoltageHigh_Type = AlarmState
_PmuAlarmBatteryVoltageHigh_Object = MibScalar
pmuAlarmBatteryVoltageHigh = _PmuAlarmBatteryVoltageHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 10),
    _PmuAlarmBatteryVoltageHigh_Type()
)
pmuAlarmBatteryVoltageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmBatteryVoltageHigh.setStatus("current")
_PmuAlarmCurrentOutHigh_Type = AlarmState
_PmuAlarmCurrentOutHigh_Object = MibScalar
pmuAlarmCurrentOutHigh = _PmuAlarmCurrentOutHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 11),
    _PmuAlarmCurrentOutHigh_Type()
)
pmuAlarmCurrentOutHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmCurrentOutHigh.setStatus("current")
_PmuAlarmVoltageOutLow_Type = AlarmState
_PmuAlarmVoltageOutLow_Object = MibScalar
pmuAlarmVoltageOutLow = _PmuAlarmVoltageOutLow_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 12),
    _PmuAlarmVoltageOutLow_Type()
)
pmuAlarmVoltageOutLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmVoltageOutLow.setStatus("current")
_PmuAlarmVoltageOutHigh_Type = AlarmState
_PmuAlarmVoltageOutHigh_Object = MibScalar
pmuAlarmVoltageOutHigh = _PmuAlarmVoltageOutHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 5, 13),
    _PmuAlarmVoltageOutHigh_Type()
)
pmuAlarmVoltageOutHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmuAlarmVoltageOutHigh.setStatus("current")
_CustomAlarms_ObjectIdentity = ObjectIdentity
customAlarms = _CustomAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6)
)
_CustomAlarm1_Type = AlarmState
_CustomAlarm1_Object = MibScalar
customAlarm1 = _CustomAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 1),
    _CustomAlarm1_Type()
)
customAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm1.setStatus("current")
_CustomAlarm2_Type = AlarmState
_CustomAlarm2_Object = MibScalar
customAlarm2 = _CustomAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 2),
    _CustomAlarm2_Type()
)
customAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm2.setStatus("current")
_CustomAlarm3_Type = AlarmState
_CustomAlarm3_Object = MibScalar
customAlarm3 = _CustomAlarm3_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 3),
    _CustomAlarm3_Type()
)
customAlarm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm3.setStatus("current")
_CustomAlarm4_Type = AlarmState
_CustomAlarm4_Object = MibScalar
customAlarm4 = _CustomAlarm4_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 4),
    _CustomAlarm4_Type()
)
customAlarm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm4.setStatus("current")
_CustomAlarm5_Type = AlarmState
_CustomAlarm5_Object = MibScalar
customAlarm5 = _CustomAlarm5_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 5),
    _CustomAlarm5_Type()
)
customAlarm5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm5.setStatus("current")
_CustomAlarm6_Type = AlarmState
_CustomAlarm6_Object = MibScalar
customAlarm6 = _CustomAlarm6_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 6),
    _CustomAlarm6_Type()
)
customAlarm6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm6.setStatus("current")
_CustomAlarm7_Type = AlarmState
_CustomAlarm7_Object = MibScalar
customAlarm7 = _CustomAlarm7_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 7),
    _CustomAlarm7_Type()
)
customAlarm7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm7.setStatus("current")
_CustomAlarm8_Type = AlarmState
_CustomAlarm8_Object = MibScalar
customAlarm8 = _CustomAlarm8_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 8),
    _CustomAlarm8_Type()
)
customAlarm8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm8.setStatus("current")
_CustomAlarm9_Type = AlarmState
_CustomAlarm9_Object = MibScalar
customAlarm9 = _CustomAlarm9_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 9),
    _CustomAlarm9_Type()
)
customAlarm9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm9.setStatus("current")
_CustomAlarm10_Type = AlarmState
_CustomAlarm10_Object = MibScalar
customAlarm10 = _CustomAlarm10_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 10),
    _CustomAlarm10_Type()
)
customAlarm10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm10.setStatus("current")
_CustomAlarm11_Type = AlarmState
_CustomAlarm11_Object = MibScalar
customAlarm11 = _CustomAlarm11_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 11),
    _CustomAlarm11_Type()
)
customAlarm11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm11.setStatus("current")
_CustomAlarm12_Type = AlarmState
_CustomAlarm12_Object = MibScalar
customAlarm12 = _CustomAlarm12_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 6, 12),
    _CustomAlarm12_Type()
)
customAlarm12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customAlarm12.setStatus("current")
_FpAlarms_ObjectIdentity = ObjectIdentity
fpAlarms = _FpAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 7)
)
_FpAlarmFan1_Type = AlarmState
_FpAlarmFan1_Object = MibScalar
fpAlarmFan1 = _FpAlarmFan1_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 7, 1),
    _FpAlarmFan1_Type()
)
fpAlarmFan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpAlarmFan1.setStatus("current")
_FpAlarmFan2_Type = AlarmState
_FpAlarmFan2_Object = MibScalar
fpAlarmFan2 = _FpAlarmFan2_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 7, 2),
    _FpAlarmFan2_Type()
)
fpAlarmFan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpAlarmFan2.setStatus("current")
_FpAlarmFan3_Type = AlarmState
_FpAlarmFan3_Object = MibScalar
fpAlarmFan3 = _FpAlarmFan3_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 7, 3),
    _FpAlarmFan3_Type()
)
fpAlarmFan3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpAlarmFan3.setStatus("current")
_FpAlarmNoFPDetected_Type = AlarmState
_FpAlarmNoFPDetected_Object = MibScalar
fpAlarmNoFPDetected = _FpAlarmNoFPDetected_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 7, 4),
    _FpAlarmNoFPDetected_Type()
)
fpAlarmNoFPDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpAlarmNoFPDetected.setStatus("current")
_FpAlarmInvalidFirmware_Type = AlarmState
_FpAlarmInvalidFirmware_Object = MibScalar
fpAlarmInvalidFirmware = _FpAlarmInvalidFirmware_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 7, 5),
    _FpAlarmInvalidFirmware_Type()
)
fpAlarmInvalidFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpAlarmInvalidFirmware.setStatus("current")
_SystemAlarms_ObjectIdentity = ObjectIdentity
systemAlarms = _SystemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8)
)
_SystemAlarmAmbientTempLow_Type = AlarmState
_SystemAlarmAmbientTempLow_Object = MibScalar
systemAlarmAmbientTempLow = _SystemAlarmAmbientTempLow_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 1),
    _SystemAlarmAmbientTempLow_Type()
)
systemAlarmAmbientTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmAmbientTempLow.setStatus("current")
_SystemAlarmAmbientTempHigh_Type = AlarmState
_SystemAlarmAmbientTempHigh_Object = MibScalar
systemAlarmAmbientTempHigh = _SystemAlarmAmbientTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 2),
    _SystemAlarmAmbientTempHigh_Type()
)
systemAlarmAmbientTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmAmbientTempHigh.setStatus("current")
_SystemAlarmExternalRefAbsent_Type = AlarmState
_SystemAlarmExternalRefAbsent_Object = MibScalar
systemAlarmExternalRefAbsent = _SystemAlarmExternalRefAbsent_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 3),
    _SystemAlarmExternalRefAbsent_Type()
)
systemAlarmExternalRefAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmExternalRefAbsent.setStatus("current")
_SystemAlarmQoSJitter_Type = AlarmState
_SystemAlarmQoSJitter_Object = MibScalar
systemAlarmQoSJitter = _SystemAlarmQoSJitter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 4),
    _SystemAlarmQoSJitter_Type()
)
systemAlarmQoSJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmQoSJitter.setStatus("current")
_SystemAlarmQoSLostPackets_Type = AlarmState
_SystemAlarmQoSLostPackets_Object = MibScalar
systemAlarmQoSLostPackets = _SystemAlarmQoSLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 5),
    _SystemAlarmQoSLostPackets_Type()
)
systemAlarmQoSLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmQoSLostPackets.setStatus("current")
_SystemAlarmFallbackControlled_Type = AlarmState
_SystemAlarmFallbackControlled_Object = MibScalar
systemAlarmFallbackControlled = _SystemAlarmFallbackControlled_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 6),
    _SystemAlarmFallbackControlled_Type()
)
systemAlarmFallbackControlled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmFallbackControlled.setStatus("current")
_SystemAlarmDuplicateNodePriority_Type = AlarmState
_SystemAlarmDuplicateNodePriority_Object = MibScalar
systemAlarmDuplicateNodePriority = _SystemAlarmDuplicateNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 7),
    _SystemAlarmDuplicateNodePriority_Type()
)
systemAlarmDuplicateNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmDuplicateNodePriority.setStatus("current")
_SystemAlarmNTPSynchronisation_Type = AlarmState
_SystemAlarmNTPSynchronisation_Object = MibScalar
systemAlarmNTPSynchronisation = _SystemAlarmNTPSynchronisation_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 8),
    _SystemAlarmNTPSynchronisation_Type()
)
systemAlarmNTPSynchronisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmNTPSynchronisation.setStatus("current")
_SystemAlarm1PPSAbsent_Type = AlarmState
_SystemAlarm1PPSAbsent_Object = MibScalar
systemAlarm1PPSAbsent = _SystemAlarm1PPSAbsent_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 9),
    _SystemAlarm1PPSAbsent_Type()
)
systemAlarm1PPSAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarm1PPSAbsent.setStatus("current")
_SystemAlarmQoSTransmitBuffer_Type = AlarmState
_SystemAlarmQoSTransmitBuffer_Object = MibScalar
systemAlarmQoSTransmitBuffer = _SystemAlarmQoSTransmitBuffer_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 10),
    _SystemAlarmQoSTransmitBuffer_Type()
)
systemAlarmQoSTransmitBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmQoSTransmitBuffer.setStatus("current")
_SystemAlarmCartesianLoopUnstable_Type = AlarmState
_SystemAlarmCartesianLoopUnstable_Object = MibScalar
systemAlarmCartesianLoopUnstable = _SystemAlarmCartesianLoopUnstable_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 11),
    _SystemAlarmCartesianLoopUnstable_Type()
)
systemAlarmCartesianLoopUnstable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmCartesianLoopUnstable.setStatus("current")
_SystemAlarmTxRCableAbsent_Type = AlarmState
_SystemAlarmTxRCableAbsent_Object = MibScalar
systemAlarmTxRCableAbsent = _SystemAlarmTxRCableAbsent_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 3, 8, 12),
    _SystemAlarmTxRCableAbsent_Type()
)
systemAlarmTxRCableAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmTxRCableAbsent.setStatus("current")
_NetworkLinks_ObjectIdentity = ObjectIdentity
networkLinks = _NetworkLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4)
)
_NetworkLinksSummary_ObjectIdentity = ObjectIdentity
networkLinksSummary = _NetworkLinksSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1)
)
_LinkInfo_ObjectIdentity = ObjectIdentity
linkInfo = _LinkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1)
)
_LinkInfoCtrlProtocolStatus_Type = ControlProtocolStatus
_LinkInfoCtrlProtocolStatus_Object = MibScalar
linkInfoCtrlProtocolStatus = _LinkInfoCtrlProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1, 1),
    _LinkInfoCtrlProtocolStatus_Type()
)
linkInfoCtrlProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInfoCtrlProtocolStatus.setStatus("current")
_LinkInfoNetworkPacketCount_Type = Counter32
_LinkInfoNetworkPacketCount_Object = MibScalar
linkInfoNetworkPacketCount = _LinkInfoNetworkPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1, 2),
    _LinkInfoNetworkPacketCount_Type()
)
linkInfoNetworkPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInfoNetworkPacketCount.setStatus("current")
_LinkInfoMPTCtrlProtocolStatus_Type = MPTControlProtocolStatus
_LinkInfoMPTCtrlProtocolStatus_Object = MibScalar
linkInfoMPTCtrlProtocolStatus = _LinkInfoMPTCtrlProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1, 3),
    _LinkInfoMPTCtrlProtocolStatus_Type()
)
linkInfoMPTCtrlProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInfoMPTCtrlProtocolStatus.setStatus("current")
_LinkInfoDMRNodeIPAddress_Type = SnmpAdminString
_LinkInfoDMRNodeIPAddress_Object = MibScalar
linkInfoDMRNodeIPAddress = _LinkInfoDMRNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1, 4),
    _LinkInfoDMRNodeIPAddress_Type()
)
linkInfoDMRNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInfoDMRNodeIPAddress.setStatus("current")
_LinkInfoDMRNodePriority_Type = Unsigned32
_LinkInfoDMRNodePriority_Object = MibScalar
linkInfoDMRNodePriority = _LinkInfoDMRNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1, 5),
    _LinkInfoDMRNodePriority_Type()
)
linkInfoDMRNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInfoDMRNodePriority.setStatus("current")
_LinkInfoMPTNodeIPAddress_Type = SnmpAdminString
_LinkInfoMPTNodeIPAddress_Object = MibScalar
linkInfoMPTNodeIPAddress = _LinkInfoMPTNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1, 6),
    _LinkInfoMPTNodeIPAddress_Type()
)
linkInfoMPTNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInfoMPTNodeIPAddress.setStatus("current")
_LinkInfoMPTNodePriority_Type = Unsigned32
_LinkInfoMPTNodePriority_Object = MibScalar
linkInfoMPTNodePriority = _LinkInfoMPTNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 1, 7),
    _LinkInfoMPTNodePriority_Type()
)
linkInfoMPTNodePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkInfoMPTNodePriority.setStatus("current")
_LinkHealth_ObjectIdentity = ObjectIdentity
linkHealth = _LinkHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 2)
)
_LinkHealthNetworkPacketLostCount_Type = Counter32
_LinkHealthNetworkPacketLostCount_Object = MibScalar
linkHealthNetworkPacketLostCount = _LinkHealthNetworkPacketLostCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 2, 2),
    _LinkHealthNetworkPacketLostCount_Type()
)
linkHealthNetworkPacketLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkHealthNetworkPacketLostCount.setStatus("current")
_LinkHealthNetworkJitterLastOver_Type = Unsigned32
_LinkHealthNetworkJitterLastOver_Object = MibScalar
linkHealthNetworkJitterLastOver = _LinkHealthNetworkJitterLastOver_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 2, 3),
    _LinkHealthNetworkJitterLastOver_Type()
)
linkHealthNetworkJitterLastOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkHealthNetworkJitterLastOver.setStatus("current")
_LinkHealthNetworkJitterCount_Type = Counter32
_LinkHealthNetworkJitterCount_Object = MibScalar
linkHealthNetworkJitterCount = _LinkHealthNetworkJitterCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 2, 4),
    _LinkHealthNetworkJitterCount_Type()
)
linkHealthNetworkJitterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkHealthNetworkJitterCount.setStatus("current")
_LinkHealthSequenceErrorsCount_Type = Counter32
_LinkHealthSequenceErrorsCount_Object = MibScalar
linkHealthSequenceErrorsCount = _LinkHealthSequenceErrorsCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 4, 1, 2, 5),
    _LinkHealthSequenceErrorsCount_Type()
)
linkHealthSequenceErrorsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkHealthSequenceErrorsCount.setStatus("current")
_NetworkInterfaces_ObjectIdentity = ObjectIdentity
networkInterfaces = _NetworkInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5)
)
_NwNtpInterface_ObjectIdentity = ObjectIdentity
nwNtpInterface = _NwNtpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 1)
)
_NwConfiguredNtpServerAddress_Type = DisplayString
_NwConfiguredNtpServerAddress_Object = MibScalar
nwConfiguredNtpServerAddress = _NwConfiguredNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 1, 1),
    _NwConfiguredNtpServerAddress_Type()
)
nwConfiguredNtpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConfiguredNtpServerAddress.setStatus("current")
_NwConfiguredNtpBackupServerAddress1_Type = DisplayString
_NwConfiguredNtpBackupServerAddress1_Object = MibScalar
nwConfiguredNtpBackupServerAddress1 = _NwConfiguredNtpBackupServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 1, 2),
    _NwConfiguredNtpBackupServerAddress1_Type()
)
nwConfiguredNtpBackupServerAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConfiguredNtpBackupServerAddress1.setStatus("current")
_NwConfiguredNtpBackupServerAddress2_Type = DisplayString
_NwConfiguredNtpBackupServerAddress2_Object = MibScalar
nwConfiguredNtpBackupServerAddress2 = _NwConfiguredNtpBackupServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 1, 3),
    _NwConfiguredNtpBackupServerAddress2_Type()
)
nwConfiguredNtpBackupServerAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwConfiguredNtpBackupServerAddress2.setStatus("current")
_NwChannelGroup_ObjectIdentity = ObjectIdentity
nwChannelGroup = _NwChannelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2)
)
_NwChannelGroupStatus_Type = ChannelGroupStatus
_NwChannelGroupStatus_Object = MibScalar
nwChannelGroupStatus = _NwChannelGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 1),
    _NwChannelGroupStatus_Type()
)
nwChannelGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupStatus.setStatus("current")
_NwChannelGroupLocalBufferLevel_Type = Milliseconds
_NwChannelGroupLocalBufferLevel_Object = MibScalar
nwChannelGroupLocalBufferLevel = _NwChannelGroupLocalBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 2),
    _NwChannelGroupLocalBufferLevel_Type()
)
nwChannelGroupLocalBufferLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupLocalBufferLevel.setStatus("current")
_NwChannelGroupEmptiestBufferLevel_Type = Milliseconds
_NwChannelGroupEmptiestBufferLevel_Object = MibScalar
nwChannelGroupEmptiestBufferLevel = _NwChannelGroupEmptiestBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 3),
    _NwChannelGroupEmptiestBufferLevel_Type()
)
nwChannelGroupEmptiestBufferLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupEmptiestBufferLevel.setStatus("current")
_NwChannelGroupMarshallingType_Type = TimingControlType
_NwChannelGroupMarshallingType_Object = MibScalar
nwChannelGroupMarshallingType = _NwChannelGroupMarshallingType_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 4),
    _NwChannelGroupMarshallingType_Type()
)
nwChannelGroupMarshallingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupMarshallingType.setStatus("current")
_NwChannelGroupMarshallingDuration_Type = Milliseconds
_NwChannelGroupMarshallingDuration_Object = MibScalar
nwChannelGroupMarshallingDuration = _NwChannelGroupMarshallingDuration_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 5),
    _NwChannelGroupMarshallingDuration_Type()
)
nwChannelGroupMarshallingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupMarshallingDuration.setStatus("current")
_NwChannelGroupReceiverSynchStatus_Type = ReceiverSyncStatus
_NwChannelGroupReceiverSynchStatus_Object = MibScalar
nwChannelGroupReceiverSynchStatus = _NwChannelGroupReceiverSynchStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 6),
    _NwChannelGroupReceiverSynchStatus_Type()
)
nwChannelGroupReceiverSynchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupReceiverSynchStatus.setStatus("current")
_NwChannelGroupTransmitterSynchStatus_Type = TransmitterSyncStatus
_NwChannelGroupTransmitterSynchStatus_Object = MibScalar
nwChannelGroupTransmitterSynchStatus = _NwChannelGroupTransmitterSynchStatus_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 7),
    _NwChannelGroupTransmitterSynchStatus_Type()
)
nwChannelGroupTransmitterSynchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupTransmitterSynchStatus.setStatus("current")
_NwChannelGroupLateStreamsCount_Type = Counter32
_NwChannelGroupLateStreamsCount_Object = MibScalar
nwChannelGroupLateStreamsCount = _NwChannelGroupLateStreamsCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 8),
    _NwChannelGroupLateStreamsCount_Type()
)
nwChannelGroupLateStreamsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupLateStreamsCount.setStatus("current")
_NwChannelGroupOverflowCount_Type = Counter32
_NwChannelGroupOverflowCount_Object = MibScalar
nwChannelGroupOverflowCount = _NwChannelGroupOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 9),
    _NwChannelGroupOverflowCount_Type()
)
nwChannelGroupOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupOverflowCount.setStatus("current")
_NwChannelGroupUnderflowCount_Type = Counter32
_NwChannelGroupUnderflowCount_Object = MibScalar
nwChannelGroupUnderflowCount = _NwChannelGroupUnderflowCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 10),
    _NwChannelGroupUnderflowCount_Type()
)
nwChannelGroupUnderflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupUnderflowCount.setStatus("current")
_NwChannelGroupLostPacketsCount_Type = Counter32
_NwChannelGroupLostPacketsCount_Object = MibScalar
nwChannelGroupLostPacketsCount = _NwChannelGroupLostPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 11),
    _NwChannelGroupLostPacketsCount_Type()
)
nwChannelGroupLostPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupLostPacketsCount.setStatus("current")
_NwChannelGroupJitter_Type = Integer32
_NwChannelGroupJitter_Object = MibScalar
nwChannelGroupJitter = _NwChannelGroupJitter_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 2, 12),
    _NwChannelGroupJitter_Type()
)
nwChannelGroupJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwChannelGroupJitter.setStatus("current")
_NwPorts_ObjectIdentity = ObjectIdentity
nwPorts = _NwPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 3)
)
_NwSvpPort_Type = Unsigned32
_NwSvpPort_Object = MibScalar
nwSvpPort = _NwSvpPort_Object(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 1, 5, 3, 1),
    _NwSvpPort_Type()
)
nwSvpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwSvpPort.setStatus("current")
_MibConformance_ObjectIdentity = ObjectIdentity
mibConformance = _MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5)
)
_MibGroups_ObjectIdentity = ObjectIdentity
mibGroups = _MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1)
)
_MibCompliance_ObjectIdentity = ObjectIdentity
mibCompliance = _MibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 2)
)

# Managed Objects groups

healthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 1)
)
healthGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "healthRunMode"),
        ("TAIT-INFRA93SERIES-MIB", "healthNetworkConnLogChan1State"),
        ("TAIT-INFRA93SERIES-MIB", "healthNetworkConnLogChan2State"),
        ("TAIT-INFRA93SERIES-MIB", "healthSecureShellRunning"))
)
if mibBuilder.loadTexts:
    healthGroup.setStatus("current")

alarmSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 2)
)
alarmSummaryGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "alarmSummaryPowerAmplifier"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryFrontPanel"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryReciter"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryBaseStation"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummarySystem"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryPowerManagementUnit"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryCustomAlarms"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryMinor"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryMajor"))
)
if mibBuilder.loadTexts:
    alarmSummaryGroup.setStatus("current")

rctSelectedChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 3)
)
rctSelectedChannelGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelNumber"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelName"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelProfileName"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelSigProfileName"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelTransmitPower"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelTxFreq"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelRxFreq"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelSystemType"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelColourCode"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelGroupName"))
)
if mibBuilder.loadTexts:
    rctSelectedChannelGroup.setStatus("current")

paTxOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 5)
)
paTxOutputGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "paTxOutputForwardPower"),
        ("TAIT-INFRA93SERIES-MIB", "paTxOutputVSWR"))
)
if mibBuilder.loadTexts:
    paTxOutputGroup.setStatus("current")

linkInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 6)
)
linkInfoGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "linkInfoCtrlProtocolStatus"),
        ("TAIT-INFRA93SERIES-MIB", "linkInfoNetworkPacketCount"),
        ("TAIT-INFRA93SERIES-MIB", "linkInfoMPTCtrlProtocolStatus"),
        ("TAIT-INFRA93SERIES-MIB", "linkInfoDMRNodeIPAddress"),
        ("TAIT-INFRA93SERIES-MIB", "linkInfoDMRNodePriority"),
        ("TAIT-INFRA93SERIES-MIB", "linkInfoMPTNodeIPAddress"),
        ("TAIT-INFRA93SERIES-MIB", "linkInfoMPTNodePriority"),
        ("TAIT-INFRA93SERIES-MIB", "linkHealthSequenceErrorsCount"),
        ("TAIT-INFRA93SERIES-MIB", "linkHealthNetworkPacketLostCount"),
        ("TAIT-INFRA93SERIES-MIB", "linkHealthNetworkJitterLastOver"),
        ("TAIT-INFRA93SERIES-MIB", "linkHealthNetworkJitterCount"))
)
if mibBuilder.loadTexts:
    linkInfoGroup.setStatus("current")

customAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 7)
)
customAlarmsGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "customAlarm1"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm2"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm3"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm4"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm5"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm6"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm7"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm8"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm9"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm10"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm11"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarm12"))
)
if mibBuilder.loadTexts:
    customAlarmsGroup.setStatus("current")

systemAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 8)
)
systemAlarmsGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "systemAlarmExternalRefAbsent"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmAmbientTempHigh"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmAmbientTempLow"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmQoSJitter"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmQoSLostPackets"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmFallbackControlled"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmDuplicateNodePriority"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmNTPSynchronisation"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarm1PPSAbsent"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmQoSTransmitBuffer"))
)
if mibBuilder.loadTexts:
    systemAlarmsGroup.setStatus("current")

fpAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 9)
)
fpAlarmsGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "fpAlarmInvalidFirmware"),
        ("TAIT-INFRA93SERIES-MIB", "fpAlarmFan2"),
        ("TAIT-INFRA93SERIES-MIB", "fpAlarmNoFPDetected"),
        ("TAIT-INFRA93SERIES-MIB", "fpAlarmFan3"),
        ("TAIT-INFRA93SERIES-MIB", "fpAlarmFan1"))
)
if mibBuilder.loadTexts:
    fpAlarmsGroup.setStatus("current")

paAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 10)
)
paAlarmsGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "paAlarmFinal1CurrentHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmDriverCurrentHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmSupplyVoltageLow"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmFinal2TemperatureHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmFinal2CurrentHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmVSWRFault"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmDriverTemperatureHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmForwardPowerLow"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmNoPADetected"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmFinal1TemperatureHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmSupplyVoltageHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmPowerFoldback"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmInvalidCalibration"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmInvalidFirmware"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmShutdownImminent"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmReversePowerHigh"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmCurrentImbalance"))
)
if mibBuilder.loadTexts:
    paAlarmsGroup.setStatus("current")

pmuAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 11)
)
pmuAlarmsGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "pmuAlarmMainsFailure"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmBatteryVoltageLow"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmBatteryVoltageHigh"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmBatteryProtect"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmInvalidFirmware"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmVoltageOutHigh"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmNoPMUDetected"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmVoltageOutLow"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmShutdownImminent"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmCurrentOutHigh"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmSelfTestFailure"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmTemperatureHigh"))
)
if mibBuilder.loadTexts:
    pmuAlarmsGroup.setStatus("current")

reciterAlarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 12)
)
reciterAlarmsGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctAlarmRxSynthOutOfLock"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmInvalidChannelSelected"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmRxCalibrationInvalid"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmOverTemperature"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmInvalidConfiguration"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarm25MHzSynthOutOfLock"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmTxCalibrationInvalid"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmTxFSynthOutOfLock"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarm6144MHzSynthOutOfLock"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmSimulcastSynch"),
        ("TAIT-INFRA93SERIES-MIB", "rctAlarmReceiverSynch"))
)
if mibBuilder.loadTexts:
    reciterAlarmsGroup.setStatus("current")

infoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 13)
)
infoGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "infoTransmitterStatus"),
        ("TAIT-INFRA93SERIES-MIB", "infoMPTFallbackNodeStatus"),
        ("TAIT-INFRA93SERIES-MIB", "infoDMRFallbackNodeStatus"),
        ("TAIT-INFRA93SERIES-MIB", "rctInfoProductCode"),
        ("TAIT-INFRA93SERIES-MIB", "rctInfoSerialNumber"),
        ("TAIT-INFRA93SERIES-MIB", "rctInfoHardwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "rctInfoFirmwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "paInfoProductCode"),
        ("TAIT-INFRA93SERIES-MIB", "paInfoSerialNumber"),
        ("TAIT-INFRA93SERIES-MIB", "paInfoHardwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "paInfoFirmwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "fpInfoProductCode"),
        ("TAIT-INFRA93SERIES-MIB", "fpInfoSerialNumber"),
        ("TAIT-INFRA93SERIES-MIB", "fpInfoHardwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "fpInfoFirmwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "licenceDmrFull"),
        ("TAIT-INFRA93SERIES-MIB", "licenceDmrExpress"),
        ("TAIT-INFRA93SERIES-MIB", "licenceDmrAccess"),
        ("TAIT-INFRA93SERIES-MIB", "licenceDmrConventional"),
        ("TAIT-INFRA93SERIES-MIB", "licenceAnalogConventional"),
        ("TAIT-INFRA93SERIES-MIB", "licenceDmrExpress20"),
        ("TAIT-INFRA93SERIES-MIB", "licenceDmrCentralVoter"),
        ("TAIT-INFRA93SERIES-MIB", "licenceDmrNetworkSatellite"))
)
if mibBuilder.loadTexts:
    infoGroup.setStatus("current")

rctReceiveQualityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 14)
)
rctReceiveQualityGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctRfRcvInterference"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfInterferenceCounter"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfInterferenceEvents"))
)
if mibBuilder.loadTexts:
    rctReceiveQualityGroup.setStatus("current")

rctReceiverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 15)
)
rctReceiverGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctRfReceiverRSSI"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverLC1RSSI"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverLC2RSSI"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverLC1RxGateState"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverLC2RxGateState"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverSelectedDecodeCTCSS"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverSelectedDecodeSubAudibleType"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverSelectedSINADGatingLevel"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverSelectedDecodeDCS"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverSelectedFrequencyResponse"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverAnalogGateState"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfReceiverIsDisabled"))
)
if mibBuilder.loadTexts:
    rctReceiverGroup.setStatus("current")

rctTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 16)
)
rctTemperatureGroup.setObjects(
    ("TAIT-INFRA93SERIES-MIB", "rctTemperatureBoard")
)
if mibBuilder.loadTexts:
    rctTemperatureGroup.setStatus("current")

pmuStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 17)
)
pmuStateGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "pmuStateMainsInState"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateBatteryInState"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateBatteryInVoltage"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateOutCurrent"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateOutVoltage"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateOutStatus"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateAuxOutState"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateBusConnect"))
)
if mibBuilder.loadTexts:
    pmuStateGroup.setStatus("current")

nwNtpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 18)
)
nwNtpInterfaceGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "nwConfiguredNtpServerAddress"),
        ("TAIT-INFRA93SERIES-MIB", "nwConfiguredNtpBackupServerAddress1"),
        ("TAIT-INFRA93SERIES-MIB", "nwConfiguredNtpBackupServerAddress2"))
)
if mibBuilder.loadTexts:
    nwNtpInterfaceGroup.setStatus("current")

rctTransmitterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 19)
)
rctTransmitterGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctRfTxSelectedEncodeCTCSS"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfTxSelectedEncodeSubAudibleType"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfTxSelectFrequencyResponse"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfTxSelectedEncodeDCS"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfTxSelectedEncodeSubAudibleDeviation"),
        ("TAIT-INFRA93SERIES-MIB", "rctRfTxRfRepeatState"))
)
if mibBuilder.loadTexts:
    rctTransmitterGroup.setStatus("current")

nwChannelGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 20)
)
nwChannelGroupGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "nwChannelGroupStatus"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupLocalBufferLevel"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupEmptiestBufferLevel"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupMarshallingType"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupMarshallingDuration"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupReceiverSynchStatus"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupTransmitterSynchStatus"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupLateStreamsCount"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupOverflowCount"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupUnderflowCount"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupLostPacketsCount"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupJitter"))
)
if mibBuilder.loadTexts:
    nwChannelGroupGroup.setStatus("current")

nwPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 21)
)
nwPortsGroup.setObjects(
    ("TAIT-INFRA93SERIES-MIB", "nwSvpPort")
)
if mibBuilder.loadTexts:
    nwPortsGroup.setStatus("current")

rctSystemInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 22)
)
rctSystemInterfaceGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctSiConfiguredBalancedLineInLevel"),
        ("TAIT-INFRA93SERIES-MIB", "rctSiConfiguredBalancedLineOutLevel"),
        ("TAIT-INFRA93SERIES-MIB", "rctSiTxKey"),
        ("TAIT-INFRA93SERIES-MIB", "rctSiRxGate"))
)
if mibBuilder.loadTexts:
    rctSystemInterfaceGroup.setStatus("current")

linearTransmissionCapability = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 23)
)
linearTransmissionCapability.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctAlarmTxRSynthOutOfLock"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmCartesianLoopUnstable"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmTxRCableAbsent"))
)
if mibBuilder.loadTexts:
    linearTransmissionCapability.setStatus("current")

pmuInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 24)
)
pmuInfoGroup.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "pmuInfoProductCode"),
        ("TAIT-INFRA93SERIES-MIB", "pmuInfoSerialNumber"),
        ("TAIT-INFRA93SERIES-MIB", "pmuInfoHardwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "pmuInfoFirmwareVersion"),
        ("TAIT-INFRA93SERIES-MIB", "pmuInfoCalibrationUpdateDate"))
)
if mibBuilder.loadTexts:
    pmuInfoGroup.setStatus("current")

deprecatedOidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 1, 27)
)
deprecatedOidGroup.setObjects(
    ("TAIT-INFRA93SERIES-MIB", "infoStandaloneNodeStatus")
)
if mibBuilder.loadTexts:
    deprecatedOidGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mibComplianceList = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3570, 2, 2, 2, 5, 2, 1)
)
mibComplianceList.setObjects(
      *(("TAIT-INFRA93SERIES-MIB", "rctTransmitterGroup"),
        ("TAIT-INFRA93SERIES-MIB", "rctReceiverGroup"),
        ("TAIT-INFRA93SERIES-MIB", "rctReceiveQualityGroup"),
        ("TAIT-INFRA93SERIES-MIB", "infoGroup"),
        ("TAIT-INFRA93SERIES-MIB", "healthGroup"),
        ("TAIT-INFRA93SERIES-MIB", "alarmSummaryGroup"),
        ("TAIT-INFRA93SERIES-MIB", "rctSelectedChannelGroup"),
        ("TAIT-INFRA93SERIES-MIB", "paTxOutputGroup"),
        ("TAIT-INFRA93SERIES-MIB", "linkInfoGroup"),
        ("TAIT-INFRA93SERIES-MIB", "customAlarmsGroup"),
        ("TAIT-INFRA93SERIES-MIB", "systemAlarmsGroup"),
        ("TAIT-INFRA93SERIES-MIB", "fpAlarmsGroup"),
        ("TAIT-INFRA93SERIES-MIB", "paAlarmsGroup"),
        ("TAIT-INFRA93SERIES-MIB", "reciterAlarmsGroup"),
        ("TAIT-INFRA93SERIES-MIB", "rctTemperatureGroup"),
        ("TAIT-INFRA93SERIES-MIB", "nwNtpInterfaceGroup"),
        ("TAIT-INFRA93SERIES-MIB", "nwChannelGroupGroup"),
        ("TAIT-INFRA93SERIES-MIB", "nwPortsGroup"),
        ("TAIT-INFRA93SERIES-MIB", "linearTransmissionCapability"),
        ("TAIT-INFRA93SERIES-MIB", "pmuAlarmsGroup"),
        ("TAIT-INFRA93SERIES-MIB", "pmuInfoGroup"),
        ("TAIT-INFRA93SERIES-MIB", "pmuStateGroup"))
)
if mibBuilder.loadTexts:
    mibComplianceList.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TAIT-INFRA93SERIES-MIB",
    **{"infra93MibMonitored": infra93MibMonitored,
       "infra93MIB": infra93MIB,
       "monitored": monitored,
       "mibObjects": mibObjects,
       "productInfo": productInfo,
       "productSummary": productSummary,
       "info": info,
       "infoTransmitterStatus": infoTransmitterStatus,
       "infoStandaloneNodeStatus": infoStandaloneNodeStatus,
       "infoMPTFallbackNodeStatus": infoMPTFallbackNodeStatus,
       "infoDMRFallbackNodeStatus": infoDMRFallbackNodeStatus,
       "health": health,
       "healthRunMode": healthRunMode,
       "healthNetworkConnLogChan1State": healthNetworkConnLogChan1State,
       "healthNetworkConnLogChan2State": healthNetworkConnLogChan2State,
       "healthSecureShellRunning": healthSecureShellRunning,
       "productEnabledFeatures": productEnabledFeatures,
       "licenceDmrFull": licenceDmrFull,
       "licenceAnalogConventional": licenceAnalogConventional,
       "licenceDmrExpress": licenceDmrExpress,
       "licenceDmrAccess": licenceDmrAccess,
       "licenceDmrConventional": licenceDmrConventional,
       "licenceDmrExpress20": licenceDmrExpress20,
       "licenceDmrCentralVoter": licenceDmrCentralVoter,
       "licenceDmrNetworkSatellite": licenceDmrNetworkSatellite,
       "modules": modules,
       "reciter": reciter,
       "rctSummary": rctSummary,
       "rctInfo": rctInfo,
       "rctInfoProductCode": rctInfoProductCode,
       "rctInfoSerialNumber": rctInfoSerialNumber,
       "rctInfoHardwareVersion": rctInfoHardwareVersion,
       "rctInfoFirmwareVersion": rctInfoFirmwareVersion,
       "rctHealth": rctHealth,
       "rctSelectedChannel": rctSelectedChannel,
       "rctSelectedChannelNumber": rctSelectedChannelNumber,
       "rctSelectedChannelName": rctSelectedChannelName,
       "rctSelectedChannelProfileName": rctSelectedChannelProfileName,
       "rctSelectedChannelSigProfileName": rctSelectedChannelSigProfileName,
       "rctSelectedChannelTransmitPower": rctSelectedChannelTransmitPower,
       "rctSelectedChannelTxFreq": rctSelectedChannelTxFreq,
       "rctSelectedChannelRxFreq": rctSelectedChannelRxFreq,
       "rctSelectedChannelSystemType": rctSelectedChannelSystemType,
       "rctSelectedChannelColourCode": rctSelectedChannelColourCode,
       "rctSelectedChannelGroupName": rctSelectedChannelGroupName,
       "rctRfReceiveQuality": rctRfReceiveQuality,
       "rctRfRcvInterference": rctRfRcvInterference,
       "rctRfInterferenceCounter": rctRfInterferenceCounter,
       "rctRfInterferenceEvents": rctRfInterferenceEvents,
       "rctRfReceiver": rctRfReceiver,
       "rctRfReceiverRSSI": rctRfReceiverRSSI,
       "rctRfReceiverLC1RSSI": rctRfReceiverLC1RSSI,
       "rctRfReceiverLC2RSSI": rctRfReceiverLC2RSSI,
       "rctRfReceiverLC1RxGateState": rctRfReceiverLC1RxGateState,
       "rctRfReceiverLC2RxGateState": rctRfReceiverLC2RxGateState,
       "rctRfReceiverSelectedDecodeCTCSS": rctRfReceiverSelectedDecodeCTCSS,
       "rctRfReceiverSelectedDecodeSubAudibleType": rctRfReceiverSelectedDecodeSubAudibleType,
       "rctRfReceiverSelectedSINADGatingLevel": rctRfReceiverSelectedSINADGatingLevel,
       "rctRfReceiverSelectedDecodeDCS": rctRfReceiverSelectedDecodeDCS,
       "rctRfReceiverSelectedFrequencyResponse": rctRfReceiverSelectedFrequencyResponse,
       "rctRfReceiverAnalogGateState": rctRfReceiverAnalogGateState,
       "rctRfReceiverIsDisabled": rctRfReceiverIsDisabled,
       "rctRfTransmitter": rctRfTransmitter,
       "rctRfTxSelectedEncodeCTCSS": rctRfTxSelectedEncodeCTCSS,
       "rctRfTxSelectedEncodeSubAudibleType": rctRfTxSelectedEncodeSubAudibleType,
       "rctRfTxSelectFrequencyResponse": rctRfTxSelectFrequencyResponse,
       "rctRfTxSelectedEncodeDCS": rctRfTxSelectedEncodeDCS,
       "rctRfTxSelectedEncodeSubAudibleDeviation": rctRfTxSelectedEncodeSubAudibleDeviation,
       "rctRfTxRfRepeatState": rctRfTxRfRepeatState,
       "rctTemperature": rctTemperature,
       "rctTemperatureBoard": rctTemperatureBoard,
       "rctSystemInterface": rctSystemInterface,
       "rctSiConfiguredBalancedLineInLevel": rctSiConfiguredBalancedLineInLevel,
       "rctSiConfiguredBalancedLineOutLevel": rctSiConfiguredBalancedLineOutLevel,
       "rctSiTxKey": rctSiTxKey,
       "rctSiRxGate": rctSiRxGate,
       "powerAmplifier": powerAmplifier,
       "paSummary": paSummary,
       "paInfo": paInfo,
       "paInfoProductCode": paInfoProductCode,
       "paInfoSerialNumber": paInfoSerialNumber,
       "paInfoHardwareVersion": paInfoHardwareVersion,
       "paInfoFirmwareVersion": paInfoFirmwareVersion,
       "paHealth": paHealth,
       "paTxOutput": paTxOutput,
       "paTxOutputForwardPower": paTxOutputForwardPower,
       "paTxOutputVSWR": paTxOutputVSWR,
       "paTemperature": paTemperature,
       "paGeneral": paGeneral,
       "powerManagementUnit": powerManagementUnit,
       "pmuSummary": pmuSummary,
       "pmuInfo": pmuInfo,
       "pmuInfoProductCode": pmuInfoProductCode,
       "pmuInfoSerialNumber": pmuInfoSerialNumber,
       "pmuInfoHardwareVersion": pmuInfoHardwareVersion,
       "pmuInfoFirmwareVersion": pmuInfoFirmwareVersion,
       "pmuInfoCalibrationUpdateDate": pmuInfoCalibrationUpdateDate,
       "pmuHealth": pmuHealth,
       "pmuSubmodules": pmuSubmodules,
       "pmuState": pmuState,
       "pmuStateMainsInState": pmuStateMainsInState,
       "pmuStateBatteryInState": pmuStateBatteryInState,
       "pmuStateBatteryInVoltage": pmuStateBatteryInVoltage,
       "pmuStateOutCurrent": pmuStateOutCurrent,
       "pmuStateOutVoltage": pmuStateOutVoltage,
       "pmuStateOutStatus": pmuStateOutStatus,
       "pmuStateAuxOutState": pmuStateAuxOutState,
       "pmuStateBusConnect": pmuStateBusConnect,
       "frontPanel": frontPanel,
       "fpSummary": fpSummary,
       "fpInfo": fpInfo,
       "fpInfoProductCode": fpInfoProductCode,
       "fpInfoSerialNumber": fpInfoSerialNumber,
       "fpInfoHardwareVersion": fpInfoHardwareVersion,
       "fpInfoFirmwareVersion": fpInfoFirmwareVersion,
       "fpHealth": fpHealth,
       "alarms": alarms,
       "alarmSummary": alarmSummary,
       "alarmSummaryBaseStation": alarmSummaryBaseStation,
       "alarmSummaryReciter": alarmSummaryReciter,
       "alarmSummaryPowerAmplifier": alarmSummaryPowerAmplifier,
       "alarmSummaryPowerManagementUnit": alarmSummaryPowerManagementUnit,
       "alarmSummaryCustomAlarms": alarmSummaryCustomAlarms,
       "alarmSummaryFrontPanel": alarmSummaryFrontPanel,
       "alarmSummarySystem": alarmSummarySystem,
       "alarmSummaryMinor": alarmSummaryMinor,
       "alarmSummaryMajor": alarmSummaryMajor,
       "reciterAlarms": reciterAlarms,
       "rctAlarmRxSynthOutOfLock": rctAlarmRxSynthOutOfLock,
       "rctAlarmInvalidChannelSelected": rctAlarmInvalidChannelSelected,
       "rctAlarmOverTemperature": rctAlarmOverTemperature,
       "rctAlarmTxCalibrationInvalid": rctAlarmTxCalibrationInvalid,
       "rctAlarmRxCalibrationInvalid": rctAlarmRxCalibrationInvalid,
       "rctAlarmInvalidConfiguration": rctAlarmInvalidConfiguration,
       "rctAlarm25MHzSynthOutOfLock": rctAlarm25MHzSynthOutOfLock,
       "rctAlarm6144MHzSynthOutOfLock": rctAlarm6144MHzSynthOutOfLock,
       "rctAlarmTxFSynthOutOfLock": rctAlarmTxFSynthOutOfLock,
       "rctAlarmSimulcastSynch": rctAlarmSimulcastSynch,
       "rctAlarmReceiverSynch": rctAlarmReceiverSynch,
       "rctAlarmTxRSynthOutOfLock": rctAlarmTxRSynthOutOfLock,
       "paAlarms": paAlarms,
       "paAlarmNoPADetected": paAlarmNoPADetected,
       "paAlarmInvalidFirmware": paAlarmInvalidFirmware,
       "paAlarmInvalidCalibration": paAlarmInvalidCalibration,
       "paAlarmForwardPowerLow": paAlarmForwardPowerLow,
       "paAlarmPowerFoldback": paAlarmPowerFoldback,
       "paAlarmReversePowerHigh": paAlarmReversePowerHigh,
       "paAlarmShutdownImminent": paAlarmShutdownImminent,
       "paAlarmVSWRFault": paAlarmVSWRFault,
       "paAlarmDriverCurrentHigh": paAlarmDriverCurrentHigh,
       "paAlarmFinal1CurrentHigh": paAlarmFinal1CurrentHigh,
       "paAlarmFinal2CurrentHigh": paAlarmFinal2CurrentHigh,
       "paAlarmCurrentImbalance": paAlarmCurrentImbalance,
       "paAlarmSupplyVoltageLow": paAlarmSupplyVoltageLow,
       "paAlarmSupplyVoltageHigh": paAlarmSupplyVoltageHigh,
       "paAlarmDriverTemperatureHigh": paAlarmDriverTemperatureHigh,
       "paAlarmFinal1TemperatureHigh": paAlarmFinal1TemperatureHigh,
       "paAlarmFinal2TemperatureHigh": paAlarmFinal2TemperatureHigh,
       "pmuAlarms": pmuAlarms,
       "pmuAlarmNoPMUDetected": pmuAlarmNoPMUDetected,
       "pmuAlarmInvalidFirmware": pmuAlarmInvalidFirmware,
       "pmuAlarmMainsFailure": pmuAlarmMainsFailure,
       "pmuAlarmSelfTestFailure": pmuAlarmSelfTestFailure,
       "pmuAlarmShutdownImminent": pmuAlarmShutdownImminent,
       "pmuAlarmTemperatureHigh": pmuAlarmTemperatureHigh,
       "pmuAlarmBatteryProtect": pmuAlarmBatteryProtect,
       "pmuAlarmBatteryVoltageLow": pmuAlarmBatteryVoltageLow,
       "pmuAlarmBatteryVoltageHigh": pmuAlarmBatteryVoltageHigh,
       "pmuAlarmCurrentOutHigh": pmuAlarmCurrentOutHigh,
       "pmuAlarmVoltageOutLow": pmuAlarmVoltageOutLow,
       "pmuAlarmVoltageOutHigh": pmuAlarmVoltageOutHigh,
       "customAlarms": customAlarms,
       "customAlarm1": customAlarm1,
       "customAlarm2": customAlarm2,
       "customAlarm3": customAlarm3,
       "customAlarm4": customAlarm4,
       "customAlarm5": customAlarm5,
       "customAlarm6": customAlarm6,
       "customAlarm7": customAlarm7,
       "customAlarm8": customAlarm8,
       "customAlarm9": customAlarm9,
       "customAlarm10": customAlarm10,
       "customAlarm11": customAlarm11,
       "customAlarm12": customAlarm12,
       "fpAlarms": fpAlarms,
       "fpAlarmFan1": fpAlarmFan1,
       "fpAlarmFan2": fpAlarmFan2,
       "fpAlarmFan3": fpAlarmFan3,
       "fpAlarmNoFPDetected": fpAlarmNoFPDetected,
       "fpAlarmInvalidFirmware": fpAlarmInvalidFirmware,
       "systemAlarms": systemAlarms,
       "systemAlarmAmbientTempLow": systemAlarmAmbientTempLow,
       "systemAlarmAmbientTempHigh": systemAlarmAmbientTempHigh,
       "systemAlarmExternalRefAbsent": systemAlarmExternalRefAbsent,
       "systemAlarmQoSJitter": systemAlarmQoSJitter,
       "systemAlarmQoSLostPackets": systemAlarmQoSLostPackets,
       "systemAlarmFallbackControlled": systemAlarmFallbackControlled,
       "systemAlarmDuplicateNodePriority": systemAlarmDuplicateNodePriority,
       "systemAlarmNTPSynchronisation": systemAlarmNTPSynchronisation,
       "systemAlarm1PPSAbsent": systemAlarm1PPSAbsent,
       "systemAlarmQoSTransmitBuffer": systemAlarmQoSTransmitBuffer,
       "systemAlarmCartesianLoopUnstable": systemAlarmCartesianLoopUnstable,
       "systemAlarmTxRCableAbsent": systemAlarmTxRCableAbsent,
       "networkLinks": networkLinks,
       "networkLinksSummary": networkLinksSummary,
       "linkInfo": linkInfo,
       "linkInfoCtrlProtocolStatus": linkInfoCtrlProtocolStatus,
       "linkInfoNetworkPacketCount": linkInfoNetworkPacketCount,
       "linkInfoMPTCtrlProtocolStatus": linkInfoMPTCtrlProtocolStatus,
       "linkInfoDMRNodeIPAddress": linkInfoDMRNodeIPAddress,
       "linkInfoDMRNodePriority": linkInfoDMRNodePriority,
       "linkInfoMPTNodeIPAddress": linkInfoMPTNodeIPAddress,
       "linkInfoMPTNodePriority": linkInfoMPTNodePriority,
       "linkHealth": linkHealth,
       "linkHealthNetworkPacketLostCount": linkHealthNetworkPacketLostCount,
       "linkHealthNetworkJitterLastOver": linkHealthNetworkJitterLastOver,
       "linkHealthNetworkJitterCount": linkHealthNetworkJitterCount,
       "linkHealthSequenceErrorsCount": linkHealthSequenceErrorsCount,
       "networkInterfaces": networkInterfaces,
       "nwNtpInterface": nwNtpInterface,
       "nwConfiguredNtpServerAddress": nwConfiguredNtpServerAddress,
       "nwConfiguredNtpBackupServerAddress1": nwConfiguredNtpBackupServerAddress1,
       "nwConfiguredNtpBackupServerAddress2": nwConfiguredNtpBackupServerAddress2,
       "nwChannelGroup": nwChannelGroup,
       "nwChannelGroupStatus": nwChannelGroupStatus,
       "nwChannelGroupLocalBufferLevel": nwChannelGroupLocalBufferLevel,
       "nwChannelGroupEmptiestBufferLevel": nwChannelGroupEmptiestBufferLevel,
       "nwChannelGroupMarshallingType": nwChannelGroupMarshallingType,
       "nwChannelGroupMarshallingDuration": nwChannelGroupMarshallingDuration,
       "nwChannelGroupReceiverSynchStatus": nwChannelGroupReceiverSynchStatus,
       "nwChannelGroupTransmitterSynchStatus": nwChannelGroupTransmitterSynchStatus,
       "nwChannelGroupLateStreamsCount": nwChannelGroupLateStreamsCount,
       "nwChannelGroupOverflowCount": nwChannelGroupOverflowCount,
       "nwChannelGroupUnderflowCount": nwChannelGroupUnderflowCount,
       "nwChannelGroupLostPacketsCount": nwChannelGroupLostPacketsCount,
       "nwChannelGroupJitter": nwChannelGroupJitter,
       "nwPorts": nwPorts,
       "nwSvpPort": nwSvpPort,
       "mibConformance": mibConformance,
       "mibGroups": mibGroups,
       "healthGroup": healthGroup,
       "alarmSummaryGroup": alarmSummaryGroup,
       "rctSelectedChannelGroup": rctSelectedChannelGroup,
       "paTxOutputGroup": paTxOutputGroup,
       "linkInfoGroup": linkInfoGroup,
       "customAlarmsGroup": customAlarmsGroup,
       "systemAlarmsGroup": systemAlarmsGroup,
       "fpAlarmsGroup": fpAlarmsGroup,
       "paAlarmsGroup": paAlarmsGroup,
       "pmuAlarmsGroup": pmuAlarmsGroup,
       "reciterAlarmsGroup": reciterAlarmsGroup,
       "infoGroup": infoGroup,
       "rctReceiveQualityGroup": rctReceiveQualityGroup,
       "rctReceiverGroup": rctReceiverGroup,
       "rctTemperatureGroup": rctTemperatureGroup,
       "pmuStateGroup": pmuStateGroup,
       "nwNtpInterfaceGroup": nwNtpInterfaceGroup,
       "rctTransmitterGroup": rctTransmitterGroup,
       "nwChannelGroupGroup": nwChannelGroupGroup,
       "nwPortsGroup": nwPortsGroup,
       "rctSystemInterfaceGroup": rctSystemInterfaceGroup,
       "linearTransmissionCapability": linearTransmissionCapability,
       "pmuInfoGroup": pmuInfoGroup,
       "deprecatedOidGroup": deprecatedOidGroup,
       "mibCompliance": mibCompliance,
       "mibComplianceList": mibComplianceList}
)
