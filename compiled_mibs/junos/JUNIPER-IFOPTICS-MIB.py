# SNMP MIB module (JUNIPER-IFOPTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-IFOPTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:15 2025
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxIlaNotifications,
 jnxIplcNotifications,
 jnxOpticsMibRoot,
 jnxOpticsNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxIlaNotifications",
    "jnxIplcNotifications",
    "jnxOpticsMibRoot",
    "jnxOpticsNotifications")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxIfOpticsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1)
)
if mibBuilder.loadTexts:
    jnxIfOpticsMib.setRevisions(
        ("2016-09-28 00:00",
         "2016-09-12 20:18",
         "2015-06-24 12:42",
         "2012-01-26 00:00",
         "2012-01-26 00:00",
         "2016-05-31 00:00",
         "2018-05-02 00:00",
         "2018-08-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxOpticsLocation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jnxNearEnd", 1),
          ("jnxFarEnd", 2))
    )



class JnxOpticsDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("jnxTxDir", 1),
          ("jnxRxDir", 2),
          ("jnxBiDir", 3))
    )



class JnxOpticsSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("jnxCritical", 1),
          ("jnxMajor", 2),
          ("jnxMinor", 3),
          ("jnxInfo", 4))
    )



class JnxOpticsServiceStateAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jnxNotSupported", 0),
          ("jnxNonServiceAffecting", 1),
          ("jnxServiceAffecting", 2))
    )



class JnxOpticsChannelSpacing(TextualConvention, Integer32):
    status = "current"
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
        *(("spacing100Ghz", 1),
          ("spacing50Ghz", 2),
          ("spacing25Ghz", 3),
          ("spacing12point5Ghz", 4),
          ("spacing6point5Ghz", 5))
    )



class JnxOpticsOTIfFecType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sdfec", 1),
          ("sdfec25", 2),
          ("hgfec", 3),
          ("sdfec15", 4))
    )



class JnxOpticsOTIfEncodingOptions(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("differential", 1),
          ("non-differential", 2))
    )



class JnxOpticsOTIfAdminStates(TextualConvention, Integer32):
    status = "current"
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
        *(("jnxAdminStateInService", 1),
          ("jnxAdminStateInServiceMA", 2),
          ("jnxAdminStateOutofService", 3),
          ("jnxAdminStateOutofServiceMA", 4))
    )



class JnxOpticsOTIfOperStates(TextualConvention, Integer32):
    status = "current"
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
        *(("jnxOperStateInit", 1),
          ("jnxOperStateNormal", 2),
          ("jnxOperStateFault", 3),
          ("jnxOperStateDegraded", 4))
    )



class JnxOpticsNotificationId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("jnxOpticsLOS", 1),
          ("jnxOpticsWavelenthLockErr", 2),
          ("jnxOpticsPowerHighAlarm", 3),
          ("jnxOpticsPowerLowAlarm", 4),
          ("jnxOpticsBiasCurrentHighAlarm", 5),
          ("jnxOpticsBiasCurrentLowAlarm", 6),
          ("jnxOpticsTemperatureHighAlarm", 7),
          ("jnxOpticsTemperaturelowAlarm", 8),
          ("jnxOpticsTxPLLLockAlarm", 9),
          ("jnxOpticsRxPLLLockAlarm", 10),
          ("jnxOpticsAvgPowerAlarm", 11),
          ("jnxOpticsRxLossAvgPowerAlarm", 12),
          ("jnxOpticsLossofACPowerAlarm", 13),
          ("jnxOpticsTxPowerHighThreshAlert", 14),
          ("jnxOpticsTxPowerLowThreshAlert", 15),
          ("jnxOpticsRxPowerHighThreshAlert", 16),
          ("jnxOpticsRxPowerLowThreshAlert", 17),
          ("jnxOpticsModuleTempHighThreshAlert", 18),
          ("jnxOpticsModuleTempLowThreshAlert", 19),
          ("jnxOptics24HourTxPowerHighThreshAlert", 20),
          ("jnxOptics24HourTxPowerLowThreshAlert", 21),
          ("jnxOptics24HourRxPowerHighThreshAlert", 22),
          ("jnxOptics24HourRxPowerLowThreshAlert", 23),
          ("jnxOptics24HourModuleTempHighThreshAlert", 24),
          ("jnxOptics24HourModuleTempLowThreshAlert", 25),
          ("jnxOpticsRxPowerHighAlarm", 26),
          ("jnxOpticsRxPowerLowAlarm", 27),
          ("jnxOpticsTxPowerHighWarning", 28),
          ("jnxOpticsTxPowerLowWarning", 29),
          ("jnxOpticsRxPowerHighWarning", 30),
          ("jnxOpticsRxPowerLowWarning", 31),
          ("jnxOpticsModuleTempHighWarning", 32),
          ("jnxOpticsModuleTempLowWarning", 33),
          ("jnxOpticsRxCarrierFreqHigh", 34),
          ("jnxOpticsRxCarrierFreqLow", 35),
          ("jnxOpticsChromaticDispHighWarning", 36),
          ("jnxOpticsChromaticDispLowWarning", 37),
          ("jnxOpticsQLowWarning", 38),
          ("jnxOpticsOSNRLowWarning", 39),
          ("jnxOpticsCarrierFreqHighAlert", 40),
          ("jnxOpticsCarrierFreqLowAlert", 41),
          ("jnxOptics24HourCarrierFreqHighAlert", 42),
          ("jnxOptics24HourCarrierFreqLowAlert", 43),
          ("jnxOpticsLossOfLock", 44),
          ("jnxOpticsLossOfSignal", 45),
          ("jnxOpticsLossOfFrame", 46),
          ("jnxOpticsLossOfMultiFrame", 47),
          ("jnxOpticsOTUBDI", 48),
          ("jnxOpticsRxModemSYncFault", 49),
          ("jnxOpticsRxModemLOL", 50),
          ("jnxOpticsRxLOA", 51),
          ("jnxOpticsModBiasControlLoopFail", 52),
          ("jnxOpticsILTAfault", 53),
          ("jnxOpticsDACcalibrationfault", 54),
          ("jnxOpticsADCcalibrationfault", 55),
          ("jnxOpticsTecCurrentHighAlert", 56),
          ("jnxOpticsTecCurrentLowAlert", 57),
          ("jnxOpticsPamHistogramHighAlert", 58),
          ("jnxOpticsResidualIsiHighAlert", 59),
          ("jnxOpticsResidualIsiLowAlert", 60),
          ("jnxOpticsFecCorrectedErrorsHighAlert", 61),
          ("jnxOpticsFecUCorrectedWordsHighAlert", 62),
          ("jnxOptics24HourTecCurrentHighAlert", 63),
          ("jnxOptics24HourTecCurrentLowAlert", 64),
          ("jnxOptics24HourPamHistogramHighAlert", 65),
          ("jnxOptics24HourResidualIsiHighAlert", 66),
          ("jnxOptics24HourResidualIsiLowAlert", 67),
          ("jnxOptics24HourFecCorrectedErrorsHighAlert", 68),
          ("jnxOptics24HourFecUCorrectedWordsHighAlert", 69),
          ("jnxOpticsLaserFreqErrorHighAlert", 70),
          ("jnxOpticsLaserFreqErrorLowAlert", 71),
          ("jnxOptics24HourLaserFreqErrorHighAlert", 72),
          ("jnxOptics24HourLaserFreqErrorLowAlert", 73),
          ("jnxOpticsSnrLowAlert", 74),
          ("jnxOptics24HourSnrLowAlert", 75),
          ("jnxOpticsPreFecBERHighAlert", 76),
          ("jnxOptics24HourPreFecBERHignAlert", 77))
    )



class JnxIplcNotificationId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92)
        )
    )
    namedValues = NamedValues(
        *(("jnxIplcFpcAwgAddLosAlarm", 1),
          ("jnxIplcFpcExpInLosAlarm", 2),
          ("jnxIplcFpcOscAddLosAlarm", 3),
          ("jnxIplcFpcOscDrpLosAlarm", 4),
          ("jnxIplcFpcLineInLosAlarm", 5),
          ("jnxIplcFpcEdfa1RefPwAlarm", 6),
          ("jnxIplcFpcEdfa1OutPwAlarm", 7),
          ("jnxIplcFpcEdfa1OutGain", 8),
          ("jnxIplcFpcEdfa1PumpEolAlarm", 9),
          ("jnxIplcFpcEdfa1TempAlarm", 10),
          ("jnxIplcFpcEdfa1OutLosAlarm", 11),
          ("jnxIplcFpcEdfa1InLosAlarm", 12),
          ("jnxIplcFpcEdfa2RefPwAlarm", 13),
          ("jnxIplcFpcEdfa2OutPwAlarm", 14),
          ("jnxIplcFpcEdfa2OutGainAlarm", 15),
          ("jnxIplcFpcEdfa2PumpEolAlarm", 16),
          ("jnxIplcFpcEdfa2TempAlarm", 17),
          ("jnxIplcFpcEdfa2OutLosAlarm", 18),
          ("jnxIplcFpcEdfa2InLosAlarm", 19),
          ("jnxIplcFpcWssTempAlarm", 20),
          ("jnxIplcFpcWssVoltAlarm", 21),
          ("jnxIplcFpcInterDiagAlarm", 22),
          ("jnxIplcFpcFwCnsistAlarm", 23),
          ("jnxIplcFpcHwFailAlarm", 24),
          ("jnxIplcFpcFwFailAlarm", 25),
          ("jnxIplcFpcOcmFailAlarm", 26),
          ("jnxIplcFpcWssFailAlarm", 27),
          ("jnxIplcFpcEdfa2FailAlarm", 28),
          ("jnxIplcFpcEdfa1FailAlarm", 29),
          ("jnxIplcFpcPwrFailAlarm", 30),
          ("jnxIplcOscTxPowerHigh15minAlert", 31),
          ("jnxIplcOscTxPowerLow15minAlert", 32),
          ("jnxIplcOscRxPowerHigh15minAlert", 33),
          ("jnxIplcOscRxPowerLow15minAlert", 34),
          ("jnxIplcOscFiberLosHigh15minAlert", 35),
          ("jnxIplcOscFiberLosLow15minAlert", 36),
          ("jnxIplcLineOutVoaHigh15minAlert", 37),
          ("jnxIplcLineOutVoaLow15minAlert", 38),
          ("jnxIplcIngressEdfaInputPwHigh15minAlert", 39),
          ("jnxIplcIngressEdfaInputPwLow15minAlert", 40),
          ("jnxIplcIngressEdfaOutputPwHigh15minAlert", 41),
          ("jnxIplcIngressEdfaOutputPwLow15minAlert", 42),
          ("jnxIplcIngressEdfaSignalPwHigh15minAlert", 43),
          ("jnxIplcIngressEdfaSignalPwLow15minAlert", 44),
          ("jnxIplcIngressEdfaPumpCurrentHigh15minAlert", 45),
          ("jnxIplcIngressEdfaPumpCurrentLow15minAlert", 46),
          ("jnxIplcEgressEdfaInputPwHigh15minAlert", 47),
          ("jnxIplcEgressEdfaInputPwLow15minAlert", 48),
          ("jnxIplcEgressEdfaOutputPwHigh15minAlert", 49),
          ("jnxIplcEgressEdfaOutputPwLow15minAlert", 50),
          ("jnxIplcEgressEdfaSignalPwHigh15minAlert", 51),
          ("jnxIplcEgressEdfaSignalPwLow15minAlert", 52),
          ("jnxIplcEgressEdfaPumpCurrentHigh15minAlert", 53),
          ("jnxIplcEgressEdfaPumpCurrentLow15minAlert", 54),
          ("jnxIplcPowerMonitorAwgAddHigh15minAlert", 55),
          ("jnxIplcPowerMonitorAwgAddLow15minAlert", 56),
          ("jnxIplcPowerMonitorExpressInHigh15minAlert", 57),
          ("jnxIplcPowerMonitorExpressInLow15minAlert", 58),
          ("jnxIplcOcmPwHigh15minAlert", 59),
          ("jnxIplcOcmPwLow15minAlert", 60),
          ("jnxIplcOscTxPowerHigh24hourAlert", 61),
          ("jnxIplcOscTxPowerLow24hourAlert", 62),
          ("jnxIplcOscRxPowerHigh24hourAlert", 63),
          ("jnxIplcOscRxPowerLow24hourAlert", 64),
          ("jnxIplcOscFiberLosHigh24hourAlert", 65),
          ("jnxIplcOscFiberLosLow24hourAlert", 66),
          ("jnxIplcLineOutVoaHigh24hourAlert", 67),
          ("jnxIplcLineOutVoaLow24hourAlert", 68),
          ("jnxIplcIngressEdfaInputPwHigh24hourAlert", 69),
          ("jnxIplcIngressEdfaInputPwLow24hourAlert", 70),
          ("jnxIplcIngressEdfaOutputPwHigh24hourAlert", 71),
          ("jnxIplcIngressEdfaOutputPwLow24hourAlert", 72),
          ("jnxIplcIngressEdfaSignalPwHigh24hourAlert", 73),
          ("jnxIplcIngressEdfaSignalPwLow24hourAlert", 74),
          ("jnxIplcIngressEdfaPumpCurrentHigh24hourAlert", 75),
          ("jnxIplcIngressEdfaPumpCurrentLow24hourAlert", 76),
          ("jnxIplcEgressEdfaInputPwHigh24hourAlert", 77),
          ("jnxIplcEgressEdfaInputPwLow24hourAlert", 78),
          ("jnxIplcEgressEdfaOutputPwHigh24hourAlert", 79),
          ("jnxIplcEgressEdfaOutputPwLow24hourAlert", 80),
          ("jnxIplcEgressEdfaSignalPwHigh24hourAlert", 81),
          ("jnxIplcEgressEdfaSignalPwLow24hourAlert", 82),
          ("jnxIplcEgressEdfaPumpCurrentHigh24hourAlert", 83),
          ("jnxIplcEgressEdfaPumpCurrentLow24hourAlert", 84),
          ("jnxIplcPowerMonitorAwgAddHigh24hourAlert", 85),
          ("jnxIplcPowerMonitorAwgAddLow24hourAlert", 86),
          ("jnxIplcPowerMonitorExpressInHigh24hourAlert", 87),
          ("jnxIplcPowerMonitorExpressInLow24hourAlert", 88),
          ("jnxIplcOcmPwHigh24hourAlert", 89),
          ("jnxIplcOcmPwLow24hourAlert", 90),
          ("jnxIplcFpcSfpLosAlarm", 91),
          ("jnxIplcFpcSfpLofAlarm", 92))
    )



class JnxIlaNotificationId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128)
        )
    )
    namedValues = NamedValues(
        *(("jnxIlaBoardTemperatureAbnormalAlarm", 1),
          ("jnxIlaPower0AbnormalAlarm", 2),
          ("jnxIlaPower1AbnormalAlarm", 3),
          ("jnxIlaFan0MissingAlarm", 4),
          ("jnxIlaFan1MissingAlarm", 5),
          ("jnxIlaFan2MissingAlarm", 6),
          ("jnxIlaFan0SpeedAbnormalAlarm", 7),
          ("jnxIlaFan1SpeedAbnormalAlarm", 8),
          ("jnxIlaFan2SpeedAbnormalAlarm", 9),
          ("jnxIlaSoftwareVersionAbnormalAlarm", 10),
          ("jnxIlaCommunicationAbnormalAlarm", 11),
          ("jnxIlaTableErrAlarm", 12),
          ("jnxIlaEdfaEabCaseTemperatureAlarm", 13),
          ("jnxIlaEdfaEabRFLAlarm", 14),
          ("jnxIlaEdfaEabOOPAlarm", 15),
          ("jnxIlaEdfaEabOOGAlarm", 16),
          ("jnxIlaEdfaEabPump0EOLAlarm", 17),
          ("jnxIlaEdfaEabPump1EOLAlarm", 18),
          ("jnxIlaEdfaEabPump0TemperatureAlarm", 19),
          ("jnxIlaEdfaEabPump1TemperatureAlarm", 20),
          ("jnxIlaEdfaEabInputLOSAlarm", 21),
          ("jnxIlaEdfaEabOutputLOSAlarm", 22),
          ("jnxIlaEdfaEabCaliTableErrAlarm", 23),
          ("jnxIlaEdfaEbaCaseTemperatureAlarm", 24),
          ("jnxIlaEdfaEbaRFLAlarm", 25),
          ("jnxIlaEdfaEbaOOPAlarm", 26),
          ("jnxIlaEdfaEbaOOGAlarm", 27),
          ("jnxIlaEdfaEbaPump0EOLAlarm", 28),
          ("jnxIlaEdfaEbaPump1EOLAlarm", 29),
          ("jnxIlaEdfaEbaPump0TemperatureAlarm", 30),
          ("jnxIlaEdfaEbaPump1TemperatureAlarm", 31),
          ("jnxIlaEdfaEbaInputLOSAlarm", 32),
          ("jnxIlaEdfaEbaOutputLOSAlarm", 33),
          ("jnxIlaEdfaEbaCaliTableErrAlarm", 34),
          ("jnxIlaOscaAddPowerLOSAlarm", 35),
          ("jnxIlaOscaDropPowerLOSAlarm", 36),
          ("jnxIlaOscbAddPowerLOSAlarm", 37),
          ("jnxIlaOscbDropPowerLOSAlarm", 38),
          ("jnxIlaOscATxPwrLow15minAlert", 39),
          ("jnxIlaOscATxPwrHigh15minAlert", 40),
          ("jnxIlaOscARxPwrLow15minAlert", 41),
          ("jnxIlaOscARxPwrHigh15minAlert", 42),
          ("jnxIlaOscAFibLossLow15minAlert", 43),
          ("jnxIlaOscAFibLossHigh15minAlert", 44),
          ("jnxIlaVoaALineOutLow15minAlert", 45),
          ("jnxIlaVoaALineOutHigh15minAlert", 46),
          ("jnxIlaOscBTxPwrLow15minAlert", 47),
          ("jnxIlaOscBTxPwrHigh15minAlert", 48),
          ("jnxIlaOscBRxPwrLow15minAlert", 49),
          ("jnxIlaOscBRxPwrHigh15minAlert", 50),
          ("jnxIlaOscBFibLossLow15minAlert", 51),
          ("jnxIlaOscBFibLossHigh15minAlert", 52),
          ("jnxIlaVoaBLineOutLow15minAlert", 53),
          ("jnxIlaVoaBLineOutHigh15minAlert", 54),
          ("jnxIlaEdfaABInputPwrLow15minAlert", 55),
          ("jnxIlaEdfaABInputPwrHigh15minAlert", 56),
          ("jnxIlaEdfaABOutputPwrLow15minAlert", 57),
          ("jnxIlaEdfaABOutputPwrHigh15minAlert", 58),
          ("jnxIlaEdfaABPump0CurLow15minAlert", 59),
          ("jnxIlaEdfaABPump0CurHigh15minAlert", 60),
          ("jnxIlaEdfaABPump1CurLow15minAlert", 61),
          ("jnxIlaEdfaABPump1CurHigh15minAlert", 62),
          ("jnxIlaEdfaABPump0TempLow15minAlert", 63),
          ("jnxIlaEdfaABPump0TempHigh15minAlert", 64),
          ("jnxIlaEdfaABPump1TempLow15minAlert", 65),
          ("jnxIlaEdfaABPump1TempHigh15minAlert", 66),
          ("jnxIlaEdfaBAInputPwrLow15minAlert", 67),
          ("jnxIlaEdfaBAInputPwrHigh15minAlert", 68),
          ("jnxIlaEdfaBAOutputPwrLow15minAlert", 69),
          ("jnxIlaEdfaBAOutputPwrHigh15minAlert", 70),
          ("jnxIlaEdfaBAPump0CurLow15minAlert", 71),
          ("jnxIlaEdfaBAPump0CurHigh15minAlert", 72),
          ("jnxIlaEdfaBAPump1CurLow15minAlert", 73),
          ("jnxIlaEdfaBAPump1CurHigh15minAlert", 74),
          ("jnxIlaEdfaBAPump0TempLow15minAlert", 75),
          ("jnxIlaEdfaBAPump0TempHigh15minAlert", 76),
          ("jnxIlaEdfaBAPump1TempLow15minAlert", 77),
          ("jnxIlaEdfaBAPump1TempHigh15minAlert", 78),
          ("jnxIla24HourOscATxPwrLowAlert", 79),
          ("jnxIla24HourOscATxPwrHighAlert", 80),
          ("jnxIla24HourOscARxPwrLowAlert", 81),
          ("jnxIla24HourOscARxPwrHighAlert", 82),
          ("jnxIla24HourOscAFibLossLowAlert", 83),
          ("jnxIla24HourOscAFibLossHighAlert", 84),
          ("jnxIla24HourVoaALineOutLowAlert", 85),
          ("jnxIla24HourVoaALineOutHighAlert", 86),
          ("jnxIla24HourOscBTxPwrLowAlert", 87),
          ("jnxIla24HourOscBTxPwrHighAlert", 88),
          ("jnxIla24HourOscBRxPwrLowAlert", 89),
          ("jnxIla24HourOscBRxPwrHighAlert", 90),
          ("jnxIla24HourOscBFibLossLowAlert", 91),
          ("jnxIla24HourOscBFibLossHighAlert", 92),
          ("jnxIla24HourVoaBLineOutLowAlert", 93),
          ("jnxIla24HourVoaBLineOutHighAlert", 94),
          ("jnxIla24HourEdfaABInputPwrLowAlert", 95),
          ("jnxIla24HourEdfaABInputPwrHighAlert", 96),
          ("jnxIla24HourEdfaABOutputPwrLowAlert", 97),
          ("jnxIla24HourEdfaABOutputPwrHighAlert", 98),
          ("jnxIla24HourEdfaABPump0CurLowAlert", 99),
          ("jnxIla24HourEdfaABPump0CurHighAlert", 100),
          ("jnxIla24HourEdfaABPump1CurLowAlert", 101),
          ("jnxIla24HourEdfaABPump1CurHighAlert", 102),
          ("jnxIla24HourEdfaABPump0TempLowAlert", 103),
          ("jnxIla24HourEdfaABPump0TempHighAlert", 104),
          ("jnxIla24HourEdfaABPump1TempLowAlert", 105),
          ("jnxIla24HourEdfaABPump1TempHighAlert", 106),
          ("jnxIla24HourEdfaBAInputPwrLowAlert", 107),
          ("jnxIla24HourEdfaBAInputPwrHighAlert", 108),
          ("jnxIla24HourEdfaBAOutputPwrLowAlert", 109),
          ("jnxIla24HourEdfaBAOutputPwrHighAlert", 110),
          ("jnxIla24HourEdfaBAPump0CurLowAlert", 111),
          ("jnxIla24HourEdfaBAPump0CurHighAlert", 112),
          ("jnxIla24HourEdfaBAPump1CurLowAlert", 113),
          ("jnxIla24HourEdfaBAPump1CurHighAlert", 114),
          ("jnxIla24HourEdfaBAPump0TempLowAlert", 115),
          ("jnxIla24HourEdfaBAPump0TempHighAlert", 116),
          ("jnxIla24HourEdfaBAPump1TempLowAlert", 117),
          ("jnxIla24HourEdfaBAPump1TempHighAlert", 118),
          ("jnxIlaEdfaABSignalPwrLow15minAlert", 119),
          ("jnxIlaEdfaABSignalPwrHigh15minAlert", 120),
          ("jnxIla24HourEdfaABSignalPwrLowAlert", 121),
          ("jnxIla24HourEdfaABSignalPwrHighAlert", 122),
          ("jnxIlaEdfaBASignalPwrLow15minAlert", 123),
          ("jnxIlaEdfaBASignalPwrHigh15minAlert", 124),
          ("jnxIla24HourEdfaBASignalPwrLowAlert", 125),
          ("jnxIla24HourEdfaBASignalPwrHighAlert", 126),
          ("jnxIlaEdfaABGainRangeErrAlarm", 127),
          ("jnxIlaEdfaBAGainRangeErrAlarm", 128))
    )



# MIB Managed Objects in the order of their OIDs

_JnxOptics_ObjectIdentity = ObjectIdentity
jnxOptics = _JnxOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1)
)
_JnxOpticsConfigTable_Object = MibTable
jnxOpticsConfigTable = _JnxOpticsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxOpticsConfigTable.setStatus("current")
_JnxOpticsConfigEntry_Object = MibTableRow
jnxOpticsConfigEntry = _JnxOpticsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1)
)
jnxOpticsConfigEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigContainerIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsConfigL3Index"),
)
if mibBuilder.loadTexts:
    jnxOpticsConfigEntry.setStatus("current")


class _JnxOpticsConfigContainerIndex_Type(Integer32):
    """Custom type jnxOpticsConfigContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigContainerIndex_Type.__name__ = "Integer32"
_JnxOpticsConfigContainerIndex_Object = MibTableColumn
jnxOpticsConfigContainerIndex = _JnxOpticsConfigContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 1),
    _JnxOpticsConfigContainerIndex_Type()
)
jnxOpticsConfigContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigContainerIndex.setStatus("current")


class _JnxOpticsConfigL1Index_Type(Integer32):
    """Custom type jnxOpticsConfigL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigL1Index_Type.__name__ = "Integer32"
_JnxOpticsConfigL1Index_Object = MibTableColumn
jnxOpticsConfigL1Index = _JnxOpticsConfigL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 2),
    _JnxOpticsConfigL1Index_Type()
)
jnxOpticsConfigL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigL1Index.setStatus("current")


class _JnxOpticsConfigL2Index_Type(Integer32):
    """Custom type jnxOpticsConfigL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigL2Index_Type.__name__ = "Integer32"
_JnxOpticsConfigL2Index_Object = MibTableColumn
jnxOpticsConfigL2Index = _JnxOpticsConfigL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 3),
    _JnxOpticsConfigL2Index_Type()
)
jnxOpticsConfigL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigL2Index.setStatus("current")


class _JnxOpticsConfigL3Index_Type(Integer32):
    """Custom type jnxOpticsConfigL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsConfigL3Index_Type.__name__ = "Integer32"
_JnxOpticsConfigL3Index_Object = MibTableColumn
jnxOpticsConfigL3Index = _JnxOpticsConfigL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 4),
    _JnxOpticsConfigL3Index_Type()
)
jnxOpticsConfigL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsConfigL3Index.setStatus("current")
_JnxOpticsType_Type = Integer32
_JnxOpticsType_Object = MibTableColumn
jnxOpticsType = _JnxOpticsType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 5),
    _JnxOpticsType_Type()
)
jnxOpticsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsType.setStatus("current")
_JnxLaserEnable_Type = TruthValue
_JnxLaserEnable_Object = MibTableColumn
jnxLaserEnable = _JnxLaserEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 6),
    _JnxLaserEnable_Type()
)
jnxLaserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxLaserEnable.setStatus("current")
_JnxWavelength_Type = Unsigned32
_JnxWavelength_Object = MibTableColumn
jnxWavelength = _JnxWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 7),
    _JnxWavelength_Type()
)
jnxWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxWavelength.setStatus("current")
if mibBuilder.loadTexts:
    jnxWavelength.setUnits("0.01 nm")
_JnxSpacing_Type = JnxOpticsChannelSpacing
_JnxSpacing_Object = MibTableColumn
jnxSpacing = _JnxSpacing_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 8),
    _JnxSpacing_Type()
)
jnxSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSpacing.setStatus("current")
_JnxModulation_Type = Unsigned32
_JnxModulation_Object = MibTableColumn
jnxModulation = _JnxModulation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 9),
    _JnxModulation_Type()
)
jnxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxModulation.setStatus("current")
_JnxTxOpticalPower_Type = Integer32
_JnxTxOpticalPower_Object = MibTableColumn
jnxTxOpticalPower = _JnxTxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 10),
    _JnxTxOpticalPower_Type()
)
jnxTxOpticalPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxTxOpticalPower.setUnits("0.01 dbm")
_JnxRxOpticalPower_Type = Integer32
_JnxRxOpticalPower_Object = MibTableColumn
jnxRxOpticalPower = _JnxRxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 11),
    _JnxRxOpticalPower_Type()
)
jnxRxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRxOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxOpticalPower.setUnits("0.01 dbm")
_JnxModuleTempHighThresh_Type = Integer32
_JnxModuleTempHighThresh_Object = MibTableColumn
jnxModuleTempHighThresh = _JnxModuleTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 12),
    _JnxModuleTempHighThresh_Type()
)
jnxModuleTempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxModuleTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxModuleTempHighThresh.setUnits("Celsius (0.01 degrees C)")
_JnxModuleTempLowThresh_Type = Integer32
_JnxModuleTempLowThresh_Object = MibTableColumn
jnxModuleTempLowThresh = _JnxModuleTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 13),
    _JnxModuleTempLowThresh_Type()
)
jnxModuleTempLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxModuleTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxModuleTempLowThresh.setUnits("Celsius (0.01 degrees C)")
_JnxTxPowerHighThresh_Type = Integer32
_JnxTxPowerHighThresh_Object = MibTableColumn
jnxTxPowerHighThresh = _JnxTxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 14),
    _JnxTxPowerHighThresh_Type()
)
jnxTxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxTxPowerHighThresh.setUnits("0.01 dbm")
_JnxTxPowerLowThresh_Type = Integer32
_JnxTxPowerLowThresh_Object = MibTableColumn
jnxTxPowerLowThresh = _JnxTxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 15),
    _JnxTxPowerLowThresh_Type()
)
jnxTxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxTxPowerLowThresh.setUnits("0.01 dbm")
_JnxRxPowerHighThresh_Type = Integer32
_JnxRxPowerHighThresh_Object = MibTableColumn
jnxRxPowerHighThresh = _JnxRxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 16),
    _JnxRxPowerHighThresh_Type()
)
jnxRxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxPowerHighThresh.setUnits("0.01 dbm")
_JnxRxPowerLowThresh_Type = Integer32
_JnxRxPowerLowThresh_Object = MibTableColumn
jnxRxPowerLowThresh = _JnxRxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 17),
    _JnxRxPowerLowThresh_Type()
)
jnxRxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxPowerLowThresh.setUnits("0.01 dbm")
_Jnx24HourModuleTempHighThresh_Type = Integer32
_Jnx24HourModuleTempHighThresh_Object = MibTableColumn
jnx24HourModuleTempHighThresh = _Jnx24HourModuleTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 18),
    _Jnx24HourModuleTempHighThresh_Type()
)
jnx24HourModuleTempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnx24HourModuleTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourModuleTempHighThresh.setUnits("Celsius (0.01 degrees C)")
_Jnx24HourModuleTempLowThresh_Type = Integer32
_Jnx24HourModuleTempLowThresh_Object = MibTableColumn
jnx24HourModuleTempLowThresh = _Jnx24HourModuleTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 19),
    _Jnx24HourModuleTempLowThresh_Type()
)
jnx24HourModuleTempLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnx24HourModuleTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourModuleTempLowThresh.setUnits("Celsius (0.01 degrees C)")
_Jnx24HourTxPowerHighThresh_Type = Integer32
_Jnx24HourTxPowerHighThresh_Object = MibTableColumn
jnx24HourTxPowerHighThresh = _Jnx24HourTxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 20),
    _Jnx24HourTxPowerHighThresh_Type()
)
jnx24HourTxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourTxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourTxPowerHighThresh.setUnits("0.01 dbm")
_Jnx24HourTxPowerLowThresh_Type = Integer32
_Jnx24HourTxPowerLowThresh_Object = MibTableColumn
jnx24HourTxPowerLowThresh = _Jnx24HourTxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 21),
    _Jnx24HourTxPowerLowThresh_Type()
)
jnx24HourTxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourTxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourTxPowerLowThresh.setUnits("0.01 dbm")
_Jnx24HourRxPowerHighThresh_Type = Integer32
_Jnx24HourRxPowerHighThresh_Object = MibTableColumn
jnx24HourRxPowerHighThresh = _Jnx24HourRxPowerHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 22),
    _Jnx24HourRxPowerHighThresh_Type()
)
jnx24HourRxPowerHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourRxPowerHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourRxPowerHighThresh.setUnits("0.01 dbm")
_Jnx24HourRxPowerLowThresh_Type = Integer32
_Jnx24HourRxPowerLowThresh_Object = MibTableColumn
jnx24HourRxPowerLowThresh = _Jnx24HourRxPowerLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 23),
    _Jnx24HourRxPowerLowThresh_Type()
)
jnx24HourRxPowerLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourRxPowerLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourRxPowerLowThresh.setUnits("0.01 dbm")
_JnxRxLosPowerWarningThresh_Type = Integer32
_JnxRxLosPowerWarningThresh_Object = MibTableColumn
jnxRxLosPowerWarningThresh = _JnxRxLosPowerWarningThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 24),
    _JnxRxLosPowerWarningThresh_Type()
)
jnxRxLosPowerWarningThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxLosPowerWarningThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxLosPowerWarningThresh.setUnits("0.01 dbm")
_JnxRxLosPowerAlarmThresh_Type = Integer32
_JnxRxLosPowerAlarmThresh_Object = MibTableColumn
jnxRxLosPowerAlarmThresh = _JnxRxLosPowerAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 25),
    _JnxRxLosPowerAlarmThresh_Type()
)
jnxRxLosPowerAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxLosPowerAlarmThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxRxLosPowerAlarmThresh.setUnits("0.01 dbm")


class _JnxOpticsCurrentStatus_Type(Bits):
    """Custom type jnxOpticsCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("opticalLos", 1),
          ("wavelenthLockErr", 2),
          ("powerHighAlarm", 3),
          ("powerLowAlarm", 4),
          ("biasCurrentHighAlarm", 5),
          ("biasCurrentLowAlarm", 6),
          ("temperatureHighAlarm", 7),
          ("temperaturelowAlarm", 8),
          ("txPLLLockAlarm", 9),
          ("rxPLLLockAlarm", 10),
          ("avgPowerAlarm", 11),
          ("rxLossAvgPowerAlarm", 12),
          ("lossofACPowerAlarm", 13),
          ("txPowerHighThreshAlert", 14),
          ("txPowerLowThreshAlert", 15),
          ("rxPowerHighThreshAlert", 16),
          ("rxPowerLowThreshAlert", 17),
          ("moduleTempHighThreshAlert", 18),
          ("moduleTempLowThreshAlert", 19),
          ("txPowerHigh24HourThreshAlert", 20),
          ("txPowerLow24HourThreshAlert", 21),
          ("rxPowerHigh24HourThreshAlert", 22),
          ("rxPowerLow24HourThreshAlert", 23),
          ("moduleTempHigh24HourThreshAlert", 24),
          ("moduleTempLow24HourThreshAlert", 25),
          ("powerRxHighAlarm", 26),
          ("powerRxLowAlarm", 27),
          ("powerTxHighWarning", 28),
          ("powerTxLowWarning", 29),
          ("powerRxHighWarning", 30),
          ("powerRxLowWarning", 31),
          ("temperatureHighWarning", 32),
          ("temperaturelowWarning", 33))
    )

_JnxOpticsCurrentStatus_Type.__name__ = "Bits"
_JnxOpticsCurrentStatus_Object = MibTableColumn
jnxOpticsCurrentStatus = _JnxOpticsCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 26),
    _JnxOpticsCurrentStatus_Type()
)
jnxOpticsCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsCurrentStatus.setStatus("current")
_JnxTxPowerHighEnableTCA_Type = TruthValue
_JnxTxPowerHighEnableTCA_Object = MibTableColumn
jnxTxPowerHighEnableTCA = _JnxTxPowerHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 27),
    _JnxTxPowerHighEnableTCA_Type()
)
jnxTxPowerHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerHighEnableTCA.setStatus("current")
_JnxTxPowerLowEnableTCA_Type = TruthValue
_JnxTxPowerLowEnableTCA_Object = MibTableColumn
jnxTxPowerLowEnableTCA = _JnxTxPowerLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 28),
    _JnxTxPowerLowEnableTCA_Type()
)
jnxTxPowerLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxTxPowerLowEnableTCA.setStatus("current")
_JnxRxPowerHighEnableTCA_Type = TruthValue
_JnxRxPowerHighEnableTCA_Object = MibTableColumn
jnxRxPowerHighEnableTCA = _JnxRxPowerHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 29),
    _JnxRxPowerHighEnableTCA_Type()
)
jnxRxPowerHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerHighEnableTCA.setStatus("current")
_JnxRxPowerLowEnableTCA_Type = TruthValue
_JnxRxPowerLowEnableTCA_Object = MibTableColumn
jnxRxPowerLowEnableTCA = _JnxRxPowerLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 30),
    _JnxRxPowerLowEnableTCA_Type()
)
jnxRxPowerLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxRxPowerLowEnableTCA.setStatus("current")
_JnxModuleTempHighEnableTCA_Type = TruthValue
_JnxModuleTempHighEnableTCA_Object = MibTableColumn
jnxModuleTempHighEnableTCA = _JnxModuleTempHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 31),
    _JnxModuleTempHighEnableTCA_Type()
)
jnxModuleTempHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxModuleTempHighEnableTCA.setStatus("current")
_JnxModuleTempLowEnableTCA_Type = TruthValue
_JnxModuleTempLowEnableTCA_Object = MibTableColumn
jnxModuleTempLowEnableTCA = _JnxModuleTempLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 32),
    _JnxModuleTempLowEnableTCA_Type()
)
jnxModuleTempLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxModuleTempLowEnableTCA.setStatus("current")
_JnxCarFreqOffsetHighEnableTCA_Type = TruthValue
_JnxCarFreqOffsetHighEnableTCA_Object = MibTableColumn
jnxCarFreqOffsetHighEnableTCA = _JnxCarFreqOffsetHighEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 33),
    _JnxCarFreqOffsetHighEnableTCA_Type()
)
jnxCarFreqOffsetHighEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetHighEnableTCA.setStatus("current")
_JnxCarFreqOffsetLowEnableTCA_Type = TruthValue
_JnxCarFreqOffsetLowEnableTCA_Object = MibTableColumn
jnxCarFreqOffsetLowEnableTCA = _JnxCarFreqOffsetLowEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 34),
    _JnxCarFreqOffsetLowEnableTCA_Type()
)
jnxCarFreqOffsetLowEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetLowEnableTCA.setStatus("current")
_JnxCarFreqOffsetHighThresh_Type = Integer32
_JnxCarFreqOffsetHighThresh_Object = MibTableColumn
jnxCarFreqOffsetHighThresh = _JnxCarFreqOffsetHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 35),
    _JnxCarFreqOffsetHighThresh_Type()
)
jnxCarFreqOffsetHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetHighThresh.setUnits("MHz")
_Jnx24HourCarFreqOffsetHighThresh_Type = Integer32
_Jnx24HourCarFreqOffsetHighThresh_Object = MibTableColumn
jnx24HourCarFreqOffsetHighThresh = _Jnx24HourCarFreqOffsetHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 36),
    _Jnx24HourCarFreqOffsetHighThresh_Type()
)
jnx24HourCarFreqOffsetHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetHighThresh.setUnits("MHz")
_JnxCarFreqOffsetLowThresh_Type = Integer32
_JnxCarFreqOffsetLowThresh_Object = MibTableColumn
jnxCarFreqOffsetLowThresh = _JnxCarFreqOffsetLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 37),
    _JnxCarFreqOffsetLowThresh_Type()
)
jnxCarFreqOffsetLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnxCarFreqOffsetLowThresh.setUnits("MHz")
_Jnx24HourCarFreqOffsetLowThresh_Type = Integer32
_Jnx24HourCarFreqOffsetLowThresh_Object = MibTableColumn
jnx24HourCarFreqOffsetLowThresh = _Jnx24HourCarFreqOffsetLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 1, 1, 38),
    _Jnx24HourCarFreqOffsetLowThresh_Type()
)
jnx24HourCarFreqOffsetLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    jnx24HourCarFreqOffsetLowThresh.setUnits("MHz")
_JnxOpticsTraceToneCfgTable_Object = MibTable
jnxOpticsTraceToneCfgTable = _JnxOpticsTraceToneCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgTable.setStatus("current")
_JnxOpticsTraceToneCfgEntry_Object = MibTableRow
jnxOpticsTraceToneCfgEntry = _JnxOpticsTraceToneCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1)
)
jnxOpticsTraceToneCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgContainerIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsTraceToneCfgL3Index"),
)
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgEntry.setStatus("current")


class _JnxOpticsTraceToneCfgContainerIndex_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgContainerIndex_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgContainerIndex_Object = MibTableColumn
jnxOpticsTraceToneCfgContainerIndex = _JnxOpticsTraceToneCfgContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 1),
    _JnxOpticsTraceToneCfgContainerIndex_Type()
)
jnxOpticsTraceToneCfgContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgContainerIndex.setStatus("current")


class _JnxOpticsTraceToneCfgL1Index_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgL1Index_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgL1Index_Object = MibTableColumn
jnxOpticsTraceToneCfgL1Index = _JnxOpticsTraceToneCfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 2),
    _JnxOpticsTraceToneCfgL1Index_Type()
)
jnxOpticsTraceToneCfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgL1Index.setStatus("current")


class _JnxOpticsTraceToneCfgL2Index_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgL2Index_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgL2Index_Object = MibTableColumn
jnxOpticsTraceToneCfgL2Index = _JnxOpticsTraceToneCfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 3),
    _JnxOpticsTraceToneCfgL2Index_Type()
)
jnxOpticsTraceToneCfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgL2Index.setStatus("current")


class _JnxOpticsTraceToneCfgL3Index_Type(Integer32):
    """Custom type jnxOpticsTraceToneCfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsTraceToneCfgL3Index_Type.__name__ = "Integer32"
_JnxOpticsTraceToneCfgL3Index_Object = MibTableColumn
jnxOpticsTraceToneCfgL3Index = _JnxOpticsTraceToneCfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 4),
    _JnxOpticsTraceToneCfgL3Index_Type()
)
jnxOpticsTraceToneCfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgL3Index.setStatus("current")
_JnxOpticsTraceToneCfgTxEnable_Type = TruthValue
_JnxOpticsTraceToneCfgTxEnable_Object = MibTableColumn
jnxOpticsTraceToneCfgTxEnable = _JnxOpticsTraceToneCfgTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 5),
    _JnxOpticsTraceToneCfgTxEnable_Type()
)
jnxOpticsTraceToneCfgTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgTxEnable.setStatus("current")
_JnxOpticsTraceToneCfgRxEnable_Type = TruthValue
_JnxOpticsTraceToneCfgRxEnable_Object = MibTableColumn
jnxOpticsTraceToneCfgRxEnable = _JnxOpticsTraceToneCfgRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 6),
    _JnxOpticsTraceToneCfgRxEnable_Type()
)
jnxOpticsTraceToneCfgRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgRxEnable.setStatus("current")
_JnxOpticsTraceToneCfgDestId_Type = OctetString
_JnxOpticsTraceToneCfgDestId_Object = MibTableColumn
jnxOpticsTraceToneCfgDestId = _JnxOpticsTraceToneCfgDestId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 7),
    _JnxOpticsTraceToneCfgDestId_Type()
)
jnxOpticsTraceToneCfgDestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgDestId.setStatus("current")
_JnxOpticsTraceToneCfgTxMsg_Type = OctetString
_JnxOpticsTraceToneCfgTxMsg_Object = MibTableColumn
jnxOpticsTraceToneCfgTxMsg = _JnxOpticsTraceToneCfgTxMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 8),
    _JnxOpticsTraceToneCfgTxMsg_Type()
)
jnxOpticsTraceToneCfgTxMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgTxMsg.setStatus("current")
_JnxOpticsTraceToneCfgRxMsg_Type = OctetString
_JnxOpticsTraceToneCfgRxMsg_Object = MibTableColumn
jnxOpticsTraceToneCfgRxMsg = _JnxOpticsTraceToneCfgRxMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 2, 1, 9),
    _JnxOpticsTraceToneCfgRxMsg_Type()
)
jnxOpticsTraceToneCfgRxMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsTraceToneCfgRxMsg.setStatus("current")
_JnxOpticsNotificationTrigDefaultHoldtimeUp_Type = Integer32
_JnxOpticsNotificationTrigDefaultHoldtimeUp_Object = MibScalar
jnxOpticsNotificationTrigDefaultHoldtimeUp = _JnxOpticsNotificationTrigDefaultHoldtimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 3),
    _JnxOpticsNotificationTrigDefaultHoldtimeUp_Type()
)
jnxOpticsNotificationTrigDefaultHoldtimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigDefaultHoldtimeUp.setStatus("current")
_JnxOpticsNotificationTrigDefaultHoldtimeDown_Type = Integer32
_JnxOpticsNotificationTrigDefaultHoldtimeDown_Object = MibScalar
jnxOpticsNotificationTrigDefaultHoldtimeDown = _JnxOpticsNotificationTrigDefaultHoldtimeDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 4),
    _JnxOpticsNotificationTrigDefaultHoldtimeDown_Type()
)
jnxOpticsNotificationTrigDefaultHoldtimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigDefaultHoldtimeDown.setStatus("current")
_JnxOpticsNotificationTrigTable_Object = MibTable
jnxOpticsNotificationTrigTable = _JnxOpticsNotificationTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigTable.setStatus("current")
_JnxOpticsNotificationTrigEntry_Object = MibTableRow
jnxOpticsNotificationTrigEntry = _JnxOpticsNotificationTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1)
)
jnxOpticsNotificationTrigEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigContainerIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigL3Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationTrigAlmId"),
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigEntry.setStatus("current")


class _JnxOpticsNotificationTrigContainerIndex_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigContainerIndex_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigContainerIndex_Object = MibTableColumn
jnxOpticsNotificationTrigContainerIndex = _JnxOpticsNotificationTrigContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 1),
    _JnxOpticsNotificationTrigContainerIndex_Type()
)
jnxOpticsNotificationTrigContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigContainerIndex.setStatus("current")


class _JnxOpticsNotificationTrigL1Index_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigL1Index_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigL1Index_Object = MibTableColumn
jnxOpticsNotificationTrigL1Index = _JnxOpticsNotificationTrigL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 2),
    _JnxOpticsNotificationTrigL1Index_Type()
)
jnxOpticsNotificationTrigL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigL1Index.setStatus("current")


class _JnxOpticsNotificationTrigL2Index_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigL2Index_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigL2Index_Object = MibTableColumn
jnxOpticsNotificationTrigL2Index = _JnxOpticsNotificationTrigL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 3),
    _JnxOpticsNotificationTrigL2Index_Type()
)
jnxOpticsNotificationTrigL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigL2Index.setStatus("current")


class _JnxOpticsNotificationTrigL3Index_Type(Integer32):
    """Custom type jnxOpticsNotificationTrigL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationTrigL3Index_Type.__name__ = "Integer32"
_JnxOpticsNotificationTrigL3Index_Object = MibTableColumn
jnxOpticsNotificationTrigL3Index = _JnxOpticsNotificationTrigL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 4),
    _JnxOpticsNotificationTrigL3Index_Type()
)
jnxOpticsNotificationTrigL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigL3Index.setStatus("current")
_JnxOpticsNotificationTrigAlmId_Type = JnxOpticsNotificationId
_JnxOpticsNotificationTrigAlmId_Object = MibTableColumn
jnxOpticsNotificationTrigAlmId = _JnxOpticsNotificationTrigAlmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 5),
    _JnxOpticsNotificationTrigAlmId_Type()
)
jnxOpticsNotificationTrigAlmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigAlmId.setStatus("current")
_JnxOpticsNotificationTrigSeverity_Type = JnxOpticsSeverity
_JnxOpticsNotificationTrigSeverity_Object = MibTableColumn
jnxOpticsNotificationTrigSeverity = _JnxOpticsNotificationTrigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 6),
    _JnxOpticsNotificationTrigSeverity_Type()
)
jnxOpticsNotificationTrigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigSeverity.setStatus("current")
_JnxOpticsNotificationTrigIgnore_Type = TruthValue
_JnxOpticsNotificationTrigIgnore_Object = MibTableColumn
jnxOpticsNotificationTrigIgnore = _JnxOpticsNotificationTrigIgnore_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 7),
    _JnxOpticsNotificationTrigIgnore_Type()
)
jnxOpticsNotificationTrigIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigIgnore.setStatus("current")
_JnxOpticsNotificationTrigHoldtimeUp_Type = Integer32
_JnxOpticsNotificationTrigHoldtimeUp_Object = MibTableColumn
jnxOpticsNotificationTrigHoldtimeUp = _JnxOpticsNotificationTrigHoldtimeUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 8),
    _JnxOpticsNotificationTrigHoldtimeUp_Type()
)
jnxOpticsNotificationTrigHoldtimeUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigHoldtimeUp.setStatus("current")
_JnxOpticsNotificationTrigHoldtimeDown_Type = Integer32
_JnxOpticsNotificationTrigHoldtimeDown_Object = MibTableColumn
jnxOpticsNotificationTrigHoldtimeDown = _JnxOpticsNotificationTrigHoldtimeDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 9),
    _JnxOpticsNotificationTrigHoldtimeDown_Type()
)
jnxOpticsNotificationTrigHoldtimeDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsNotificationTrigHoldtimeDown.setStatus("current")
_JnxOpticsTrigServiceStateAction_Type = JnxOpticsServiceStateAction
_JnxOpticsTrigServiceStateAction_Object = MibTableColumn
jnxOpticsTrigServiceStateAction = _JnxOpticsTrigServiceStateAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 5, 1, 10),
    _JnxOpticsTrigServiceStateAction_Type()
)
jnxOpticsTrigServiceStateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsTrigServiceStateAction.setStatus("current")
_JnxOpticsClearAllPMs_Type = TruthValue
_JnxOpticsClearAllPMs_Object = MibScalar
jnxOpticsClearAllPMs = _JnxOpticsClearAllPMs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 6),
    _JnxOpticsClearAllPMs_Type()
)
jnxOpticsClearAllPMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearAllPMs.setStatus("current")
_JnxOpticsClearIfPMsTable_Object = MibTable
jnxOpticsClearIfPMsTable = _JnxOpticsClearIfPMsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxOpticsClearIfPMsTable.setStatus("current")
_JnxOpticsClearIfPMsEntry_Object = MibTableRow
jnxOpticsClearIfPMsEntry = _JnxOpticsClearIfPMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1)
)
jnxOpticsClearIfPMsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsClearIfPMsEntry.setStatus("current")
_JnxOpticsClearCurrent_Type = TruthValue
_JnxOpticsClearCurrent_Object = MibTableColumn
jnxOpticsClearCurrent = _JnxOpticsClearCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 1),
    _JnxOpticsClearCurrent_Type()
)
jnxOpticsClearCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearCurrent.setStatus("current")
_JnxOpticsClearInterfaceInterval_Type = TruthValue
_JnxOpticsClearInterfaceInterval_Object = MibTableColumn
jnxOpticsClearInterfaceInterval = _JnxOpticsClearInterfaceInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 2),
    _JnxOpticsClearInterfaceInterval_Type()
)
jnxOpticsClearInterfaceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearInterfaceInterval.setStatus("current")
_JnxOpticsClearInterfaceDay_Type = TruthValue
_JnxOpticsClearInterfaceDay_Object = MibTableColumn
jnxOpticsClearInterfaceDay = _JnxOpticsClearInterfaceDay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 3),
    _JnxOpticsClearInterfaceDay_Type()
)
jnxOpticsClearInterfaceDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearInterfaceDay.setStatus("current")
_JnxOpticsClearInterfaceAll_Type = TruthValue
_JnxOpticsClearInterfaceAll_Object = MibTableColumn
jnxOpticsClearInterfaceAll = _JnxOpticsClearInterfaceAll_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 7, 1, 4),
    _JnxOpticsClearInterfaceAll_Type()
)
jnxOpticsClearInterfaceAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsClearInterfaceAll.setStatus("current")
_JnxOpticsOTIfConfigTable_Object = MibTable
jnxOpticsOTIfConfigTable = _JnxOpticsOTIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8)
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfConfigTable.setStatus("current")
_JnxOpticsOTIfConfigEntry_Object = MibTableRow
jnxOpticsOTIfConfigEntry = _JnxOpticsOTIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1)
)
jnxOpticsOTIfConfigEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOTIfConfigContainerIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOTIfConfigL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOTIfConfigL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOTIfConfigL3Index"),
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfConfigEntry.setStatus("current")


class _JnxOpticsOTIfConfigContainerIndex_Type(Integer32):
    """Custom type jnxOpticsOTIfConfigContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOTIfConfigContainerIndex_Type.__name__ = "Integer32"
_JnxOpticsOTIfConfigContainerIndex_Object = MibTableColumn
jnxOpticsOTIfConfigContainerIndex = _JnxOpticsOTIfConfigContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 1),
    _JnxOpticsOTIfConfigContainerIndex_Type()
)
jnxOpticsOTIfConfigContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOTIfConfigContainerIndex.setStatus("current")


class _JnxOpticsOTIfConfigL1Index_Type(Integer32):
    """Custom type jnxOpticsOTIfConfigL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOTIfConfigL1Index_Type.__name__ = "Integer32"
_JnxOpticsOTIfConfigL1Index_Object = MibTableColumn
jnxOpticsOTIfConfigL1Index = _JnxOpticsOTIfConfigL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 2),
    _JnxOpticsOTIfConfigL1Index_Type()
)
jnxOpticsOTIfConfigL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOTIfConfigL1Index.setStatus("current")


class _JnxOpticsOTIfConfigL2Index_Type(Integer32):
    """Custom type jnxOpticsOTIfConfigL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOTIfConfigL2Index_Type.__name__ = "Integer32"
_JnxOpticsOTIfConfigL2Index_Object = MibTableColumn
jnxOpticsOTIfConfigL2Index = _JnxOpticsOTIfConfigL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 3),
    _JnxOpticsOTIfConfigL2Index_Type()
)
jnxOpticsOTIfConfigL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOTIfConfigL2Index.setStatus("current")


class _JnxOpticsOTIfConfigL3Index_Type(Integer32):
    """Custom type jnxOpticsOTIfConfigL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOTIfConfigL3Index_Type.__name__ = "Integer32"
_JnxOpticsOTIfConfigL3Index_Object = MibTableColumn
jnxOpticsOTIfConfigL3Index = _JnxOpticsOTIfConfigL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 4),
    _JnxOpticsOTIfConfigL3Index_Type()
)
jnxOpticsOTIfConfigL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOTIfConfigL3Index.setStatus("current")
_JnxOpticsOTIfLaserEnable_Type = TruthValue
_JnxOpticsOTIfLaserEnable_Object = MibTableColumn
jnxOpticsOTIfLaserEnable = _JnxOpticsOTIfLaserEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 5),
    _JnxOpticsOTIfLaserEnable_Type()
)
jnxOpticsOTIfLaserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfLaserEnable.setStatus("current")
_JnxOpticsOTIfFecMode_Type = JnxOpticsOTIfFecType
_JnxOpticsOTIfFecMode_Object = MibTableColumn
jnxOpticsOTIfFecMode = _JnxOpticsOTIfFecMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 6),
    _JnxOpticsOTIfFecMode_Type()
)
jnxOpticsOTIfFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfFecMode.setStatus("current")
_JnxOpticsOTIfEncodingOption_Type = JnxOpticsOTIfEncodingOptions
_JnxOpticsOTIfEncodingOption_Object = MibTableColumn
jnxOpticsOTIfEncodingOption = _JnxOpticsOTIfEncodingOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 7),
    _JnxOpticsOTIfEncodingOption_Type()
)
jnxOpticsOTIfEncodingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfEncodingOption.setStatus("current")


class _JnxOpticsOTIfModulation_Type(Integer32):
    """Custom type jnxOpticsOTIfModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOTIfModulation_Type.__name__ = "Integer32"
_JnxOpticsOTIfModulation_Object = MibTableColumn
jnxOpticsOTIfModulation = _JnxOpticsOTIfModulation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 8),
    _JnxOpticsOTIfModulation_Type()
)
jnxOpticsOTIfModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfModulation.setStatus("current")
_JnxOpticsOTIfAdminState_Type = JnxOpticsOTIfAdminStates
_JnxOpticsOTIfAdminState_Object = MibTableColumn
jnxOpticsOTIfAdminState = _JnxOpticsOTIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 9),
    _JnxOpticsOTIfAdminState_Type()
)
jnxOpticsOTIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfAdminState.setStatus("current")
_JnxOpticsOTIfOperState_Type = JnxOpticsOTIfOperStates
_JnxOpticsOTIfOperState_Object = MibTableColumn
jnxOpticsOTIfOperState = _JnxOpticsOTIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 10),
    _JnxOpticsOTIfOperState_Type()
)
jnxOpticsOTIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfOperState.setStatus("current")
_JnxOpticsOTIfHighPolarization_Type = TruthValue
_JnxOpticsOTIfHighPolarization_Object = MibTableColumn
jnxOpticsOTIfHighPolarization = _JnxOpticsOTIfHighPolarization_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 11),
    _JnxOpticsOTIfHighPolarization_Type()
)
jnxOpticsOTIfHighPolarization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfHighPolarization.setStatus("current")
_JnxOpticsOTIfPreFecBERThresholdMantissa_Type = Integer32
_JnxOpticsOTIfPreFecBERThresholdMantissa_Object = MibTableColumn
jnxOpticsOTIfPreFecBERThresholdMantissa = _JnxOpticsOTIfPreFecBERThresholdMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 12),
    _JnxOpticsOTIfPreFecBERThresholdMantissa_Type()
)
jnxOpticsOTIfPreFecBERThresholdMantissa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPreFecBERThresholdMantissa.setStatus("current")
_JnxOpticsOTIfPreFecBERThresholdExponent_Type = Integer32
_JnxOpticsOTIfPreFecBERThresholdExponent_Object = MibTableColumn
jnxOpticsOTIfPreFecBERThresholdExponent = _JnxOpticsOTIfPreFecBERThresholdExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 13),
    _JnxOpticsOTIfPreFecBERThresholdExponent_Type()
)
jnxOpticsOTIfPreFecBERThresholdExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPreFecBERThresholdExponent.setStatus("current")
_JnxOpticsOTIfPreFecBERThresholdTime_Type = Integer32
_JnxOpticsOTIfPreFecBERThresholdTime_Object = MibTableColumn
jnxOpticsOTIfPreFecBERThresholdTime = _JnxOpticsOTIfPreFecBERThresholdTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 14),
    _JnxOpticsOTIfPreFecBERThresholdTime_Type()
)
jnxOpticsOTIfPreFecBERThresholdTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPreFecBERThresholdTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPreFecBERThresholdTime.setUnits("ms")
_JnxOpticsOTIfPreFecBERThresholdClearMantissa_Type = Integer32
_JnxOpticsOTIfPreFecBERThresholdClearMantissa_Object = MibTableColumn
jnxOpticsOTIfPreFecBERThresholdClearMantissa = _JnxOpticsOTIfPreFecBERThresholdClearMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 15),
    _JnxOpticsOTIfPreFecBERThresholdClearMantissa_Type()
)
jnxOpticsOTIfPreFecBERThresholdClearMantissa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPreFecBERThresholdClearMantissa.setStatus("current")
_JnxOpticsOTIfPreFecBERThresholdClearExponent_Type = Integer32
_JnxOpticsOTIfPreFecBERThresholdClearExponent_Object = MibTableColumn
jnxOpticsOTIfPreFecBERThresholdClearExponent = _JnxOpticsOTIfPreFecBERThresholdClearExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 1, 8, 1, 16),
    _JnxOpticsOTIfPreFecBERThresholdClearExponent_Type()
)
jnxOpticsOTIfPreFecBERThresholdClearExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPreFecBERThresholdClearExponent.setStatus("current")
_JnxOpticsPerformanceMonitoring_ObjectIdentity = ObjectIdentity
jnxOpticsPerformanceMonitoring = _JnxOpticsPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2)
)
_JnxOpticsPMCurrentTable_Object = MibTable
jnxOpticsPMCurrentTable = _JnxOpticsPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxOpticsPMCurrentTable.setStatus("current")
_JnxOpticsPMCurrentEntry_Object = MibTableRow
jnxOpticsPMCurrentEntry = _JnxOpticsPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1)
)
jnxOpticsPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsPMCurrentEntry.setStatus("current")
_JnxPMCurChromaticDispersion_Type = Integer32
_JnxPMCurChromaticDispersion_Object = MibTableColumn
jnxPMCurChromaticDispersion = _JnxPMCurChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 1),
    _JnxPMCurChromaticDispersion_Type()
)
jnxPMCurChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurChromaticDispersion.setUnits("ps/nm")
_JnxPMCurDiffGroupDelay_Type = Integer32
_JnxPMCurDiffGroupDelay_Object = MibTableColumn
jnxPMCurDiffGroupDelay = _JnxPMCurDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 2),
    _JnxPMCurDiffGroupDelay_Type()
)
jnxPMCurDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurDiffGroupDelay.setUnits("ps")
_JnxPMCurPolarizationState_Type = Integer32
_JnxPMCurPolarizationState_Object = MibTableColumn
jnxPMCurPolarizationState = _JnxPMCurPolarizationState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 3),
    _JnxPMCurPolarizationState_Type()
)
jnxPMCurPolarizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurPolarizationState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurPolarizationState.setUnits("rad/s")
_JnxPMCurPolarDepLoss_Type = Integer32
_JnxPMCurPolarDepLoss_Object = MibTableColumn
jnxPMCurPolarDepLoss = _JnxPMCurPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 4),
    _JnxPMCurPolarDepLoss_Type()
)
jnxPMCurPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurQ_Type = Integer32
_JnxPMCurQ_Object = MibTableColumn
jnxPMCurQ = _JnxPMCurQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 5),
    _JnxPMCurQ_Type()
)
jnxPMCurQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurQ.setUnits("0.1 dB")
_JnxPMCurSNR_Type = Integer32
_JnxPMCurSNR_Object = MibTableColumn
jnxPMCurSNR = _JnxPMCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 6),
    _JnxPMCurSNR_Type()
)
jnxPMCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurSNR.setUnits("0.1 dB")
_JnxPMCurTxOutputPower_Type = Integer32
_JnxPMCurTxOutputPower_Object = MibTableColumn
jnxPMCurTxOutputPower = _JnxPMCurTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 7),
    _JnxPMCurTxOutputPower_Type()
)
jnxPMCurTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurRxInputPower_Type = Integer32
_JnxPMCurRxInputPower_Object = MibTableColumn
jnxPMCurRxInputPower = _JnxPMCurRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 8),
    _JnxPMCurRxInputPower_Type()
)
jnxPMCurRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurRxInputPower.setUnits("0.01 dbm")
_JnxPMCurMinChromaticDispersion_Type = Integer32
_JnxPMCurMinChromaticDispersion_Object = MibTableColumn
jnxPMCurMinChromaticDispersion = _JnxPMCurMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 9),
    _JnxPMCurMinChromaticDispersion_Type()
)
jnxPMCurMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinChromaticDispersion.setUnits("ps/nm")
_JnxPMCurMaxChromaticDispersion_Type = Integer32
_JnxPMCurMaxChromaticDispersion_Object = MibTableColumn
jnxPMCurMaxChromaticDispersion = _JnxPMCurMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 10),
    _JnxPMCurMaxChromaticDispersion_Type()
)
jnxPMCurMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxChromaticDispersion.setUnits("ps/nm")
_JnxPMCurAvgChromaticDispersion_Type = Integer32
_JnxPMCurAvgChromaticDispersion_Object = MibTableColumn
jnxPMCurAvgChromaticDispersion = _JnxPMCurAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 11),
    _JnxPMCurAvgChromaticDispersion_Type()
)
jnxPMCurAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgChromaticDispersion.setUnits("ps/nm")
_JnxPMCurMinDiffGroupDelay_Type = Integer32
_JnxPMCurMinDiffGroupDelay_Object = MibTableColumn
jnxPMCurMinDiffGroupDelay = _JnxPMCurMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 12),
    _JnxPMCurMinDiffGroupDelay_Type()
)
jnxPMCurMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinDiffGroupDelay.setUnits("ps")
_JnxPMCurMaxDiffGroupDelay_Type = Integer32
_JnxPMCurMaxDiffGroupDelay_Object = MibTableColumn
jnxPMCurMaxDiffGroupDelay = _JnxPMCurMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 13),
    _JnxPMCurMaxDiffGroupDelay_Type()
)
jnxPMCurMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxDiffGroupDelay.setUnits("ps")
_JnxPMCurAvgDiffGroupDelay_Type = Integer32
_JnxPMCurAvgDiffGroupDelay_Object = MibTableColumn
jnxPMCurAvgDiffGroupDelay = _JnxPMCurAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 14),
    _JnxPMCurAvgDiffGroupDelay_Type()
)
jnxPMCurAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgDiffGroupDelay.setUnits("ps")
_JnxPMCurMinPolarState_Type = Integer32
_JnxPMCurMinPolarState_Object = MibTableColumn
jnxPMCurMinPolarState = _JnxPMCurMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 15),
    _JnxPMCurMinPolarState_Type()
)
jnxPMCurMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarState.setUnits("rad/s")
_JnxPMCurMaxPolarState_Type = Integer32
_JnxPMCurMaxPolarState_Object = MibTableColumn
jnxPMCurMaxPolarState = _JnxPMCurMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 16),
    _JnxPMCurMaxPolarState_Type()
)
jnxPMCurMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarState.setUnits("rad/s")
_JnxPMCurAvgPolarState_Type = Integer32
_JnxPMCurAvgPolarState_Object = MibTableColumn
jnxPMCurAvgPolarState = _JnxPMCurAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 17),
    _JnxPMCurAvgPolarState_Type()
)
jnxPMCurAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarState.setUnits("rad/s")
_JnxPMCurMinPolarDepLoss_Type = Integer32
_JnxPMCurMinPolarDepLoss_Object = MibTableColumn
jnxPMCurMinPolarDepLoss = _JnxPMCurMinPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 18),
    _JnxPMCurMinPolarDepLoss_Type()
)
jnxPMCurMinPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurMaxPolarDepLoss_Type = Integer32
_JnxPMCurMaxPolarDepLoss_Object = MibTableColumn
jnxPMCurMaxPolarDepLoss = _JnxPMCurMaxPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 19),
    _JnxPMCurMaxPolarDepLoss_Type()
)
jnxPMCurMaxPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurAvgPolarDepLoss_Type = Integer32
_JnxPMCurAvgPolarDepLoss_Object = MibTableColumn
jnxPMCurAvgPolarDepLoss = _JnxPMCurAvgPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 20),
    _JnxPMCurAvgPolarDepLoss_Type()
)
jnxPMCurAvgPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgPolarDepLoss.setUnits("0.1 dB")
_JnxPMCurMinQ_Type = Integer32
_JnxPMCurMinQ_Object = MibTableColumn
jnxPMCurMinQ = _JnxPMCurMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 21),
    _JnxPMCurMinQ_Type()
)
jnxPMCurMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinQ.setUnits("0.1 dB")
_JnxPMCurMaxQ_Type = Integer32
_JnxPMCurMaxQ_Object = MibTableColumn
jnxPMCurMaxQ = _JnxPMCurMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 22),
    _JnxPMCurMaxQ_Type()
)
jnxPMCurMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxQ.setUnits("0.1 dB")
_JnxPMCurAvgQ_Type = Integer32
_JnxPMCurAvgQ_Object = MibTableColumn
jnxPMCurAvgQ = _JnxPMCurAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 23),
    _JnxPMCurAvgQ_Type()
)
jnxPMCurAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgQ.setUnits("0.1 dB")
_JnxPMCurMinSNR_Type = Integer32
_JnxPMCurMinSNR_Object = MibTableColumn
jnxPMCurMinSNR = _JnxPMCurMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 24),
    _JnxPMCurMinSNR_Type()
)
jnxPMCurMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinSNR.setUnits("0.1 dB")
_JnxPMCurMaxSNR_Type = Integer32
_JnxPMCurMaxSNR_Object = MibTableColumn
jnxPMCurMaxSNR = _JnxPMCurMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 25),
    _JnxPMCurMaxSNR_Type()
)
jnxPMCurMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxSNR.setUnits("0.1 dB")
_JnxPMCurAvgSNR_Type = Integer32
_JnxPMCurAvgSNR_Object = MibTableColumn
jnxPMCurAvgSNR = _JnxPMCurAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 26),
    _JnxPMCurAvgSNR_Type()
)
jnxPMCurAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgSNR.setUnits("0.1 dB")
_JnxPMCurMinTxOutputPower_Type = Integer32
_JnxPMCurMinTxOutputPower_Object = MibTableColumn
jnxPMCurMinTxOutputPower = _JnxPMCurMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 27),
    _JnxPMCurMinTxOutputPower_Type()
)
jnxPMCurMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurMaxTxOutputPower_Type = Integer32
_JnxPMCurMaxTxOutputPower_Object = MibTableColumn
jnxPMCurMaxTxOutputPower = _JnxPMCurMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 28),
    _JnxPMCurMaxTxOutputPower_Type()
)
jnxPMCurMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurAvgTxOutputPower_Type = Integer32
_JnxPMCurAvgTxOutputPower_Object = MibTableColumn
jnxPMCurAvgTxOutputPower = _JnxPMCurAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 29),
    _JnxPMCurAvgTxOutputPower_Type()
)
jnxPMCurAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxOutputPower.setUnits("0.01 dbm")
_JnxPMCurMinRxInputPower_Type = Integer32
_JnxPMCurMinRxInputPower_Object = MibTableColumn
jnxPMCurMinRxInputPower = _JnxPMCurMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 30),
    _JnxPMCurMinRxInputPower_Type()
)
jnxPMCurMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinRxInputPower.setUnits("0.01 dbm")
_JnxPMCurMaxRxInputPower_Type = Integer32
_JnxPMCurMaxRxInputPower_Object = MibTableColumn
jnxPMCurMaxRxInputPower = _JnxPMCurMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 31),
    _JnxPMCurMaxRxInputPower_Type()
)
jnxPMCurMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxInputPower.setUnits("0.01 dbm")
_JnxPMCurAvgRxInputPower_Type = Integer32
_JnxPMCurAvgRxInputPower_Object = MibTableColumn
jnxPMCurAvgRxInputPower = _JnxPMCurAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 32),
    _JnxPMCurAvgRxInputPower_Type()
)
jnxPMCurAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxInputPower.setUnits("0.01 dbm")
_JnxPMCurSuspectedFlag_Type = TruthValue
_JnxPMCurSuspectedFlag_Object = MibTableColumn
jnxPMCurSuspectedFlag = _JnxPMCurSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 33),
    _JnxPMCurSuspectedFlag_Type()
)
jnxPMCurSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurSuspectedFlag.setStatus("current")
_JnxPMCurSuspectReason_Type = Integer32
_JnxPMCurSuspectReason_Object = MibTableColumn
jnxPMCurSuspectReason = _JnxPMCurSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 34),
    _JnxPMCurSuspectReason_Type()
)
jnxPMCurSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurSuspectReason.setStatus("current")
_JnxPMCurTxLaserBiasCurrent_Type = Integer32
_JnxPMCurTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurTxLaserBiasCurrent = _JnxPMCurTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 35),
    _JnxPMCurTxLaserBiasCurrent_Type()
)
jnxPMCurTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMinTxLaserBiasCurrent_Type = Integer32
_JnxPMCurMinTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMinTxLaserBiasCurrent = _JnxPMCurMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 36),
    _JnxPMCurMinTxLaserBiasCurrent_Type()
)
jnxPMCurMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMaxTxLaserBiasCurrent_Type = Integer32
_JnxPMCurMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMaxTxLaserBiasCurrent = _JnxPMCurMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 37),
    _JnxPMCurMaxTxLaserBiasCurrent_Type()
)
jnxPMCurMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurAvgTxLaserBiasCurrent_Type = Integer32
_JnxPMCurAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurAvgTxLaserBiasCurrent = _JnxPMCurAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 38),
    _JnxPMCurAvgTxLaserBiasCurrent_Type()
)
jnxPMCurAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurTemperature_Type = Integer32
_JnxPMCurTemperature_Object = MibTableColumn
jnxPMCurTemperature = _JnxPMCurTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 39),
    _JnxPMCurTemperature_Type()
)
jnxPMCurTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurTemperature.setUnits(".1 Celcius")
_JnxPMCurMinTemperature_Type = Integer32
_JnxPMCurMinTemperature_Object = MibTableColumn
jnxPMCurMinTemperature = _JnxPMCurMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 40),
    _JnxPMCurMinTemperature_Type()
)
jnxPMCurMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinTemperature.setUnits(".1 Celcius")
_JnxPMCurMaxTemperature_Type = Integer32
_JnxPMCurMaxTemperature_Object = MibTableColumn
jnxPMCurMaxTemperature = _JnxPMCurMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 41),
    _JnxPMCurMaxTemperature_Type()
)
jnxPMCurMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxTemperature.setUnits(".1 Celcius")
_JnxPMCurAvgTemperature_Type = Integer32
_JnxPMCurAvgTemperature_Object = MibTableColumn
jnxPMCurAvgTemperature = _JnxPMCurAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 42),
    _JnxPMCurAvgTemperature_Type()
)
jnxPMCurAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgTemperature.setUnits(".1 Celcius")
_JnxPMCurCarFreqOffset_Type = Integer32
_JnxPMCurCarFreqOffset_Object = MibTableColumn
jnxPMCurCarFreqOffset = _JnxPMCurCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 43),
    _JnxPMCurCarFreqOffset_Type()
)
jnxPMCurCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurCarFreqOffset.setUnits("MHz")
_JnxPMCurMinCarFreqOffset_Type = Integer32
_JnxPMCurMinCarFreqOffset_Object = MibTableColumn
jnxPMCurMinCarFreqOffset = _JnxPMCurMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 44),
    _JnxPMCurMinCarFreqOffset_Type()
)
jnxPMCurMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinCarFreqOffset.setUnits("MHz")
_JnxPMCurMaxCarFreqOffset_Type = Integer32
_JnxPMCurMaxCarFreqOffset_Object = MibTableColumn
jnxPMCurMaxCarFreqOffset = _JnxPMCurMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 45),
    _JnxPMCurMaxCarFreqOffset_Type()
)
jnxPMCurMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxCarFreqOffset.setUnits("MHz")
_JnxPMCurAvgCarFreqOffset_Type = Integer32
_JnxPMCurAvgCarFreqOffset_Object = MibTableColumn
jnxPMCurAvgCarFreqOffset = _JnxPMCurAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 46),
    _JnxPMCurAvgCarFreqOffset_Type()
)
jnxPMCurAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgCarFreqOffset.setUnits("MHz")
_JnxPMCurRxLaserBiasCurrent_Type = Integer32
_JnxPMCurRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurRxLaserBiasCurrent = _JnxPMCurRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 47),
    _JnxPMCurRxLaserBiasCurrent_Type()
)
jnxPMCurRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMinRxLaserBiasCurrent_Type = Integer32
_JnxPMCurMinRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMinRxLaserBiasCurrent = _JnxPMCurMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 48),
    _JnxPMCurMinRxLaserBiasCurrent_Type()
)
jnxPMCurMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurMaxRxLaserBiasCurrent_Type = Integer32
_JnxPMCurMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurMaxRxLaserBiasCurrent = _JnxPMCurMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 49),
    _JnxPMCurMaxRxLaserBiasCurrent_Type()
)
jnxPMCurMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurAvgRxLaserBiasCurrent_Type = Integer32
_JnxPMCurAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxPMCurAvgRxLaserBiasCurrent = _JnxPMCurAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 50),
    _JnxPMCurAvgRxLaserBiasCurrent_Type()
)
jnxPMCurAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMCurTecCurrent_Type = Integer32
_JnxPMCurTecCurrent_Object = MibTableColumn
jnxPMCurTecCurrent = _JnxPMCurTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 51),
    _JnxPMCurTecCurrent_Type()
)
jnxPMCurTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurTecCurrent.setUnits(".1 mA")
_JnxPMCurMinTecCurrent_Type = Integer32
_JnxPMCurMinTecCurrent_Object = MibTableColumn
jnxPMCurMinTecCurrent = _JnxPMCurMinTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 52),
    _JnxPMCurMinTecCurrent_Type()
)
jnxPMCurMinTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinTecCurrent.setUnits(".1 mA")
_JnxPMCurMaxTecCurrent_Type = Integer32
_JnxPMCurMaxTecCurrent_Object = MibTableColumn
jnxPMCurMaxTecCurrent = _JnxPMCurMaxTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 53),
    _JnxPMCurMaxTecCurrent_Type()
)
jnxPMCurMaxTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxTecCurrent.setUnits(".1 mA")
_JnxPMCurAvgTecCurrent_Type = Integer32
_JnxPMCurAvgTecCurrent_Object = MibTableColumn
jnxPMCurAvgTecCurrent = _JnxPMCurAvgTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 54),
    _JnxPMCurAvgTecCurrent_Type()
)
jnxPMCurAvgTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgTecCurrent.setUnits(".1 mA")
_JnxPMCurResidualDispersion_Type = Integer32
_JnxPMCurResidualDispersion_Object = MibTableColumn
jnxPMCurResidualDispersion = _JnxPMCurResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 55),
    _JnxPMCurResidualDispersion_Type()
)
jnxPMCurResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurResidualDispersion.setUnits(".1 ps/nm")
_JnxPMCurMinResidualDispersion_Type = Integer32
_JnxPMCurMinResidualDispersion_Object = MibTableColumn
jnxPMCurMinResidualDispersion = _JnxPMCurMinResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 56),
    _JnxPMCurMinResidualDispersion_Type()
)
jnxPMCurMinResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinResidualDispersion.setUnits(".1 ps/nm")
_JnxPMCurMaxResidualDispersion_Type = Integer32
_JnxPMCurMaxResidualDispersion_Object = MibTableColumn
jnxPMCurMaxResidualDispersion = _JnxPMCurMaxResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 57),
    _JnxPMCurMaxResidualDispersion_Type()
)
jnxPMCurMaxResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxResidualDispersion.setUnits(".1 ps/nm")
_JnxPMCurAvgResidualDispersion_Type = Integer32
_JnxPMCurAvgResidualDispersion_Object = MibTableColumn
jnxPMCurAvgResidualDispersion = _JnxPMCurAvgResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 58),
    _JnxPMCurAvgResidualDispersion_Type()
)
jnxPMCurAvgResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgResidualDispersion.setUnits(".1 ps/nm")
_JnxPMCurLevelHistogram_Type = Integer32
_JnxPMCurLevelHistogram_Object = MibTableColumn
jnxPMCurLevelHistogram = _JnxPMCurLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 59),
    _JnxPMCurLevelHistogram_Type()
)
jnxPMCurLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurLevelHistogram.setStatus("current")
_JnxPMCurMinLevelHistogram_Type = Integer32
_JnxPMCurMinLevelHistogram_Object = MibTableColumn
jnxPMCurMinLevelHistogram = _JnxPMCurMinLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 60),
    _JnxPMCurMinLevelHistogram_Type()
)
jnxPMCurMinLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinLevelHistogram.setStatus("current")
_JnxPMCurMaxLevelHistogram_Type = Integer32
_JnxPMCurMaxLevelHistogram_Object = MibTableColumn
jnxPMCurMaxLevelHistogram = _JnxPMCurMaxLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 61),
    _JnxPMCurMaxLevelHistogram_Type()
)
jnxPMCurMaxLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxLevelHistogram.setStatus("current")
_JnxPMCurAvgLevelHistogram_Type = Integer32
_JnxPMCurAvgLevelHistogram_Object = MibTableColumn
jnxPMCurAvgLevelHistogram = _JnxPMCurAvgLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 62),
    _JnxPMCurAvgLevelHistogram_Type()
)
jnxPMCurAvgLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgLevelHistogram.setStatus("current")
_JnxPMCurLaserFrequencyError_Type = Integer32
_JnxPMCurLaserFrequencyError_Object = MibTableColumn
jnxPMCurLaserFrequencyError = _JnxPMCurLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 63),
    _JnxPMCurLaserFrequencyError_Type()
)
jnxPMCurLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurLaserFrequencyError.setUnits("MHz")
_JnxPMCurMinLaserFrequencyError_Type = Integer32
_JnxPMCurMinLaserFrequencyError_Object = MibTableColumn
jnxPMCurMinLaserFrequencyError = _JnxPMCurMinLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 64),
    _JnxPMCurMinLaserFrequencyError_Type()
)
jnxPMCurMinLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMinLaserFrequencyError.setUnits("MHz")
_JnxPMCurMaxLaserFrequencyError_Type = Integer32
_JnxPMCurMaxLaserFrequencyError_Object = MibTableColumn
jnxPMCurMaxLaserFrequencyError = _JnxPMCurMaxLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 65),
    _JnxPMCurMaxLaserFrequencyError_Type()
)
jnxPMCurMaxLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurMaxLaserFrequencyError.setUnits("MHz")
_JnxPMCurAvgLaserFrequencyError_Type = Integer32
_JnxPMCurAvgLaserFrequencyError_Object = MibTableColumn
jnxPMCurAvgLaserFrequencyError = _JnxPMCurAvgLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 66),
    _JnxPMCurAvgLaserFrequencyError_Type()
)
jnxPMCurAvgLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMCurAvgLaserFrequencyError.setUnits("MHz")
_JnxPMCurFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMCurFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMCurFECCorrectedErrorsMantissa = _JnxPMCurFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 67),
    _JnxPMCurFECCorrectedErrorsMantissa_Type()
)
jnxPMCurFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMCurFECCorrectedErrorsExponent_Type = Integer32
_JnxPMCurFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMCurFECCorrectedErrorsExponent = _JnxPMCurFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 68),
    _JnxPMCurFECCorrectedErrorsExponent_Type()
)
jnxPMCurFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurFECCorrectedErrorsExponent.setStatus("current")
_JnxPMCurMinFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMCurMinFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMCurMinFECCorrectedErrorsMantissa = _JnxPMCurMinFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 69),
    _JnxPMCurMinFECCorrectedErrorsMantissa_Type()
)
jnxPMCurMinFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMCurMinFECCorrectedErrorsExponent_Type = Integer32
_JnxPMCurMinFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMCurMinFECCorrectedErrorsExponent = _JnxPMCurMinFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 70),
    _JnxPMCurMinFECCorrectedErrorsExponent_Type()
)
jnxPMCurMinFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinFECCorrectedErrorsExponent.setStatus("current")
_JnxPMCurMaxFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMCurMaxFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMCurMaxFECCorrectedErrorsMantissa = _JnxPMCurMaxFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 71),
    _JnxPMCurMaxFECCorrectedErrorsMantissa_Type()
)
jnxPMCurMaxFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMCurMaxFECCorrectedErrorsExponent_Type = Integer32
_JnxPMCurMaxFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMCurMaxFECCorrectedErrorsExponent = _JnxPMCurMaxFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 72),
    _JnxPMCurMaxFECCorrectedErrorsExponent_Type()
)
jnxPMCurMaxFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxFECCorrectedErrorsExponent.setStatus("current")
_JnxPMCurAvgFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMCurAvgFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMCurAvgFECCorrectedErrorsMantissa = _JnxPMCurAvgFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 73),
    _JnxPMCurAvgFECCorrectedErrorsMantissa_Type()
)
jnxPMCurAvgFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMCurAvgFECCorrectedErrorsExponent_Type = Integer32
_JnxPMCurAvgFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMCurAvgFECCorrectedErrorsExponent = _JnxPMCurAvgFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 74),
    _JnxPMCurAvgFECCorrectedErrorsExponent_Type()
)
jnxPMCurAvgFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgFECCorrectedErrorsExponent.setStatus("current")
_JnxPMCurFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMCurFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMCurFECUCorrectedWordsMantissa = _JnxPMCurFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 75),
    _JnxPMCurFECUCorrectedWordsMantissa_Type()
)
jnxPMCurFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMCurFECUCorrectedWordsExponent_Type = Integer32
_JnxPMCurFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMCurFECUCorrectedWordsExponent = _JnxPMCurFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 76),
    _JnxPMCurFECUCorrectedWordsExponent_Type()
)
jnxPMCurFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurFECUCorrectedWordsExponent.setStatus("current")
_JnxPMCurMinFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMCurMinFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMCurMinFECUCorrectedWordsMantissa = _JnxPMCurMinFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 77),
    _JnxPMCurMinFECUCorrectedWordsMantissa_Type()
)
jnxPMCurMinFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMCurMinFECUCorrectedWordsExponent_Type = Integer32
_JnxPMCurMinFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMCurMinFECUCorrectedWordsExponent = _JnxPMCurMinFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 78),
    _JnxPMCurMinFECUCorrectedWordsExponent_Type()
)
jnxPMCurMinFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMinFECUCorrectedWordsExponent.setStatus("current")
_JnxPMCurMaxFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMCurMaxFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMCurMaxFECUCorrectedWordsMantissa = _JnxPMCurMaxFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 79),
    _JnxPMCurMaxFECUCorrectedWordsMantissa_Type()
)
jnxPMCurMaxFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMCurMaxFECUCorrectedWordsExponent_Type = Integer32
_JnxPMCurMaxFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMCurMaxFECUCorrectedWordsExponent = _JnxPMCurMaxFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 80),
    _JnxPMCurMaxFECUCorrectedWordsExponent_Type()
)
jnxPMCurMaxFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurMaxFECUCorrectedWordsExponent.setStatus("current")
_JnxPMCurAvgFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMCurAvgFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMCurAvgFECUCorrectedWordsMantissa = _JnxPMCurAvgFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 81),
    _JnxPMCurAvgFECUCorrectedWordsMantissa_Type()
)
jnxPMCurAvgFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMCurAvgFECUCorrectedWordsExponent_Type = Integer32
_JnxPMCurAvgFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMCurAvgFECUCorrectedWordsExponent = _JnxPMCurAvgFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 1, 1, 82),
    _JnxPMCurAvgFECUCorrectedWordsExponent_Type()
)
jnxPMCurAvgFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMCurAvgFECUCorrectedWordsExponent.setStatus("current")
_JnxOpticsPMIntervalTable_Object = MibTable
jnxOpticsPMIntervalTable = _JnxOpticsPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxOpticsPMIntervalTable.setStatus("current")
_JnxOpticsPMIntervalEntry_Object = MibTableRow
jnxOpticsPMIntervalEntry = _JnxOpticsPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1)
)
jnxOpticsPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxOpticsPMIntervalEntry.setStatus("current")


class _JnxOpticsPMIntervalNumber_Type(Unsigned32):
    """Custom type jnxOpticsPMIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxOpticsPMIntervalNumber_Type.__name__ = "Unsigned32"
_JnxOpticsPMIntervalNumber_Object = MibTableColumn
jnxOpticsPMIntervalNumber = _JnxOpticsPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 1),
    _JnxOpticsPMIntervalNumber_Type()
)
jnxOpticsPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsPMIntervalNumber.setStatus("current")
_JnxPMIntMinChromaticDispersion_Type = Integer32
_JnxPMIntMinChromaticDispersion_Object = MibTableColumn
jnxPMIntMinChromaticDispersion = _JnxPMIntMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 2),
    _JnxPMIntMinChromaticDispersion_Type()
)
jnxPMIntMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinChromaticDispersion.setUnits("ps/nm")
_JnxPMIntMaxChromaticDispersion_Type = Integer32
_JnxPMIntMaxChromaticDispersion_Object = MibTableColumn
jnxPMIntMaxChromaticDispersion = _JnxPMIntMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 3),
    _JnxPMIntMaxChromaticDispersion_Type()
)
jnxPMIntMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxChromaticDispersion.setUnits("ps/nm")
_JnxPMIntAvgChromaticDispersion_Type = Integer32
_JnxPMIntAvgChromaticDispersion_Object = MibTableColumn
jnxPMIntAvgChromaticDispersion = _JnxPMIntAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 4),
    _JnxPMIntAvgChromaticDispersion_Type()
)
jnxPMIntAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgChromaticDispersion.setUnits("ps/nm")
_JnxPMIntMinDiffGroupDelay_Type = Integer32
_JnxPMIntMinDiffGroupDelay_Object = MibTableColumn
jnxPMIntMinDiffGroupDelay = _JnxPMIntMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 5),
    _JnxPMIntMinDiffGroupDelay_Type()
)
jnxPMIntMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinDiffGroupDelay.setUnits("ps")
_JnxPMIntMaxDiffGroupDelay_Type = Integer32
_JnxPMIntMaxDiffGroupDelay_Object = MibTableColumn
jnxPMIntMaxDiffGroupDelay = _JnxPMIntMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 6),
    _JnxPMIntMaxDiffGroupDelay_Type()
)
jnxPMIntMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxDiffGroupDelay.setUnits("ps")
_JnxPMIntAvgDiffGroupDelay_Type = Integer32
_JnxPMIntAvgDiffGroupDelay_Object = MibTableColumn
jnxPMIntAvgDiffGroupDelay = _JnxPMIntAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 7),
    _JnxPMIntAvgDiffGroupDelay_Type()
)
jnxPMIntAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgDiffGroupDelay.setUnits("ps")
_JnxPMIntMinPolarState_Type = Integer32
_JnxPMIntMinPolarState_Object = MibTableColumn
jnxPMIntMinPolarState = _JnxPMIntMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 8),
    _JnxPMIntMinPolarState_Type()
)
jnxPMIntMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarState.setUnits("rad/s")
_JnxPMIntMaxPolarState_Type = Integer32
_JnxPMIntMaxPolarState_Object = MibTableColumn
jnxPMIntMaxPolarState = _JnxPMIntMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 9),
    _JnxPMIntMaxPolarState_Type()
)
jnxPMIntMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarState.setUnits("rad/s")
_JnxPMIntAvgPolarState_Type = Integer32
_JnxPMIntAvgPolarState_Object = MibTableColumn
jnxPMIntAvgPolarState = _JnxPMIntAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 10),
    _JnxPMIntAvgPolarState_Type()
)
jnxPMIntAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarState.setUnits("rad/s")
_JnxPMIntMinPolarDependentLoss_Type = Integer32
_JnxPMIntMinPolarDependentLoss_Object = MibTableColumn
jnxPMIntMinPolarDependentLoss = _JnxPMIntMinPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 11),
    _JnxPMIntMinPolarDependentLoss_Type()
)
jnxPMIntMinPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinPolarDependentLoss.setUnits("0.1 dB")
_JnxPMIntMaxPolarDependentLoss_Type = Integer32
_JnxPMIntMaxPolarDependentLoss_Object = MibTableColumn
jnxPMIntMaxPolarDependentLoss = _JnxPMIntMaxPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 12),
    _JnxPMIntMaxPolarDependentLoss_Type()
)
jnxPMIntMaxPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxPolarDependentLoss.setUnits("0.1 dB")
_JnxPMIntAvgPolarDependentLoss_Type = Integer32
_JnxPMIntAvgPolarDependentLoss_Object = MibTableColumn
jnxPMIntAvgPolarDependentLoss = _JnxPMIntAvgPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 13),
    _JnxPMIntAvgPolarDependentLoss_Type()
)
jnxPMIntAvgPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgPolarDependentLoss.setUnits("0.1 dB")
_JnxPMIntMinQ_Type = Integer32
_JnxPMIntMinQ_Object = MibTableColumn
jnxPMIntMinQ = _JnxPMIntMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 14),
    _JnxPMIntMinQ_Type()
)
jnxPMIntMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinQ.setUnits("0.1 dB")
_JnxPMIntMaxQ_Type = Integer32
_JnxPMIntMaxQ_Object = MibTableColumn
jnxPMIntMaxQ = _JnxPMIntMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 15),
    _JnxPMIntMaxQ_Type()
)
jnxPMIntMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxQ.setUnits("0.1 dB")
_JnxPMIntAvgQ_Type = Integer32
_JnxPMIntAvgQ_Object = MibTableColumn
jnxPMIntAvgQ = _JnxPMIntAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 16),
    _JnxPMIntAvgQ_Type()
)
jnxPMIntAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgQ.setUnits("0.1 dB")
_JnxPMIntMinSNR_Type = Integer32
_JnxPMIntMinSNR_Object = MibTableColumn
jnxPMIntMinSNR = _JnxPMIntMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 17),
    _JnxPMIntMinSNR_Type()
)
jnxPMIntMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinSNR.setUnits("0.1 dB")
_JnxPMIntMaxSNR_Type = Integer32
_JnxPMIntMaxSNR_Object = MibTableColumn
jnxPMIntMaxSNR = _JnxPMIntMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 18),
    _JnxPMIntMaxSNR_Type()
)
jnxPMIntMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxSNR.setUnits("0.1 dB")
_JnxPMIntAvgSNR_Type = Integer32
_JnxPMIntAvgSNR_Object = MibTableColumn
jnxPMIntAvgSNR = _JnxPMIntAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 19),
    _JnxPMIntAvgSNR_Type()
)
jnxPMIntAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgSNR.setUnits("0.1 dB")
_JnxPMIntMinTxOutputPower_Type = Integer32
_JnxPMIntMinTxOutputPower_Object = MibTableColumn
jnxPMIntMinTxOutputPower = _JnxPMIntMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 20),
    _JnxPMIntMinTxOutputPower_Type()
)
jnxPMIntMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinTxOutputPower.setUnits("0.01 dbm")
_JnxPMIntMaxTxOutputPower_Type = Integer32
_JnxPMIntMaxTxOutputPower_Object = MibTableColumn
jnxPMIntMaxTxOutputPower = _JnxPMIntMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 21),
    _JnxPMIntMaxTxOutputPower_Type()
)
jnxPMIntMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxOutputPower.setUnits("0.01 dbm")
_JnxPMIntAvgTxOutputPower_Type = Integer32
_JnxPMIntAvgTxOutputPower_Object = MibTableColumn
jnxPMIntAvgTxOutputPower = _JnxPMIntAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 22),
    _JnxPMIntAvgTxOutputPower_Type()
)
jnxPMIntAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxOutputPower.setUnits("0.01 dbm")
_JnxPMIntMinRxInputPower_Type = Integer32
_JnxPMIntMinRxInputPower_Object = MibTableColumn
jnxPMIntMinRxInputPower = _JnxPMIntMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 23),
    _JnxPMIntMinRxInputPower_Type()
)
jnxPMIntMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinRxInputPower.setUnits("0.01 dbm")
_JnxPMIntMaxRxInputPower_Type = Integer32
_JnxPMIntMaxRxInputPower_Object = MibTableColumn
jnxPMIntMaxRxInputPower = _JnxPMIntMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 24),
    _JnxPMIntMaxRxInputPower_Type()
)
jnxPMIntMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxInputPower.setUnits("0.01 dbm")
_JnxPMIntAvgRxInputPower_Type = Integer32
_JnxPMIntAvgRxInputPower_Object = MibTableColumn
jnxPMIntAvgRxInputPower = _JnxPMIntAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 25),
    _JnxPMIntAvgRxInputPower_Type()
)
jnxPMIntAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxInputPower.setUnits("0.01 dbm")
_JnxPMIntTimeStamp_Type = DateAndTime
_JnxPMIntTimeStamp_Object = MibTableColumn
jnxPMIntTimeStamp = _JnxPMIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 26),
    _JnxPMIntTimeStamp_Type()
)
jnxPMIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntTimeStamp.setStatus("current")
_JnxPMIntSuspectedFlag_Type = TruthValue
_JnxPMIntSuspectedFlag_Object = MibTableColumn
jnxPMIntSuspectedFlag = _JnxPMIntSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 27),
    _JnxPMIntSuspectedFlag_Type()
)
jnxPMIntSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntSuspectedFlag.setStatus("current")
_JnxPMIntSuspectReason_Type = Integer32
_JnxPMIntSuspectReason_Object = MibTableColumn
jnxPMIntSuspectReason = _JnxPMIntSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 28),
    _JnxPMIntSuspectReason_Type()
)
jnxPMIntSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntSuspectReason.setStatus("current")
_JnxPMIntMinTxLaserBiasCurrent_Type = Integer32
_JnxPMIntMinTxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMinTxLaserBiasCurrent = _JnxPMIntMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 29),
    _JnxPMIntMinTxLaserBiasCurrent_Type()
)
jnxPMIntMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntMaxTxLaserBiasCurrent_Type = Integer32
_JnxPMIntMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMaxTxLaserBiasCurrent = _JnxPMIntMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 30),
    _JnxPMIntMaxTxLaserBiasCurrent_Type()
)
jnxPMIntMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntAvgTxLaserBiasCurrent_Type = Integer32
_JnxPMIntAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntAvgTxLaserBiasCurrent = _JnxPMIntAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 31),
    _JnxPMIntAvgTxLaserBiasCurrent_Type()
)
jnxPMIntAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntMinTemperature_Type = Integer32
_JnxPMIntMinTemperature_Object = MibTableColumn
jnxPMIntMinTemperature = _JnxPMIntMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 32),
    _JnxPMIntMinTemperature_Type()
)
jnxPMIntMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinTemperature.setUnits(".1 Celcius")
_JnxPMIntMaxTemperature_Type = Integer32
_JnxPMIntMaxTemperature_Object = MibTableColumn
jnxPMIntMaxTemperature = _JnxPMIntMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 33),
    _JnxPMIntMaxTemperature_Type()
)
jnxPMIntMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxTemperature.setUnits(".1 Celcius")
_JnxPMIntAvgTemperature_Type = Integer32
_JnxPMIntAvgTemperature_Object = MibTableColumn
jnxPMIntAvgTemperature = _JnxPMIntAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 34),
    _JnxPMIntAvgTemperature_Type()
)
jnxPMIntAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgTemperature.setUnits(".1 Celcius")
_JnxPMIntMinCarFreqOffset_Type = Integer32
_JnxPMIntMinCarFreqOffset_Object = MibTableColumn
jnxPMIntMinCarFreqOffset = _JnxPMIntMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 35),
    _JnxPMIntMinCarFreqOffset_Type()
)
jnxPMIntMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinCarFreqOffset.setUnits("Mhz")
_JnxPMIntMaxCarFreqOffset_Type = Integer32
_JnxPMIntMaxCarFreqOffset_Object = MibTableColumn
jnxPMIntMaxCarFreqOffset = _JnxPMIntMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 36),
    _JnxPMIntMaxCarFreqOffset_Type()
)
jnxPMIntMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxCarFreqOffset.setUnits("MHz")
_JnxPMIntAvgCarFreqOffset_Type = Integer32
_JnxPMIntAvgCarFreqOffset_Object = MibTableColumn
jnxPMIntAvgCarFreqOffset = _JnxPMIntAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 37),
    _JnxPMIntAvgCarFreqOffset_Type()
)
jnxPMIntAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgCarFreqOffset.setUnits("MHz")
_JnxPMIntMinRxLaserBiasCurrent_Type = Integer32
_JnxPMIntMinRxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMinRxLaserBiasCurrent = _JnxPMIntMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 38),
    _JnxPMIntMinRxLaserBiasCurrent_Type()
)
jnxPMIntMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntMaxRxLaserBiasCurrent_Type = Integer32
_JnxPMIntMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntMaxRxLaserBiasCurrent = _JnxPMIntMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 39),
    _JnxPMIntMaxRxLaserBiasCurrent_Type()
)
jnxPMIntMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntAvgRxLaserBiasCurrent_Type = Integer32
_JnxPMIntAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxPMIntAvgRxLaserBiasCurrent = _JnxPMIntAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 40),
    _JnxPMIntAvgRxLaserBiasCurrent_Type()
)
jnxPMIntAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMIntMinTecCurrent_Type = Integer32
_JnxPMIntMinTecCurrent_Object = MibTableColumn
jnxPMIntMinTecCurrent = _JnxPMIntMinTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 41),
    _JnxPMIntMinTecCurrent_Type()
)
jnxPMIntMinTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinTecCurrent.setUnits(".1 mA")
_JnxPMIntMaxTecCurrent_Type = Integer32
_JnxPMIntMaxTecCurrent_Object = MibTableColumn
jnxPMIntMaxTecCurrent = _JnxPMIntMaxTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 42),
    _JnxPMIntMaxTecCurrent_Type()
)
jnxPMIntMaxTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxTecCurrent.setUnits(".1 mA")
_JnxPMIntAvgTecCurrent_Type = Integer32
_JnxPMIntAvgTecCurrent_Object = MibTableColumn
jnxPMIntAvgTecCurrent = _JnxPMIntAvgTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 43),
    _JnxPMIntAvgTecCurrent_Type()
)
jnxPMIntAvgTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgTecCurrent.setUnits(".1 mA")
_JnxPMIntMinResidualDispersion_Type = Integer32
_JnxPMIntMinResidualDispersion_Object = MibTableColumn
jnxPMIntMinResidualDispersion = _JnxPMIntMinResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 44),
    _JnxPMIntMinResidualDispersion_Type()
)
jnxPMIntMinResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinResidualDispersion.setUnits("ps/nm")
_JnxPMIntMaxResidualDispersion_Type = Integer32
_JnxPMIntMaxResidualDispersion_Object = MibTableColumn
jnxPMIntMaxResidualDispersion = _JnxPMIntMaxResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 45),
    _JnxPMIntMaxResidualDispersion_Type()
)
jnxPMIntMaxResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxResidualDispersion.setUnits("ps/nm")
_JnxPMIntAvgResidualDispersion_Type = Integer32
_JnxPMIntAvgResidualDispersion_Object = MibTableColumn
jnxPMIntAvgResidualDispersion = _JnxPMIntAvgResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 46),
    _JnxPMIntAvgResidualDispersion_Type()
)
jnxPMIntAvgResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgResidualDispersion.setUnits("ps/nm")
_JnxPMIntMinLevelHistogram_Type = Integer32
_JnxPMIntMinLevelHistogram_Object = MibTableColumn
jnxPMIntMinLevelHistogram = _JnxPMIntMinLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 47),
    _JnxPMIntMinLevelHistogram_Type()
)
jnxPMIntMinLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinLevelHistogram.setStatus("current")
_JnxPMIntMaxLevelHistogram_Type = Integer32
_JnxPMIntMaxLevelHistogram_Object = MibTableColumn
jnxPMIntMaxLevelHistogram = _JnxPMIntMaxLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 48),
    _JnxPMIntMaxLevelHistogram_Type()
)
jnxPMIntMaxLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxLevelHistogram.setStatus("current")
_JnxPMIntAvgLevelHistogram_Type = Integer32
_JnxPMIntAvgLevelHistogram_Object = MibTableColumn
jnxPMIntAvgLevelHistogram = _JnxPMIntAvgLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 49),
    _JnxPMIntAvgLevelHistogram_Type()
)
jnxPMIntAvgLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgLevelHistogram.setStatus("current")
_JnxPMIntMinLaserFrequencyError_Type = Integer32
_JnxPMIntMinLaserFrequencyError_Object = MibTableColumn
jnxPMIntMinLaserFrequencyError = _JnxPMIntMinLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 50),
    _JnxPMIntMinLaserFrequencyError_Type()
)
jnxPMIntMinLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMinLaserFrequencyError.setUnits(".1 Celcius")
_JnxPMIntMaxLaserFrequencyError_Type = Integer32
_JnxPMIntMaxLaserFrequencyError_Object = MibTableColumn
jnxPMIntMaxLaserFrequencyError = _JnxPMIntMaxLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 51),
    _JnxPMIntMaxLaserFrequencyError_Type()
)
jnxPMIntMaxLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntMaxLaserFrequencyError.setUnits(".1 Celcius")
_JnxPMIntAvgLaserFrequencyError_Type = Integer32
_JnxPMIntAvgLaserFrequencyError_Object = MibTableColumn
jnxPMIntAvgLaserFrequencyError = _JnxPMIntAvgLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 52),
    _JnxPMIntAvgLaserFrequencyError_Type()
)
jnxPMIntAvgLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMIntAvgLaserFrequencyError.setUnits(".1 Celcius")
_JnxPMIntMinFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMIntMinFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMIntMinFECCorrectedErrorsMantissa = _JnxPMIntMinFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 53),
    _JnxPMIntMinFECCorrectedErrorsMantissa_Type()
)
jnxPMIntMinFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMIntMinFECCorrectedErrorsExponent_Type = Integer32
_JnxPMIntMinFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMIntMinFECCorrectedErrorsExponent = _JnxPMIntMinFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 54),
    _JnxPMIntMinFECCorrectedErrorsExponent_Type()
)
jnxPMIntMinFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinFECCorrectedErrorsExponent.setStatus("current")
_JnxPMIntMaxFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMIntMaxFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMIntMaxFECCorrectedErrorsMantissa = _JnxPMIntMaxFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 55),
    _JnxPMIntMaxFECCorrectedErrorsMantissa_Type()
)
jnxPMIntMaxFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMIntMaxFECCorrectedErrorsExponent_Type = Integer32
_JnxPMIntMaxFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMIntMaxFECCorrectedErrorsExponent = _JnxPMIntMaxFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 56),
    _JnxPMIntMaxFECCorrectedErrorsExponent_Type()
)
jnxPMIntMaxFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxFECCorrectedErrorsExponent.setStatus("current")
_JnxPMIntAvgFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMIntAvgFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMIntAvgFECCorrectedErrorsMantissa = _JnxPMIntAvgFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 57),
    _JnxPMIntAvgFECCorrectedErrorsMantissa_Type()
)
jnxPMIntAvgFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMIntAvgFECCorrectedErrorsExponent_Type = Integer32
_JnxPMIntAvgFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMIntAvgFECCorrectedErrorsExponent = _JnxPMIntAvgFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 58),
    _JnxPMIntAvgFECCorrectedErrorsExponent_Type()
)
jnxPMIntAvgFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgFECCorrectedErrorsExponent.setStatus("current")
_JnxPMIntMinFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMIntMinFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMIntMinFECUCorrectedWordsMantissa = _JnxPMIntMinFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 59),
    _JnxPMIntMinFECUCorrectedWordsMantissa_Type()
)
jnxPMIntMinFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMIntMinFECUCorrectedWordsExponent_Type = Integer32
_JnxPMIntMinFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMIntMinFECUCorrectedWordsExponent = _JnxPMIntMinFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 60),
    _JnxPMIntMinFECUCorrectedWordsExponent_Type()
)
jnxPMIntMinFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMinFECUCorrectedWordsExponent.setStatus("current")
_JnxPMIntMaxFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMIntMaxFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMIntMaxFECUCorrectedWordsMantissa = _JnxPMIntMaxFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 61),
    _JnxPMIntMaxFECUCorrectedWordsMantissa_Type()
)
jnxPMIntMaxFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMIntMaxFECUCorrectedWordsExponent_Type = Integer32
_JnxPMIntMaxFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMIntMaxFECUCorrectedWordsExponent = _JnxPMIntMaxFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 62),
    _JnxPMIntMaxFECUCorrectedWordsExponent_Type()
)
jnxPMIntMaxFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntMaxFECUCorrectedWordsExponent.setStatus("current")
_JnxPMIntAvgFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMIntAvgFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMIntAvgFECUCorrectedWordsMantissa = _JnxPMIntAvgFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 63),
    _JnxPMIntAvgFECUCorrectedWordsMantissa_Type()
)
jnxPMIntAvgFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMIntAvgFECUCorrectedWordsExponent_Type = Integer32
_JnxPMIntAvgFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMIntAvgFECUCorrectedWordsExponent = _JnxPMIntAvgFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 2, 1, 64),
    _JnxPMIntAvgFECUCorrectedWordsExponent_Type()
)
jnxPMIntAvgFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMIntAvgFECUCorrectedWordsExponent.setStatus("current")
_JnxOpticsPMDayTable_Object = MibTable
jnxOpticsPMDayTable = _JnxOpticsPMDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxOpticsPMDayTable.setStatus("current")
_JnxOpticsPMDayEntry_Object = MibTableRow
jnxOpticsPMDayEntry = _JnxOpticsPMDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1)
)
jnxOpticsPMDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsPMDayIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsPMDayEntry.setStatus("current")


class _JnxOpticsPMDayIndex_Type(Unsigned32):
    """Custom type jnxOpticsPMDayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_JnxOpticsPMDayIndex_Type.__name__ = "Unsigned32"
_JnxOpticsPMDayIndex_Object = MibTableColumn
jnxOpticsPMDayIndex = _JnxOpticsPMDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 1),
    _JnxOpticsPMDayIndex_Type()
)
jnxOpticsPMDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsPMDayIndex.setStatus("current")
_JnxPMDayMinChromaticDispersion_Type = Integer32
_JnxPMDayMinChromaticDispersion_Object = MibTableColumn
jnxPMDayMinChromaticDispersion = _JnxPMDayMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 2),
    _JnxPMDayMinChromaticDispersion_Type()
)
jnxPMDayMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinChromaticDispersion.setUnits("ps/nm")
_JnxPMDayMaxChromaticDispersion_Type = Integer32
_JnxPMDayMaxChromaticDispersion_Object = MibTableColumn
jnxPMDayMaxChromaticDispersion = _JnxPMDayMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 3),
    _JnxPMDayMaxChromaticDispersion_Type()
)
jnxPMDayMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxChromaticDispersion.setUnits("ps/nm")
_JnxPMDayAvgChromaticDispersion_Type = Integer32
_JnxPMDayAvgChromaticDispersion_Object = MibTableColumn
jnxPMDayAvgChromaticDispersion = _JnxPMDayAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 4),
    _JnxPMDayAvgChromaticDispersion_Type()
)
jnxPMDayAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgChromaticDispersion.setUnits("ps/nm")
_JnxPMDayMinDiffGroupDelay_Type = Integer32
_JnxPMDayMinDiffGroupDelay_Object = MibTableColumn
jnxPMDayMinDiffGroupDelay = _JnxPMDayMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 5),
    _JnxPMDayMinDiffGroupDelay_Type()
)
jnxPMDayMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinDiffGroupDelay.setUnits("ps")
_JnxPMDayMaxDiffGroupDelay_Type = Integer32
_JnxPMDayMaxDiffGroupDelay_Object = MibTableColumn
jnxPMDayMaxDiffGroupDelay = _JnxPMDayMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 6),
    _JnxPMDayMaxDiffGroupDelay_Type()
)
jnxPMDayMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxDiffGroupDelay.setUnits("ps")
_JnxPMDayAvgDiffGroupDelay_Type = Integer32
_JnxPMDayAvgDiffGroupDelay_Object = MibTableColumn
jnxPMDayAvgDiffGroupDelay = _JnxPMDayAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 7),
    _JnxPMDayAvgDiffGroupDelay_Type()
)
jnxPMDayAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgDiffGroupDelay.setUnits("ps")
_JnxPMDayMinPolarState_Type = Integer32
_JnxPMDayMinPolarState_Object = MibTableColumn
jnxPMDayMinPolarState = _JnxPMDayMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 8),
    _JnxPMDayMinPolarState_Type()
)
jnxPMDayMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarState.setUnits("rad/s")
_JnxPMDayMaxPolarState_Type = Integer32
_JnxPMDayMaxPolarState_Object = MibTableColumn
jnxPMDayMaxPolarState = _JnxPMDayMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 9),
    _JnxPMDayMaxPolarState_Type()
)
jnxPMDayMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarState.setUnits("rad/s")
_JnxPMDayAvgPolarState_Type = Integer32
_JnxPMDayAvgPolarState_Object = MibTableColumn
jnxPMDayAvgPolarState = _JnxPMDayAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 10),
    _JnxPMDayAvgPolarState_Type()
)
jnxPMDayAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarState.setUnits("rad/s")
_JnxPMDayMinPolarDependentLoss_Type = Integer32
_JnxPMDayMinPolarDependentLoss_Object = MibTableColumn
jnxPMDayMinPolarDependentLoss = _JnxPMDayMinPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 11),
    _JnxPMDayMinPolarDependentLoss_Type()
)
jnxPMDayMinPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinPolarDependentLoss.setUnits("0.1 dB")
_JnxPMDayMaxPolarDependentLoss_Type = Integer32
_JnxPMDayMaxPolarDependentLoss_Object = MibTableColumn
jnxPMDayMaxPolarDependentLoss = _JnxPMDayMaxPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 12),
    _JnxPMDayMaxPolarDependentLoss_Type()
)
jnxPMDayMaxPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxPolarDependentLoss.setUnits("0.1 dB")
_JnxPMDayAvgPolarDependentLoss_Type = Integer32
_JnxPMDayAvgPolarDependentLoss_Object = MibTableColumn
jnxPMDayAvgPolarDependentLoss = _JnxPMDayAvgPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 13),
    _JnxPMDayAvgPolarDependentLoss_Type()
)
jnxPMDayAvgPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgPolarDependentLoss.setUnits("0.1 dB")
_JnxPMDayMinQ_Type = Integer32
_JnxPMDayMinQ_Object = MibTableColumn
jnxPMDayMinQ = _JnxPMDayMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 14),
    _JnxPMDayMinQ_Type()
)
jnxPMDayMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinQ.setUnits("0.1 dB")
_JnxPMDayMaxQ_Type = Integer32
_JnxPMDayMaxQ_Object = MibTableColumn
jnxPMDayMaxQ = _JnxPMDayMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 15),
    _JnxPMDayMaxQ_Type()
)
jnxPMDayMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxQ.setUnits("0.1 dB")
_JnxPMDayAvgQ_Type = Integer32
_JnxPMDayAvgQ_Object = MibTableColumn
jnxPMDayAvgQ = _JnxPMDayAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 16),
    _JnxPMDayAvgQ_Type()
)
jnxPMDayAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgQ.setUnits("0.1 dB")
_JnxPMDayMinSNR_Type = Integer32
_JnxPMDayMinSNR_Object = MibTableColumn
jnxPMDayMinSNR = _JnxPMDayMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 17),
    _JnxPMDayMinSNR_Type()
)
jnxPMDayMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinSNR.setUnits("0.1 dB")
_JnxPMDayMaxSNR_Type = Integer32
_JnxPMDayMaxSNR_Object = MibTableColumn
jnxPMDayMaxSNR = _JnxPMDayMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 18),
    _JnxPMDayMaxSNR_Type()
)
jnxPMDayMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxSNR.setUnits("0.1 dB")
_JnxPMDayAvgSNR_Type = Integer32
_JnxPMDayAvgSNR_Object = MibTableColumn
jnxPMDayAvgSNR = _JnxPMDayAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 19),
    _JnxPMDayAvgSNR_Type()
)
jnxPMDayAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgSNR.setUnits("0.1 dB")
_JnxPMDayMinTxOutputPower_Type = Integer32
_JnxPMDayMinTxOutputPower_Object = MibTableColumn
jnxPMDayMinTxOutputPower = _JnxPMDayMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 20),
    _JnxPMDayMinTxOutputPower_Type()
)
jnxPMDayMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinTxOutputPower.setUnits("0.01 dbm")
_JnxPMDayMaxTxOutputPower_Type = Integer32
_JnxPMDayMaxTxOutputPower_Object = MibTableColumn
jnxPMDayMaxTxOutputPower = _JnxPMDayMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 21),
    _JnxPMDayMaxTxOutputPower_Type()
)
jnxPMDayMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxOutputPower.setUnits("0.01 dbm")
_JnxPMDayAvgTxOutputPower_Type = Integer32
_JnxPMDayAvgTxOutputPower_Object = MibTableColumn
jnxPMDayAvgTxOutputPower = _JnxPMDayAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 22),
    _JnxPMDayAvgTxOutputPower_Type()
)
jnxPMDayAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxOutputPower.setUnits("0.01 dbm")
_JnxPMDayMinRxInputPower_Type = Integer32
_JnxPMDayMinRxInputPower_Object = MibTableColumn
jnxPMDayMinRxInputPower = _JnxPMDayMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 23),
    _JnxPMDayMinRxInputPower_Type()
)
jnxPMDayMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinRxInputPower.setUnits("0.01 dbm")
_JnxPMDayMaxRxInputPower_Type = Integer32
_JnxPMDayMaxRxInputPower_Object = MibTableColumn
jnxPMDayMaxRxInputPower = _JnxPMDayMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 24),
    _JnxPMDayMaxRxInputPower_Type()
)
jnxPMDayMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxInputPower.setUnits("0.01 dbm")
_JnxPMDayAvgRxInputPower_Type = Integer32
_JnxPMDayAvgRxInputPower_Object = MibTableColumn
jnxPMDayAvgRxInputPower = _JnxPMDayAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 25),
    _JnxPMDayAvgRxInputPower_Type()
)
jnxPMDayAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxInputPower.setUnits("0.01 dbm")
_JnxPMDayTimeStamp_Type = DateAndTime
_JnxPMDayTimeStamp_Object = MibTableColumn
jnxPMDayTimeStamp = _JnxPMDayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 26),
    _JnxPMDayTimeStamp_Type()
)
jnxPMDayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayTimeStamp.setStatus("current")
_JnxPMDaySuspectedFlag_Type = TruthValue
_JnxPMDaySuspectedFlag_Object = MibTableColumn
jnxPMDaySuspectedFlag = _JnxPMDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 27),
    _JnxPMDaySuspectedFlag_Type()
)
jnxPMDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDaySuspectedFlag.setStatus("current")
_JnxPMDaySuspectReason_Type = Integer32
_JnxPMDaySuspectReason_Object = MibTableColumn
jnxPMDaySuspectReason = _JnxPMDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 28),
    _JnxPMDaySuspectReason_Type()
)
jnxPMDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDaySuspectReason.setStatus("current")
_JnxPMDayMinTxLaserBiasCurrent_Type = Integer32
_JnxPMDayMinTxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMinTxLaserBiasCurrent = _JnxPMDayMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 29),
    _JnxPMDayMinTxLaserBiasCurrent_Type()
)
jnxPMDayMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayMaxTxLaserBiasCurrent_Type = Integer32
_JnxPMDayMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMaxTxLaserBiasCurrent = _JnxPMDayMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 30),
    _JnxPMDayMaxTxLaserBiasCurrent_Type()
)
jnxPMDayMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayAvgTxLaserBiasCurrent_Type = Integer32
_JnxPMDayAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayAvgTxLaserBiasCurrent = _JnxPMDayAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 31),
    _JnxPMDayAvgTxLaserBiasCurrent_Type()
)
jnxPMDayAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayMinTemperature_Type = Integer32
_JnxPMDayMinTemperature_Object = MibTableColumn
jnxPMDayMinTemperature = _JnxPMDayMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 32),
    _JnxPMDayMinTemperature_Type()
)
jnxPMDayMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinTemperature.setUnits(".1 Celcius")
_JnxPMDayMaxTemperature_Type = Integer32
_JnxPMDayMaxTemperature_Object = MibTableColumn
jnxPMDayMaxTemperature = _JnxPMDayMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 33),
    _JnxPMDayMaxTemperature_Type()
)
jnxPMDayMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxTemperature.setUnits(".1 Celcius")
_JnxPMDayAvgTemperature_Type = Integer32
_JnxPMDayAvgTemperature_Object = MibTableColumn
jnxPMDayAvgTemperature = _JnxPMDayAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 34),
    _JnxPMDayAvgTemperature_Type()
)
jnxPMDayAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgTemperature.setUnits(".1 Celcius")
_JnxPMDayMinCarFreqOffset_Type = Integer32
_JnxPMDayMinCarFreqOffset_Object = MibTableColumn
jnxPMDayMinCarFreqOffset = _JnxPMDayMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 35),
    _JnxPMDayMinCarFreqOffset_Type()
)
jnxPMDayMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinCarFreqOffset.setUnits("Mhz")
_JnxPMDayMaxCarFreqOffset_Type = Integer32
_JnxPMDayMaxCarFreqOffset_Object = MibTableColumn
jnxPMDayMaxCarFreqOffset = _JnxPMDayMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 36),
    _JnxPMDayMaxCarFreqOffset_Type()
)
jnxPMDayMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxCarFreqOffset.setUnits("MHz")
_JnxPMDayAvgCarFreqOffset_Type = Integer32
_JnxPMDayAvgCarFreqOffset_Object = MibTableColumn
jnxPMDayAvgCarFreqOffset = _JnxPMDayAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 37),
    _JnxPMDayAvgCarFreqOffset_Type()
)
jnxPMDayAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgCarFreqOffset.setUnits("MHz")
_JnxPMDayMinRxLaserBiasCurrent_Type = Integer32
_JnxPMDayMinRxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMinRxLaserBiasCurrent = _JnxPMDayMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 38),
    _JnxPMDayMinRxLaserBiasCurrent_Type()
)
jnxPMDayMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayMaxRxLaserBiasCurrent_Type = Integer32
_JnxPMDayMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayMaxRxLaserBiasCurrent = _JnxPMDayMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 39),
    _JnxPMDayMaxRxLaserBiasCurrent_Type()
)
jnxPMDayMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayAvgRxLaserBiasCurrent_Type = Integer32
_JnxPMDayAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxPMDayAvgRxLaserBiasCurrent = _JnxPMDayAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 40),
    _JnxPMDayAvgRxLaserBiasCurrent_Type()
)
jnxPMDayAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxPMDayMinTecCurrent_Type = Integer32
_JnxPMDayMinTecCurrent_Object = MibTableColumn
jnxPMDayMinTecCurrent = _JnxPMDayMinTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 41),
    _JnxPMDayMinTecCurrent_Type()
)
jnxPMDayMinTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinTecCurrent.setUnits(".1 mA")
_JnxPMDayMaxTecCurrent_Type = Integer32
_JnxPMDayMaxTecCurrent_Object = MibTableColumn
jnxPMDayMaxTecCurrent = _JnxPMDayMaxTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 42),
    _JnxPMDayMaxTecCurrent_Type()
)
jnxPMDayMaxTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxTecCurrent.setUnits(".1 mA")
_JnxPMDayAvgTecCurrent_Type = Integer32
_JnxPMDayAvgTecCurrent_Object = MibTableColumn
jnxPMDayAvgTecCurrent = _JnxPMDayAvgTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 43),
    _JnxPMDayAvgTecCurrent_Type()
)
jnxPMDayAvgTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgTecCurrent.setUnits(".1 mA")
_JnxPMDayMinResidualDispersion_Type = Integer32
_JnxPMDayMinResidualDispersion_Object = MibTableColumn
jnxPMDayMinResidualDispersion = _JnxPMDayMinResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 44),
    _JnxPMDayMinResidualDispersion_Type()
)
jnxPMDayMinResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinResidualDispersion.setUnits("ps/nm")
_JnxPMDayMaxResidualDispersion_Type = Integer32
_JnxPMDayMaxResidualDispersion_Object = MibTableColumn
jnxPMDayMaxResidualDispersion = _JnxPMDayMaxResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 45),
    _JnxPMDayMaxResidualDispersion_Type()
)
jnxPMDayMaxResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxResidualDispersion.setUnits("ps/nm")
_JnxPMDayAvgResidualDispersion_Type = Integer32
_JnxPMDayAvgResidualDispersion_Object = MibTableColumn
jnxPMDayAvgResidualDispersion = _JnxPMDayAvgResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 46),
    _JnxPMDayAvgResidualDispersion_Type()
)
jnxPMDayAvgResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgResidualDispersion.setUnits("ps/nm")
_JnxPMDayMinLevelHistogram_Type = Integer32
_JnxPMDayMinLevelHistogram_Object = MibTableColumn
jnxPMDayMinLevelHistogram = _JnxPMDayMinLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 47),
    _JnxPMDayMinLevelHistogram_Type()
)
jnxPMDayMinLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinLevelHistogram.setStatus("current")
_JnxPMDayMaxLevelHistogram_Type = Integer32
_JnxPMDayMaxLevelHistogram_Object = MibTableColumn
jnxPMDayMaxLevelHistogram = _JnxPMDayMaxLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 48),
    _JnxPMDayMaxLevelHistogram_Type()
)
jnxPMDayMaxLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxLevelHistogram.setStatus("current")
_JnxPMDayAvgLevelHistogram_Type = Integer32
_JnxPMDayAvgLevelHistogram_Object = MibTableColumn
jnxPMDayAvgLevelHistogram = _JnxPMDayAvgLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 49),
    _JnxPMDayAvgLevelHistogram_Type()
)
jnxPMDayAvgLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgLevelHistogram.setStatus("current")
_JnxPMDayMinLaserFrequencyError_Type = Integer32
_JnxPMDayMinLaserFrequencyError_Object = MibTableColumn
jnxPMDayMinLaserFrequencyError = _JnxPMDayMinLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 50),
    _JnxPMDayMinLaserFrequencyError_Type()
)
jnxPMDayMinLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMinLaserFrequencyError.setUnits(".1 Celcius")
_JnxPMDayMaxLaserFrequencyError_Type = Integer32
_JnxPMDayMaxLaserFrequencyError_Object = MibTableColumn
jnxPMDayMaxLaserFrequencyError = _JnxPMDayMaxLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 51),
    _JnxPMDayMaxLaserFrequencyError_Type()
)
jnxPMDayMaxLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayMaxLaserFrequencyError.setUnits(".1 Celcius")
_JnxPMDayAvgLaserFrequencyError_Type = Integer32
_JnxPMDayAvgLaserFrequencyError_Object = MibTableColumn
jnxPMDayAvgLaserFrequencyError = _JnxPMDayAvgLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 52),
    _JnxPMDayAvgLaserFrequencyError_Type()
)
jnxPMDayAvgLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxPMDayAvgLaserFrequencyError.setUnits(".1 Celcius")
_JnxPMDayMinFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMDayMinFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMDayMinFECCorrectedErrorsMantissa = _JnxPMDayMinFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 53),
    _JnxPMDayMinFECCorrectedErrorsMantissa_Type()
)
jnxPMDayMinFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMDayMinFECCorrectedErrorsExponent_Type = Integer32
_JnxPMDayMinFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMDayMinFECCorrectedErrorsExponent = _JnxPMDayMinFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 54),
    _JnxPMDayMinFECCorrectedErrorsExponent_Type()
)
jnxPMDayMinFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinFECCorrectedErrorsExponent.setStatus("current")
_JnxPMDayMaxFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMDayMaxFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMDayMaxFECCorrectedErrorsMantissa = _JnxPMDayMaxFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 55),
    _JnxPMDayMaxFECCorrectedErrorsMantissa_Type()
)
jnxPMDayMaxFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMDayMaxFECCorrectedErrorsExponent_Type = Integer32
_JnxPMDayMaxFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMDayMaxFECCorrectedErrorsExponent = _JnxPMDayMaxFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 56),
    _JnxPMDayMaxFECCorrectedErrorsExponent_Type()
)
jnxPMDayMaxFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxFECCorrectedErrorsExponent.setStatus("current")
_JnxPMDayAvgFECCorrectedErrorsMantissa_Type = Integer32
_JnxPMDayAvgFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxPMDayAvgFECCorrectedErrorsMantissa = _JnxPMDayAvgFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 57),
    _JnxPMDayAvgFECCorrectedErrorsMantissa_Type()
)
jnxPMDayAvgFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgFECCorrectedErrorsMantissa.setStatus("current")
_JnxPMDayAvgFECCorrectedErrorsExponent_Type = Integer32
_JnxPMDayAvgFECCorrectedErrorsExponent_Object = MibTableColumn
jnxPMDayAvgFECCorrectedErrorsExponent = _JnxPMDayAvgFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 58),
    _JnxPMDayAvgFECCorrectedErrorsExponent_Type()
)
jnxPMDayAvgFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgFECCorrectedErrorsExponent.setStatus("current")
_JnxPMDayMinFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMDayMinFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMDayMinFECUCorrectedWordsMantissa = _JnxPMDayMinFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 59),
    _JnxPMDayMinFECUCorrectedWordsMantissa_Type()
)
jnxPMDayMinFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMDayMinFECUCorrectedWordsExponent_Type = Integer32
_JnxPMDayMinFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMDayMinFECUCorrectedWordsExponent = _JnxPMDayMinFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 60),
    _JnxPMDayMinFECUCorrectedWordsExponent_Type()
)
jnxPMDayMinFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMinFECUCorrectedWordsExponent.setStatus("current")
_JnxPMDayMaxFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMDayMaxFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMDayMaxFECUCorrectedWordsMantissa = _JnxPMDayMaxFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 61),
    _JnxPMDayMaxFECUCorrectedWordsMantissa_Type()
)
jnxPMDayMaxFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMDayMaxFECUCorrectedWordsExponent_Type = Integer32
_JnxPMDayMaxFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMDayMaxFECUCorrectedWordsExponent = _JnxPMDayMaxFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 62),
    _JnxPMDayMaxFECUCorrectedWordsExponent_Type()
)
jnxPMDayMaxFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayMaxFECUCorrectedWordsExponent.setStatus("current")
_JnxPMDayAvgFECUCorrectedWordsMantissa_Type = Integer32
_JnxPMDayAvgFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxPMDayAvgFECUCorrectedWordsMantissa = _JnxPMDayAvgFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 63),
    _JnxPMDayAvgFECUCorrectedWordsMantissa_Type()
)
jnxPMDayAvgFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgFECUCorrectedWordsMantissa.setStatus("current")
_JnxPMDayAvgFECUCorrectedWordsExponent_Type = Integer32
_JnxPMDayAvgFECUCorrectedWordsExponent_Object = MibTableColumn
jnxPMDayAvgFECUCorrectedWordsExponent = _JnxPMDayAvgFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 3, 1, 64),
    _JnxPMDayAvgFECUCorrectedWordsExponent_Type()
)
jnxPMDayAvgFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPMDayAvgFECUCorrectedWordsExponent.setStatus("current")
_JnxOpticsOTIfPMFECCurrentTable_Object = MibTable
jnxOpticsOTIfPMFECCurrentTable = _JnxOpticsOTIfPMFECCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentTable.setStatus("current")
_JnxOpticsOTIfPMFECCurrentEntry_Object = MibTableRow
jnxOpticsOTIfPMFECCurrentEntry = _JnxOpticsOTIfPMFECCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1)
)
jnxOpticsOTIfPMFECCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentEntry.setStatus("current")
_JnxOpticsOTIfPMFECCurrentSuspectedFlag_Type = TruthValue
_JnxOpticsOTIfPMFECCurrentSuspectedFlag_Object = MibTableColumn
jnxOpticsOTIfPMFECCurrentSuspectedFlag = _JnxOpticsOTIfPMFECCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 1),
    _JnxOpticsOTIfPMFECCurrentSuspectedFlag_Type()
)
jnxOpticsOTIfPMFECCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentSuspectedFlag.setStatus("current")
_JnxOpticsOTIfPMCurrentFECCorrectedErr_Type = Counter64
_JnxOpticsOTIfPMCurrentFECCorrectedErr_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECCorrectedErr = _JnxOpticsOTIfPMCurrentFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 2),
    _JnxOpticsOTIfPMCurrentFECCorrectedErr_Type()
)
jnxOpticsOTIfPMCurrentFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECCorrectedErr.setStatus("current")
_JnxOpticsOTIfPMCurrentFECUncorrectedWords_Type = Counter64
_JnxOpticsOTIfPMCurrentFECUncorrectedWords_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECUncorrectedWords = _JnxOpticsOTIfPMCurrentFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 3),
    _JnxOpticsOTIfPMCurrentFECUncorrectedWords_Type()
)
jnxOpticsOTIfPMCurrentFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECUncorrectedWords.setStatus("current")
_JnxOpticsOTIfPMCurrentFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECBERMantissa = _JnxOpticsOTIfPMCurrentFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 4),
    _JnxOpticsOTIfPMCurrentFECBERMantissa_Type()
)
jnxOpticsOTIfPMCurrentFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMCurrentFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECBERExponent = _JnxOpticsOTIfPMCurrentFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 5),
    _JnxOpticsOTIfPMCurrentFECBERExponent_Type()
)
jnxOpticsOTIfPMCurrentFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMCurrentFECMinBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECMinBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECMinBERMantissa = _JnxOpticsOTIfPMCurrentFECMinBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 6),
    _JnxOpticsOTIfPMCurrentFECMinBERMantissa_Type()
)
jnxOpticsOTIfPMCurrentFECMinBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECMinBERMantissa.setStatus("current")
_JnxOpticsOTIfPMCurrentFECMinBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECMinBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECMinBERExponent = _JnxOpticsOTIfPMCurrentFECMinBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 7),
    _JnxOpticsOTIfPMCurrentFECMinBERExponent_Type()
)
jnxOpticsOTIfPMCurrentFECMinBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECMinBERExponent.setStatus("current")
_JnxOpticsOTIfPMCurrentFECMaxBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECMaxBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECMaxBERMantissa = _JnxOpticsOTIfPMCurrentFECMaxBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 8),
    _JnxOpticsOTIfPMCurrentFECMaxBERMantissa_Type()
)
jnxOpticsOTIfPMCurrentFECMaxBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECMaxBERMantissa.setStatus("current")
_JnxOpticsOTIfPMCurrentFECMaxBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECMaxBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECMaxBERExponent = _JnxOpticsOTIfPMCurrentFECMaxBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 9),
    _JnxOpticsOTIfPMCurrentFECMaxBERExponent_Type()
)
jnxOpticsOTIfPMCurrentFECMaxBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECMaxBERExponent.setStatus("current")
_JnxOpticsOTIfPMCurrentFECAvgBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECAvgBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECAvgBERMantissa = _JnxOpticsOTIfPMCurrentFECAvgBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 10),
    _JnxOpticsOTIfPMCurrentFECAvgBERMantissa_Type()
)
jnxOpticsOTIfPMCurrentFECAvgBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECAvgBERMantissa.setStatus("current")
_JnxOpticsOTIfPMCurrentFECAvgBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECAvgBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECAvgBERExponent = _JnxOpticsOTIfPMCurrentFECAvgBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 11),
    _JnxOpticsOTIfPMCurrentFECAvgBERExponent_Type()
)
jnxOpticsOTIfPMCurrentFECAvgBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECAvgBERExponent.setStatus("current")
_JnxOpticsOTIfPMCurrentFECElapsedTime_Type = Unsigned32
_JnxOpticsOTIfPMCurrentFECElapsedTime_Object = MibTableColumn
jnxOpticsOTIfPMCurrentFECElapsedTime = _JnxOpticsOTIfPMCurrentFECElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 12),
    _JnxOpticsOTIfPMCurrentFECElapsedTime_Type()
)
jnxOpticsOTIfPMCurrentFECElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentFECElapsedTime.setUnits("seconds")
_JnxOpticsOTIfPMFECCurSuspectReason_Type = Integer32
_JnxOpticsOTIfPMFECCurSuspectReason_Object = MibTableColumn
jnxOpticsOTIfPMFECCurSuspectReason = _JnxOpticsOTIfPMFECCurSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 4, 1, 13),
    _JnxOpticsOTIfPMFECCurSuspectReason_Type()
)
jnxOpticsOTIfPMFECCurSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurSuspectReason.setStatus("current")
_JnxOpticsOTIfPMFECIntervalTable_Object = MibTable
jnxOpticsOTIfPMFECIntervalTable = _JnxOpticsOTIfPMFECIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5)
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECIntervalTable.setStatus("current")
_JnxOpticsOTIfPMFECIntervalEntry_Object = MibTableRow
jnxOpticsOTIfPMFECIntervalEntry = _JnxOpticsOTIfPMFECIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1)
)
jnxOpticsOTIfPMFECIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOTIfPMFECIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECIntervalEntry.setStatus("current")
_JnxOpticsOTIfPMFECIntervalNumber_Type = Unsigned32
_JnxOpticsOTIfPMFECIntervalNumber_Object = MibTableColumn
jnxOpticsOTIfPMFECIntervalNumber = _JnxOpticsOTIfPMFECIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 1),
    _JnxOpticsOTIfPMFECIntervalNumber_Type()
)
jnxOpticsOTIfPMFECIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECIntervalNumber.setStatus("current")
_JnxOpticsOTIfPMFECIntervalSuspectedFlag_Type = TruthValue
_JnxOpticsOTIfPMFECIntervalSuspectedFlag_Object = MibTableColumn
jnxOpticsOTIfPMFECIntervalSuspectedFlag = _JnxOpticsOTIfPMFECIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 2),
    _JnxOpticsOTIfPMFECIntervalSuspectedFlag_Type()
)
jnxOpticsOTIfPMFECIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECIntervalSuspectedFlag.setStatus("current")
_JnxOpticsOTIfPMIntervalFECCorrectedErr_Type = Counter64
_JnxOpticsOTIfPMIntervalFECCorrectedErr_Object = MibTableColumn
jnxOpticsOTIfPMIntervalFECCorrectedErr = _JnxOpticsOTIfPMIntervalFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 3),
    _JnxOpticsOTIfPMIntervalFECCorrectedErr_Type()
)
jnxOpticsOTIfPMIntervalFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalFECCorrectedErr.setStatus("current")
_JnxOpticsOTIfPMIntervalFECUncorrectedWords_Type = Counter64
_JnxOpticsOTIfPMIntervalFECUncorrectedWords_Object = MibTableColumn
jnxOpticsOTIfPMIntervalFECUncorrectedWords = _JnxOpticsOTIfPMIntervalFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 4),
    _JnxOpticsOTIfPMIntervalFECUncorrectedWords_Type()
)
jnxOpticsOTIfPMIntervalFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalFECUncorrectedWords.setStatus("current")
_JnxOpticsOTIfPMIntervalMinFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMIntervalMinFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMIntervalMinFECBERMantissa = _JnxOpticsOTIfPMIntervalMinFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 5),
    _JnxOpticsOTIfPMIntervalMinFECBERMantissa_Type()
)
jnxOpticsOTIfPMIntervalMinFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalMinFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMIntervalMinFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMIntervalMinFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMIntervalMinFECBERExponent = _JnxOpticsOTIfPMIntervalMinFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 6),
    _JnxOpticsOTIfPMIntervalMinFECBERExponent_Type()
)
jnxOpticsOTIfPMIntervalMinFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalMinFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMIntervalMaxFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMIntervalMaxFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMIntervalMaxFECBERMantissa = _JnxOpticsOTIfPMIntervalMaxFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 7),
    _JnxOpticsOTIfPMIntervalMaxFECBERMantissa_Type()
)
jnxOpticsOTIfPMIntervalMaxFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalMaxFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMIntervalMaxFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMIntervalMaxFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMIntervalMaxFECBERExponent = _JnxOpticsOTIfPMIntervalMaxFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 8),
    _JnxOpticsOTIfPMIntervalMaxFECBERExponent_Type()
)
jnxOpticsOTIfPMIntervalMaxFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalMaxFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMIntervalAvgFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMIntervalAvgFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMIntervalAvgFECBERMantissa = _JnxOpticsOTIfPMIntervalAvgFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 9),
    _JnxOpticsOTIfPMIntervalAvgFECBERMantissa_Type()
)
jnxOpticsOTIfPMIntervalAvgFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalAvgFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMIntervalAvgFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMIntervalAvgFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMIntervalAvgFECBERExponent = _JnxOpticsOTIfPMIntervalAvgFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 10),
    _JnxOpticsOTIfPMIntervalAvgFECBERExponent_Type()
)
jnxOpticsOTIfPMIntervalAvgFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMIntervalAvgFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMFECIntervalTimeStamp_Type = DateAndTime
_JnxOpticsOTIfPMFECIntervalTimeStamp_Object = MibTableColumn
jnxOpticsOTIfPMFECIntervalTimeStamp = _JnxOpticsOTIfPMFECIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 11),
    _JnxOpticsOTIfPMFECIntervalTimeStamp_Type()
)
jnxOpticsOTIfPMFECIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECIntervalTimeStamp.setStatus("current")
_JnxOpticsOTIfPMFECIntSuspectReason_Type = Integer32
_JnxOpticsOTIfPMFECIntSuspectReason_Object = MibTableColumn
jnxOpticsOTIfPMFECIntSuspectReason = _JnxOpticsOTIfPMFECIntSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 5, 1, 12),
    _JnxOpticsOTIfPMFECIntSuspectReason_Type()
)
jnxOpticsOTIfPMFECIntSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECIntSuspectReason.setStatus("current")
_JnxOpticsOTIfPMFECCurrentDayTable_Object = MibTable
jnxOpticsOTIfPMFECCurrentDayTable = _JnxOpticsOTIfPMFECCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6)
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentDayTable.setStatus("current")
_JnxOpticsOTIfPMFECCurrentDayEntry_Object = MibTableRow
jnxOpticsOTIfPMFECCurrentDayEntry = _JnxOpticsOTIfPMFECCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1)
)
jnxOpticsOTIfPMFECCurrentDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentDayEntry.setStatus("current")
_JnxOpticsOTIfPMFECCurrentDaySuspectedFlag_Type = TruthValue
_JnxOpticsOTIfPMFECCurrentDaySuspectedFlag_Object = MibTableColumn
jnxOpticsOTIfPMFECCurrentDaySuspectedFlag = _JnxOpticsOTIfPMFECCurrentDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 1),
    _JnxOpticsOTIfPMFECCurrentDaySuspectedFlag_Type()
)
jnxOpticsOTIfPMFECCurrentDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentDaySuspectedFlag.setStatus("current")
_JnxOpticsOTIfPMCurrentDayFECCorrectedErr_Type = Counter64
_JnxOpticsOTIfPMCurrentDayFECCorrectedErr_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayFECCorrectedErr = _JnxOpticsOTIfPMCurrentDayFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 2),
    _JnxOpticsOTIfPMCurrentDayFECCorrectedErr_Type()
)
jnxOpticsOTIfPMCurrentDayFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayFECCorrectedErr.setStatus("current")
_JnxOpticsOTIfPMCurrentDayFECUncorrectedWords_Type = Counter64
_JnxOpticsOTIfPMCurrentDayFECUncorrectedWords_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayFECUncorrectedWords = _JnxOpticsOTIfPMCurrentDayFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 3),
    _JnxOpticsOTIfPMCurrentDayFECUncorrectedWords_Type()
)
jnxOpticsOTIfPMCurrentDayFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayFECUncorrectedWords.setStatus("current")
_JnxOpticsOTIfPMCurrentDayMinFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMCurrentDayMinFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayMinFECBERMantissa = _JnxOpticsOTIfPMCurrentDayMinFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 4),
    _JnxOpticsOTIfPMCurrentDayMinFECBERMantissa_Type()
)
jnxOpticsOTIfPMCurrentDayMinFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayMinFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMCurrentDayMinFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMCurrentDayMinFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayMinFECBERExponent = _JnxOpticsOTIfPMCurrentDayMinFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 5),
    _JnxOpticsOTIfPMCurrentDayMinFECBERExponent_Type()
)
jnxOpticsOTIfPMCurrentDayMinFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayMinFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMCurrentDayMaxFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMCurrentDayMaxFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayMaxFECBERMantissa = _JnxOpticsOTIfPMCurrentDayMaxFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 6),
    _JnxOpticsOTIfPMCurrentDayMaxFECBERMantissa_Type()
)
jnxOpticsOTIfPMCurrentDayMaxFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayMaxFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMCurrentDayMaxFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMCurrentDayMaxFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayMaxFECBERExponent = _JnxOpticsOTIfPMCurrentDayMaxFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 7),
    _JnxOpticsOTIfPMCurrentDayMaxFECBERExponent_Type()
)
jnxOpticsOTIfPMCurrentDayMaxFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayMaxFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMCurrentDayAvgFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMCurrentDayAvgFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayAvgFECBERMantissa = _JnxOpticsOTIfPMCurrentDayAvgFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 8),
    _JnxOpticsOTIfPMCurrentDayAvgFECBERMantissa_Type()
)
jnxOpticsOTIfPMCurrentDayAvgFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayAvgFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMCurrentDayAvgFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMCurrentDayAvgFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMCurrentDayAvgFECBERExponent = _JnxOpticsOTIfPMCurrentDayAvgFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 9),
    _JnxOpticsOTIfPMCurrentDayAvgFECBERExponent_Type()
)
jnxOpticsOTIfPMCurrentDayAvgFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMCurrentDayAvgFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMFECCurrentDayElapsedTime_Type = Unsigned32
_JnxOpticsOTIfPMFECCurrentDayElapsedTime_Object = MibTableColumn
jnxOpticsOTIfPMFECCurrentDayElapsedTime = _JnxOpticsOTIfPMFECCurrentDayElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 10),
    _JnxOpticsOTIfPMFECCurrentDayElapsedTime_Type()
)
jnxOpticsOTIfPMFECCurrentDayElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentDayElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurrentDayElapsedTime.setUnits("seconds")
_JnxOpticsOTIfPMFECCurDaySuspectReason_Type = Integer32
_JnxOpticsOTIfPMFECCurDaySuspectReason_Object = MibTableColumn
jnxOpticsOTIfPMFECCurDaySuspectReason = _JnxOpticsOTIfPMFECCurDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 6, 1, 11),
    _JnxOpticsOTIfPMFECCurDaySuspectReason_Type()
)
jnxOpticsOTIfPMFECCurDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECCurDaySuspectReason.setStatus("current")
_JnxOpticsOTIfPMFECPrevDayTable_Object = MibTable
jnxOpticsOTIfPMFECPrevDayTable = _JnxOpticsOTIfPMFECPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7)
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECPrevDayTable.setStatus("current")
_JnxOpticsOTIfPMFECPrevDayEntry_Object = MibTableRow
jnxOpticsOTIfPMFECPrevDayEntry = _JnxOpticsOTIfPMFECPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1)
)
jnxOpticsOTIfPMFECPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECPrevDayEntry.setStatus("current")
_JnxOpticsOTIfPMFECPrevDaySuspectedFlag_Type = TruthValue
_JnxOpticsOTIfPMFECPrevDaySuspectedFlag_Object = MibTableColumn
jnxOpticsOTIfPMFECPrevDaySuspectedFlag = _JnxOpticsOTIfPMFECPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 1),
    _JnxOpticsOTIfPMFECPrevDaySuspectedFlag_Type()
)
jnxOpticsOTIfPMFECPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECPrevDaySuspectedFlag.setStatus("current")
_JnxOpticsOTIfPMPrevDayFECCorrectedErr_Type = Counter64
_JnxOpticsOTIfPMPrevDayFECCorrectedErr_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayFECCorrectedErr = _JnxOpticsOTIfPMPrevDayFECCorrectedErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 2),
    _JnxOpticsOTIfPMPrevDayFECCorrectedErr_Type()
)
jnxOpticsOTIfPMPrevDayFECCorrectedErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayFECCorrectedErr.setStatus("current")
_JnxOpticsOTIfPMPrevDayFECUncorrectedWords_Type = Counter64
_JnxOpticsOTIfPMPrevDayFECUncorrectedWords_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayFECUncorrectedWords = _JnxOpticsOTIfPMPrevDayFECUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 3),
    _JnxOpticsOTIfPMPrevDayFECUncorrectedWords_Type()
)
jnxOpticsOTIfPMPrevDayFECUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayFECUncorrectedWords.setStatus("current")
_JnxOpticsOTIfPMPrevDayMinFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMPrevDayMinFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayMinFECBERMantissa = _JnxOpticsOTIfPMPrevDayMinFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 4),
    _JnxOpticsOTIfPMPrevDayMinFECBERMantissa_Type()
)
jnxOpticsOTIfPMPrevDayMinFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayMinFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMPrevDayMinFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMPrevDayMinFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayMinFECBERExponent = _JnxOpticsOTIfPMPrevDayMinFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 5),
    _JnxOpticsOTIfPMPrevDayMinFECBERExponent_Type()
)
jnxOpticsOTIfPMPrevDayMinFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayMinFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMPrevDayMaxFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMPrevDayMaxFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayMaxFECBERMantissa = _JnxOpticsOTIfPMPrevDayMaxFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 6),
    _JnxOpticsOTIfPMPrevDayMaxFECBERMantissa_Type()
)
jnxOpticsOTIfPMPrevDayMaxFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayMaxFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMPrevDayMaxFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMPrevDayMaxFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayMaxFECBERExponent = _JnxOpticsOTIfPMPrevDayMaxFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 7),
    _JnxOpticsOTIfPMPrevDayMaxFECBERExponent_Type()
)
jnxOpticsOTIfPMPrevDayMaxFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayMaxFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMPrevDayAvgFECBERMantissa_Type = Unsigned32
_JnxOpticsOTIfPMPrevDayAvgFECBERMantissa_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayAvgFECBERMantissa = _JnxOpticsOTIfPMPrevDayAvgFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 8),
    _JnxOpticsOTIfPMPrevDayAvgFECBERMantissa_Type()
)
jnxOpticsOTIfPMPrevDayAvgFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayAvgFECBERMantissa.setStatus("current")
_JnxOpticsOTIfPMPrevDayAvgFECBERExponent_Type = Unsigned32
_JnxOpticsOTIfPMPrevDayAvgFECBERExponent_Object = MibTableColumn
jnxOpticsOTIfPMPrevDayAvgFECBERExponent = _JnxOpticsOTIfPMPrevDayAvgFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 9),
    _JnxOpticsOTIfPMPrevDayAvgFECBERExponent_Type()
)
jnxOpticsOTIfPMPrevDayAvgFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMPrevDayAvgFECBERExponent.setStatus("current")
_JnxOpticsOTIfPMFECPrevDayTimeStamp_Type = DateAndTime
_JnxOpticsOTIfPMFECPrevDayTimeStamp_Object = MibTableColumn
jnxOpticsOTIfPMFECPrevDayTimeStamp = _JnxOpticsOTIfPMFECPrevDayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 10),
    _JnxOpticsOTIfPMFECPrevDayTimeStamp_Type()
)
jnxOpticsOTIfPMFECPrevDayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECPrevDayTimeStamp.setStatus("current")
_JnxOpticsOTIfPMFECPrevDaySuspectReason_Type = Integer32
_JnxOpticsOTIfPMFECPrevDaySuspectReason_Object = MibTableColumn
jnxOpticsOTIfPMFECPrevDaySuspectReason = _JnxOpticsOTIfPMFECPrevDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 7, 1, 11),
    _JnxOpticsOTIfPMFECPrevDaySuspectReason_Type()
)
jnxOpticsOTIfPMFECPrevDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECPrevDaySuspectReason.setStatus("current")
_JnxOpticsOTIfPMFECConfigTable_Object = MibTable
jnxOpticsOTIfPMFECConfigTable = _JnxOpticsOTIfPMFECConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8)
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECConfigTable.setStatus("current")
_JnxOpticsOTIfPMFECConfigEntry_Object = MibTableRow
jnxOpticsOTIfPMFECConfigEntry = _JnxOpticsOTIfPMFECConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8, 1)
)
jnxOpticsOTIfPMFECConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECConfigEntry.setStatus("current")
_JnxOpticsOTIfPMFECValidIntervals_Type = Unsigned32
_JnxOpticsOTIfPMFECValidIntervals_Object = MibTableColumn
jnxOpticsOTIfPMFECValidIntervals = _JnxOpticsOTIfPMFECValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8, 1, 1),
    _JnxOpticsOTIfPMFECValidIntervals_Type()
)
jnxOpticsOTIfPMFECValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECValidIntervals.setStatus("current")
_JnxOpticsOTIfPM15MinPreFECBERMantissaThreshold_Type = Unsigned32
_JnxOpticsOTIfPM15MinPreFECBERMantissaThreshold_Object = MibTableColumn
jnxOpticsOTIfPM15MinPreFECBERMantissaThreshold = _JnxOpticsOTIfPM15MinPreFECBERMantissaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8, 1, 2),
    _JnxOpticsOTIfPM15MinPreFECBERMantissaThreshold_Type()
)
jnxOpticsOTIfPM15MinPreFECBERMantissaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPM15MinPreFECBERMantissaThreshold.setStatus("current")
_JnxOpticsOTIfPM15MinPreFECBERExponentThreshold_Type = Unsigned32
_JnxOpticsOTIfPM15MinPreFECBERExponentThreshold_Object = MibTableColumn
jnxOpticsOTIfPM15MinPreFECBERExponentThreshold = _JnxOpticsOTIfPM15MinPreFECBERExponentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8, 1, 3),
    _JnxOpticsOTIfPM15MinPreFECBERExponentThreshold_Type()
)
jnxOpticsOTIfPM15MinPreFECBERExponentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPM15MinPreFECBERExponentThreshold.setStatus("current")
_JnxOpticsOTIfPM24HourPreFECBERMantissaThreshold_Type = Unsigned32
_JnxOpticsOTIfPM24HourPreFECBERMantissaThreshold_Object = MibTableColumn
jnxOpticsOTIfPM24HourPreFECBERMantissaThreshold = _JnxOpticsOTIfPM24HourPreFECBERMantissaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8, 1, 4),
    _JnxOpticsOTIfPM24HourPreFECBERMantissaThreshold_Type()
)
jnxOpticsOTIfPM24HourPreFECBERMantissaThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPM24HourPreFECBERMantissaThreshold.setStatus("current")
_JnxOpticsOTIfPM24HourPreFECBERExponentThreshold_Type = Unsigned32
_JnxOpticsOTIfPM24HourPreFECBERExponentThreshold_Object = MibTableColumn
jnxOpticsOTIfPM24HourPreFECBERExponentThreshold = _JnxOpticsOTIfPM24HourPreFECBERExponentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8, 1, 5),
    _JnxOpticsOTIfPM24HourPreFECBERExponentThreshold_Type()
)
jnxOpticsOTIfPM24HourPreFECBERExponentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPM24HourPreFECBERExponentThreshold.setStatus("current")
_JnxOpticsOTIfPMFECBEREnableTCA_Type = TruthValue
_JnxOpticsOTIfPMFECBEREnableTCA_Object = MibTableColumn
jnxOpticsOTIfPMFECBEREnableTCA = _JnxOpticsOTIfPMFECBEREnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 8, 1, 6),
    _JnxOpticsOTIfPMFECBEREnableTCA_Type()
)
jnxOpticsOTIfPMFECBEREnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOTIfPMFECBEREnableTCA.setStatus("current")
_JnxIfOpticsPMCurrentTable_Object = MibTable
jnxIfOpticsPMCurrentTable = _JnxIfOpticsPMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9)
)
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurrentTable.setStatus("current")
_JnxIfOpticsPMCurrentEntry_Object = MibTableRow
jnxIfOpticsPMCurrentEntry = _JnxIfOpticsPMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1)
)
jnxIfOpticsPMCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIfOpticsPMCurrentLaneIndex"),
)
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurrentEntry.setStatus("current")


class _JnxIfOpticsPMCurrentLaneIndex_Type(Unsigned32):
    """Custom type jnxIfOpticsPMCurrentLaneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxIfOpticsPMCurrentLaneIndex_Type.__name__ = "Unsigned32"
_JnxIfOpticsPMCurrentLaneIndex_Object = MibTableColumn
jnxIfOpticsPMCurrentLaneIndex = _JnxIfOpticsPMCurrentLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 1),
    _JnxIfOpticsPMCurrentLaneIndex_Type()
)
jnxIfOpticsPMCurrentLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurrentLaneIndex.setStatus("current")
_JnxIfOpticsPMCurChromaticDispersion_Type = Integer32
_JnxIfOpticsPMCurChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMCurChromaticDispersion = _JnxIfOpticsPMCurChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 2),
    _JnxIfOpticsPMCurChromaticDispersion_Type()
)
jnxIfOpticsPMCurChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMCurDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMCurDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMCurDiffGroupDelay = _JnxIfOpticsPMCurDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 3),
    _JnxIfOpticsPMCurDiffGroupDelay_Type()
)
jnxIfOpticsPMCurDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMCurPolarizationState_Type = Integer32
_JnxIfOpticsPMCurPolarizationState_Object = MibTableColumn
jnxIfOpticsPMCurPolarizationState = _JnxIfOpticsPMCurPolarizationState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 4),
    _JnxIfOpticsPMCurPolarizationState_Type()
)
jnxIfOpticsPMCurPolarizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurPolarizationState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurPolarizationState.setUnits("rad/s")
_JnxIfOpticsPMCurPolarDepLoss_Type = Integer32
_JnxIfOpticsPMCurPolarDepLoss_Object = MibTableColumn
jnxIfOpticsPMCurPolarDepLoss = _JnxIfOpticsPMCurPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 5),
    _JnxIfOpticsPMCurPolarDepLoss_Type()
)
jnxIfOpticsPMCurPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurPolarDepLoss.setUnits("0.1 dB")
_JnxIfOpticsPMCurQ_Type = Integer32
_JnxIfOpticsPMCurQ_Object = MibTableColumn
jnxIfOpticsPMCurQ = _JnxIfOpticsPMCurQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 6),
    _JnxIfOpticsPMCurQ_Type()
)
jnxIfOpticsPMCurQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurQ.setUnits("0.1 dB")
_JnxIfOpticsPMCurSNR_Type = Integer32
_JnxIfOpticsPMCurSNR_Object = MibTableColumn
jnxIfOpticsPMCurSNR = _JnxIfOpticsPMCurSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 7),
    _JnxIfOpticsPMCurSNR_Type()
)
jnxIfOpticsPMCurSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurSNR.setUnits("0.1 dB")
_JnxIfOpticsPMCurTxOutputPower_Type = Integer32
_JnxIfOpticsPMCurTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMCurTxOutputPower = _JnxIfOpticsPMCurTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 8),
    _JnxIfOpticsPMCurTxOutputPower_Type()
)
jnxIfOpticsPMCurTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurRxInputPower_Type = Integer32
_JnxIfOpticsPMCurRxInputPower_Object = MibTableColumn
jnxIfOpticsPMCurRxInputPower = _JnxIfOpticsPMCurRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 9),
    _JnxIfOpticsPMCurRxInputPower_Type()
)
jnxIfOpticsPMCurRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurMinChromaticDispersion_Type = Integer32
_JnxIfOpticsPMCurMinChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMCurMinChromaticDispersion = _JnxIfOpticsPMCurMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 10),
    _JnxIfOpticsPMCurMinChromaticDispersion_Type()
)
jnxIfOpticsPMCurMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMCurMaxChromaticDispersion_Type = Integer32
_JnxIfOpticsPMCurMaxChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMCurMaxChromaticDispersion = _JnxIfOpticsPMCurMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 11),
    _JnxIfOpticsPMCurMaxChromaticDispersion_Type()
)
jnxIfOpticsPMCurMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMCurAvgChromaticDispersion_Type = Integer32
_JnxIfOpticsPMCurAvgChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMCurAvgChromaticDispersion = _JnxIfOpticsPMCurAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 12),
    _JnxIfOpticsPMCurAvgChromaticDispersion_Type()
)
jnxIfOpticsPMCurAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMCurMinDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMCurMinDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMCurMinDiffGroupDelay = _JnxIfOpticsPMCurMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 13),
    _JnxIfOpticsPMCurMinDiffGroupDelay_Type()
)
jnxIfOpticsPMCurMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMCurMaxDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMCurMaxDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMCurMaxDiffGroupDelay = _JnxIfOpticsPMCurMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 14),
    _JnxIfOpticsPMCurMaxDiffGroupDelay_Type()
)
jnxIfOpticsPMCurMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMCurAvgDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMCurAvgDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMCurAvgDiffGroupDelay = _JnxIfOpticsPMCurAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 15),
    _JnxIfOpticsPMCurAvgDiffGroupDelay_Type()
)
jnxIfOpticsPMCurAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMCurMinPolarState_Type = Integer32
_JnxIfOpticsPMCurMinPolarState_Object = MibTableColumn
jnxIfOpticsPMCurMinPolarState = _JnxIfOpticsPMCurMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 16),
    _JnxIfOpticsPMCurMinPolarState_Type()
)
jnxIfOpticsPMCurMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinPolarState.setUnits("rad/s")
_JnxIfOpticsPMCurMaxPolarState_Type = Integer32
_JnxIfOpticsPMCurMaxPolarState_Object = MibTableColumn
jnxIfOpticsPMCurMaxPolarState = _JnxIfOpticsPMCurMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 17),
    _JnxIfOpticsPMCurMaxPolarState_Type()
)
jnxIfOpticsPMCurMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxPolarState.setUnits("rad/s")
_JnxIfOpticsPMCurAvgPolarState_Type = Integer32
_JnxIfOpticsPMCurAvgPolarState_Object = MibTableColumn
jnxIfOpticsPMCurAvgPolarState = _JnxIfOpticsPMCurAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 18),
    _JnxIfOpticsPMCurAvgPolarState_Type()
)
jnxIfOpticsPMCurAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgPolarState.setUnits("rad/s")
_JnxIfOpticsPMCurMinPolarDepLoss_Type = Integer32
_JnxIfOpticsPMCurMinPolarDepLoss_Object = MibTableColumn
jnxIfOpticsPMCurMinPolarDepLoss = _JnxIfOpticsPMCurMinPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 19),
    _JnxIfOpticsPMCurMinPolarDepLoss_Type()
)
jnxIfOpticsPMCurMinPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinPolarDepLoss.setUnits("0.1 dB")
_JnxIfOpticsPMCurMaxPolarDepLoss_Type = Integer32
_JnxIfOpticsPMCurMaxPolarDepLoss_Object = MibTableColumn
jnxIfOpticsPMCurMaxPolarDepLoss = _JnxIfOpticsPMCurMaxPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 20),
    _JnxIfOpticsPMCurMaxPolarDepLoss_Type()
)
jnxIfOpticsPMCurMaxPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxPolarDepLoss.setUnits("0.1 dB")
_JnxIfOpticsPMCurAvgPolarDepLoss_Type = Integer32
_JnxIfOpticsPMCurAvgPolarDepLoss_Object = MibTableColumn
jnxIfOpticsPMCurAvgPolarDepLoss = _JnxIfOpticsPMCurAvgPolarDepLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 21),
    _JnxIfOpticsPMCurAvgPolarDepLoss_Type()
)
jnxIfOpticsPMCurAvgPolarDepLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgPolarDepLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgPolarDepLoss.setUnits("0.1 dB")
_JnxIfOpticsPMCurMinQ_Type = Integer32
_JnxIfOpticsPMCurMinQ_Object = MibTableColumn
jnxIfOpticsPMCurMinQ = _JnxIfOpticsPMCurMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 22),
    _JnxIfOpticsPMCurMinQ_Type()
)
jnxIfOpticsPMCurMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinQ.setUnits("0.1 dB")
_JnxIfOpticsPMCurMaxQ_Type = Integer32
_JnxIfOpticsPMCurMaxQ_Object = MibTableColumn
jnxIfOpticsPMCurMaxQ = _JnxIfOpticsPMCurMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 23),
    _JnxIfOpticsPMCurMaxQ_Type()
)
jnxIfOpticsPMCurMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxQ.setUnits("0.1 dB")
_JnxIfOpticsPMCurAvgQ_Type = Integer32
_JnxIfOpticsPMCurAvgQ_Object = MibTableColumn
jnxIfOpticsPMCurAvgQ = _JnxIfOpticsPMCurAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 24),
    _JnxIfOpticsPMCurAvgQ_Type()
)
jnxIfOpticsPMCurAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgQ.setUnits("0.1 dB")
_JnxIfOpticsPMCurMinSNR_Type = Integer32
_JnxIfOpticsPMCurMinSNR_Object = MibTableColumn
jnxIfOpticsPMCurMinSNR = _JnxIfOpticsPMCurMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 25),
    _JnxIfOpticsPMCurMinSNR_Type()
)
jnxIfOpticsPMCurMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinSNR.setUnits("0.1 dB")
_JnxIfOpticsPMCurMaxSNR_Type = Integer32
_JnxIfOpticsPMCurMaxSNR_Object = MibTableColumn
jnxIfOpticsPMCurMaxSNR = _JnxIfOpticsPMCurMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 26),
    _JnxIfOpticsPMCurMaxSNR_Type()
)
jnxIfOpticsPMCurMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxSNR.setUnits("0.1 dB")
_JnxIfOpticsPMCurAvgSNR_Type = Integer32
_JnxIfOpticsPMCurAvgSNR_Object = MibTableColumn
jnxIfOpticsPMCurAvgSNR = _JnxIfOpticsPMCurAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 27),
    _JnxIfOpticsPMCurAvgSNR_Type()
)
jnxIfOpticsPMCurAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgSNR.setUnits("0.1 dB")
_JnxIfOpticsPMCurMinTxOutputPower_Type = Integer32
_JnxIfOpticsPMCurMinTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMCurMinTxOutputPower = _JnxIfOpticsPMCurMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 28),
    _JnxIfOpticsPMCurMinTxOutputPower_Type()
)
jnxIfOpticsPMCurMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurMaxTxOutputPower_Type = Integer32
_JnxIfOpticsPMCurMaxTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMCurMaxTxOutputPower = _JnxIfOpticsPMCurMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 29),
    _JnxIfOpticsPMCurMaxTxOutputPower_Type()
)
jnxIfOpticsPMCurMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurAvgTxOutputPower_Type = Integer32
_JnxIfOpticsPMCurAvgTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMCurAvgTxOutputPower = _JnxIfOpticsPMCurAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 30),
    _JnxIfOpticsPMCurAvgTxOutputPower_Type()
)
jnxIfOpticsPMCurAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurMinRxInputPower_Type = Integer32
_JnxIfOpticsPMCurMinRxInputPower_Object = MibTableColumn
jnxIfOpticsPMCurMinRxInputPower = _JnxIfOpticsPMCurMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 31),
    _JnxIfOpticsPMCurMinRxInputPower_Type()
)
jnxIfOpticsPMCurMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurMaxRxInputPower_Type = Integer32
_JnxIfOpticsPMCurMaxRxInputPower_Object = MibTableColumn
jnxIfOpticsPMCurMaxRxInputPower = _JnxIfOpticsPMCurMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 32),
    _JnxIfOpticsPMCurMaxRxInputPower_Type()
)
jnxIfOpticsPMCurMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurAvgRxInputPower_Type = Integer32
_JnxIfOpticsPMCurAvgRxInputPower_Object = MibTableColumn
jnxIfOpticsPMCurAvgRxInputPower = _JnxIfOpticsPMCurAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 33),
    _JnxIfOpticsPMCurAvgRxInputPower_Type()
)
jnxIfOpticsPMCurAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMCurSuspectedFlag_Type = TruthValue
_JnxIfOpticsPMCurSuspectedFlag_Object = MibTableColumn
jnxIfOpticsPMCurSuspectedFlag = _JnxIfOpticsPMCurSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 34),
    _JnxIfOpticsPMCurSuspectedFlag_Type()
)
jnxIfOpticsPMCurSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurSuspectedFlag.setStatus("current")
_JnxIfOpticsPMCurSuspectReason_Type = Integer32
_JnxIfOpticsPMCurSuspectReason_Object = MibTableColumn
jnxIfOpticsPMCurSuspectReason = _JnxIfOpticsPMCurSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 35),
    _JnxIfOpticsPMCurSuspectReason_Type()
)
jnxIfOpticsPMCurSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurSuspectReason.setStatus("current")
_JnxIfOpticsPMCurTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurTxLaserBiasCurrent = _JnxIfOpticsPMCurTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 36),
    _JnxIfOpticsPMCurTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurMinTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurMinTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurMinTxLaserBiasCurrent = _JnxIfOpticsPMCurMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 37),
    _JnxIfOpticsPMCurMinTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurMaxTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurMaxTxLaserBiasCurrent = _JnxIfOpticsPMCurMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 38),
    _JnxIfOpticsPMCurMaxTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurAvgTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurAvgTxLaserBiasCurrent = _JnxIfOpticsPMCurAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 39),
    _JnxIfOpticsPMCurAvgTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurTemperature_Type = Integer32
_JnxIfOpticsPMCurTemperature_Object = MibTableColumn
jnxIfOpticsPMCurTemperature = _JnxIfOpticsPMCurTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 40),
    _JnxIfOpticsPMCurTemperature_Type()
)
jnxIfOpticsPMCurTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTemperature.setUnits("Celcius")
_JnxIfOpticsPMCurMinTemperature_Type = Integer32
_JnxIfOpticsPMCurMinTemperature_Object = MibTableColumn
jnxIfOpticsPMCurMinTemperature = _JnxIfOpticsPMCurMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 41),
    _JnxIfOpticsPMCurMinTemperature_Type()
)
jnxIfOpticsPMCurMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTemperature.setUnits("Celcius")
_JnxIfOpticsPMCurMaxTemperature_Type = Integer32
_JnxIfOpticsPMCurMaxTemperature_Object = MibTableColumn
jnxIfOpticsPMCurMaxTemperature = _JnxIfOpticsPMCurMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 42),
    _JnxIfOpticsPMCurMaxTemperature_Type()
)
jnxIfOpticsPMCurMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTemperature.setUnits("Celcius")
_JnxIfOpticsPMCurAvgTemperature_Type = Integer32
_JnxIfOpticsPMCurAvgTemperature_Object = MibTableColumn
jnxIfOpticsPMCurAvgTemperature = _JnxIfOpticsPMCurAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 43),
    _JnxIfOpticsPMCurAvgTemperature_Type()
)
jnxIfOpticsPMCurAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTemperature.setUnits("Celcius")
_JnxIfOpticsPMCurCarFreqOffset_Type = Integer32
_JnxIfOpticsPMCurCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMCurCarFreqOffset = _JnxIfOpticsPMCurCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 44),
    _JnxIfOpticsPMCurCarFreqOffset_Type()
)
jnxIfOpticsPMCurCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMCurMinCarFreqOffset_Type = Integer32
_JnxIfOpticsPMCurMinCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMCurMinCarFreqOffset = _JnxIfOpticsPMCurMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 45),
    _JnxIfOpticsPMCurMinCarFreqOffset_Type()
)
jnxIfOpticsPMCurMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMCurMaxCarFreqOffset_Type = Integer32
_JnxIfOpticsPMCurMaxCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMCurMaxCarFreqOffset = _JnxIfOpticsPMCurMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 46),
    _JnxIfOpticsPMCurMaxCarFreqOffset_Type()
)
jnxIfOpticsPMCurMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMCurAvgCarFreqOffset_Type = Integer32
_JnxIfOpticsPMCurAvgCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMCurAvgCarFreqOffset = _JnxIfOpticsPMCurAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 47),
    _JnxIfOpticsPMCurAvgCarFreqOffset_Type()
)
jnxIfOpticsPMCurAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMCurRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurRxLaserBiasCurrent = _JnxIfOpticsPMCurRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 48),
    _JnxIfOpticsPMCurRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurMinRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurMinRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurMinRxLaserBiasCurrent = _JnxIfOpticsPMCurMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 49),
    _JnxIfOpticsPMCurMinRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurMaxRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurMaxRxLaserBiasCurrent = _JnxIfOpticsPMCurMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 50),
    _JnxIfOpticsPMCurMaxRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurAvgRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMCurAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMCurAvgRxLaserBiasCurrent = _JnxIfOpticsPMCurAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 51),
    _JnxIfOpticsPMCurAvgRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMCurAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurTecCurrent_Type = Integer32
_JnxIfOpticsPMCurTecCurrent_Object = MibTableColumn
jnxIfOpticsPMCurTecCurrent = _JnxIfOpticsPMCurTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 52),
    _JnxIfOpticsPMCurTecCurrent_Type()
)
jnxIfOpticsPMCurTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurMinTecCurrent_Type = Integer32
_JnxIfOpticsPMCurMinTecCurrent_Object = MibTableColumn
jnxIfOpticsPMCurMinTecCurrent = _JnxIfOpticsPMCurMinTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 53),
    _JnxIfOpticsPMCurMinTecCurrent_Type()
)
jnxIfOpticsPMCurMinTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurMaxTecCurrent_Type = Integer32
_JnxIfOpticsPMCurMaxTecCurrent_Object = MibTableColumn
jnxIfOpticsPMCurMaxTecCurrent = _JnxIfOpticsPMCurMaxTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 54),
    _JnxIfOpticsPMCurMaxTecCurrent_Type()
)
jnxIfOpticsPMCurMaxTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurAvgTecCurrent_Type = Integer32
_JnxIfOpticsPMCurAvgTecCurrent_Object = MibTableColumn
jnxIfOpticsPMCurAvgTecCurrent = _JnxIfOpticsPMCurAvgTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 55),
    _JnxIfOpticsPMCurAvgTecCurrent_Type()
)
jnxIfOpticsPMCurAvgTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMCurResidualDispersion_Type = Integer32
_JnxIfOpticsPMCurResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMCurResidualDispersion = _JnxIfOpticsPMCurResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 56),
    _JnxIfOpticsPMCurResidualDispersion_Type()
)
jnxIfOpticsPMCurResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMCurMinResidualDispersion_Type = Integer32
_JnxIfOpticsPMCurMinResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMCurMinResidualDispersion = _JnxIfOpticsPMCurMinResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 57),
    _JnxIfOpticsPMCurMinResidualDispersion_Type()
)
jnxIfOpticsPMCurMinResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMCurMaxResidualDispersion_Type = Integer32
_JnxIfOpticsPMCurMaxResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMCurMaxResidualDispersion = _JnxIfOpticsPMCurMaxResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 58),
    _JnxIfOpticsPMCurMaxResidualDispersion_Type()
)
jnxIfOpticsPMCurMaxResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMCurAvgResidualDispersion_Type = Integer32
_JnxIfOpticsPMCurAvgResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMCurAvgResidualDispersion = _JnxIfOpticsPMCurAvgResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 59),
    _JnxIfOpticsPMCurAvgResidualDispersion_Type()
)
jnxIfOpticsPMCurAvgResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMCurLevelHistogram_Type = Integer32
_JnxIfOpticsPMCurLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMCurLevelHistogram = _JnxIfOpticsPMCurLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 60),
    _JnxIfOpticsPMCurLevelHistogram_Type()
)
jnxIfOpticsPMCurLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurLevelHistogram.setStatus("current")
_JnxIfOpticsPMCurMinLevelHistogram_Type = Integer32
_JnxIfOpticsPMCurMinLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMCurMinLevelHistogram = _JnxIfOpticsPMCurMinLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 61),
    _JnxIfOpticsPMCurMinLevelHistogram_Type()
)
jnxIfOpticsPMCurMinLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinLevelHistogram.setStatus("current")
_JnxIfOpticsPMCurMaxLevelHistogram_Type = Integer32
_JnxIfOpticsPMCurMaxLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMCurMaxLevelHistogram = _JnxIfOpticsPMCurMaxLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 62),
    _JnxIfOpticsPMCurMaxLevelHistogram_Type()
)
jnxIfOpticsPMCurMaxLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxLevelHistogram.setStatus("current")
_JnxIfOpticsPMCurAvgLevelHistogram_Type = Integer32
_JnxIfOpticsPMCurAvgLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMCurAvgLevelHistogram = _JnxIfOpticsPMCurAvgLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 63),
    _JnxIfOpticsPMCurAvgLevelHistogram_Type()
)
jnxIfOpticsPMCurAvgLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgLevelHistogram.setStatus("current")
_JnxIfOpticsPMCurLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMCurLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMCurLaserFrequencyError = _JnxIfOpticsPMCurLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 64),
    _JnxIfOpticsPMCurLaserFrequencyError_Type()
)
jnxIfOpticsPMCurLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMCurMinLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMCurMinLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMCurMinLaserFrequencyError = _JnxIfOpticsPMCurMinLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 65),
    _JnxIfOpticsPMCurMinLaserFrequencyError_Type()
)
jnxIfOpticsPMCurMinLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMCurMaxLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMCurMaxLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMCurMaxLaserFrequencyError = _JnxIfOpticsPMCurMaxLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 66),
    _JnxIfOpticsPMCurMaxLaserFrequencyError_Type()
)
jnxIfOpticsPMCurMaxLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMCurAvgLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMCurAvgLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMCurAvgLaserFrequencyError = _JnxIfOpticsPMCurAvgLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 67),
    _JnxIfOpticsPMCurAvgLaserFrequencyError_Type()
)
jnxIfOpticsPMCurAvgLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMCurFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMCurFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurFECCorrectedErrorsMantissa = _JnxIfOpticsPMCurFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 68),
    _JnxIfOpticsPMCurFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMCurFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMCurFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMCurFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMCurFECCorrectedErrorsExponent = _JnxIfOpticsPMCurFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 69),
    _JnxIfOpticsPMCurFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMCurFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMCurMinFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMCurMinFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurMinFECCorrectedErrorsMantissa = _JnxIfOpticsPMCurMinFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 70),
    _JnxIfOpticsPMCurMinFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMCurMinFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMCurMinFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMCurMinFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMCurMinFECCorrectedErrorsExponent = _JnxIfOpticsPMCurMinFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 71),
    _JnxIfOpticsPMCurMinFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMCurMinFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa = _JnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 72),
    _JnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMCurMaxFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMCurMaxFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMCurMaxFECCorrectedErrorsExponent = _JnxIfOpticsPMCurMaxFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 73),
    _JnxIfOpticsPMCurMaxFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMCurMaxFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa = _JnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 74),
    _JnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMCurAvgFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMCurAvgFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMCurAvgFECCorrectedErrorsExponent = _JnxIfOpticsPMCurAvgFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 75),
    _JnxIfOpticsPMCurAvgFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMCurAvgFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMCurFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMCurFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurFECUCorrectedWordsMantissa = _JnxIfOpticsPMCurFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 76),
    _JnxIfOpticsPMCurFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMCurFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMCurFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMCurFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMCurFECUCorrectedWordsExponent = _JnxIfOpticsPMCurFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 77),
    _JnxIfOpticsPMCurFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMCurFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMCurMinFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMCurMinFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurMinFECUCorrectedWordsMantissa = _JnxIfOpticsPMCurMinFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 78),
    _JnxIfOpticsPMCurMinFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMCurMinFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMCurMinFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMCurMinFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMCurMinFECUCorrectedWordsExponent = _JnxIfOpticsPMCurMinFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 79),
    _JnxIfOpticsPMCurMinFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMCurMinFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMinFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa = _JnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 80),
    _JnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMCurMaxFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMCurMaxFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMCurMaxFECUCorrectedWordsExponent = _JnxIfOpticsPMCurMaxFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 81),
    _JnxIfOpticsPMCurMaxFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMCurMaxFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurMaxFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa = _JnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 82),
    _JnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMCurAvgFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMCurAvgFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMCurAvgFECUCorrectedWordsExponent = _JnxIfOpticsPMCurAvgFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 9, 1, 83),
    _JnxIfOpticsPMCurAvgFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMCurAvgFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMCurAvgFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMIntervalTable_Object = MibTable
jnxIfOpticsPMIntervalTable = _JnxIfOpticsPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10)
)
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntervalTable.setStatus("current")
_JnxIfOpticsPMIntervalEntry_Object = MibTableRow
jnxIfOpticsPMIntervalEntry = _JnxIfOpticsPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1)
)
jnxIfOpticsPMIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIfOpticsPMIntervalLaneIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIfOpticsPMIntervalNumber"),
)
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntervalEntry.setStatus("current")


class _JnxIfOpticsPMIntervalLaneIndex_Type(Unsigned32):
    """Custom type jnxIfOpticsPMIntervalLaneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxIfOpticsPMIntervalLaneIndex_Type.__name__ = "Unsigned32"
_JnxIfOpticsPMIntervalLaneIndex_Object = MibTableColumn
jnxIfOpticsPMIntervalLaneIndex = _JnxIfOpticsPMIntervalLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 1),
    _JnxIfOpticsPMIntervalLaneIndex_Type()
)
jnxIfOpticsPMIntervalLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntervalLaneIndex.setStatus("current")


class _JnxIfOpticsPMIntervalNumber_Type(Unsigned32):
    """Custom type jnxIfOpticsPMIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxIfOpticsPMIntervalNumber_Type.__name__ = "Unsigned32"
_JnxIfOpticsPMIntervalNumber_Object = MibTableColumn
jnxIfOpticsPMIntervalNumber = _JnxIfOpticsPMIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 2),
    _JnxIfOpticsPMIntervalNumber_Type()
)
jnxIfOpticsPMIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntervalNumber.setStatus("current")
_JnxIfOpticsPMIntMinChromaticDispersion_Type = Integer32
_JnxIfOpticsPMIntMinChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMIntMinChromaticDispersion = _JnxIfOpticsPMIntMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 3),
    _JnxIfOpticsPMIntMinChromaticDispersion_Type()
)
jnxIfOpticsPMIntMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMIntMaxChromaticDispersion_Type = Integer32
_JnxIfOpticsPMIntMaxChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMIntMaxChromaticDispersion = _JnxIfOpticsPMIntMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 4),
    _JnxIfOpticsPMIntMaxChromaticDispersion_Type()
)
jnxIfOpticsPMIntMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMIntAvgChromaticDispersion_Type = Integer32
_JnxIfOpticsPMIntAvgChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMIntAvgChromaticDispersion = _JnxIfOpticsPMIntAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 5),
    _JnxIfOpticsPMIntAvgChromaticDispersion_Type()
)
jnxIfOpticsPMIntAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMIntMinDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMIntMinDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMIntMinDiffGroupDelay = _JnxIfOpticsPMIntMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 6),
    _JnxIfOpticsPMIntMinDiffGroupDelay_Type()
)
jnxIfOpticsPMIntMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMIntMaxDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMIntMaxDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMIntMaxDiffGroupDelay = _JnxIfOpticsPMIntMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 7),
    _JnxIfOpticsPMIntMaxDiffGroupDelay_Type()
)
jnxIfOpticsPMIntMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMIntAvgDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMIntAvgDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMIntAvgDiffGroupDelay = _JnxIfOpticsPMIntAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 8),
    _JnxIfOpticsPMIntAvgDiffGroupDelay_Type()
)
jnxIfOpticsPMIntAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMIntMinPolarState_Type = Integer32
_JnxIfOpticsPMIntMinPolarState_Object = MibTableColumn
jnxIfOpticsPMIntMinPolarState = _JnxIfOpticsPMIntMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 9),
    _JnxIfOpticsPMIntMinPolarState_Type()
)
jnxIfOpticsPMIntMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinPolarState.setUnits("rad/s")
_JnxIfOpticsPMIntMaxPolarState_Type = Integer32
_JnxIfOpticsPMIntMaxPolarState_Object = MibTableColumn
jnxIfOpticsPMIntMaxPolarState = _JnxIfOpticsPMIntMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 10),
    _JnxIfOpticsPMIntMaxPolarState_Type()
)
jnxIfOpticsPMIntMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxPolarState.setUnits("rad/s")
_JnxIfOpticsPMIntAvgPolarState_Type = Integer32
_JnxIfOpticsPMIntAvgPolarState_Object = MibTableColumn
jnxIfOpticsPMIntAvgPolarState = _JnxIfOpticsPMIntAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 11),
    _JnxIfOpticsPMIntAvgPolarState_Type()
)
jnxIfOpticsPMIntAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgPolarState.setUnits("rad/s")
_JnxIfOpticsPMIntMinPolarDependentLoss_Type = Integer32
_JnxIfOpticsPMIntMinPolarDependentLoss_Object = MibTableColumn
jnxIfOpticsPMIntMinPolarDependentLoss = _JnxIfOpticsPMIntMinPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 12),
    _JnxIfOpticsPMIntMinPolarDependentLoss_Type()
)
jnxIfOpticsPMIntMinPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinPolarDependentLoss.setUnits("0.1 dB")
_JnxIfOpticsPMIntMaxPolarDependentLoss_Type = Integer32
_JnxIfOpticsPMIntMaxPolarDependentLoss_Object = MibTableColumn
jnxIfOpticsPMIntMaxPolarDependentLoss = _JnxIfOpticsPMIntMaxPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 13),
    _JnxIfOpticsPMIntMaxPolarDependentLoss_Type()
)
jnxIfOpticsPMIntMaxPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxPolarDependentLoss.setUnits("0.1 dB")
_JnxIfOpticsPMIntAvgPolarDependentLoss_Type = Integer32
_JnxIfOpticsPMIntAvgPolarDependentLoss_Object = MibTableColumn
jnxIfOpticsPMIntAvgPolarDependentLoss = _JnxIfOpticsPMIntAvgPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 14),
    _JnxIfOpticsPMIntAvgPolarDependentLoss_Type()
)
jnxIfOpticsPMIntAvgPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgPolarDependentLoss.setUnits("0.1 dB")
_JnxIfOpticsPMIntMinQ_Type = Integer32
_JnxIfOpticsPMIntMinQ_Object = MibTableColumn
jnxIfOpticsPMIntMinQ = _JnxIfOpticsPMIntMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 15),
    _JnxIfOpticsPMIntMinQ_Type()
)
jnxIfOpticsPMIntMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinQ.setUnits("0.1 dB")
_JnxIfOpticsPMIntMaxQ_Type = Integer32
_JnxIfOpticsPMIntMaxQ_Object = MibTableColumn
jnxIfOpticsPMIntMaxQ = _JnxIfOpticsPMIntMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 16),
    _JnxIfOpticsPMIntMaxQ_Type()
)
jnxIfOpticsPMIntMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxQ.setUnits("0.1 dB")
_JnxIfOpticsPMIntAvgQ_Type = Integer32
_JnxIfOpticsPMIntAvgQ_Object = MibTableColumn
jnxIfOpticsPMIntAvgQ = _JnxIfOpticsPMIntAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 17),
    _JnxIfOpticsPMIntAvgQ_Type()
)
jnxIfOpticsPMIntAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgQ.setUnits("0.1 dB")
_JnxIfOpticsPMIntMinSNR_Type = Integer32
_JnxIfOpticsPMIntMinSNR_Object = MibTableColumn
jnxIfOpticsPMIntMinSNR = _JnxIfOpticsPMIntMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 18),
    _JnxIfOpticsPMIntMinSNR_Type()
)
jnxIfOpticsPMIntMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinSNR.setUnits("0.1 dB")
_JnxIfOpticsPMIntMaxSNR_Type = Integer32
_JnxIfOpticsPMIntMaxSNR_Object = MibTableColumn
jnxIfOpticsPMIntMaxSNR = _JnxIfOpticsPMIntMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 19),
    _JnxIfOpticsPMIntMaxSNR_Type()
)
jnxIfOpticsPMIntMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxSNR.setUnits("0.1 dB")
_JnxIfOpticsPMIntAvgSNR_Type = Integer32
_JnxIfOpticsPMIntAvgSNR_Object = MibTableColumn
jnxIfOpticsPMIntAvgSNR = _JnxIfOpticsPMIntAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 20),
    _JnxIfOpticsPMIntAvgSNR_Type()
)
jnxIfOpticsPMIntAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgSNR.setUnits("0.1 dB")
_JnxIfOpticsPMIntMinTxOutputPower_Type = Integer32
_JnxIfOpticsPMIntMinTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMIntMinTxOutputPower = _JnxIfOpticsPMIntMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 21),
    _JnxIfOpticsPMIntMinTxOutputPower_Type()
)
jnxIfOpticsPMIntMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMIntMaxTxOutputPower_Type = Integer32
_JnxIfOpticsPMIntMaxTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMIntMaxTxOutputPower = _JnxIfOpticsPMIntMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 22),
    _JnxIfOpticsPMIntMaxTxOutputPower_Type()
)
jnxIfOpticsPMIntMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMIntAvgTxOutputPower_Type = Integer32
_JnxIfOpticsPMIntAvgTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMIntAvgTxOutputPower = _JnxIfOpticsPMIntAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 23),
    _JnxIfOpticsPMIntAvgTxOutputPower_Type()
)
jnxIfOpticsPMIntAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMIntMinRxInputPower_Type = Integer32
_JnxIfOpticsPMIntMinRxInputPower_Object = MibTableColumn
jnxIfOpticsPMIntMinRxInputPower = _JnxIfOpticsPMIntMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 24),
    _JnxIfOpticsPMIntMinRxInputPower_Type()
)
jnxIfOpticsPMIntMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMIntMaxRxInputPower_Type = Integer32
_JnxIfOpticsPMIntMaxRxInputPower_Object = MibTableColumn
jnxIfOpticsPMIntMaxRxInputPower = _JnxIfOpticsPMIntMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 25),
    _JnxIfOpticsPMIntMaxRxInputPower_Type()
)
jnxIfOpticsPMIntMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMIntAvgRxInputPower_Type = Integer32
_JnxIfOpticsPMIntAvgRxInputPower_Object = MibTableColumn
jnxIfOpticsPMIntAvgRxInputPower = _JnxIfOpticsPMIntAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 26),
    _JnxIfOpticsPMIntAvgRxInputPower_Type()
)
jnxIfOpticsPMIntAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMIntTimeStamp_Type = DateAndTime
_JnxIfOpticsPMIntTimeStamp_Object = MibTableColumn
jnxIfOpticsPMIntTimeStamp = _JnxIfOpticsPMIntTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 27),
    _JnxIfOpticsPMIntTimeStamp_Type()
)
jnxIfOpticsPMIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntTimeStamp.setStatus("current")
_JnxIfOpticsPMIntSuspectedFlag_Type = TruthValue
_JnxIfOpticsPMIntSuspectedFlag_Object = MibTableColumn
jnxIfOpticsPMIntSuspectedFlag = _JnxIfOpticsPMIntSuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 28),
    _JnxIfOpticsPMIntSuspectedFlag_Type()
)
jnxIfOpticsPMIntSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntSuspectedFlag.setStatus("current")
_JnxIfOpticsPMIntSuspectReason_Type = Integer32
_JnxIfOpticsPMIntSuspectReason_Object = MibTableColumn
jnxIfOpticsPMIntSuspectReason = _JnxIfOpticsPMIntSuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 29),
    _JnxIfOpticsPMIntSuspectReason_Type()
)
jnxIfOpticsPMIntSuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntSuspectReason.setStatus("current")
_JnxIfOpticsPMIntMinTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMIntMinTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMIntMinTxLaserBiasCurrent = _JnxIfOpticsPMIntMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 30),
    _JnxIfOpticsPMIntMinTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMIntMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntMaxTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMIntMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMIntMaxTxLaserBiasCurrent = _JnxIfOpticsPMIntMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 31),
    _JnxIfOpticsPMIntMaxTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMIntMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntAvgTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMIntAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMIntAvgTxLaserBiasCurrent = _JnxIfOpticsPMIntAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 32),
    _JnxIfOpticsPMIntAvgTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMIntAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntMinTemperature_Type = Integer32
_JnxIfOpticsPMIntMinTemperature_Object = MibTableColumn
jnxIfOpticsPMIntMinTemperature = _JnxIfOpticsPMIntMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 33),
    _JnxIfOpticsPMIntMinTemperature_Type()
)
jnxIfOpticsPMIntMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTemperature.setUnits("Celcius")
_JnxIfOpticsPMIntMaxTemperature_Type = Integer32
_JnxIfOpticsPMIntMaxTemperature_Object = MibTableColumn
jnxIfOpticsPMIntMaxTemperature = _JnxIfOpticsPMIntMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 34),
    _JnxIfOpticsPMIntMaxTemperature_Type()
)
jnxIfOpticsPMIntMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTemperature.setUnits("Celcius")
_JnxIfOpticsPMIntAvgTemperature_Type = Integer32
_JnxIfOpticsPMIntAvgTemperature_Object = MibTableColumn
jnxIfOpticsPMIntAvgTemperature = _JnxIfOpticsPMIntAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 35),
    _JnxIfOpticsPMIntAvgTemperature_Type()
)
jnxIfOpticsPMIntAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTemperature.setUnits("Celcius")
_JnxIfOpticsPMIntMinCarFreqOffset_Type = Integer32
_JnxIfOpticsPMIntMinCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMIntMinCarFreqOffset = _JnxIfOpticsPMIntMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 36),
    _JnxIfOpticsPMIntMinCarFreqOffset_Type()
)
jnxIfOpticsPMIntMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinCarFreqOffset.setUnits("Mhz")
_JnxIfOpticsPMIntMaxCarFreqOffset_Type = Integer32
_JnxIfOpticsPMIntMaxCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMIntMaxCarFreqOffset = _JnxIfOpticsPMIntMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 37),
    _JnxIfOpticsPMIntMaxCarFreqOffset_Type()
)
jnxIfOpticsPMIntMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMIntAvgCarFreqOffset_Type = Integer32
_JnxIfOpticsPMIntAvgCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMIntAvgCarFreqOffset = _JnxIfOpticsPMIntAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 38),
    _JnxIfOpticsPMIntAvgCarFreqOffset_Type()
)
jnxIfOpticsPMIntAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMIntMinRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMIntMinRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMIntMinRxLaserBiasCurrent = _JnxIfOpticsPMIntMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 39),
    _JnxIfOpticsPMIntMinRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMIntMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntMaxRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMIntMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMIntMaxRxLaserBiasCurrent = _JnxIfOpticsPMIntMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 40),
    _JnxIfOpticsPMIntMaxRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMIntMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntAvgRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMIntAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMIntAvgRxLaserBiasCurrent = _JnxIfOpticsPMIntAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 41),
    _JnxIfOpticsPMIntAvgRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMIntAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntMinTecCurrent_Type = Integer32
_JnxIfOpticsPMIntMinTecCurrent_Object = MibTableColumn
jnxIfOpticsPMIntMinTecCurrent = _JnxIfOpticsPMIntMinTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 42),
    _JnxIfOpticsPMIntMinTecCurrent_Type()
)
jnxIfOpticsPMIntMinTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntMaxTecCurrent_Type = Integer32
_JnxIfOpticsPMIntMaxTecCurrent_Object = MibTableColumn
jnxIfOpticsPMIntMaxTecCurrent = _JnxIfOpticsPMIntMaxTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 43),
    _JnxIfOpticsPMIntMaxTecCurrent_Type()
)
jnxIfOpticsPMIntMaxTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntAvgTecCurrent_Type = Integer32
_JnxIfOpticsPMIntAvgTecCurrent_Object = MibTableColumn
jnxIfOpticsPMIntAvgTecCurrent = _JnxIfOpticsPMIntAvgTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 44),
    _JnxIfOpticsPMIntAvgTecCurrent_Type()
)
jnxIfOpticsPMIntAvgTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMIntMinResidualDispersion_Type = Integer32
_JnxIfOpticsPMIntMinResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMIntMinResidualDispersion = _JnxIfOpticsPMIntMinResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 45),
    _JnxIfOpticsPMIntMinResidualDispersion_Type()
)
jnxIfOpticsPMIntMinResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMIntMaxResidualDispersion_Type = Integer32
_JnxIfOpticsPMIntMaxResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMIntMaxResidualDispersion = _JnxIfOpticsPMIntMaxResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 46),
    _JnxIfOpticsPMIntMaxResidualDispersion_Type()
)
jnxIfOpticsPMIntMaxResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMIntAvgResidualDispersion_Type = Integer32
_JnxIfOpticsPMIntAvgResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMIntAvgResidualDispersion = _JnxIfOpticsPMIntAvgResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 47),
    _JnxIfOpticsPMIntAvgResidualDispersion_Type()
)
jnxIfOpticsPMIntAvgResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMIntMinLevelHistogram_Type = Integer32
_JnxIfOpticsPMIntMinLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMIntMinLevelHistogram = _JnxIfOpticsPMIntMinLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 48),
    _JnxIfOpticsPMIntMinLevelHistogram_Type()
)
jnxIfOpticsPMIntMinLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinLevelHistogram.setStatus("current")
_JnxIfOpticsPMIntMaxLevelHistogram_Type = Integer32
_JnxIfOpticsPMIntMaxLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMIntMaxLevelHistogram = _JnxIfOpticsPMIntMaxLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 49),
    _JnxIfOpticsPMIntMaxLevelHistogram_Type()
)
jnxIfOpticsPMIntMaxLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxLevelHistogram.setStatus("current")
_JnxIfOpticsPMIntAvgLevelHistogram_Type = Integer32
_JnxIfOpticsPMIntAvgLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMIntAvgLevelHistogram = _JnxIfOpticsPMIntAvgLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 50),
    _JnxIfOpticsPMIntAvgLevelHistogram_Type()
)
jnxIfOpticsPMIntAvgLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgLevelHistogram.setStatus("current")
_JnxIfOpticsPMIntMinLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMIntMinLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMIntMinLaserFrequencyError = _JnxIfOpticsPMIntMinLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 51),
    _JnxIfOpticsPMIntMinLaserFrequencyError_Type()
)
jnxIfOpticsPMIntMinLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMIntMaxLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMIntMaxLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMIntMaxLaserFrequencyError = _JnxIfOpticsPMIntMaxLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 52),
    _JnxIfOpticsPMIntMaxLaserFrequencyError_Type()
)
jnxIfOpticsPMIntMaxLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMIntAvgLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMIntAvgLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMIntAvgLaserFrequencyError = _JnxIfOpticsPMIntAvgLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 53),
    _JnxIfOpticsPMIntAvgLaserFrequencyError_Type()
)
jnxIfOpticsPMIntAvgLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMIntMinFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMIntMinFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMIntMinFECCorrectedErrorsMantissa = _JnxIfOpticsPMIntMinFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 54),
    _JnxIfOpticsPMIntMinFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMIntMinFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMIntMinFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMIntMinFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMIntMinFECCorrectedErrorsExponent = _JnxIfOpticsPMIntMinFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 55),
    _JnxIfOpticsPMIntMinFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMIntMinFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa = _JnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 56),
    _JnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMIntMaxFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMIntMaxFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMIntMaxFECCorrectedErrorsExponent = _JnxIfOpticsPMIntMaxFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 57),
    _JnxIfOpticsPMIntMaxFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMIntMaxFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa = _JnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 58),
    _JnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMIntAvgFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMIntAvgFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMIntAvgFECCorrectedErrorsExponent = _JnxIfOpticsPMIntAvgFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 59),
    _JnxIfOpticsPMIntAvgFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMIntAvgFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMIntMinFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMIntMinFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMIntMinFECUCorrectedWordsMantissa = _JnxIfOpticsPMIntMinFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 60),
    _JnxIfOpticsPMIntMinFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMIntMinFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMIntMinFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMIntMinFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMIntMinFECUCorrectedWordsExponent = _JnxIfOpticsPMIntMinFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 61),
    _JnxIfOpticsPMIntMinFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMIntMinFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMinFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa = _JnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 62),
    _JnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMIntMaxFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMIntMaxFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMIntMaxFECUCorrectedWordsExponent = _JnxIfOpticsPMIntMaxFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 63),
    _JnxIfOpticsPMIntMaxFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMIntMaxFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntMaxFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa = _JnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 64),
    _JnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMIntAvgFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMIntAvgFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMIntAvgFECUCorrectedWordsExponent = _JnxIfOpticsPMIntAvgFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 10, 1, 65),
    _JnxIfOpticsPMIntAvgFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMIntAvgFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMIntAvgFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMDayTable_Object = MibTable
jnxIfOpticsPMDayTable = _JnxIfOpticsPMDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11)
)
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayTable.setStatus("current")
_JnxIfOpticsPMDayEntry_Object = MibTableRow
jnxIfOpticsPMDayEntry = _JnxIfOpticsPMDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1)
)
jnxIfOpticsPMDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIfOpticsPMDayLaneIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIfOpticsPMDayIndex"),
)
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayEntry.setStatus("current")


class _JnxIfOpticsPMDayLaneIndex_Type(Unsigned32):
    """Custom type jnxIfOpticsPMDayLaneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_JnxIfOpticsPMDayLaneIndex_Type.__name__ = "Unsigned32"
_JnxIfOpticsPMDayLaneIndex_Object = MibTableColumn
jnxIfOpticsPMDayLaneIndex = _JnxIfOpticsPMDayLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 1),
    _JnxIfOpticsPMDayLaneIndex_Type()
)
jnxIfOpticsPMDayLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayLaneIndex.setStatus("current")


class _JnxIfOpticsPMDayIndex_Type(Unsigned32):
    """Custom type jnxIfOpticsPMDayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_JnxIfOpticsPMDayIndex_Type.__name__ = "Unsigned32"
_JnxIfOpticsPMDayIndex_Object = MibTableColumn
jnxIfOpticsPMDayIndex = _JnxIfOpticsPMDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 2),
    _JnxIfOpticsPMDayIndex_Type()
)
jnxIfOpticsPMDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayIndex.setStatus("current")
_JnxIfOpticsPMDayMinChromaticDispersion_Type = Integer32
_JnxIfOpticsPMDayMinChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMDayMinChromaticDispersion = _JnxIfOpticsPMDayMinChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 3),
    _JnxIfOpticsPMDayMinChromaticDispersion_Type()
)
jnxIfOpticsPMDayMinChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMDayMaxChromaticDispersion_Type = Integer32
_JnxIfOpticsPMDayMaxChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMDayMaxChromaticDispersion = _JnxIfOpticsPMDayMaxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 4),
    _JnxIfOpticsPMDayMaxChromaticDispersion_Type()
)
jnxIfOpticsPMDayMaxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMDayAvgChromaticDispersion_Type = Integer32
_JnxIfOpticsPMDayAvgChromaticDispersion_Object = MibTableColumn
jnxIfOpticsPMDayAvgChromaticDispersion = _JnxIfOpticsPMDayAvgChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 5),
    _JnxIfOpticsPMDayAvgChromaticDispersion_Type()
)
jnxIfOpticsPMDayAvgChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgChromaticDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgChromaticDispersion.setUnits("ps/nm")
_JnxIfOpticsPMDayMinDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMDayMinDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMDayMinDiffGroupDelay = _JnxIfOpticsPMDayMinDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 6),
    _JnxIfOpticsPMDayMinDiffGroupDelay_Type()
)
jnxIfOpticsPMDayMinDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMDayMaxDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMDayMaxDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMDayMaxDiffGroupDelay = _JnxIfOpticsPMDayMaxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 7),
    _JnxIfOpticsPMDayMaxDiffGroupDelay_Type()
)
jnxIfOpticsPMDayMaxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMDayAvgDiffGroupDelay_Type = Integer32
_JnxIfOpticsPMDayAvgDiffGroupDelay_Object = MibTableColumn
jnxIfOpticsPMDayAvgDiffGroupDelay = _JnxIfOpticsPMDayAvgDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 8),
    _JnxIfOpticsPMDayAvgDiffGroupDelay_Type()
)
jnxIfOpticsPMDayAvgDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgDiffGroupDelay.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgDiffGroupDelay.setUnits("ps")
_JnxIfOpticsPMDayMinPolarState_Type = Integer32
_JnxIfOpticsPMDayMinPolarState_Object = MibTableColumn
jnxIfOpticsPMDayMinPolarState = _JnxIfOpticsPMDayMinPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 9),
    _JnxIfOpticsPMDayMinPolarState_Type()
)
jnxIfOpticsPMDayMinPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinPolarState.setUnits("rad/s")
_JnxIfOpticsPMDayMaxPolarState_Type = Integer32
_JnxIfOpticsPMDayMaxPolarState_Object = MibTableColumn
jnxIfOpticsPMDayMaxPolarState = _JnxIfOpticsPMDayMaxPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 10),
    _JnxIfOpticsPMDayMaxPolarState_Type()
)
jnxIfOpticsPMDayMaxPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxPolarState.setUnits("rad/s")
_JnxIfOpticsPMDayAvgPolarState_Type = Integer32
_JnxIfOpticsPMDayAvgPolarState_Object = MibTableColumn
jnxIfOpticsPMDayAvgPolarState = _JnxIfOpticsPMDayAvgPolarState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 11),
    _JnxIfOpticsPMDayAvgPolarState_Type()
)
jnxIfOpticsPMDayAvgPolarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgPolarState.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgPolarState.setUnits("rad/s")
_JnxIfOpticsPMDayMinPolarDependentLoss_Type = Integer32
_JnxIfOpticsPMDayMinPolarDependentLoss_Object = MibTableColumn
jnxIfOpticsPMDayMinPolarDependentLoss = _JnxIfOpticsPMDayMinPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 12),
    _JnxIfOpticsPMDayMinPolarDependentLoss_Type()
)
jnxIfOpticsPMDayMinPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinPolarDependentLoss.setUnits("0.1 dB")
_JnxIfOpticsPMDayMaxPolarDependentLoss_Type = Integer32
_JnxIfOpticsPMDayMaxPolarDependentLoss_Object = MibTableColumn
jnxIfOpticsPMDayMaxPolarDependentLoss = _JnxIfOpticsPMDayMaxPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 13),
    _JnxIfOpticsPMDayMaxPolarDependentLoss_Type()
)
jnxIfOpticsPMDayMaxPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxPolarDependentLoss.setUnits("0.1 dB")
_JnxIfOpticsPMDayAvgPolarDependentLoss_Type = Integer32
_JnxIfOpticsPMDayAvgPolarDependentLoss_Object = MibTableColumn
jnxIfOpticsPMDayAvgPolarDependentLoss = _JnxIfOpticsPMDayAvgPolarDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 14),
    _JnxIfOpticsPMDayAvgPolarDependentLoss_Type()
)
jnxIfOpticsPMDayAvgPolarDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgPolarDependentLoss.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgPolarDependentLoss.setUnits("0.1 dB")
_JnxIfOpticsPMDayMinQ_Type = Integer32
_JnxIfOpticsPMDayMinQ_Object = MibTableColumn
jnxIfOpticsPMDayMinQ = _JnxIfOpticsPMDayMinQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 15),
    _JnxIfOpticsPMDayMinQ_Type()
)
jnxIfOpticsPMDayMinQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinQ.setUnits("0.1 dB")
_JnxIfOpticsPMDayMaxQ_Type = Integer32
_JnxIfOpticsPMDayMaxQ_Object = MibTableColumn
jnxIfOpticsPMDayMaxQ = _JnxIfOpticsPMDayMaxQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 16),
    _JnxIfOpticsPMDayMaxQ_Type()
)
jnxIfOpticsPMDayMaxQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxQ.setUnits("0.1 dB")
_JnxIfOpticsPMDayAvgQ_Type = Integer32
_JnxIfOpticsPMDayAvgQ_Object = MibTableColumn
jnxIfOpticsPMDayAvgQ = _JnxIfOpticsPMDayAvgQ_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 17),
    _JnxIfOpticsPMDayAvgQ_Type()
)
jnxIfOpticsPMDayAvgQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgQ.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgQ.setUnits("0.1 dB")
_JnxIfOpticsPMDayMinSNR_Type = Integer32
_JnxIfOpticsPMDayMinSNR_Object = MibTableColumn
jnxIfOpticsPMDayMinSNR = _JnxIfOpticsPMDayMinSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 18),
    _JnxIfOpticsPMDayMinSNR_Type()
)
jnxIfOpticsPMDayMinSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinSNR.setUnits("0.1 dB")
_JnxIfOpticsPMDayMaxSNR_Type = Integer32
_JnxIfOpticsPMDayMaxSNR_Object = MibTableColumn
jnxIfOpticsPMDayMaxSNR = _JnxIfOpticsPMDayMaxSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 19),
    _JnxIfOpticsPMDayMaxSNR_Type()
)
jnxIfOpticsPMDayMaxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxSNR.setUnits("0.1 dB")
_JnxIfOpticsPMDayAvgSNR_Type = Integer32
_JnxIfOpticsPMDayAvgSNR_Object = MibTableColumn
jnxIfOpticsPMDayAvgSNR = _JnxIfOpticsPMDayAvgSNR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 20),
    _JnxIfOpticsPMDayAvgSNR_Type()
)
jnxIfOpticsPMDayAvgSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgSNR.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgSNR.setUnits("0.1 dB")
_JnxIfOpticsPMDayMinTxOutputPower_Type = Integer32
_JnxIfOpticsPMDayMinTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMDayMinTxOutputPower = _JnxIfOpticsPMDayMinTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 21),
    _JnxIfOpticsPMDayMinTxOutputPower_Type()
)
jnxIfOpticsPMDayMinTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMDayMaxTxOutputPower_Type = Integer32
_JnxIfOpticsPMDayMaxTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMDayMaxTxOutputPower = _JnxIfOpticsPMDayMaxTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 22),
    _JnxIfOpticsPMDayMaxTxOutputPower_Type()
)
jnxIfOpticsPMDayMaxTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMDayAvgTxOutputPower_Type = Integer32
_JnxIfOpticsPMDayAvgTxOutputPower_Object = MibTableColumn
jnxIfOpticsPMDayAvgTxOutputPower = _JnxIfOpticsPMDayAvgTxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 23),
    _JnxIfOpticsPMDayAvgTxOutputPower_Type()
)
jnxIfOpticsPMDayAvgTxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTxOutputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMDayMinRxInputPower_Type = Integer32
_JnxIfOpticsPMDayMinRxInputPower_Object = MibTableColumn
jnxIfOpticsPMDayMinRxInputPower = _JnxIfOpticsPMDayMinRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 24),
    _JnxIfOpticsPMDayMinRxInputPower_Type()
)
jnxIfOpticsPMDayMinRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMDayMaxRxInputPower_Type = Integer32
_JnxIfOpticsPMDayMaxRxInputPower_Object = MibTableColumn
jnxIfOpticsPMDayMaxRxInputPower = _JnxIfOpticsPMDayMaxRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 25),
    _JnxIfOpticsPMDayMaxRxInputPower_Type()
)
jnxIfOpticsPMDayMaxRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMDayAvgRxInputPower_Type = Integer32
_JnxIfOpticsPMDayAvgRxInputPower_Object = MibTableColumn
jnxIfOpticsPMDayAvgRxInputPower = _JnxIfOpticsPMDayAvgRxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 26),
    _JnxIfOpticsPMDayAvgRxInputPower_Type()
)
jnxIfOpticsPMDayAvgRxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgRxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgRxInputPower.setUnits("0.01 dbm")
_JnxIfOpticsPMDayTimeStamp_Type = DateAndTime
_JnxIfOpticsPMDayTimeStamp_Object = MibTableColumn
jnxIfOpticsPMDayTimeStamp = _JnxIfOpticsPMDayTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 27),
    _JnxIfOpticsPMDayTimeStamp_Type()
)
jnxIfOpticsPMDayTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayTimeStamp.setStatus("current")
_JnxIfOpticsPMDaySuspectedFlag_Type = TruthValue
_JnxIfOpticsPMDaySuspectedFlag_Object = MibTableColumn
jnxIfOpticsPMDaySuspectedFlag = _JnxIfOpticsPMDaySuspectedFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 28),
    _JnxIfOpticsPMDaySuspectedFlag_Type()
)
jnxIfOpticsPMDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDaySuspectedFlag.setStatus("current")
_JnxIfOpticsPMDaySuspectReason_Type = Integer32
_JnxIfOpticsPMDaySuspectReason_Object = MibTableColumn
jnxIfOpticsPMDaySuspectReason = _JnxIfOpticsPMDaySuspectReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 29),
    _JnxIfOpticsPMDaySuspectReason_Type()
)
jnxIfOpticsPMDaySuspectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDaySuspectReason.setStatus("current")
_JnxIfOpticsPMDayMinTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMDayMinTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMDayMinTxLaserBiasCurrent = _JnxIfOpticsPMDayMinTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 30),
    _JnxIfOpticsPMDayMinTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMDayMinTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayMaxTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMDayMaxTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMDayMaxTxLaserBiasCurrent = _JnxIfOpticsPMDayMaxTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 31),
    _JnxIfOpticsPMDayMaxTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMDayMaxTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayAvgTxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMDayAvgTxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMDayAvgTxLaserBiasCurrent = _JnxIfOpticsPMDayAvgTxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 32),
    _JnxIfOpticsPMDayAvgTxLaserBiasCurrent_Type()
)
jnxIfOpticsPMDayAvgTxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayMinTemperature_Type = Integer32
_JnxIfOpticsPMDayMinTemperature_Object = MibTableColumn
jnxIfOpticsPMDayMinTemperature = _JnxIfOpticsPMDayMinTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 33),
    _JnxIfOpticsPMDayMinTemperature_Type()
)
jnxIfOpticsPMDayMinTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTemperature.setUnits("Celcius")
_JnxIfOpticsPMDayMaxTemperature_Type = Integer32
_JnxIfOpticsPMDayMaxTemperature_Object = MibTableColumn
jnxIfOpticsPMDayMaxTemperature = _JnxIfOpticsPMDayMaxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 34),
    _JnxIfOpticsPMDayMaxTemperature_Type()
)
jnxIfOpticsPMDayMaxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTemperature.setUnits("Celcius")
_JnxIfOpticsPMDayAvgTemperature_Type = Integer32
_JnxIfOpticsPMDayAvgTemperature_Object = MibTableColumn
jnxIfOpticsPMDayAvgTemperature = _JnxIfOpticsPMDayAvgTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 35),
    _JnxIfOpticsPMDayAvgTemperature_Type()
)
jnxIfOpticsPMDayAvgTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTemperature.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTemperature.setUnits("Celcius")
_JnxIfOpticsPMDayMinCarFreqOffset_Type = Integer32
_JnxIfOpticsPMDayMinCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMDayMinCarFreqOffset = _JnxIfOpticsPMDayMinCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 36),
    _JnxIfOpticsPMDayMinCarFreqOffset_Type()
)
jnxIfOpticsPMDayMinCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinCarFreqOffset.setUnits("Mhz")
_JnxIfOpticsPMDayMaxCarFreqOffset_Type = Integer32
_JnxIfOpticsPMDayMaxCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMDayMaxCarFreqOffset = _JnxIfOpticsPMDayMaxCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 37),
    _JnxIfOpticsPMDayMaxCarFreqOffset_Type()
)
jnxIfOpticsPMDayMaxCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMDayAvgCarFreqOffset_Type = Integer32
_JnxIfOpticsPMDayAvgCarFreqOffset_Object = MibTableColumn
jnxIfOpticsPMDayAvgCarFreqOffset = _JnxIfOpticsPMDayAvgCarFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 38),
    _JnxIfOpticsPMDayAvgCarFreqOffset_Type()
)
jnxIfOpticsPMDayAvgCarFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgCarFreqOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgCarFreqOffset.setUnits("MHz")
_JnxIfOpticsPMDayMinRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMDayMinRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMDayMinRxLaserBiasCurrent = _JnxIfOpticsPMDayMinRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 39),
    _JnxIfOpticsPMDayMinRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMDayMinRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayMaxRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMDayMaxRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMDayMaxRxLaserBiasCurrent = _JnxIfOpticsPMDayMaxRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 40),
    _JnxIfOpticsPMDayMaxRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMDayMaxRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayAvgRxLaserBiasCurrent_Type = Integer32
_JnxIfOpticsPMDayAvgRxLaserBiasCurrent_Object = MibTableColumn
jnxIfOpticsPMDayAvgRxLaserBiasCurrent = _JnxIfOpticsPMDayAvgRxLaserBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 41),
    _JnxIfOpticsPMDayAvgRxLaserBiasCurrent_Type()
)
jnxIfOpticsPMDayAvgRxLaserBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgRxLaserBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgRxLaserBiasCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayMinTecCurrent_Type = Integer32
_JnxIfOpticsPMDayMinTecCurrent_Object = MibTableColumn
jnxIfOpticsPMDayMinTecCurrent = _JnxIfOpticsPMDayMinTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 42),
    _JnxIfOpticsPMDayMinTecCurrent_Type()
)
jnxIfOpticsPMDayMinTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayMaxTecCurrent_Type = Integer32
_JnxIfOpticsPMDayMaxTecCurrent_Object = MibTableColumn
jnxIfOpticsPMDayMaxTecCurrent = _JnxIfOpticsPMDayMaxTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 43),
    _JnxIfOpticsPMDayMaxTecCurrent_Type()
)
jnxIfOpticsPMDayMaxTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayAvgTecCurrent_Type = Integer32
_JnxIfOpticsPMDayAvgTecCurrent_Object = MibTableColumn
jnxIfOpticsPMDayAvgTecCurrent = _JnxIfOpticsPMDayAvgTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 44),
    _JnxIfOpticsPMDayAvgTecCurrent_Type()
)
jnxIfOpticsPMDayAvgTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTecCurrent.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgTecCurrent.setUnits(".1 mA")
_JnxIfOpticsPMDayMinResidualDispersion_Type = Integer32
_JnxIfOpticsPMDayMinResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMDayMinResidualDispersion = _JnxIfOpticsPMDayMinResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 45),
    _JnxIfOpticsPMDayMinResidualDispersion_Type()
)
jnxIfOpticsPMDayMinResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMDayMaxResidualDispersion_Type = Integer32
_JnxIfOpticsPMDayMaxResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMDayMaxResidualDispersion = _JnxIfOpticsPMDayMaxResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 46),
    _JnxIfOpticsPMDayMaxResidualDispersion_Type()
)
jnxIfOpticsPMDayMaxResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMDayAvgResidualDispersion_Type = Integer32
_JnxIfOpticsPMDayAvgResidualDispersion_Object = MibTableColumn
jnxIfOpticsPMDayAvgResidualDispersion = _JnxIfOpticsPMDayAvgResidualDispersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 47),
    _JnxIfOpticsPMDayAvgResidualDispersion_Type()
)
jnxIfOpticsPMDayAvgResidualDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgResidualDispersion.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgResidualDispersion.setUnits("0.1 ps/nm")
_JnxIfOpticsPMDayMinLevelHistogram_Type = Integer32
_JnxIfOpticsPMDayMinLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMDayMinLevelHistogram = _JnxIfOpticsPMDayMinLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 48),
    _JnxIfOpticsPMDayMinLevelHistogram_Type()
)
jnxIfOpticsPMDayMinLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinLevelHistogram.setStatus("current")
_JnxIfOpticsPMDayMaxLevelHistogram_Type = Integer32
_JnxIfOpticsPMDayMaxLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMDayMaxLevelHistogram = _JnxIfOpticsPMDayMaxLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 49),
    _JnxIfOpticsPMDayMaxLevelHistogram_Type()
)
jnxIfOpticsPMDayMaxLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxLevelHistogram.setStatus("current")
_JnxIfOpticsPMDayAvgLevelHistogram_Type = Integer32
_JnxIfOpticsPMDayAvgLevelHistogram_Object = MibTableColumn
jnxIfOpticsPMDayAvgLevelHistogram = _JnxIfOpticsPMDayAvgLevelHistogram_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 50),
    _JnxIfOpticsPMDayAvgLevelHistogram_Type()
)
jnxIfOpticsPMDayAvgLevelHistogram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgLevelHistogram.setStatus("current")
_JnxIfOpticsPMDayMinLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMDayMinLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMDayMinLaserFrequencyError = _JnxIfOpticsPMDayMinLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 51),
    _JnxIfOpticsPMDayMinLaserFrequencyError_Type()
)
jnxIfOpticsPMDayMinLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMDayMaxLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMDayMaxLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMDayMaxLaserFrequencyError = _JnxIfOpticsPMDayMaxLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 52),
    _JnxIfOpticsPMDayMaxLaserFrequencyError_Type()
)
jnxIfOpticsPMDayMaxLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMDayAvgLaserFrequencyError_Type = Integer32
_JnxIfOpticsPMDayAvgLaserFrequencyError_Object = MibTableColumn
jnxIfOpticsPMDayAvgLaserFrequencyError = _JnxIfOpticsPMDayAvgLaserFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 53),
    _JnxIfOpticsPMDayAvgLaserFrequencyError_Type()
)
jnxIfOpticsPMDayAvgLaserFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgLaserFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgLaserFrequencyError.setUnits("MHz")
_JnxIfOpticsPMDayMinFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMDayMinFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMDayMinFECCorrectedErrorsMantissa = _JnxIfOpticsPMDayMinFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 54),
    _JnxIfOpticsPMDayMinFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMDayMinFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMDayMinFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMDayMinFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMDayMinFECCorrectedErrorsExponent = _JnxIfOpticsPMDayMinFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 55),
    _JnxIfOpticsPMDayMinFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMDayMinFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa = _JnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 56),
    _JnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMDayMaxFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMDayMaxFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMDayMaxFECCorrectedErrorsExponent = _JnxIfOpticsPMDayMaxFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 57),
    _JnxIfOpticsPMDayMaxFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMDayMaxFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa_Type = Integer32
_JnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa_Object = MibTableColumn
jnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa = _JnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 58),
    _JnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa_Type()
)
jnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa.setStatus("current")
_JnxIfOpticsPMDayAvgFECCorrectedErrorsExponent_Type = Integer32
_JnxIfOpticsPMDayAvgFECCorrectedErrorsExponent_Object = MibTableColumn
jnxIfOpticsPMDayAvgFECCorrectedErrorsExponent = _JnxIfOpticsPMDayAvgFECCorrectedErrorsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 59),
    _JnxIfOpticsPMDayAvgFECCorrectedErrorsExponent_Type()
)
jnxIfOpticsPMDayAvgFECCorrectedErrorsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgFECCorrectedErrorsExponent.setStatus("current")
_JnxIfOpticsPMDayMinFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMDayMinFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMDayMinFECUCorrectedWordsMantissa = _JnxIfOpticsPMDayMinFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 60),
    _JnxIfOpticsPMDayMinFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMDayMinFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMDayMinFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMDayMinFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMDayMinFECUCorrectedWordsExponent = _JnxIfOpticsPMDayMinFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 61),
    _JnxIfOpticsPMDayMinFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMDayMinFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMinFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa = _JnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 62),
    _JnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMDayMaxFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMDayMaxFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMDayMaxFECUCorrectedWordsExponent = _JnxIfOpticsPMDayMaxFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 63),
    _JnxIfOpticsPMDayMaxFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMDayMaxFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayMaxFECUCorrectedWordsExponent.setStatus("current")
_JnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa_Type = Integer32
_JnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa_Object = MibTableColumn
jnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa = _JnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 64),
    _JnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa_Type()
)
jnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa.setStatus("current")
_JnxIfOpticsPMDayAvgFECUCorrectedWordsExponent_Type = Integer32
_JnxIfOpticsPMDayAvgFECUCorrectedWordsExponent_Object = MibTableColumn
jnxIfOpticsPMDayAvgFECUCorrectedWordsExponent = _JnxIfOpticsPMDayAvgFECUCorrectedWordsExponent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 2, 11, 1, 65),
    _JnxIfOpticsPMDayAvgFECUCorrectedWordsExponent_Type()
)
jnxIfOpticsPMDayAvgFECUCorrectedWordsExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfOpticsPMDayAvgFECUCorrectedWordsExponent.setStatus("current")
_JnxOpticsAlarm_ObjectIdentity = ObjectIdentity
jnxOpticsAlarm = _JnxOpticsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3)
)
_JnxOpticsNotificationTable_Object = MibTable
jnxOpticsNotificationTable = _JnxOpticsNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationTable.setStatus("current")
_JnxOpticsNotificationEntry_Object = MibTableRow
jnxOpticsNotificationEntry = _JnxOpticsNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1)
)
jnxOpticsNotificationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLocation"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDirection"),
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationEntry.setStatus("current")
_JnxOpticsNotificationLocation_Type = JnxOpticsLocation
_JnxOpticsNotificationLocation_Object = MibTableColumn
jnxOpticsNotificationLocation = _JnxOpticsNotificationLocation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 1),
    _JnxOpticsNotificationLocation_Type()
)
jnxOpticsNotificationLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationLocation.setStatus("current")
_JnxOpticsNotificationDirection_Type = JnxOpticsDirection
_JnxOpticsNotificationDirection_Object = MibTableColumn
jnxOpticsNotificationDirection = _JnxOpticsNotificationDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 2),
    _JnxOpticsNotificationDirection_Type()
)
jnxOpticsNotificationDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationDirection.setStatus("current")
_JnxOpticsLastNotificationId_Type = JnxOpticsNotificationId
_JnxOpticsLastNotificationId_Object = MibTableColumn
jnxOpticsLastNotificationId = _JnxOpticsLastNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 3),
    _JnxOpticsLastNotificationId_Type()
)
jnxOpticsLastNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsLastNotificationId.setStatus("current")
_JnxOpticsNotificationSeverity_Type = JnxOpticsSeverity
_JnxOpticsNotificationSeverity_Object = MibTableColumn
jnxOpticsNotificationSeverity = _JnxOpticsNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 4),
    _JnxOpticsNotificationSeverity_Type()
)
jnxOpticsNotificationSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationSeverity.setStatus("current")
_JnxOpticsNotificationDate_Type = DateAndTime
_JnxOpticsNotificationDate_Object = MibTableColumn
jnxOpticsNotificationDate = _JnxOpticsNotificationDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 5),
    _JnxOpticsNotificationDate_Type()
)
jnxOpticsNotificationDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOpticsNotificationDate.setStatus("current")


class _JnxOpticsNotificationLaneIndex_Type(Integer32):
    """Custom type jnxOpticsNotificationLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsNotificationLaneIndex_Type.__name__ = "Integer32"
_JnxOpticsNotificationLaneIndex_Object = MibTableColumn
jnxOpticsNotificationLaneIndex = _JnxOpticsNotificationLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 3, 1, 1, 6),
    _JnxOpticsNotificationLaneIndex_Type()
)
jnxOpticsNotificationLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsNotificationLaneIndex.setStatus("current")
_JnxOpticsOCh2_ObjectIdentity = ObjectIdentity
jnxOpticsOCh2 = _JnxOpticsOCh2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4)
)
_JnxOpticsOCh2ConfigTable_Object = MibTable
jnxOpticsOCh2ConfigTable = _JnxOpticsOCh2ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jnxOpticsOCh2ConfigTable.setStatus("obsolete")
_JnxOpticsOCh2ConfigEntry_Object = MibTableRow
jnxOpticsOCh2ConfigEntry = _JnxOpticsOCh2ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1)
)
jnxOpticsOCh2ConfigEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2CfgContIndex"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2CfgL1Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2CfgL2Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2CfgL3Index"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2CfgL4Index"),
)
if mibBuilder.loadTexts:
    jnxOpticsOCh2ConfigEntry.setStatus("obsolete")


class _JnxOpticsOCh2CfgContIndex_Type(Integer32):
    """Custom type jnxOpticsOCh2CfgContIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2CfgContIndex_Type.__name__ = "Integer32"
_JnxOpticsOCh2CfgContIndex_Object = MibTableColumn
jnxOpticsOCh2CfgContIndex = _JnxOpticsOCh2CfgContIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 1),
    _JnxOpticsOCh2CfgContIndex_Type()
)
jnxOpticsOCh2CfgContIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CfgContIndex.setStatus("obsolete")


class _JnxOpticsOCh2CfgL1Index_Type(Integer32):
    """Custom type jnxOpticsOCh2CfgL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2CfgL1Index_Type.__name__ = "Integer32"
_JnxOpticsOCh2CfgL1Index_Object = MibTableColumn
jnxOpticsOCh2CfgL1Index = _JnxOpticsOCh2CfgL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 2),
    _JnxOpticsOCh2CfgL1Index_Type()
)
jnxOpticsOCh2CfgL1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CfgL1Index.setStatus("obsolete")


class _JnxOpticsOCh2CfgL2Index_Type(Integer32):
    """Custom type jnxOpticsOCh2CfgL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2CfgL2Index_Type.__name__ = "Integer32"
_JnxOpticsOCh2CfgL2Index_Object = MibTableColumn
jnxOpticsOCh2CfgL2Index = _JnxOpticsOCh2CfgL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 3),
    _JnxOpticsOCh2CfgL2Index_Type()
)
jnxOpticsOCh2CfgL2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CfgL2Index.setStatus("obsolete")


class _JnxOpticsOCh2CfgL3Index_Type(Integer32):
    """Custom type jnxOpticsOCh2CfgL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2CfgL3Index_Type.__name__ = "Integer32"
_JnxOpticsOCh2CfgL3Index_Object = MibTableColumn
jnxOpticsOCh2CfgL3Index = _JnxOpticsOCh2CfgL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 4),
    _JnxOpticsOCh2CfgL3Index_Type()
)
jnxOpticsOCh2CfgL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CfgL3Index.setStatus("obsolete")


class _JnxOpticsOCh2CfgL4Index_Type(Integer32):
    """Custom type jnxOpticsOCh2CfgL4Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2CfgL4Index_Type.__name__ = "Integer32"
_JnxOpticsOCh2CfgL4Index_Object = MibTableColumn
jnxOpticsOCh2CfgL4Index = _JnxOpticsOCh2CfgL4Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 5),
    _JnxOpticsOCh2CfgL4Index_Type()
)
jnxOpticsOCh2CfgL4Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CfgL4Index.setStatus("obsolete")
_JnxOpticsOCh2Type_Type = Integer32
_JnxOpticsOCh2Type_Object = MibTableColumn
jnxOpticsOCh2Type = _JnxOpticsOCh2Type_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 6),
    _JnxOpticsOCh2Type_Type()
)
jnxOpticsOCh2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2Type.setStatus("obsolete")
_JnxOpticsOCh2LaserEnable_Type = TruthValue
_JnxOpticsOCh2LaserEnable_Object = MibTableColumn
jnxOpticsOCh2LaserEnable = _JnxOpticsOCh2LaserEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 7),
    _JnxOpticsOCh2LaserEnable_Type()
)
jnxOpticsOCh2LaserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2LaserEnable.setStatus("obsolete")
_JnxOpticsOCh2Wavelength_Type = Unsigned32
_JnxOpticsOCh2Wavelength_Object = MibTableColumn
jnxOpticsOCh2Wavelength = _JnxOpticsOCh2Wavelength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 8),
    _JnxOpticsOCh2Wavelength_Type()
)
jnxOpticsOCh2Wavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2Wavelength.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2Wavelength.setUnits("0.01 nm")
_JnxOpticsOCh2Spacing_Type = JnxOpticsChannelSpacing
_JnxOpticsOCh2Spacing_Object = MibTableColumn
jnxOpticsOCh2Spacing = _JnxOpticsOCh2Spacing_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 9),
    _JnxOpticsOCh2Spacing_Type()
)
jnxOpticsOCh2Spacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2Spacing.setStatus("obsolete")
_JnxOpticsOCh2Modulation_Type = Unsigned32
_JnxOpticsOCh2Modulation_Object = MibTableColumn
jnxOpticsOCh2Modulation = _JnxOpticsOCh2Modulation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 10),
    _JnxOpticsOCh2Modulation_Type()
)
jnxOpticsOCh2Modulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2Modulation.setStatus("obsolete")
_JnxOpticsOCh2TxOpticalPower_Type = Integer32
_JnxOpticsOCh2TxOpticalPower_Object = MibTableColumn
jnxOpticsOCh2TxOpticalPower = _JnxOpticsOCh2TxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 11),
    _JnxOpticsOCh2TxOpticalPower_Type()
)
jnxOpticsOCh2TxOpticalPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxOpticalPower.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxOpticalPower.setUnits("0.01 dbm")
_JnxOpticsOCh2RxOpticalPower_Type = Integer32
_JnxOpticsOCh2RxOpticalPower_Object = MibTableColumn
jnxOpticsOCh2RxOpticalPower = _JnxOpticsOCh2RxOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 12),
    _JnxOpticsOCh2RxOpticalPower_Type()
)
jnxOpticsOCh2RxOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxOpticalPower.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxOpticalPower.setUnits("0.01 dbm")
_JnxOpticsOCh2ModTempHighThresh_Type = Integer32
_JnxOpticsOCh2ModTempHighThresh_Object = MibTableColumn
jnxOpticsOCh2ModTempHighThresh = _JnxOpticsOCh2ModTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 13),
    _JnxOpticsOCh2ModTempHighThresh_Type()
)
jnxOpticsOCh2ModTempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2ModTempHighThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2ModTempHighThresh.setUnits("Celsius (0.01 degrees C)")
_JnxOpticsOCh2ModTempLowThresh_Type = Integer32
_JnxOpticsOCh2ModTempLowThresh_Object = MibTableColumn
jnxOpticsOCh2ModTempLowThresh = _JnxOpticsOCh2ModTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 14),
    _JnxOpticsOCh2ModTempLowThresh_Type()
)
jnxOpticsOCh2ModTempLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2ModTempLowThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2ModTempLowThresh.setUnits("Celsius (0.01 degrees C)")
_JnxOpticsOCh2TxPowHighThresh_Type = Integer32
_JnxOpticsOCh2TxPowHighThresh_Object = MibTableColumn
jnxOpticsOCh2TxPowHighThresh = _JnxOpticsOCh2TxPowHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 15),
    _JnxOpticsOCh2TxPowHighThresh_Type()
)
jnxOpticsOCh2TxPowHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxPowHighThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxPowHighThresh.setUnits("0.01 dbm")
_JnxOpticsOCh2TxPowLowThresh_Type = Integer32
_JnxOpticsOCh2TxPowLowThresh_Object = MibTableColumn
jnxOpticsOCh2TxPowLowThresh = _JnxOpticsOCh2TxPowLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 16),
    _JnxOpticsOCh2TxPowLowThresh_Type()
)
jnxOpticsOCh2TxPowLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxPowLowThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxPowLowThresh.setUnits("0.01 dbm")
_JnxOpticsOCh2RxPowHighThresh_Type = Integer32
_JnxOpticsOCh2RxPowHighThresh_Object = MibTableColumn
jnxOpticsOCh2RxPowHighThresh = _JnxOpticsOCh2RxPowHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 17),
    _JnxOpticsOCh2RxPowHighThresh_Type()
)
jnxOpticsOCh2RxPowHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxPowHighThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxPowHighThresh.setUnits("0.01 dbm")
_JnxOpticsOCh2RxPowLowThresh_Type = Integer32
_JnxOpticsOCh2RxPowLowThresh_Object = MibTableColumn
jnxOpticsOCh2RxPowLowThresh = _JnxOpticsOCh2RxPowLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 18),
    _JnxOpticsOCh2RxPowLowThresh_Type()
)
jnxOpticsOCh2RxPowLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxPowLowThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxPowLowThresh.setUnits("0.01 dbm")
_JnxOpticsOCh24HourModTemHiThresh_Type = Integer32
_JnxOpticsOCh24HourModTemHiThresh_Object = MibTableColumn
jnxOpticsOCh24HourModTemHiThresh = _JnxOpticsOCh24HourModTemHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 19),
    _JnxOpticsOCh24HourModTemHiThresh_Type()
)
jnxOpticsOCh24HourModTemHiThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourModTemHiThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourModTemHiThresh.setUnits("Celsius (0.01 degrees C)")
_JnxOpticsOCh24HourModTemLoThresh_Type = Integer32
_JnxOpticsOCh24HourModTemLoThresh_Object = MibTableColumn
jnxOpticsOCh24HourModTemLoThresh = _JnxOpticsOCh24HourModTemLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 20),
    _JnxOpticsOCh24HourModTemLoThresh_Type()
)
jnxOpticsOCh24HourModTemLoThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourModTemLoThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourModTemLoThresh.setUnits("Celsius (0.01 degrees C)")
_JnxOpticsOCh24HourTxPowHiThresh_Type = Integer32
_JnxOpticsOCh24HourTxPowHiThresh_Object = MibTableColumn
jnxOpticsOCh24HourTxPowHiThresh = _JnxOpticsOCh24HourTxPowHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 21),
    _JnxOpticsOCh24HourTxPowHiThresh_Type()
)
jnxOpticsOCh24HourTxPowHiThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourTxPowHiThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourTxPowHiThresh.setUnits("0.01 dbm")
_JnxOpticsOCh24HourTxPowLoThresh_Type = Integer32
_JnxOpticsOCh24HourTxPowLoThresh_Object = MibTableColumn
jnxOpticsOCh24HourTxPowLoThresh = _JnxOpticsOCh24HourTxPowLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 22),
    _JnxOpticsOCh24HourTxPowLoThresh_Type()
)
jnxOpticsOCh24HourTxPowLoThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourTxPowLoThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourTxPowLoThresh.setUnits("0.01 dbm")
_JnxOpticsOCh24HourRxPowHiThresh_Type = Integer32
_JnxOpticsOCh24HourRxPowHiThresh_Object = MibTableColumn
jnxOpticsOCh24HourRxPowHiThresh = _JnxOpticsOCh24HourRxPowHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 23),
    _JnxOpticsOCh24HourRxPowHiThresh_Type()
)
jnxOpticsOCh24HourRxPowHiThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourRxPowHiThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourRxPowHiThresh.setUnits("0.01 dbm")
_JnxOpticsOCh24HourRxPowLoThresh_Type = Integer32
_JnxOpticsOCh24HourRxPowLoThresh_Object = MibTableColumn
jnxOpticsOCh24HourRxPowLoThresh = _JnxOpticsOCh24HourRxPowLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 24),
    _JnxOpticsOCh24HourRxPowLoThresh_Type()
)
jnxOpticsOCh24HourRxPowLoThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourRxPowLoThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourRxPowLoThresh.setUnits("0.01 dbm")
_JnxOpticsOCh2RxLosPowWarnThresh_Type = Integer32
_JnxOpticsOCh2RxLosPowWarnThresh_Object = MibTableColumn
jnxOpticsOCh2RxLosPowWarnThresh = _JnxOpticsOCh2RxLosPowWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 25),
    _JnxOpticsOCh2RxLosPowWarnThresh_Type()
)
jnxOpticsOCh2RxLosPowWarnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxLosPowWarnThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxLosPowWarnThresh.setUnits("0.01 dbm")
_JnxOpticsOCh2RxLosPowAlarmThresh_Type = Integer32
_JnxOpticsOCh2RxLosPowAlarmThresh_Object = MibTableColumn
jnxOpticsOCh2RxLosPowAlarmThresh = _JnxOpticsOCh2RxLosPowAlarmThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 26),
    _JnxOpticsOCh2RxLosPowAlarmThresh_Type()
)
jnxOpticsOCh2RxLosPowAlarmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxLosPowAlarmThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxLosPowAlarmThresh.setUnits("0.01 dbm")


class _JnxOpticsOCh2CurrentStatus_Type(Bits):
    """Custom type jnxOpticsOCh2CurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("opticalLos", 1),
          ("wavelenthLockErr", 2),
          ("powerHighAlarm", 3),
          ("powerLowAlarm", 4),
          ("biasCurrentHighAlarm", 5),
          ("biasCurrentLowAlarm", 6),
          ("temperatureHighAlarm", 7),
          ("temperaturelowAlarm", 8),
          ("txPLLLockAlarm", 9),
          ("rxPLLLockAlarm", 10),
          ("avgPowerAlarm", 11),
          ("rxLossAvgPowerAlarm", 12),
          ("lossofACPowerAlarm", 13),
          ("txPowerHighThreshAlert", 14),
          ("txPowerLowThreshAlert", 15),
          ("rxPowerHighThreshAlert", 16),
          ("rxPowerLowThreshAlert", 17),
          ("moduleTempHighThreshAlert", 18),
          ("moduleTempLowThreshAlert", 19),
          ("txPowerHigh24HourThreshAlert", 20),
          ("txPowerLow24HourThreshAlert", 21),
          ("rxPowerHigh24HourThreshAlert", 22),
          ("rxPowerLow24HourThreshAlert", 23),
          ("moduleTempHigh24HourThreshAlert", 24),
          ("moduleTempLow24HourThreshAlert", 25),
          ("powerRxHighAlarm", 26),
          ("powerRxLowAlarm", 27),
          ("powerTxHighWarning", 28),
          ("powerTxLowWarning", 29),
          ("powerRxHighWarning", 30),
          ("powerRxLowWarning", 31),
          ("temperatureHighWarning", 32),
          ("temperaturelowWarning", 33))
    )

_JnxOpticsOCh2CurrentStatus_Type.__name__ = "Bits"
_JnxOpticsOCh2CurrentStatus_Object = MibTableColumn
jnxOpticsOCh2CurrentStatus = _JnxOpticsOCh2CurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 27),
    _JnxOpticsOCh2CurrentStatus_Type()
)
jnxOpticsOCh2CurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CurrentStatus.setStatus("obsolete")
_JnxOpticsOCh2TxPowHiEnableTCA_Type = TruthValue
_JnxOpticsOCh2TxPowHiEnableTCA_Object = MibTableColumn
jnxOpticsOCh2TxPowHiEnableTCA = _JnxOpticsOCh2TxPowHiEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 28),
    _JnxOpticsOCh2TxPowHiEnableTCA_Type()
)
jnxOpticsOCh2TxPowHiEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxPowHiEnableTCA.setStatus("obsolete")
_JnxOpticsOCh2TxPowLoEnableTCA_Type = TruthValue
_JnxOpticsOCh2TxPowLoEnableTCA_Object = MibTableColumn
jnxOpticsOCh2TxPowLoEnableTCA = _JnxOpticsOCh2TxPowLoEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 29),
    _JnxOpticsOCh2TxPowLoEnableTCA_Type()
)
jnxOpticsOCh2TxPowLoEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TxPowLoEnableTCA.setStatus("obsolete")
_JnxOpticsOCh2RxPowHiEnableTCA_Type = TruthValue
_JnxOpticsOCh2RxPowHiEnableTCA_Object = MibTableColumn
jnxOpticsOCh2RxPowHiEnableTCA = _JnxOpticsOCh2RxPowHiEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 30),
    _JnxOpticsOCh2RxPowHiEnableTCA_Type()
)
jnxOpticsOCh2RxPowHiEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxPowHiEnableTCA.setStatus("obsolete")
_JnxOpticsOCh2RxPowLoEnableTCA_Type = TruthValue
_JnxOpticsOCh2RxPowLoEnableTCA_Object = MibTableColumn
jnxOpticsOCh2RxPowLoEnableTCA = _JnxOpticsOCh2RxPowLoEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 31),
    _JnxOpticsOCh2RxPowLoEnableTCA_Type()
)
jnxOpticsOCh2RxPowLoEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2RxPowLoEnableTCA.setStatus("obsolete")
_JnxOpticsOCh2ModTempHiEnableTCA_Type = TruthValue
_JnxOpticsOCh2ModTempHiEnableTCA_Object = MibTableColumn
jnxOpticsOCh2ModTempHiEnableTCA = _JnxOpticsOCh2ModTempHiEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 32),
    _JnxOpticsOCh2ModTempHiEnableTCA_Type()
)
jnxOpticsOCh2ModTempHiEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2ModTempHiEnableTCA.setStatus("obsolete")
_JnxOpticsOCh2ModTempLoEnableTCA_Type = TruthValue
_JnxOpticsOCh2ModTempLoEnableTCA_Object = MibTableColumn
jnxOpticsOCh2ModTempLoEnableTCA = _JnxOpticsOCh2ModTempLoEnableTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 33),
    _JnxOpticsOCh2ModTempLoEnableTCA_Type()
)
jnxOpticsOCh2ModTempLoEnableTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2ModTempLoEnableTCA.setStatus("obsolete")
_JnxOpticsOCh2CarFreqOffHiEnTCA_Type = TruthValue
_JnxOpticsOCh2CarFreqOffHiEnTCA_Object = MibTableColumn
jnxOpticsOCh2CarFreqOffHiEnTCA = _JnxOpticsOCh2CarFreqOffHiEnTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 34),
    _JnxOpticsOCh2CarFreqOffHiEnTCA_Type()
)
jnxOpticsOCh2CarFreqOffHiEnTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CarFreqOffHiEnTCA.setStatus("obsolete")
_JnxOpticsOCh2CarFreqOffLoEnTCA_Type = TruthValue
_JnxOpticsOCh2CarFreqOffLoEnTCA_Object = MibTableColumn
jnxOpticsOCh2CarFreqOffLoEnTCA = _JnxOpticsOCh2CarFreqOffLoEnTCA_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 35),
    _JnxOpticsOCh2CarFreqOffLoEnTCA_Type()
)
jnxOpticsOCh2CarFreqOffLoEnTCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CarFreqOffLoEnTCA.setStatus("obsolete")
_JnxOpticsOCh2CarFreqOffHiThresh_Type = Integer32
_JnxOpticsOCh2CarFreqOffHiThresh_Object = MibTableColumn
jnxOpticsOCh2CarFreqOffHiThresh = _JnxOpticsOCh2CarFreqOffHiThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 36),
    _JnxOpticsOCh2CarFreqOffHiThresh_Type()
)
jnxOpticsOCh2CarFreqOffHiThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CarFreqOffHiThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CarFreqOffHiThresh.setUnits("MHz")
_JnxOpticsOCh24HourCarFreqOffHiTh_Type = Integer32
_JnxOpticsOCh24HourCarFreqOffHiTh_Object = MibTableColumn
jnxOpticsOCh24HourCarFreqOffHiTh = _JnxOpticsOCh24HourCarFreqOffHiTh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 37),
    _JnxOpticsOCh24HourCarFreqOffHiTh_Type()
)
jnxOpticsOCh24HourCarFreqOffHiTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourCarFreqOffHiTh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourCarFreqOffHiTh.setUnits("MHz")
_JnxOpticsOCh2CarFreqOffLoThresh_Type = Integer32
_JnxOpticsOCh2CarFreqOffLoThresh_Object = MibTableColumn
jnxOpticsOCh2CarFreqOffLoThresh = _JnxOpticsOCh2CarFreqOffLoThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 38),
    _JnxOpticsOCh2CarFreqOffLoThresh_Type()
)
jnxOpticsOCh2CarFreqOffLoThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CarFreqOffLoThresh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh2CarFreqOffLoThresh.setUnits("MHz")
_JnxOpticsOCh24HourCarFreqOffLoTh_Type = Integer32
_JnxOpticsOCh24HourCarFreqOffLoTh_Object = MibTableColumn
jnxOpticsOCh24HourCarFreqOffLoTh = _JnxOpticsOCh24HourCarFreqOffLoTh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 1, 1, 39),
    _JnxOpticsOCh24HourCarFreqOffLoTh_Type()
)
jnxOpticsOCh24HourCarFreqOffLoTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourCarFreqOffLoTh.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxOpticsOCh24HourCarFreqOffLoTh.setUnits("MHz")
_JnxOpticsOCh2TraceToneCfgTable_Object = MibTable
jnxOpticsOCh2TraceToneCfgTable = _JnxOpticsOCh2TraceToneCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2)
)
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgTable.setStatus("obsolete")
_JnxOpticsOCh2TraceToneCfgEntry_Object = MibTableRow
jnxOpticsOCh2TraceToneCfgEntry = _JnxOpticsOCh2TraceToneCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1)
)
jnxOpticsOCh2TraceToneCfgEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2TraceToneCfgIndx"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2TraceToneCfgL1Indx"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2TraceToneCfgL2Indx"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2TraceToneCfgL3Indx"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxOpticsOCh2TraceToneCfgL4Indx"),
)
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgEntry.setStatus("obsolete")


class _JnxOpticsOCh2TraceToneCfgIndx_Type(Integer32):
    """Custom type jnxOpticsOCh2TraceToneCfgIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2TraceToneCfgIndx_Type.__name__ = "Integer32"
_JnxOpticsOCh2TraceToneCfgIndx_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgIndx = _JnxOpticsOCh2TraceToneCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 1),
    _JnxOpticsOCh2TraceToneCfgIndx_Type()
)
jnxOpticsOCh2TraceToneCfgIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgIndx.setStatus("obsolete")


class _JnxOpticsOCh2TraceToneCfgL1Indx_Type(Integer32):
    """Custom type jnxOpticsOCh2TraceToneCfgL1Indx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2TraceToneCfgL1Indx_Type.__name__ = "Integer32"
_JnxOpticsOCh2TraceToneCfgL1Indx_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgL1Indx = _JnxOpticsOCh2TraceToneCfgL1Indx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 2),
    _JnxOpticsOCh2TraceToneCfgL1Indx_Type()
)
jnxOpticsOCh2TraceToneCfgL1Indx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgL1Indx.setStatus("obsolete")


class _JnxOpticsOCh2TraceToneCfgL2Indx_Type(Integer32):
    """Custom type jnxOpticsOCh2TraceToneCfgL2Indx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2TraceToneCfgL2Indx_Type.__name__ = "Integer32"
_JnxOpticsOCh2TraceToneCfgL2Indx_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgL2Indx = _JnxOpticsOCh2TraceToneCfgL2Indx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 3),
    _JnxOpticsOCh2TraceToneCfgL2Indx_Type()
)
jnxOpticsOCh2TraceToneCfgL2Indx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgL2Indx.setStatus("obsolete")


class _JnxOpticsOCh2TraceToneCfgL3Indx_Type(Integer32):
    """Custom type jnxOpticsOCh2TraceToneCfgL3Indx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2TraceToneCfgL3Indx_Type.__name__ = "Integer32"
_JnxOpticsOCh2TraceToneCfgL3Indx_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgL3Indx = _JnxOpticsOCh2TraceToneCfgL3Indx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 4),
    _JnxOpticsOCh2TraceToneCfgL3Indx_Type()
)
jnxOpticsOCh2TraceToneCfgL3Indx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgL3Indx.setStatus("obsolete")


class _JnxOpticsOCh2TraceToneCfgL4Indx_Type(Integer32):
    """Custom type jnxOpticsOCh2TraceToneCfgL4Indx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxOpticsOCh2TraceToneCfgL4Indx_Type.__name__ = "Integer32"
_JnxOpticsOCh2TraceToneCfgL4Indx_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgL4Indx = _JnxOpticsOCh2TraceToneCfgL4Indx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 5),
    _JnxOpticsOCh2TraceToneCfgL4Indx_Type()
)
jnxOpticsOCh2TraceToneCfgL4Indx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgL4Indx.setStatus("obsolete")
_JnxOpticsOCh2TraceToneCfgTxEn_Type = TruthValue
_JnxOpticsOCh2TraceToneCfgTxEn_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgTxEn = _JnxOpticsOCh2TraceToneCfgTxEn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 6),
    _JnxOpticsOCh2TraceToneCfgTxEn_Type()
)
jnxOpticsOCh2TraceToneCfgTxEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgTxEn.setStatus("obsolete")
_JnxOpticsOCh2TraceToneCfgRxEn_Type = TruthValue
_JnxOpticsOCh2TraceToneCfgRxEn_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgRxEn = _JnxOpticsOCh2TraceToneCfgRxEn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 7),
    _JnxOpticsOCh2TraceToneCfgRxEn_Type()
)
jnxOpticsOCh2TraceToneCfgRxEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgRxEn.setStatus("obsolete")
_JnxOpticsOCh2TraceToneCfgDestId_Type = OctetString
_JnxOpticsOCh2TraceToneCfgDestId_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgDestId = _JnxOpticsOCh2TraceToneCfgDestId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 8),
    _JnxOpticsOCh2TraceToneCfgDestId_Type()
)
jnxOpticsOCh2TraceToneCfgDestId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgDestId.setStatus("obsolete")
_JnxOpticsOCh2TraceToneCfgTxMsg_Type = OctetString
_JnxOpticsOCh2TraceToneCfgTxMsg_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgTxMsg = _JnxOpticsOCh2TraceToneCfgTxMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 9),
    _JnxOpticsOCh2TraceToneCfgTxMsg_Type()
)
jnxOpticsOCh2TraceToneCfgTxMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgTxMsg.setStatus("obsolete")
_JnxOpticsOCh2TraceToneCfgRxMsg_Type = OctetString
_JnxOpticsOCh2TraceToneCfgRxMsg_Object = MibTableColumn
jnxOpticsOCh2TraceToneCfgRxMsg = _JnxOpticsOCh2TraceToneCfgRxMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 4, 2, 1, 10),
    _JnxOpticsOCh2TraceToneCfgRxMsg_Type()
)
jnxOpticsOCh2TraceToneCfgRxMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOpticsOCh2TraceToneCfgRxMsg.setStatus("obsolete")
_JnxIplcAlarm_ObjectIdentity = ObjectIdentity
jnxIplcAlarm = _JnxIplcAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5)
)
_JnxIplcNotificationTable_Object = MibTable
jnxIplcNotificationTable = _JnxIplcNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1)
)
if mibBuilder.loadTexts:
    jnxIplcNotificationTable.setStatus("current")
_JnxIplcNotificationEntry_Object = MibTableRow
jnxIplcNotificationEntry = _JnxIplcNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1)
)
jnxIplcNotificationEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationSlot"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationChannel"),
)
if mibBuilder.loadTexts:
    jnxIplcNotificationEntry.setStatus("current")
_JnxIplcNotificationLocation_Type = JnxOpticsLocation
_JnxIplcNotificationLocation_Object = MibTableColumn
jnxIplcNotificationLocation = _JnxIplcNotificationLocation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1, 1),
    _JnxIplcNotificationLocation_Type()
)
jnxIplcNotificationLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIplcNotificationLocation.setStatus("current")
_JnxIplcNotificationDirection_Type = JnxOpticsDirection
_JnxIplcNotificationDirection_Object = MibTableColumn
jnxIplcNotificationDirection = _JnxIplcNotificationDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1, 2),
    _JnxIplcNotificationDirection_Type()
)
jnxIplcNotificationDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIplcNotificationDirection.setStatus("current")


class _JnxIplcNotificationSlot_Type(Integer32):
    """Custom type jnxIplcNotificationSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIplcNotificationSlot_Type.__name__ = "Integer32"
_JnxIplcNotificationSlot_Object = MibTableColumn
jnxIplcNotificationSlot = _JnxIplcNotificationSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1, 3),
    _JnxIplcNotificationSlot_Type()
)
jnxIplcNotificationSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIplcNotificationSlot.setStatus("current")


class _JnxIplcNotificationChannel_Type(Integer32):
    """Custom type jnxIplcNotificationChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIplcNotificationChannel_Type.__name__ = "Integer32"
_JnxIplcNotificationChannel_Object = MibTableColumn
jnxIplcNotificationChannel = _JnxIplcNotificationChannel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1, 4),
    _JnxIplcNotificationChannel_Type()
)
jnxIplcNotificationChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIplcNotificationChannel.setStatus("current")
_JnxIplcLastNotificationId_Type = JnxIplcNotificationId
_JnxIplcLastNotificationId_Object = MibTableColumn
jnxIplcLastNotificationId = _JnxIplcLastNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1, 5),
    _JnxIplcLastNotificationId_Type()
)
jnxIplcLastNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIplcLastNotificationId.setStatus("current")
_JnxIplcNotificationSeverity_Type = JnxOpticsSeverity
_JnxIplcNotificationSeverity_Object = MibTableColumn
jnxIplcNotificationSeverity = _JnxIplcNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1, 6),
    _JnxIplcNotificationSeverity_Type()
)
jnxIplcNotificationSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIplcNotificationSeverity.setStatus("current")
_JnxIplcNotificationDate_Type = DateAndTime
_JnxIplcNotificationDate_Object = MibTableColumn
jnxIplcNotificationDate = _JnxIplcNotificationDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 5, 1, 1, 7),
    _JnxIplcNotificationDate_Type()
)
jnxIplcNotificationDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIplcNotificationDate.setStatus("current")
_JnxIlaAlarm_ObjectIdentity = ObjectIdentity
jnxIlaAlarm = _JnxIlaAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6)
)
_JnxIlaNotificationTable_Object = MibTable
jnxIlaNotificationTable = _JnxIlaNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1)
)
if mibBuilder.loadTexts:
    jnxIlaNotificationTable.setStatus("current")
_JnxIlaNotificationEntry_Object = MibTableRow
jnxIlaNotificationEntry = _JnxIlaNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1)
)
jnxIlaNotificationEntry.setIndexNames(
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationSlot"),
    (0, "JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationIlaID"),
)
if mibBuilder.loadTexts:
    jnxIlaNotificationEntry.setStatus("current")
_JnxIlaNotificationLocation_Type = JnxOpticsLocation
_JnxIlaNotificationLocation_Object = MibTableColumn
jnxIlaNotificationLocation = _JnxIlaNotificationLocation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1, 1),
    _JnxIlaNotificationLocation_Type()
)
jnxIlaNotificationLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIlaNotificationLocation.setStatus("current")
_JnxIlaNotificationDirection_Type = JnxOpticsDirection
_JnxIlaNotificationDirection_Object = MibTableColumn
jnxIlaNotificationDirection = _JnxIlaNotificationDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1, 2),
    _JnxIlaNotificationDirection_Type()
)
jnxIlaNotificationDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIlaNotificationDirection.setStatus("current")


class _JnxIlaNotificationSlot_Type(Integer32):
    """Custom type jnxIlaNotificationSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIlaNotificationSlot_Type.__name__ = "Integer32"
_JnxIlaNotificationSlot_Object = MibTableColumn
jnxIlaNotificationSlot = _JnxIlaNotificationSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1, 3),
    _JnxIlaNotificationSlot_Type()
)
jnxIlaNotificationSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIlaNotificationSlot.setStatus("current")


class _JnxIlaNotificationIlaID_Type(Integer32):
    """Custom type jnxIlaNotificationIlaID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_JnxIlaNotificationIlaID_Type.__name__ = "Integer32"
_JnxIlaNotificationIlaID_Object = MibTableColumn
jnxIlaNotificationIlaID = _JnxIlaNotificationIlaID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1, 4),
    _JnxIlaNotificationIlaID_Type()
)
jnxIlaNotificationIlaID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIlaNotificationIlaID.setStatus("current")
_JnxIlaLastNotificationId_Type = JnxIlaNotificationId
_JnxIlaLastNotificationId_Object = MibTableColumn
jnxIlaLastNotificationId = _JnxIlaLastNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1, 5),
    _JnxIlaLastNotificationId_Type()
)
jnxIlaLastNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIlaLastNotificationId.setStatus("current")
_JnxIlaNotificationSeverity_Type = JnxOpticsSeverity
_JnxIlaNotificationSeverity_Object = MibTableColumn
jnxIlaNotificationSeverity = _JnxIlaNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1, 6),
    _JnxIlaNotificationSeverity_Type()
)
jnxIlaNotificationSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIlaNotificationSeverity.setStatus("current")
_JnxIlaNotificationDate_Type = DateAndTime
_JnxIlaNotificationDate_Object = MibTableColumn
jnxIlaNotificationDate = _JnxIlaNotificationDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 71, 1, 6, 1, 1, 7),
    _JnxIlaNotificationDate_Type()
)
jnxIlaNotificationDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxIlaNotificationDate.setStatus("current")
_JnxOpticsNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxOpticsNotificationPrefix = _JnxOpticsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0)
)
_JnxIplcNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxIplcNotificationPrefix = _JnxIplcNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 28, 0)
)
_JnxIlaNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxIlaNotificationPrefix = _JnxIlaNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 29, 0)
)

# Managed Objects groups


# Notification objects

jnxOpticsNotificationSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0, 1)
)
jnxOpticsNotificationSet.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDirection"),
        ("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDate"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLaneIndex"))
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationSet.setStatus(
        "current"
    )

jnxOpticsNotificationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0, 2)
)
jnxOpticsNotificationCleared.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDirection"),
        ("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationDate"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsNotificationLaneIndex"))
)
if mibBuilder.loadTexts:
    jnxOpticsNotificationCleared.setStatus(
        "current"
    )

jnxIfOpticsNotificationAdminStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0, 3)
)
jnxIfOpticsNotificationAdminStatus.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsOTIfAdminState"))
)
if mibBuilder.loadTexts:
    jnxIfOpticsNotificationAdminStatus.setStatus(
        "current"
    )

jnxIfOpticsNotificationOperStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 22, 0, 4)
)
jnxIfOpticsNotificationOperStatus.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-IFOPTICS-MIB", "jnxOpticsOTIfOperState"))
)
if mibBuilder.loadTexts:
    jnxIfOpticsNotificationOperStatus.setStatus(
        "current"
    )

jnxIplcNotificationSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 28, 0, 1)
)
jnxIplcNotificationSet.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationDirection"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationSlot"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationChannel"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationDate"))
)
if mibBuilder.loadTexts:
    jnxIplcNotificationSet.setStatus(
        "current"
    )

jnxIplcNotificationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 28, 0, 2)
)
jnxIplcNotificationCleared.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationDirection"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationSlot"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationChannel"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIplcNotificationDate"))
)
if mibBuilder.loadTexts:
    jnxIplcNotificationCleared.setStatus(
        "current"
    )

jnxIlaNotificationSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 29, 0, 1)
)
jnxIlaNotificationSet.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationDirection"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationSlot"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationIlaID"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationDate"))
)
if mibBuilder.loadTexts:
    jnxIlaNotificationSet.setStatus(
        "current"
    )

jnxIlaNotificationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 29, 0, 2)
)
jnxIlaNotificationCleared.setObjects(
      *(("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationLocation"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationDirection"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationSlot"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationIlaID"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaLastNotificationId"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationSeverity"),
        ("JUNIPER-IFOPTICS-MIB", "jnxIlaNotificationDate"))
)
if mibBuilder.loadTexts:
    jnxIlaNotificationCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IFOPTICS-MIB",
    **{"JnxOpticsLocation": JnxOpticsLocation,
       "JnxOpticsDirection": JnxOpticsDirection,
       "JnxOpticsSeverity": JnxOpticsSeverity,
       "JnxOpticsServiceStateAction": JnxOpticsServiceStateAction,
       "JnxOpticsChannelSpacing": JnxOpticsChannelSpacing,
       "JnxOpticsOTIfFecType": JnxOpticsOTIfFecType,
       "JnxOpticsOTIfEncodingOptions": JnxOpticsOTIfEncodingOptions,
       "JnxOpticsOTIfAdminStates": JnxOpticsOTIfAdminStates,
       "JnxOpticsOTIfOperStates": JnxOpticsOTIfOperStates,
       "JnxOpticsNotificationId": JnxOpticsNotificationId,
       "JnxIplcNotificationId": JnxIplcNotificationId,
       "JnxIlaNotificationId": JnxIlaNotificationId,
       "jnxIfOpticsMib": jnxIfOpticsMib,
       "jnxOptics": jnxOptics,
       "jnxOpticsConfigTable": jnxOpticsConfigTable,
       "jnxOpticsConfigEntry": jnxOpticsConfigEntry,
       "jnxOpticsConfigContainerIndex": jnxOpticsConfigContainerIndex,
       "jnxOpticsConfigL1Index": jnxOpticsConfigL1Index,
       "jnxOpticsConfigL2Index": jnxOpticsConfigL2Index,
       "jnxOpticsConfigL3Index": jnxOpticsConfigL3Index,
       "jnxOpticsType": jnxOpticsType,
       "jnxLaserEnable": jnxLaserEnable,
       "jnxWavelength": jnxWavelength,
       "jnxSpacing": jnxSpacing,
       "jnxModulation": jnxModulation,
       "jnxTxOpticalPower": jnxTxOpticalPower,
       "jnxRxOpticalPower": jnxRxOpticalPower,
       "jnxModuleTempHighThresh": jnxModuleTempHighThresh,
       "jnxModuleTempLowThresh": jnxModuleTempLowThresh,
       "jnxTxPowerHighThresh": jnxTxPowerHighThresh,
       "jnxTxPowerLowThresh": jnxTxPowerLowThresh,
       "jnxRxPowerHighThresh": jnxRxPowerHighThresh,
       "jnxRxPowerLowThresh": jnxRxPowerLowThresh,
       "jnx24HourModuleTempHighThresh": jnx24HourModuleTempHighThresh,
       "jnx24HourModuleTempLowThresh": jnx24HourModuleTempLowThresh,
       "jnx24HourTxPowerHighThresh": jnx24HourTxPowerHighThresh,
       "jnx24HourTxPowerLowThresh": jnx24HourTxPowerLowThresh,
       "jnx24HourRxPowerHighThresh": jnx24HourRxPowerHighThresh,
       "jnx24HourRxPowerLowThresh": jnx24HourRxPowerLowThresh,
       "jnxRxLosPowerWarningThresh": jnxRxLosPowerWarningThresh,
       "jnxRxLosPowerAlarmThresh": jnxRxLosPowerAlarmThresh,
       "jnxOpticsCurrentStatus": jnxOpticsCurrentStatus,
       "jnxTxPowerHighEnableTCA": jnxTxPowerHighEnableTCA,
       "jnxTxPowerLowEnableTCA": jnxTxPowerLowEnableTCA,
       "jnxRxPowerHighEnableTCA": jnxRxPowerHighEnableTCA,
       "jnxRxPowerLowEnableTCA": jnxRxPowerLowEnableTCA,
       "jnxModuleTempHighEnableTCA": jnxModuleTempHighEnableTCA,
       "jnxModuleTempLowEnableTCA": jnxModuleTempLowEnableTCA,
       "jnxCarFreqOffsetHighEnableTCA": jnxCarFreqOffsetHighEnableTCA,
       "jnxCarFreqOffsetLowEnableTCA": jnxCarFreqOffsetLowEnableTCA,
       "jnxCarFreqOffsetHighThresh": jnxCarFreqOffsetHighThresh,
       "jnx24HourCarFreqOffsetHighThresh": jnx24HourCarFreqOffsetHighThresh,
       "jnxCarFreqOffsetLowThresh": jnxCarFreqOffsetLowThresh,
       "jnx24HourCarFreqOffsetLowThresh": jnx24HourCarFreqOffsetLowThresh,
       "jnxOpticsTraceToneCfgTable": jnxOpticsTraceToneCfgTable,
       "jnxOpticsTraceToneCfgEntry": jnxOpticsTraceToneCfgEntry,
       "jnxOpticsTraceToneCfgContainerIndex": jnxOpticsTraceToneCfgContainerIndex,
       "jnxOpticsTraceToneCfgL1Index": jnxOpticsTraceToneCfgL1Index,
       "jnxOpticsTraceToneCfgL2Index": jnxOpticsTraceToneCfgL2Index,
       "jnxOpticsTraceToneCfgL3Index": jnxOpticsTraceToneCfgL3Index,
       "jnxOpticsTraceToneCfgTxEnable": jnxOpticsTraceToneCfgTxEnable,
       "jnxOpticsTraceToneCfgRxEnable": jnxOpticsTraceToneCfgRxEnable,
       "jnxOpticsTraceToneCfgDestId": jnxOpticsTraceToneCfgDestId,
       "jnxOpticsTraceToneCfgTxMsg": jnxOpticsTraceToneCfgTxMsg,
       "jnxOpticsTraceToneCfgRxMsg": jnxOpticsTraceToneCfgRxMsg,
       "jnxOpticsNotificationTrigDefaultHoldtimeUp": jnxOpticsNotificationTrigDefaultHoldtimeUp,
       "jnxOpticsNotificationTrigDefaultHoldtimeDown": jnxOpticsNotificationTrigDefaultHoldtimeDown,
       "jnxOpticsNotificationTrigTable": jnxOpticsNotificationTrigTable,
       "jnxOpticsNotificationTrigEntry": jnxOpticsNotificationTrigEntry,
       "jnxOpticsNotificationTrigContainerIndex": jnxOpticsNotificationTrigContainerIndex,
       "jnxOpticsNotificationTrigL1Index": jnxOpticsNotificationTrigL1Index,
       "jnxOpticsNotificationTrigL2Index": jnxOpticsNotificationTrigL2Index,
       "jnxOpticsNotificationTrigL3Index": jnxOpticsNotificationTrigL3Index,
       "jnxOpticsNotificationTrigAlmId": jnxOpticsNotificationTrigAlmId,
       "jnxOpticsNotificationTrigSeverity": jnxOpticsNotificationTrigSeverity,
       "jnxOpticsNotificationTrigIgnore": jnxOpticsNotificationTrigIgnore,
       "jnxOpticsNotificationTrigHoldtimeUp": jnxOpticsNotificationTrigHoldtimeUp,
       "jnxOpticsNotificationTrigHoldtimeDown": jnxOpticsNotificationTrigHoldtimeDown,
       "jnxOpticsTrigServiceStateAction": jnxOpticsTrigServiceStateAction,
       "jnxOpticsClearAllPMs": jnxOpticsClearAllPMs,
       "jnxOpticsClearIfPMsTable": jnxOpticsClearIfPMsTable,
       "jnxOpticsClearIfPMsEntry": jnxOpticsClearIfPMsEntry,
       "jnxOpticsClearCurrent": jnxOpticsClearCurrent,
       "jnxOpticsClearInterfaceInterval": jnxOpticsClearInterfaceInterval,
       "jnxOpticsClearInterfaceDay": jnxOpticsClearInterfaceDay,
       "jnxOpticsClearInterfaceAll": jnxOpticsClearInterfaceAll,
       "jnxOpticsOTIfConfigTable": jnxOpticsOTIfConfigTable,
       "jnxOpticsOTIfConfigEntry": jnxOpticsOTIfConfigEntry,
       "jnxOpticsOTIfConfigContainerIndex": jnxOpticsOTIfConfigContainerIndex,
       "jnxOpticsOTIfConfigL1Index": jnxOpticsOTIfConfigL1Index,
       "jnxOpticsOTIfConfigL2Index": jnxOpticsOTIfConfigL2Index,
       "jnxOpticsOTIfConfigL3Index": jnxOpticsOTIfConfigL3Index,
       "jnxOpticsOTIfLaserEnable": jnxOpticsOTIfLaserEnable,
       "jnxOpticsOTIfFecMode": jnxOpticsOTIfFecMode,
       "jnxOpticsOTIfEncodingOption": jnxOpticsOTIfEncodingOption,
       "jnxOpticsOTIfModulation": jnxOpticsOTIfModulation,
       "jnxOpticsOTIfAdminState": jnxOpticsOTIfAdminState,
       "jnxOpticsOTIfOperState": jnxOpticsOTIfOperState,
       "jnxOpticsOTIfHighPolarization": jnxOpticsOTIfHighPolarization,
       "jnxOpticsOTIfPreFecBERThresholdMantissa": jnxOpticsOTIfPreFecBERThresholdMantissa,
       "jnxOpticsOTIfPreFecBERThresholdExponent": jnxOpticsOTIfPreFecBERThresholdExponent,
       "jnxOpticsOTIfPreFecBERThresholdTime": jnxOpticsOTIfPreFecBERThresholdTime,
       "jnxOpticsOTIfPreFecBERThresholdClearMantissa": jnxOpticsOTIfPreFecBERThresholdClearMantissa,
       "jnxOpticsOTIfPreFecBERThresholdClearExponent": jnxOpticsOTIfPreFecBERThresholdClearExponent,
       "jnxOpticsPerformanceMonitoring": jnxOpticsPerformanceMonitoring,
       "jnxOpticsPMCurrentTable": jnxOpticsPMCurrentTable,
       "jnxOpticsPMCurrentEntry": jnxOpticsPMCurrentEntry,
       "jnxPMCurChromaticDispersion": jnxPMCurChromaticDispersion,
       "jnxPMCurDiffGroupDelay": jnxPMCurDiffGroupDelay,
       "jnxPMCurPolarizationState": jnxPMCurPolarizationState,
       "jnxPMCurPolarDepLoss": jnxPMCurPolarDepLoss,
       "jnxPMCurQ": jnxPMCurQ,
       "jnxPMCurSNR": jnxPMCurSNR,
       "jnxPMCurTxOutputPower": jnxPMCurTxOutputPower,
       "jnxPMCurRxInputPower": jnxPMCurRxInputPower,
       "jnxPMCurMinChromaticDispersion": jnxPMCurMinChromaticDispersion,
       "jnxPMCurMaxChromaticDispersion": jnxPMCurMaxChromaticDispersion,
       "jnxPMCurAvgChromaticDispersion": jnxPMCurAvgChromaticDispersion,
       "jnxPMCurMinDiffGroupDelay": jnxPMCurMinDiffGroupDelay,
       "jnxPMCurMaxDiffGroupDelay": jnxPMCurMaxDiffGroupDelay,
       "jnxPMCurAvgDiffGroupDelay": jnxPMCurAvgDiffGroupDelay,
       "jnxPMCurMinPolarState": jnxPMCurMinPolarState,
       "jnxPMCurMaxPolarState": jnxPMCurMaxPolarState,
       "jnxPMCurAvgPolarState": jnxPMCurAvgPolarState,
       "jnxPMCurMinPolarDepLoss": jnxPMCurMinPolarDepLoss,
       "jnxPMCurMaxPolarDepLoss": jnxPMCurMaxPolarDepLoss,
       "jnxPMCurAvgPolarDepLoss": jnxPMCurAvgPolarDepLoss,
       "jnxPMCurMinQ": jnxPMCurMinQ,
       "jnxPMCurMaxQ": jnxPMCurMaxQ,
       "jnxPMCurAvgQ": jnxPMCurAvgQ,
       "jnxPMCurMinSNR": jnxPMCurMinSNR,
       "jnxPMCurMaxSNR": jnxPMCurMaxSNR,
       "jnxPMCurAvgSNR": jnxPMCurAvgSNR,
       "jnxPMCurMinTxOutputPower": jnxPMCurMinTxOutputPower,
       "jnxPMCurMaxTxOutputPower": jnxPMCurMaxTxOutputPower,
       "jnxPMCurAvgTxOutputPower": jnxPMCurAvgTxOutputPower,
       "jnxPMCurMinRxInputPower": jnxPMCurMinRxInputPower,
       "jnxPMCurMaxRxInputPower": jnxPMCurMaxRxInputPower,
       "jnxPMCurAvgRxInputPower": jnxPMCurAvgRxInputPower,
       "jnxPMCurSuspectedFlag": jnxPMCurSuspectedFlag,
       "jnxPMCurSuspectReason": jnxPMCurSuspectReason,
       "jnxPMCurTxLaserBiasCurrent": jnxPMCurTxLaserBiasCurrent,
       "jnxPMCurMinTxLaserBiasCurrent": jnxPMCurMinTxLaserBiasCurrent,
       "jnxPMCurMaxTxLaserBiasCurrent": jnxPMCurMaxTxLaserBiasCurrent,
       "jnxPMCurAvgTxLaserBiasCurrent": jnxPMCurAvgTxLaserBiasCurrent,
       "jnxPMCurTemperature": jnxPMCurTemperature,
       "jnxPMCurMinTemperature": jnxPMCurMinTemperature,
       "jnxPMCurMaxTemperature": jnxPMCurMaxTemperature,
       "jnxPMCurAvgTemperature": jnxPMCurAvgTemperature,
       "jnxPMCurCarFreqOffset": jnxPMCurCarFreqOffset,
       "jnxPMCurMinCarFreqOffset": jnxPMCurMinCarFreqOffset,
       "jnxPMCurMaxCarFreqOffset": jnxPMCurMaxCarFreqOffset,
       "jnxPMCurAvgCarFreqOffset": jnxPMCurAvgCarFreqOffset,
       "jnxPMCurRxLaserBiasCurrent": jnxPMCurRxLaserBiasCurrent,
       "jnxPMCurMinRxLaserBiasCurrent": jnxPMCurMinRxLaserBiasCurrent,
       "jnxPMCurMaxRxLaserBiasCurrent": jnxPMCurMaxRxLaserBiasCurrent,
       "jnxPMCurAvgRxLaserBiasCurrent": jnxPMCurAvgRxLaserBiasCurrent,
       "jnxPMCurTecCurrent": jnxPMCurTecCurrent,
       "jnxPMCurMinTecCurrent": jnxPMCurMinTecCurrent,
       "jnxPMCurMaxTecCurrent": jnxPMCurMaxTecCurrent,
       "jnxPMCurAvgTecCurrent": jnxPMCurAvgTecCurrent,
       "jnxPMCurResidualDispersion": jnxPMCurResidualDispersion,
       "jnxPMCurMinResidualDispersion": jnxPMCurMinResidualDispersion,
       "jnxPMCurMaxResidualDispersion": jnxPMCurMaxResidualDispersion,
       "jnxPMCurAvgResidualDispersion": jnxPMCurAvgResidualDispersion,
       "jnxPMCurLevelHistogram": jnxPMCurLevelHistogram,
       "jnxPMCurMinLevelHistogram": jnxPMCurMinLevelHistogram,
       "jnxPMCurMaxLevelHistogram": jnxPMCurMaxLevelHistogram,
       "jnxPMCurAvgLevelHistogram": jnxPMCurAvgLevelHistogram,
       "jnxPMCurLaserFrequencyError": jnxPMCurLaserFrequencyError,
       "jnxPMCurMinLaserFrequencyError": jnxPMCurMinLaserFrequencyError,
       "jnxPMCurMaxLaserFrequencyError": jnxPMCurMaxLaserFrequencyError,
       "jnxPMCurAvgLaserFrequencyError": jnxPMCurAvgLaserFrequencyError,
       "jnxPMCurFECCorrectedErrorsMantissa": jnxPMCurFECCorrectedErrorsMantissa,
       "jnxPMCurFECCorrectedErrorsExponent": jnxPMCurFECCorrectedErrorsExponent,
       "jnxPMCurMinFECCorrectedErrorsMantissa": jnxPMCurMinFECCorrectedErrorsMantissa,
       "jnxPMCurMinFECCorrectedErrorsExponent": jnxPMCurMinFECCorrectedErrorsExponent,
       "jnxPMCurMaxFECCorrectedErrorsMantissa": jnxPMCurMaxFECCorrectedErrorsMantissa,
       "jnxPMCurMaxFECCorrectedErrorsExponent": jnxPMCurMaxFECCorrectedErrorsExponent,
       "jnxPMCurAvgFECCorrectedErrorsMantissa": jnxPMCurAvgFECCorrectedErrorsMantissa,
       "jnxPMCurAvgFECCorrectedErrorsExponent": jnxPMCurAvgFECCorrectedErrorsExponent,
       "jnxPMCurFECUCorrectedWordsMantissa": jnxPMCurFECUCorrectedWordsMantissa,
       "jnxPMCurFECUCorrectedWordsExponent": jnxPMCurFECUCorrectedWordsExponent,
       "jnxPMCurMinFECUCorrectedWordsMantissa": jnxPMCurMinFECUCorrectedWordsMantissa,
       "jnxPMCurMinFECUCorrectedWordsExponent": jnxPMCurMinFECUCorrectedWordsExponent,
       "jnxPMCurMaxFECUCorrectedWordsMantissa": jnxPMCurMaxFECUCorrectedWordsMantissa,
       "jnxPMCurMaxFECUCorrectedWordsExponent": jnxPMCurMaxFECUCorrectedWordsExponent,
       "jnxPMCurAvgFECUCorrectedWordsMantissa": jnxPMCurAvgFECUCorrectedWordsMantissa,
       "jnxPMCurAvgFECUCorrectedWordsExponent": jnxPMCurAvgFECUCorrectedWordsExponent,
       "jnxOpticsPMIntervalTable": jnxOpticsPMIntervalTable,
       "jnxOpticsPMIntervalEntry": jnxOpticsPMIntervalEntry,
       "jnxOpticsPMIntervalNumber": jnxOpticsPMIntervalNumber,
       "jnxPMIntMinChromaticDispersion": jnxPMIntMinChromaticDispersion,
       "jnxPMIntMaxChromaticDispersion": jnxPMIntMaxChromaticDispersion,
       "jnxPMIntAvgChromaticDispersion": jnxPMIntAvgChromaticDispersion,
       "jnxPMIntMinDiffGroupDelay": jnxPMIntMinDiffGroupDelay,
       "jnxPMIntMaxDiffGroupDelay": jnxPMIntMaxDiffGroupDelay,
       "jnxPMIntAvgDiffGroupDelay": jnxPMIntAvgDiffGroupDelay,
       "jnxPMIntMinPolarState": jnxPMIntMinPolarState,
       "jnxPMIntMaxPolarState": jnxPMIntMaxPolarState,
       "jnxPMIntAvgPolarState": jnxPMIntAvgPolarState,
       "jnxPMIntMinPolarDependentLoss": jnxPMIntMinPolarDependentLoss,
       "jnxPMIntMaxPolarDependentLoss": jnxPMIntMaxPolarDependentLoss,
       "jnxPMIntAvgPolarDependentLoss": jnxPMIntAvgPolarDependentLoss,
       "jnxPMIntMinQ": jnxPMIntMinQ,
       "jnxPMIntMaxQ": jnxPMIntMaxQ,
       "jnxPMIntAvgQ": jnxPMIntAvgQ,
       "jnxPMIntMinSNR": jnxPMIntMinSNR,
       "jnxPMIntMaxSNR": jnxPMIntMaxSNR,
       "jnxPMIntAvgSNR": jnxPMIntAvgSNR,
       "jnxPMIntMinTxOutputPower": jnxPMIntMinTxOutputPower,
       "jnxPMIntMaxTxOutputPower": jnxPMIntMaxTxOutputPower,
       "jnxPMIntAvgTxOutputPower": jnxPMIntAvgTxOutputPower,
       "jnxPMIntMinRxInputPower": jnxPMIntMinRxInputPower,
       "jnxPMIntMaxRxInputPower": jnxPMIntMaxRxInputPower,
       "jnxPMIntAvgRxInputPower": jnxPMIntAvgRxInputPower,
       "jnxPMIntTimeStamp": jnxPMIntTimeStamp,
       "jnxPMIntSuspectedFlag": jnxPMIntSuspectedFlag,
       "jnxPMIntSuspectReason": jnxPMIntSuspectReason,
       "jnxPMIntMinTxLaserBiasCurrent": jnxPMIntMinTxLaserBiasCurrent,
       "jnxPMIntMaxTxLaserBiasCurrent": jnxPMIntMaxTxLaserBiasCurrent,
       "jnxPMIntAvgTxLaserBiasCurrent": jnxPMIntAvgTxLaserBiasCurrent,
       "jnxPMIntMinTemperature": jnxPMIntMinTemperature,
       "jnxPMIntMaxTemperature": jnxPMIntMaxTemperature,
       "jnxPMIntAvgTemperature": jnxPMIntAvgTemperature,
       "jnxPMIntMinCarFreqOffset": jnxPMIntMinCarFreqOffset,
       "jnxPMIntMaxCarFreqOffset": jnxPMIntMaxCarFreqOffset,
       "jnxPMIntAvgCarFreqOffset": jnxPMIntAvgCarFreqOffset,
       "jnxPMIntMinRxLaserBiasCurrent": jnxPMIntMinRxLaserBiasCurrent,
       "jnxPMIntMaxRxLaserBiasCurrent": jnxPMIntMaxRxLaserBiasCurrent,
       "jnxPMIntAvgRxLaserBiasCurrent": jnxPMIntAvgRxLaserBiasCurrent,
       "jnxPMIntMinTecCurrent": jnxPMIntMinTecCurrent,
       "jnxPMIntMaxTecCurrent": jnxPMIntMaxTecCurrent,
       "jnxPMIntAvgTecCurrent": jnxPMIntAvgTecCurrent,
       "jnxPMIntMinResidualDispersion": jnxPMIntMinResidualDispersion,
       "jnxPMIntMaxResidualDispersion": jnxPMIntMaxResidualDispersion,
       "jnxPMIntAvgResidualDispersion": jnxPMIntAvgResidualDispersion,
       "jnxPMIntMinLevelHistogram": jnxPMIntMinLevelHistogram,
       "jnxPMIntMaxLevelHistogram": jnxPMIntMaxLevelHistogram,
       "jnxPMIntAvgLevelHistogram": jnxPMIntAvgLevelHistogram,
       "jnxPMIntMinLaserFrequencyError": jnxPMIntMinLaserFrequencyError,
       "jnxPMIntMaxLaserFrequencyError": jnxPMIntMaxLaserFrequencyError,
       "jnxPMIntAvgLaserFrequencyError": jnxPMIntAvgLaserFrequencyError,
       "jnxPMIntMinFECCorrectedErrorsMantissa": jnxPMIntMinFECCorrectedErrorsMantissa,
       "jnxPMIntMinFECCorrectedErrorsExponent": jnxPMIntMinFECCorrectedErrorsExponent,
       "jnxPMIntMaxFECCorrectedErrorsMantissa": jnxPMIntMaxFECCorrectedErrorsMantissa,
       "jnxPMIntMaxFECCorrectedErrorsExponent": jnxPMIntMaxFECCorrectedErrorsExponent,
       "jnxPMIntAvgFECCorrectedErrorsMantissa": jnxPMIntAvgFECCorrectedErrorsMantissa,
       "jnxPMIntAvgFECCorrectedErrorsExponent": jnxPMIntAvgFECCorrectedErrorsExponent,
       "jnxPMIntMinFECUCorrectedWordsMantissa": jnxPMIntMinFECUCorrectedWordsMantissa,
       "jnxPMIntMinFECUCorrectedWordsExponent": jnxPMIntMinFECUCorrectedWordsExponent,
       "jnxPMIntMaxFECUCorrectedWordsMantissa": jnxPMIntMaxFECUCorrectedWordsMantissa,
       "jnxPMIntMaxFECUCorrectedWordsExponent": jnxPMIntMaxFECUCorrectedWordsExponent,
       "jnxPMIntAvgFECUCorrectedWordsMantissa": jnxPMIntAvgFECUCorrectedWordsMantissa,
       "jnxPMIntAvgFECUCorrectedWordsExponent": jnxPMIntAvgFECUCorrectedWordsExponent,
       "jnxOpticsPMDayTable": jnxOpticsPMDayTable,
       "jnxOpticsPMDayEntry": jnxOpticsPMDayEntry,
       "jnxOpticsPMDayIndex": jnxOpticsPMDayIndex,
       "jnxPMDayMinChromaticDispersion": jnxPMDayMinChromaticDispersion,
       "jnxPMDayMaxChromaticDispersion": jnxPMDayMaxChromaticDispersion,
       "jnxPMDayAvgChromaticDispersion": jnxPMDayAvgChromaticDispersion,
       "jnxPMDayMinDiffGroupDelay": jnxPMDayMinDiffGroupDelay,
       "jnxPMDayMaxDiffGroupDelay": jnxPMDayMaxDiffGroupDelay,
       "jnxPMDayAvgDiffGroupDelay": jnxPMDayAvgDiffGroupDelay,
       "jnxPMDayMinPolarState": jnxPMDayMinPolarState,
       "jnxPMDayMaxPolarState": jnxPMDayMaxPolarState,
       "jnxPMDayAvgPolarState": jnxPMDayAvgPolarState,
       "jnxPMDayMinPolarDependentLoss": jnxPMDayMinPolarDependentLoss,
       "jnxPMDayMaxPolarDependentLoss": jnxPMDayMaxPolarDependentLoss,
       "jnxPMDayAvgPolarDependentLoss": jnxPMDayAvgPolarDependentLoss,
       "jnxPMDayMinQ": jnxPMDayMinQ,
       "jnxPMDayMaxQ": jnxPMDayMaxQ,
       "jnxPMDayAvgQ": jnxPMDayAvgQ,
       "jnxPMDayMinSNR": jnxPMDayMinSNR,
       "jnxPMDayMaxSNR": jnxPMDayMaxSNR,
       "jnxPMDayAvgSNR": jnxPMDayAvgSNR,
       "jnxPMDayMinTxOutputPower": jnxPMDayMinTxOutputPower,
       "jnxPMDayMaxTxOutputPower": jnxPMDayMaxTxOutputPower,
       "jnxPMDayAvgTxOutputPower": jnxPMDayAvgTxOutputPower,
       "jnxPMDayMinRxInputPower": jnxPMDayMinRxInputPower,
       "jnxPMDayMaxRxInputPower": jnxPMDayMaxRxInputPower,
       "jnxPMDayAvgRxInputPower": jnxPMDayAvgRxInputPower,
       "jnxPMDayTimeStamp": jnxPMDayTimeStamp,
       "jnxPMDaySuspectedFlag": jnxPMDaySuspectedFlag,
       "jnxPMDaySuspectReason": jnxPMDaySuspectReason,
       "jnxPMDayMinTxLaserBiasCurrent": jnxPMDayMinTxLaserBiasCurrent,
       "jnxPMDayMaxTxLaserBiasCurrent": jnxPMDayMaxTxLaserBiasCurrent,
       "jnxPMDayAvgTxLaserBiasCurrent": jnxPMDayAvgTxLaserBiasCurrent,
       "jnxPMDayMinTemperature": jnxPMDayMinTemperature,
       "jnxPMDayMaxTemperature": jnxPMDayMaxTemperature,
       "jnxPMDayAvgTemperature": jnxPMDayAvgTemperature,
       "jnxPMDayMinCarFreqOffset": jnxPMDayMinCarFreqOffset,
       "jnxPMDayMaxCarFreqOffset": jnxPMDayMaxCarFreqOffset,
       "jnxPMDayAvgCarFreqOffset": jnxPMDayAvgCarFreqOffset,
       "jnxPMDayMinRxLaserBiasCurrent": jnxPMDayMinRxLaserBiasCurrent,
       "jnxPMDayMaxRxLaserBiasCurrent": jnxPMDayMaxRxLaserBiasCurrent,
       "jnxPMDayAvgRxLaserBiasCurrent": jnxPMDayAvgRxLaserBiasCurrent,
       "jnxPMDayMinTecCurrent": jnxPMDayMinTecCurrent,
       "jnxPMDayMaxTecCurrent": jnxPMDayMaxTecCurrent,
       "jnxPMDayAvgTecCurrent": jnxPMDayAvgTecCurrent,
       "jnxPMDayMinResidualDispersion": jnxPMDayMinResidualDispersion,
       "jnxPMDayMaxResidualDispersion": jnxPMDayMaxResidualDispersion,
       "jnxPMDayAvgResidualDispersion": jnxPMDayAvgResidualDispersion,
       "jnxPMDayMinLevelHistogram": jnxPMDayMinLevelHistogram,
       "jnxPMDayMaxLevelHistogram": jnxPMDayMaxLevelHistogram,
       "jnxPMDayAvgLevelHistogram": jnxPMDayAvgLevelHistogram,
       "jnxPMDayMinLaserFrequencyError": jnxPMDayMinLaserFrequencyError,
       "jnxPMDayMaxLaserFrequencyError": jnxPMDayMaxLaserFrequencyError,
       "jnxPMDayAvgLaserFrequencyError": jnxPMDayAvgLaserFrequencyError,
       "jnxPMDayMinFECCorrectedErrorsMantissa": jnxPMDayMinFECCorrectedErrorsMantissa,
       "jnxPMDayMinFECCorrectedErrorsExponent": jnxPMDayMinFECCorrectedErrorsExponent,
       "jnxPMDayMaxFECCorrectedErrorsMantissa": jnxPMDayMaxFECCorrectedErrorsMantissa,
       "jnxPMDayMaxFECCorrectedErrorsExponent": jnxPMDayMaxFECCorrectedErrorsExponent,
       "jnxPMDayAvgFECCorrectedErrorsMantissa": jnxPMDayAvgFECCorrectedErrorsMantissa,
       "jnxPMDayAvgFECCorrectedErrorsExponent": jnxPMDayAvgFECCorrectedErrorsExponent,
       "jnxPMDayMinFECUCorrectedWordsMantissa": jnxPMDayMinFECUCorrectedWordsMantissa,
       "jnxPMDayMinFECUCorrectedWordsExponent": jnxPMDayMinFECUCorrectedWordsExponent,
       "jnxPMDayMaxFECUCorrectedWordsMantissa": jnxPMDayMaxFECUCorrectedWordsMantissa,
       "jnxPMDayMaxFECUCorrectedWordsExponent": jnxPMDayMaxFECUCorrectedWordsExponent,
       "jnxPMDayAvgFECUCorrectedWordsMantissa": jnxPMDayAvgFECUCorrectedWordsMantissa,
       "jnxPMDayAvgFECUCorrectedWordsExponent": jnxPMDayAvgFECUCorrectedWordsExponent,
       "jnxOpticsOTIfPMFECCurrentTable": jnxOpticsOTIfPMFECCurrentTable,
       "jnxOpticsOTIfPMFECCurrentEntry": jnxOpticsOTIfPMFECCurrentEntry,
       "jnxOpticsOTIfPMFECCurrentSuspectedFlag": jnxOpticsOTIfPMFECCurrentSuspectedFlag,
       "jnxOpticsOTIfPMCurrentFECCorrectedErr": jnxOpticsOTIfPMCurrentFECCorrectedErr,
       "jnxOpticsOTIfPMCurrentFECUncorrectedWords": jnxOpticsOTIfPMCurrentFECUncorrectedWords,
       "jnxOpticsOTIfPMCurrentFECBERMantissa": jnxOpticsOTIfPMCurrentFECBERMantissa,
       "jnxOpticsOTIfPMCurrentFECBERExponent": jnxOpticsOTIfPMCurrentFECBERExponent,
       "jnxOpticsOTIfPMCurrentFECMinBERMantissa": jnxOpticsOTIfPMCurrentFECMinBERMantissa,
       "jnxOpticsOTIfPMCurrentFECMinBERExponent": jnxOpticsOTIfPMCurrentFECMinBERExponent,
       "jnxOpticsOTIfPMCurrentFECMaxBERMantissa": jnxOpticsOTIfPMCurrentFECMaxBERMantissa,
       "jnxOpticsOTIfPMCurrentFECMaxBERExponent": jnxOpticsOTIfPMCurrentFECMaxBERExponent,
       "jnxOpticsOTIfPMCurrentFECAvgBERMantissa": jnxOpticsOTIfPMCurrentFECAvgBERMantissa,
       "jnxOpticsOTIfPMCurrentFECAvgBERExponent": jnxOpticsOTIfPMCurrentFECAvgBERExponent,
       "jnxOpticsOTIfPMCurrentFECElapsedTime": jnxOpticsOTIfPMCurrentFECElapsedTime,
       "jnxOpticsOTIfPMFECCurSuspectReason": jnxOpticsOTIfPMFECCurSuspectReason,
       "jnxOpticsOTIfPMFECIntervalTable": jnxOpticsOTIfPMFECIntervalTable,
       "jnxOpticsOTIfPMFECIntervalEntry": jnxOpticsOTIfPMFECIntervalEntry,
       "jnxOpticsOTIfPMFECIntervalNumber": jnxOpticsOTIfPMFECIntervalNumber,
       "jnxOpticsOTIfPMFECIntervalSuspectedFlag": jnxOpticsOTIfPMFECIntervalSuspectedFlag,
       "jnxOpticsOTIfPMIntervalFECCorrectedErr": jnxOpticsOTIfPMIntervalFECCorrectedErr,
       "jnxOpticsOTIfPMIntervalFECUncorrectedWords": jnxOpticsOTIfPMIntervalFECUncorrectedWords,
       "jnxOpticsOTIfPMIntervalMinFECBERMantissa": jnxOpticsOTIfPMIntervalMinFECBERMantissa,
       "jnxOpticsOTIfPMIntervalMinFECBERExponent": jnxOpticsOTIfPMIntervalMinFECBERExponent,
       "jnxOpticsOTIfPMIntervalMaxFECBERMantissa": jnxOpticsOTIfPMIntervalMaxFECBERMantissa,
       "jnxOpticsOTIfPMIntervalMaxFECBERExponent": jnxOpticsOTIfPMIntervalMaxFECBERExponent,
       "jnxOpticsOTIfPMIntervalAvgFECBERMantissa": jnxOpticsOTIfPMIntervalAvgFECBERMantissa,
       "jnxOpticsOTIfPMIntervalAvgFECBERExponent": jnxOpticsOTIfPMIntervalAvgFECBERExponent,
       "jnxOpticsOTIfPMFECIntervalTimeStamp": jnxOpticsOTIfPMFECIntervalTimeStamp,
       "jnxOpticsOTIfPMFECIntSuspectReason": jnxOpticsOTIfPMFECIntSuspectReason,
       "jnxOpticsOTIfPMFECCurrentDayTable": jnxOpticsOTIfPMFECCurrentDayTable,
       "jnxOpticsOTIfPMFECCurrentDayEntry": jnxOpticsOTIfPMFECCurrentDayEntry,
       "jnxOpticsOTIfPMFECCurrentDaySuspectedFlag": jnxOpticsOTIfPMFECCurrentDaySuspectedFlag,
       "jnxOpticsOTIfPMCurrentDayFECCorrectedErr": jnxOpticsOTIfPMCurrentDayFECCorrectedErr,
       "jnxOpticsOTIfPMCurrentDayFECUncorrectedWords": jnxOpticsOTIfPMCurrentDayFECUncorrectedWords,
       "jnxOpticsOTIfPMCurrentDayMinFECBERMantissa": jnxOpticsOTIfPMCurrentDayMinFECBERMantissa,
       "jnxOpticsOTIfPMCurrentDayMinFECBERExponent": jnxOpticsOTIfPMCurrentDayMinFECBERExponent,
       "jnxOpticsOTIfPMCurrentDayMaxFECBERMantissa": jnxOpticsOTIfPMCurrentDayMaxFECBERMantissa,
       "jnxOpticsOTIfPMCurrentDayMaxFECBERExponent": jnxOpticsOTIfPMCurrentDayMaxFECBERExponent,
       "jnxOpticsOTIfPMCurrentDayAvgFECBERMantissa": jnxOpticsOTIfPMCurrentDayAvgFECBERMantissa,
       "jnxOpticsOTIfPMCurrentDayAvgFECBERExponent": jnxOpticsOTIfPMCurrentDayAvgFECBERExponent,
       "jnxOpticsOTIfPMFECCurrentDayElapsedTime": jnxOpticsOTIfPMFECCurrentDayElapsedTime,
       "jnxOpticsOTIfPMFECCurDaySuspectReason": jnxOpticsOTIfPMFECCurDaySuspectReason,
       "jnxOpticsOTIfPMFECPrevDayTable": jnxOpticsOTIfPMFECPrevDayTable,
       "jnxOpticsOTIfPMFECPrevDayEntry": jnxOpticsOTIfPMFECPrevDayEntry,
       "jnxOpticsOTIfPMFECPrevDaySuspectedFlag": jnxOpticsOTIfPMFECPrevDaySuspectedFlag,
       "jnxOpticsOTIfPMPrevDayFECCorrectedErr": jnxOpticsOTIfPMPrevDayFECCorrectedErr,
       "jnxOpticsOTIfPMPrevDayFECUncorrectedWords": jnxOpticsOTIfPMPrevDayFECUncorrectedWords,
       "jnxOpticsOTIfPMPrevDayMinFECBERMantissa": jnxOpticsOTIfPMPrevDayMinFECBERMantissa,
       "jnxOpticsOTIfPMPrevDayMinFECBERExponent": jnxOpticsOTIfPMPrevDayMinFECBERExponent,
       "jnxOpticsOTIfPMPrevDayMaxFECBERMantissa": jnxOpticsOTIfPMPrevDayMaxFECBERMantissa,
       "jnxOpticsOTIfPMPrevDayMaxFECBERExponent": jnxOpticsOTIfPMPrevDayMaxFECBERExponent,
       "jnxOpticsOTIfPMPrevDayAvgFECBERMantissa": jnxOpticsOTIfPMPrevDayAvgFECBERMantissa,
       "jnxOpticsOTIfPMPrevDayAvgFECBERExponent": jnxOpticsOTIfPMPrevDayAvgFECBERExponent,
       "jnxOpticsOTIfPMFECPrevDayTimeStamp": jnxOpticsOTIfPMFECPrevDayTimeStamp,
       "jnxOpticsOTIfPMFECPrevDaySuspectReason": jnxOpticsOTIfPMFECPrevDaySuspectReason,
       "jnxOpticsOTIfPMFECConfigTable": jnxOpticsOTIfPMFECConfigTable,
       "jnxOpticsOTIfPMFECConfigEntry": jnxOpticsOTIfPMFECConfigEntry,
       "jnxOpticsOTIfPMFECValidIntervals": jnxOpticsOTIfPMFECValidIntervals,
       "jnxOpticsOTIfPM15MinPreFECBERMantissaThreshold": jnxOpticsOTIfPM15MinPreFECBERMantissaThreshold,
       "jnxOpticsOTIfPM15MinPreFECBERExponentThreshold": jnxOpticsOTIfPM15MinPreFECBERExponentThreshold,
       "jnxOpticsOTIfPM24HourPreFECBERMantissaThreshold": jnxOpticsOTIfPM24HourPreFECBERMantissaThreshold,
       "jnxOpticsOTIfPM24HourPreFECBERExponentThreshold": jnxOpticsOTIfPM24HourPreFECBERExponentThreshold,
       "jnxOpticsOTIfPMFECBEREnableTCA": jnxOpticsOTIfPMFECBEREnableTCA,
       "jnxIfOpticsPMCurrentTable": jnxIfOpticsPMCurrentTable,
       "jnxIfOpticsPMCurrentEntry": jnxIfOpticsPMCurrentEntry,
       "jnxIfOpticsPMCurrentLaneIndex": jnxIfOpticsPMCurrentLaneIndex,
       "jnxIfOpticsPMCurChromaticDispersion": jnxIfOpticsPMCurChromaticDispersion,
       "jnxIfOpticsPMCurDiffGroupDelay": jnxIfOpticsPMCurDiffGroupDelay,
       "jnxIfOpticsPMCurPolarizationState": jnxIfOpticsPMCurPolarizationState,
       "jnxIfOpticsPMCurPolarDepLoss": jnxIfOpticsPMCurPolarDepLoss,
       "jnxIfOpticsPMCurQ": jnxIfOpticsPMCurQ,
       "jnxIfOpticsPMCurSNR": jnxIfOpticsPMCurSNR,
       "jnxIfOpticsPMCurTxOutputPower": jnxIfOpticsPMCurTxOutputPower,
       "jnxIfOpticsPMCurRxInputPower": jnxIfOpticsPMCurRxInputPower,
       "jnxIfOpticsPMCurMinChromaticDispersion": jnxIfOpticsPMCurMinChromaticDispersion,
       "jnxIfOpticsPMCurMaxChromaticDispersion": jnxIfOpticsPMCurMaxChromaticDispersion,
       "jnxIfOpticsPMCurAvgChromaticDispersion": jnxIfOpticsPMCurAvgChromaticDispersion,
       "jnxIfOpticsPMCurMinDiffGroupDelay": jnxIfOpticsPMCurMinDiffGroupDelay,
       "jnxIfOpticsPMCurMaxDiffGroupDelay": jnxIfOpticsPMCurMaxDiffGroupDelay,
       "jnxIfOpticsPMCurAvgDiffGroupDelay": jnxIfOpticsPMCurAvgDiffGroupDelay,
       "jnxIfOpticsPMCurMinPolarState": jnxIfOpticsPMCurMinPolarState,
       "jnxIfOpticsPMCurMaxPolarState": jnxIfOpticsPMCurMaxPolarState,
       "jnxIfOpticsPMCurAvgPolarState": jnxIfOpticsPMCurAvgPolarState,
       "jnxIfOpticsPMCurMinPolarDepLoss": jnxIfOpticsPMCurMinPolarDepLoss,
       "jnxIfOpticsPMCurMaxPolarDepLoss": jnxIfOpticsPMCurMaxPolarDepLoss,
       "jnxIfOpticsPMCurAvgPolarDepLoss": jnxIfOpticsPMCurAvgPolarDepLoss,
       "jnxIfOpticsPMCurMinQ": jnxIfOpticsPMCurMinQ,
       "jnxIfOpticsPMCurMaxQ": jnxIfOpticsPMCurMaxQ,
       "jnxIfOpticsPMCurAvgQ": jnxIfOpticsPMCurAvgQ,
       "jnxIfOpticsPMCurMinSNR": jnxIfOpticsPMCurMinSNR,
       "jnxIfOpticsPMCurMaxSNR": jnxIfOpticsPMCurMaxSNR,
       "jnxIfOpticsPMCurAvgSNR": jnxIfOpticsPMCurAvgSNR,
       "jnxIfOpticsPMCurMinTxOutputPower": jnxIfOpticsPMCurMinTxOutputPower,
       "jnxIfOpticsPMCurMaxTxOutputPower": jnxIfOpticsPMCurMaxTxOutputPower,
       "jnxIfOpticsPMCurAvgTxOutputPower": jnxIfOpticsPMCurAvgTxOutputPower,
       "jnxIfOpticsPMCurMinRxInputPower": jnxIfOpticsPMCurMinRxInputPower,
       "jnxIfOpticsPMCurMaxRxInputPower": jnxIfOpticsPMCurMaxRxInputPower,
       "jnxIfOpticsPMCurAvgRxInputPower": jnxIfOpticsPMCurAvgRxInputPower,
       "jnxIfOpticsPMCurSuspectedFlag": jnxIfOpticsPMCurSuspectedFlag,
       "jnxIfOpticsPMCurSuspectReason": jnxIfOpticsPMCurSuspectReason,
       "jnxIfOpticsPMCurTxLaserBiasCurrent": jnxIfOpticsPMCurTxLaserBiasCurrent,
       "jnxIfOpticsPMCurMinTxLaserBiasCurrent": jnxIfOpticsPMCurMinTxLaserBiasCurrent,
       "jnxIfOpticsPMCurMaxTxLaserBiasCurrent": jnxIfOpticsPMCurMaxTxLaserBiasCurrent,
       "jnxIfOpticsPMCurAvgTxLaserBiasCurrent": jnxIfOpticsPMCurAvgTxLaserBiasCurrent,
       "jnxIfOpticsPMCurTemperature": jnxIfOpticsPMCurTemperature,
       "jnxIfOpticsPMCurMinTemperature": jnxIfOpticsPMCurMinTemperature,
       "jnxIfOpticsPMCurMaxTemperature": jnxIfOpticsPMCurMaxTemperature,
       "jnxIfOpticsPMCurAvgTemperature": jnxIfOpticsPMCurAvgTemperature,
       "jnxIfOpticsPMCurCarFreqOffset": jnxIfOpticsPMCurCarFreqOffset,
       "jnxIfOpticsPMCurMinCarFreqOffset": jnxIfOpticsPMCurMinCarFreqOffset,
       "jnxIfOpticsPMCurMaxCarFreqOffset": jnxIfOpticsPMCurMaxCarFreqOffset,
       "jnxIfOpticsPMCurAvgCarFreqOffset": jnxIfOpticsPMCurAvgCarFreqOffset,
       "jnxIfOpticsPMCurRxLaserBiasCurrent": jnxIfOpticsPMCurRxLaserBiasCurrent,
       "jnxIfOpticsPMCurMinRxLaserBiasCurrent": jnxIfOpticsPMCurMinRxLaserBiasCurrent,
       "jnxIfOpticsPMCurMaxRxLaserBiasCurrent": jnxIfOpticsPMCurMaxRxLaserBiasCurrent,
       "jnxIfOpticsPMCurAvgRxLaserBiasCurrent": jnxIfOpticsPMCurAvgRxLaserBiasCurrent,
       "jnxIfOpticsPMCurTecCurrent": jnxIfOpticsPMCurTecCurrent,
       "jnxIfOpticsPMCurMinTecCurrent": jnxIfOpticsPMCurMinTecCurrent,
       "jnxIfOpticsPMCurMaxTecCurrent": jnxIfOpticsPMCurMaxTecCurrent,
       "jnxIfOpticsPMCurAvgTecCurrent": jnxIfOpticsPMCurAvgTecCurrent,
       "jnxIfOpticsPMCurResidualDispersion": jnxIfOpticsPMCurResidualDispersion,
       "jnxIfOpticsPMCurMinResidualDispersion": jnxIfOpticsPMCurMinResidualDispersion,
       "jnxIfOpticsPMCurMaxResidualDispersion": jnxIfOpticsPMCurMaxResidualDispersion,
       "jnxIfOpticsPMCurAvgResidualDispersion": jnxIfOpticsPMCurAvgResidualDispersion,
       "jnxIfOpticsPMCurLevelHistogram": jnxIfOpticsPMCurLevelHistogram,
       "jnxIfOpticsPMCurMinLevelHistogram": jnxIfOpticsPMCurMinLevelHistogram,
       "jnxIfOpticsPMCurMaxLevelHistogram": jnxIfOpticsPMCurMaxLevelHistogram,
       "jnxIfOpticsPMCurAvgLevelHistogram": jnxIfOpticsPMCurAvgLevelHistogram,
       "jnxIfOpticsPMCurLaserFrequencyError": jnxIfOpticsPMCurLaserFrequencyError,
       "jnxIfOpticsPMCurMinLaserFrequencyError": jnxIfOpticsPMCurMinLaserFrequencyError,
       "jnxIfOpticsPMCurMaxLaserFrequencyError": jnxIfOpticsPMCurMaxLaserFrequencyError,
       "jnxIfOpticsPMCurAvgLaserFrequencyError": jnxIfOpticsPMCurAvgLaserFrequencyError,
       "jnxIfOpticsPMCurFECCorrectedErrorsMantissa": jnxIfOpticsPMCurFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMCurFECCorrectedErrorsExponent": jnxIfOpticsPMCurFECCorrectedErrorsExponent,
       "jnxIfOpticsPMCurMinFECCorrectedErrorsMantissa": jnxIfOpticsPMCurMinFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMCurMinFECCorrectedErrorsExponent": jnxIfOpticsPMCurMinFECCorrectedErrorsExponent,
       "jnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa": jnxIfOpticsPMCurMaxFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMCurMaxFECCorrectedErrorsExponent": jnxIfOpticsPMCurMaxFECCorrectedErrorsExponent,
       "jnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa": jnxIfOpticsPMCurAvgFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMCurAvgFECCorrectedErrorsExponent": jnxIfOpticsPMCurAvgFECCorrectedErrorsExponent,
       "jnxIfOpticsPMCurFECUCorrectedWordsMantissa": jnxIfOpticsPMCurFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMCurFECUCorrectedWordsExponent": jnxIfOpticsPMCurFECUCorrectedWordsExponent,
       "jnxIfOpticsPMCurMinFECUCorrectedWordsMantissa": jnxIfOpticsPMCurMinFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMCurMinFECUCorrectedWordsExponent": jnxIfOpticsPMCurMinFECUCorrectedWordsExponent,
       "jnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa": jnxIfOpticsPMCurMaxFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMCurMaxFECUCorrectedWordsExponent": jnxIfOpticsPMCurMaxFECUCorrectedWordsExponent,
       "jnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa": jnxIfOpticsPMCurAvgFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMCurAvgFECUCorrectedWordsExponent": jnxIfOpticsPMCurAvgFECUCorrectedWordsExponent,
       "jnxIfOpticsPMIntervalTable": jnxIfOpticsPMIntervalTable,
       "jnxIfOpticsPMIntervalEntry": jnxIfOpticsPMIntervalEntry,
       "jnxIfOpticsPMIntervalLaneIndex": jnxIfOpticsPMIntervalLaneIndex,
       "jnxIfOpticsPMIntervalNumber": jnxIfOpticsPMIntervalNumber,
       "jnxIfOpticsPMIntMinChromaticDispersion": jnxIfOpticsPMIntMinChromaticDispersion,
       "jnxIfOpticsPMIntMaxChromaticDispersion": jnxIfOpticsPMIntMaxChromaticDispersion,
       "jnxIfOpticsPMIntAvgChromaticDispersion": jnxIfOpticsPMIntAvgChromaticDispersion,
       "jnxIfOpticsPMIntMinDiffGroupDelay": jnxIfOpticsPMIntMinDiffGroupDelay,
       "jnxIfOpticsPMIntMaxDiffGroupDelay": jnxIfOpticsPMIntMaxDiffGroupDelay,
       "jnxIfOpticsPMIntAvgDiffGroupDelay": jnxIfOpticsPMIntAvgDiffGroupDelay,
       "jnxIfOpticsPMIntMinPolarState": jnxIfOpticsPMIntMinPolarState,
       "jnxIfOpticsPMIntMaxPolarState": jnxIfOpticsPMIntMaxPolarState,
       "jnxIfOpticsPMIntAvgPolarState": jnxIfOpticsPMIntAvgPolarState,
       "jnxIfOpticsPMIntMinPolarDependentLoss": jnxIfOpticsPMIntMinPolarDependentLoss,
       "jnxIfOpticsPMIntMaxPolarDependentLoss": jnxIfOpticsPMIntMaxPolarDependentLoss,
       "jnxIfOpticsPMIntAvgPolarDependentLoss": jnxIfOpticsPMIntAvgPolarDependentLoss,
       "jnxIfOpticsPMIntMinQ": jnxIfOpticsPMIntMinQ,
       "jnxIfOpticsPMIntMaxQ": jnxIfOpticsPMIntMaxQ,
       "jnxIfOpticsPMIntAvgQ": jnxIfOpticsPMIntAvgQ,
       "jnxIfOpticsPMIntMinSNR": jnxIfOpticsPMIntMinSNR,
       "jnxIfOpticsPMIntMaxSNR": jnxIfOpticsPMIntMaxSNR,
       "jnxIfOpticsPMIntAvgSNR": jnxIfOpticsPMIntAvgSNR,
       "jnxIfOpticsPMIntMinTxOutputPower": jnxIfOpticsPMIntMinTxOutputPower,
       "jnxIfOpticsPMIntMaxTxOutputPower": jnxIfOpticsPMIntMaxTxOutputPower,
       "jnxIfOpticsPMIntAvgTxOutputPower": jnxIfOpticsPMIntAvgTxOutputPower,
       "jnxIfOpticsPMIntMinRxInputPower": jnxIfOpticsPMIntMinRxInputPower,
       "jnxIfOpticsPMIntMaxRxInputPower": jnxIfOpticsPMIntMaxRxInputPower,
       "jnxIfOpticsPMIntAvgRxInputPower": jnxIfOpticsPMIntAvgRxInputPower,
       "jnxIfOpticsPMIntTimeStamp": jnxIfOpticsPMIntTimeStamp,
       "jnxIfOpticsPMIntSuspectedFlag": jnxIfOpticsPMIntSuspectedFlag,
       "jnxIfOpticsPMIntSuspectReason": jnxIfOpticsPMIntSuspectReason,
       "jnxIfOpticsPMIntMinTxLaserBiasCurrent": jnxIfOpticsPMIntMinTxLaserBiasCurrent,
       "jnxIfOpticsPMIntMaxTxLaserBiasCurrent": jnxIfOpticsPMIntMaxTxLaserBiasCurrent,
       "jnxIfOpticsPMIntAvgTxLaserBiasCurrent": jnxIfOpticsPMIntAvgTxLaserBiasCurrent,
       "jnxIfOpticsPMIntMinTemperature": jnxIfOpticsPMIntMinTemperature,
       "jnxIfOpticsPMIntMaxTemperature": jnxIfOpticsPMIntMaxTemperature,
       "jnxIfOpticsPMIntAvgTemperature": jnxIfOpticsPMIntAvgTemperature,
       "jnxIfOpticsPMIntMinCarFreqOffset": jnxIfOpticsPMIntMinCarFreqOffset,
       "jnxIfOpticsPMIntMaxCarFreqOffset": jnxIfOpticsPMIntMaxCarFreqOffset,
       "jnxIfOpticsPMIntAvgCarFreqOffset": jnxIfOpticsPMIntAvgCarFreqOffset,
       "jnxIfOpticsPMIntMinRxLaserBiasCurrent": jnxIfOpticsPMIntMinRxLaserBiasCurrent,
       "jnxIfOpticsPMIntMaxRxLaserBiasCurrent": jnxIfOpticsPMIntMaxRxLaserBiasCurrent,
       "jnxIfOpticsPMIntAvgRxLaserBiasCurrent": jnxIfOpticsPMIntAvgRxLaserBiasCurrent,
       "jnxIfOpticsPMIntMinTecCurrent": jnxIfOpticsPMIntMinTecCurrent,
       "jnxIfOpticsPMIntMaxTecCurrent": jnxIfOpticsPMIntMaxTecCurrent,
       "jnxIfOpticsPMIntAvgTecCurrent": jnxIfOpticsPMIntAvgTecCurrent,
       "jnxIfOpticsPMIntMinResidualDispersion": jnxIfOpticsPMIntMinResidualDispersion,
       "jnxIfOpticsPMIntMaxResidualDispersion": jnxIfOpticsPMIntMaxResidualDispersion,
       "jnxIfOpticsPMIntAvgResidualDispersion": jnxIfOpticsPMIntAvgResidualDispersion,
       "jnxIfOpticsPMIntMinLevelHistogram": jnxIfOpticsPMIntMinLevelHistogram,
       "jnxIfOpticsPMIntMaxLevelHistogram": jnxIfOpticsPMIntMaxLevelHistogram,
       "jnxIfOpticsPMIntAvgLevelHistogram": jnxIfOpticsPMIntAvgLevelHistogram,
       "jnxIfOpticsPMIntMinLaserFrequencyError": jnxIfOpticsPMIntMinLaserFrequencyError,
       "jnxIfOpticsPMIntMaxLaserFrequencyError": jnxIfOpticsPMIntMaxLaserFrequencyError,
       "jnxIfOpticsPMIntAvgLaserFrequencyError": jnxIfOpticsPMIntAvgLaserFrequencyError,
       "jnxIfOpticsPMIntMinFECCorrectedErrorsMantissa": jnxIfOpticsPMIntMinFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMIntMinFECCorrectedErrorsExponent": jnxIfOpticsPMIntMinFECCorrectedErrorsExponent,
       "jnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa": jnxIfOpticsPMIntMaxFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMIntMaxFECCorrectedErrorsExponent": jnxIfOpticsPMIntMaxFECCorrectedErrorsExponent,
       "jnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa": jnxIfOpticsPMIntAvgFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMIntAvgFECCorrectedErrorsExponent": jnxIfOpticsPMIntAvgFECCorrectedErrorsExponent,
       "jnxIfOpticsPMIntMinFECUCorrectedWordsMantissa": jnxIfOpticsPMIntMinFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMIntMinFECUCorrectedWordsExponent": jnxIfOpticsPMIntMinFECUCorrectedWordsExponent,
       "jnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa": jnxIfOpticsPMIntMaxFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMIntMaxFECUCorrectedWordsExponent": jnxIfOpticsPMIntMaxFECUCorrectedWordsExponent,
       "jnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa": jnxIfOpticsPMIntAvgFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMIntAvgFECUCorrectedWordsExponent": jnxIfOpticsPMIntAvgFECUCorrectedWordsExponent,
       "jnxIfOpticsPMDayTable": jnxIfOpticsPMDayTable,
       "jnxIfOpticsPMDayEntry": jnxIfOpticsPMDayEntry,
       "jnxIfOpticsPMDayLaneIndex": jnxIfOpticsPMDayLaneIndex,
       "jnxIfOpticsPMDayIndex": jnxIfOpticsPMDayIndex,
       "jnxIfOpticsPMDayMinChromaticDispersion": jnxIfOpticsPMDayMinChromaticDispersion,
       "jnxIfOpticsPMDayMaxChromaticDispersion": jnxIfOpticsPMDayMaxChromaticDispersion,
       "jnxIfOpticsPMDayAvgChromaticDispersion": jnxIfOpticsPMDayAvgChromaticDispersion,
       "jnxIfOpticsPMDayMinDiffGroupDelay": jnxIfOpticsPMDayMinDiffGroupDelay,
       "jnxIfOpticsPMDayMaxDiffGroupDelay": jnxIfOpticsPMDayMaxDiffGroupDelay,
       "jnxIfOpticsPMDayAvgDiffGroupDelay": jnxIfOpticsPMDayAvgDiffGroupDelay,
       "jnxIfOpticsPMDayMinPolarState": jnxIfOpticsPMDayMinPolarState,
       "jnxIfOpticsPMDayMaxPolarState": jnxIfOpticsPMDayMaxPolarState,
       "jnxIfOpticsPMDayAvgPolarState": jnxIfOpticsPMDayAvgPolarState,
       "jnxIfOpticsPMDayMinPolarDependentLoss": jnxIfOpticsPMDayMinPolarDependentLoss,
       "jnxIfOpticsPMDayMaxPolarDependentLoss": jnxIfOpticsPMDayMaxPolarDependentLoss,
       "jnxIfOpticsPMDayAvgPolarDependentLoss": jnxIfOpticsPMDayAvgPolarDependentLoss,
       "jnxIfOpticsPMDayMinQ": jnxIfOpticsPMDayMinQ,
       "jnxIfOpticsPMDayMaxQ": jnxIfOpticsPMDayMaxQ,
       "jnxIfOpticsPMDayAvgQ": jnxIfOpticsPMDayAvgQ,
       "jnxIfOpticsPMDayMinSNR": jnxIfOpticsPMDayMinSNR,
       "jnxIfOpticsPMDayMaxSNR": jnxIfOpticsPMDayMaxSNR,
       "jnxIfOpticsPMDayAvgSNR": jnxIfOpticsPMDayAvgSNR,
       "jnxIfOpticsPMDayMinTxOutputPower": jnxIfOpticsPMDayMinTxOutputPower,
       "jnxIfOpticsPMDayMaxTxOutputPower": jnxIfOpticsPMDayMaxTxOutputPower,
       "jnxIfOpticsPMDayAvgTxOutputPower": jnxIfOpticsPMDayAvgTxOutputPower,
       "jnxIfOpticsPMDayMinRxInputPower": jnxIfOpticsPMDayMinRxInputPower,
       "jnxIfOpticsPMDayMaxRxInputPower": jnxIfOpticsPMDayMaxRxInputPower,
       "jnxIfOpticsPMDayAvgRxInputPower": jnxIfOpticsPMDayAvgRxInputPower,
       "jnxIfOpticsPMDayTimeStamp": jnxIfOpticsPMDayTimeStamp,
       "jnxIfOpticsPMDaySuspectedFlag": jnxIfOpticsPMDaySuspectedFlag,
       "jnxIfOpticsPMDaySuspectReason": jnxIfOpticsPMDaySuspectReason,
       "jnxIfOpticsPMDayMinTxLaserBiasCurrent": jnxIfOpticsPMDayMinTxLaserBiasCurrent,
       "jnxIfOpticsPMDayMaxTxLaserBiasCurrent": jnxIfOpticsPMDayMaxTxLaserBiasCurrent,
       "jnxIfOpticsPMDayAvgTxLaserBiasCurrent": jnxIfOpticsPMDayAvgTxLaserBiasCurrent,
       "jnxIfOpticsPMDayMinTemperature": jnxIfOpticsPMDayMinTemperature,
       "jnxIfOpticsPMDayMaxTemperature": jnxIfOpticsPMDayMaxTemperature,
       "jnxIfOpticsPMDayAvgTemperature": jnxIfOpticsPMDayAvgTemperature,
       "jnxIfOpticsPMDayMinCarFreqOffset": jnxIfOpticsPMDayMinCarFreqOffset,
       "jnxIfOpticsPMDayMaxCarFreqOffset": jnxIfOpticsPMDayMaxCarFreqOffset,
       "jnxIfOpticsPMDayAvgCarFreqOffset": jnxIfOpticsPMDayAvgCarFreqOffset,
       "jnxIfOpticsPMDayMinRxLaserBiasCurrent": jnxIfOpticsPMDayMinRxLaserBiasCurrent,
       "jnxIfOpticsPMDayMaxRxLaserBiasCurrent": jnxIfOpticsPMDayMaxRxLaserBiasCurrent,
       "jnxIfOpticsPMDayAvgRxLaserBiasCurrent": jnxIfOpticsPMDayAvgRxLaserBiasCurrent,
       "jnxIfOpticsPMDayMinTecCurrent": jnxIfOpticsPMDayMinTecCurrent,
       "jnxIfOpticsPMDayMaxTecCurrent": jnxIfOpticsPMDayMaxTecCurrent,
       "jnxIfOpticsPMDayAvgTecCurrent": jnxIfOpticsPMDayAvgTecCurrent,
       "jnxIfOpticsPMDayMinResidualDispersion": jnxIfOpticsPMDayMinResidualDispersion,
       "jnxIfOpticsPMDayMaxResidualDispersion": jnxIfOpticsPMDayMaxResidualDispersion,
       "jnxIfOpticsPMDayAvgResidualDispersion": jnxIfOpticsPMDayAvgResidualDispersion,
       "jnxIfOpticsPMDayMinLevelHistogram": jnxIfOpticsPMDayMinLevelHistogram,
       "jnxIfOpticsPMDayMaxLevelHistogram": jnxIfOpticsPMDayMaxLevelHistogram,
       "jnxIfOpticsPMDayAvgLevelHistogram": jnxIfOpticsPMDayAvgLevelHistogram,
       "jnxIfOpticsPMDayMinLaserFrequencyError": jnxIfOpticsPMDayMinLaserFrequencyError,
       "jnxIfOpticsPMDayMaxLaserFrequencyError": jnxIfOpticsPMDayMaxLaserFrequencyError,
       "jnxIfOpticsPMDayAvgLaserFrequencyError": jnxIfOpticsPMDayAvgLaserFrequencyError,
       "jnxIfOpticsPMDayMinFECCorrectedErrorsMantissa": jnxIfOpticsPMDayMinFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMDayMinFECCorrectedErrorsExponent": jnxIfOpticsPMDayMinFECCorrectedErrorsExponent,
       "jnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa": jnxIfOpticsPMDayMaxFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMDayMaxFECCorrectedErrorsExponent": jnxIfOpticsPMDayMaxFECCorrectedErrorsExponent,
       "jnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa": jnxIfOpticsPMDayAvgFECCorrectedErrorsMantissa,
       "jnxIfOpticsPMDayAvgFECCorrectedErrorsExponent": jnxIfOpticsPMDayAvgFECCorrectedErrorsExponent,
       "jnxIfOpticsPMDayMinFECUCorrectedWordsMantissa": jnxIfOpticsPMDayMinFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMDayMinFECUCorrectedWordsExponent": jnxIfOpticsPMDayMinFECUCorrectedWordsExponent,
       "jnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa": jnxIfOpticsPMDayMaxFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMDayMaxFECUCorrectedWordsExponent": jnxIfOpticsPMDayMaxFECUCorrectedWordsExponent,
       "jnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa": jnxIfOpticsPMDayAvgFECUCorrectedWordsMantissa,
       "jnxIfOpticsPMDayAvgFECUCorrectedWordsExponent": jnxIfOpticsPMDayAvgFECUCorrectedWordsExponent,
       "jnxOpticsAlarm": jnxOpticsAlarm,
       "jnxOpticsNotificationTable": jnxOpticsNotificationTable,
       "jnxOpticsNotificationEntry": jnxOpticsNotificationEntry,
       "jnxOpticsNotificationLocation": jnxOpticsNotificationLocation,
       "jnxOpticsNotificationDirection": jnxOpticsNotificationDirection,
       "jnxOpticsLastNotificationId": jnxOpticsLastNotificationId,
       "jnxOpticsNotificationSeverity": jnxOpticsNotificationSeverity,
       "jnxOpticsNotificationDate": jnxOpticsNotificationDate,
       "jnxOpticsNotificationLaneIndex": jnxOpticsNotificationLaneIndex,
       "jnxOpticsOCh2": jnxOpticsOCh2,
       "jnxOpticsOCh2ConfigTable": jnxOpticsOCh2ConfigTable,
       "jnxOpticsOCh2ConfigEntry": jnxOpticsOCh2ConfigEntry,
       "jnxOpticsOCh2CfgContIndex": jnxOpticsOCh2CfgContIndex,
       "jnxOpticsOCh2CfgL1Index": jnxOpticsOCh2CfgL1Index,
       "jnxOpticsOCh2CfgL2Index": jnxOpticsOCh2CfgL2Index,
       "jnxOpticsOCh2CfgL3Index": jnxOpticsOCh2CfgL3Index,
       "jnxOpticsOCh2CfgL4Index": jnxOpticsOCh2CfgL4Index,
       "jnxOpticsOCh2Type": jnxOpticsOCh2Type,
       "jnxOpticsOCh2LaserEnable": jnxOpticsOCh2LaserEnable,
       "jnxOpticsOCh2Wavelength": jnxOpticsOCh2Wavelength,
       "jnxOpticsOCh2Spacing": jnxOpticsOCh2Spacing,
       "jnxOpticsOCh2Modulation": jnxOpticsOCh2Modulation,
       "jnxOpticsOCh2TxOpticalPower": jnxOpticsOCh2TxOpticalPower,
       "jnxOpticsOCh2RxOpticalPower": jnxOpticsOCh2RxOpticalPower,
       "jnxOpticsOCh2ModTempHighThresh": jnxOpticsOCh2ModTempHighThresh,
       "jnxOpticsOCh2ModTempLowThresh": jnxOpticsOCh2ModTempLowThresh,
       "jnxOpticsOCh2TxPowHighThresh": jnxOpticsOCh2TxPowHighThresh,
       "jnxOpticsOCh2TxPowLowThresh": jnxOpticsOCh2TxPowLowThresh,
       "jnxOpticsOCh2RxPowHighThresh": jnxOpticsOCh2RxPowHighThresh,
       "jnxOpticsOCh2RxPowLowThresh": jnxOpticsOCh2RxPowLowThresh,
       "jnxOpticsOCh24HourModTemHiThresh": jnxOpticsOCh24HourModTemHiThresh,
       "jnxOpticsOCh24HourModTemLoThresh": jnxOpticsOCh24HourModTemLoThresh,
       "jnxOpticsOCh24HourTxPowHiThresh": jnxOpticsOCh24HourTxPowHiThresh,
       "jnxOpticsOCh24HourTxPowLoThresh": jnxOpticsOCh24HourTxPowLoThresh,
       "jnxOpticsOCh24HourRxPowHiThresh": jnxOpticsOCh24HourRxPowHiThresh,
       "jnxOpticsOCh24HourRxPowLoThresh": jnxOpticsOCh24HourRxPowLoThresh,
       "jnxOpticsOCh2RxLosPowWarnThresh": jnxOpticsOCh2RxLosPowWarnThresh,
       "jnxOpticsOCh2RxLosPowAlarmThresh": jnxOpticsOCh2RxLosPowAlarmThresh,
       "jnxOpticsOCh2CurrentStatus": jnxOpticsOCh2CurrentStatus,
       "jnxOpticsOCh2TxPowHiEnableTCA": jnxOpticsOCh2TxPowHiEnableTCA,
       "jnxOpticsOCh2TxPowLoEnableTCA": jnxOpticsOCh2TxPowLoEnableTCA,
       "jnxOpticsOCh2RxPowHiEnableTCA": jnxOpticsOCh2RxPowHiEnableTCA,
       "jnxOpticsOCh2RxPowLoEnableTCA": jnxOpticsOCh2RxPowLoEnableTCA,
       "jnxOpticsOCh2ModTempHiEnableTCA": jnxOpticsOCh2ModTempHiEnableTCA,
       "jnxOpticsOCh2ModTempLoEnableTCA": jnxOpticsOCh2ModTempLoEnableTCA,
       "jnxOpticsOCh2CarFreqOffHiEnTCA": jnxOpticsOCh2CarFreqOffHiEnTCA,
       "jnxOpticsOCh2CarFreqOffLoEnTCA": jnxOpticsOCh2CarFreqOffLoEnTCA,
       "jnxOpticsOCh2CarFreqOffHiThresh": jnxOpticsOCh2CarFreqOffHiThresh,
       "jnxOpticsOCh24HourCarFreqOffHiTh": jnxOpticsOCh24HourCarFreqOffHiTh,
       "jnxOpticsOCh2CarFreqOffLoThresh": jnxOpticsOCh2CarFreqOffLoThresh,
       "jnxOpticsOCh24HourCarFreqOffLoTh": jnxOpticsOCh24HourCarFreqOffLoTh,
       "jnxOpticsOCh2TraceToneCfgTable": jnxOpticsOCh2TraceToneCfgTable,
       "jnxOpticsOCh2TraceToneCfgEntry": jnxOpticsOCh2TraceToneCfgEntry,
       "jnxOpticsOCh2TraceToneCfgIndx": jnxOpticsOCh2TraceToneCfgIndx,
       "jnxOpticsOCh2TraceToneCfgL1Indx": jnxOpticsOCh2TraceToneCfgL1Indx,
       "jnxOpticsOCh2TraceToneCfgL2Indx": jnxOpticsOCh2TraceToneCfgL2Indx,
       "jnxOpticsOCh2TraceToneCfgL3Indx": jnxOpticsOCh2TraceToneCfgL3Indx,
       "jnxOpticsOCh2TraceToneCfgL4Indx": jnxOpticsOCh2TraceToneCfgL4Indx,
       "jnxOpticsOCh2TraceToneCfgTxEn": jnxOpticsOCh2TraceToneCfgTxEn,
       "jnxOpticsOCh2TraceToneCfgRxEn": jnxOpticsOCh2TraceToneCfgRxEn,
       "jnxOpticsOCh2TraceToneCfgDestId": jnxOpticsOCh2TraceToneCfgDestId,
       "jnxOpticsOCh2TraceToneCfgTxMsg": jnxOpticsOCh2TraceToneCfgTxMsg,
       "jnxOpticsOCh2TraceToneCfgRxMsg": jnxOpticsOCh2TraceToneCfgRxMsg,
       "jnxIplcAlarm": jnxIplcAlarm,
       "jnxIplcNotificationTable": jnxIplcNotificationTable,
       "jnxIplcNotificationEntry": jnxIplcNotificationEntry,
       "jnxIplcNotificationLocation": jnxIplcNotificationLocation,
       "jnxIplcNotificationDirection": jnxIplcNotificationDirection,
       "jnxIplcNotificationSlot": jnxIplcNotificationSlot,
       "jnxIplcNotificationChannel": jnxIplcNotificationChannel,
       "jnxIplcLastNotificationId": jnxIplcLastNotificationId,
       "jnxIplcNotificationSeverity": jnxIplcNotificationSeverity,
       "jnxIplcNotificationDate": jnxIplcNotificationDate,
       "jnxIlaAlarm": jnxIlaAlarm,
       "jnxIlaNotificationTable": jnxIlaNotificationTable,
       "jnxIlaNotificationEntry": jnxIlaNotificationEntry,
       "jnxIlaNotificationLocation": jnxIlaNotificationLocation,
       "jnxIlaNotificationDirection": jnxIlaNotificationDirection,
       "jnxIlaNotificationSlot": jnxIlaNotificationSlot,
       "jnxIlaNotificationIlaID": jnxIlaNotificationIlaID,
       "jnxIlaLastNotificationId": jnxIlaLastNotificationId,
       "jnxIlaNotificationSeverity": jnxIlaNotificationSeverity,
       "jnxIlaNotificationDate": jnxIlaNotificationDate,
       "jnxOpticsNotificationPrefix": jnxOpticsNotificationPrefix,
       "jnxOpticsNotificationSet": jnxOpticsNotificationSet,
       "jnxOpticsNotificationCleared": jnxOpticsNotificationCleared,
       "jnxIfOpticsNotificationAdminStatus": jnxIfOpticsNotificationAdminStatus,
       "jnxIfOpticsNotificationOperStatus": jnxIfOpticsNotificationOperStatus,
       "jnxIplcNotificationPrefix": jnxIplcNotificationPrefix,
       "jnxIplcNotificationSet": jnxIplcNotificationSet,
       "jnxIplcNotificationCleared": jnxIplcNotificationCleared,
       "jnxIlaNotificationPrefix": jnxIlaNotificationPrefix,
       "jnxIlaNotificationSet": jnxIlaNotificationSet,
       "jnxIlaNotificationCleared": jnxIlaNotificationCleared}
)
