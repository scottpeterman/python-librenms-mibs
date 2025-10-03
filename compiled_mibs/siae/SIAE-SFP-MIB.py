# SNMP MIB module (SIAE-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-SFP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:41 2025
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

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74)
)
if mibBuilder.loadTexts:
    sfp.setRevisions(
        ("2016-12-15 00:00",
         "2016-09-29 00:00",
         "2014-02-03 00:00",
         "2013-12-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Temperature(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )



class PhysicalQuantity(TextualConvention, Integer32):
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
        *(("phyQtTemperature", 1),
          ("phyQtVoltage", 2),
          ("phyQtTxBias", 3),
          ("phyQtTxPower", 4),
          ("phyQtRxPower", 5))
    )



# MIB Managed Objects in the order of their OIDs



class _SfpMibVersion_Type(Integer32):
    """Custom type sfpMibVersion based on Integer32"""
    defaultValue = 1


_SfpMibVersion_Type.__name__ = "Integer32"
_SfpMibVersion_Object = MibScalar
sfpMibVersion = _SfpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 1),
    _SfpMibVersion_Type()
)
sfpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpMibVersion.setStatus("current")
_SfpSerialIdTable_Object = MibTable
sfpSerialIdTable = _SfpSerialIdTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2)
)
if mibBuilder.loadTexts:
    sfpSerialIdTable.setStatus("current")
_SfpSerialIdEntry_Object = MibTableRow
sfpSerialIdEntry = _SfpSerialIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1)
)
sfpSerialIdEntry.setIndexNames(
    (0, "SIAE-SFP-MIB", "sfpModuleId"),
)
if mibBuilder.loadTexts:
    sfpSerialIdEntry.setStatus("current")
_SfpModuleId_Type = Integer32
_SfpModuleId_Object = MibTableColumn
sfpModuleId = _SfpModuleId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 1),
    _SfpModuleId_Type()
)
sfpModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpModuleId.setStatus("current")
_SfpSerialIdValid_Type = TruthValue
_SfpSerialIdValid_Object = MibTableColumn
sfpSerialIdValid = _SfpSerialIdValid_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 2),
    _SfpSerialIdValid_Type()
)
sfpSerialIdValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSerialIdValid.setStatus("current")


class _SfpVendorName_Type(OctetString):
    """Custom type sfpVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorName_Type.__name__ = "OctetString"
_SfpVendorName_Object = MibTableColumn
sfpVendorName = _SfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 3),
    _SfpVendorName_Type()
)
sfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorName.setStatus("current")


class _SfpVendorPartNumber_Type(OctetString):
    """Custom type sfpVendorPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorPartNumber_Type.__name__ = "OctetString"
_SfpVendorPartNumber_Object = MibTableColumn
sfpVendorPartNumber = _SfpVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 4),
    _SfpVendorPartNumber_Type()
)
sfpVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorPartNumber.setStatus("current")


class _SfpVendorRev_Type(OctetString):
    """Custom type sfpVendorRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SfpVendorRev_Type.__name__ = "OctetString"
_SfpVendorRev_Object = MibTableColumn
sfpVendorRev = _SfpVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 5),
    _SfpVendorRev_Type()
)
sfpVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorRev.setStatus("current")


class _SfpVendorSN_Type(OctetString):
    """Custom type sfpVendorSN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorSN_Type.__name__ = "OctetString"
_SfpVendorSN_Object = MibTableColumn
sfpVendorSN = _SfpVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 6),
    _SfpVendorSN_Type()
)
sfpVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSN.setStatus("current")


class _SfpVendorDateCode_Type(OctetString):
    """Custom type sfpVendorDateCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SfpVendorDateCode_Type.__name__ = "OctetString"
_SfpVendorDateCode_Object = MibTableColumn
sfpVendorDateCode = _SfpVendorDateCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 7),
    _SfpVendorDateCode_Type()
)
sfpVendorDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorDateCode.setStatus("current")


class _SfpDiagMonitorCode_Type(Bits):
    """Custom type sfpDiagMonitorCode based on Bits"""
    namedValues = NamedValues(
        *(("sfpDMCtypeLegacy", 0),
          ("sfpDMCtypeImplemented", 1),
          ("sfpDMCtypeInternalCal", 2),
          ("sfpDMCtypeExternalCal", 3),
          ("sfpDMCtypeRxAvgPwr", 4),
          ("sfpDMCtypeAddrChngReqrd", 5))
    )

_SfpDiagMonitorCode_Type.__name__ = "Bits"
_SfpDiagMonitorCode_Object = MibTableColumn
sfpDiagMonitorCode = _SfpDiagMonitorCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 8),
    _SfpDiagMonitorCode_Type()
)
sfpDiagMonitorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagMonitorCode.setStatus("current")


class _SfpEnhancedOptionsCode_Type(Bits):
    """Custom type sfpEnhancedOptionsCode based on Bits"""
    namedValues = NamedValues(
        *(("sfpEOCalarmsImplemented", 0),
          ("sfpEOCSoftTxDisable", 1),
          ("sfpEOCSoftTxFault", 2),
          ("sfpEOCSoftRxLOS", 3),
          ("sfpEOCSoftRateSelect", 4))
    )

_SfpEnhancedOptionsCode_Type.__name__ = "Bits"
_SfpEnhancedOptionsCode_Object = MibTableColumn
sfpEnhancedOptionsCode = _SfpEnhancedOptionsCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 9),
    _SfpEnhancedOptionsCode_Type()
)
sfpEnhancedOptionsCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpEnhancedOptionsCode.setStatus("current")


class _SfpOptions_Type(Bits):
    """Custom type sfpOptions based on Bits"""
    namedValues = NamedValues(
        *(("sfpOPTRateSelect", 0),
          ("sfpOPTTxDisable", 1),
          ("sfpOPTTxFault", 2),
          ("sfpOPTInvertedLOS", 3),
          ("sfpOPTlos", 4))
    )

_SfpOptions_Type.__name__ = "Bits"
_SfpOptions_Object = MibTableColumn
sfpOptions = _SfpOptions_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 10),
    _SfpOptions_Type()
)
sfpOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpOptions.setStatus("current")


class _SfpFibreChannelMedia_Type(Bits):
    """Custom type sfpFibreChannelMedia based on Bits"""
    namedValues = NamedValues(
        *(("sfpMultiMode62u5", 0),
          ("sfpMultiMode50u0", 1),
          ("sfpSingleMode", 2),
          ("sfpTwistedAxialPair", 3),
          ("sfpShieldedTwistedPair", 4),
          ("sfpMiniatureCoax", 5),
          ("sfpVideoCoax", 6))
    )

_SfpFibreChannelMedia_Type.__name__ = "Bits"
_SfpFibreChannelMedia_Object = MibTableColumn
sfpFibreChannelMedia = _SfpFibreChannelMedia_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 11),
    _SfpFibreChannelMedia_Type()
)
sfpFibreChannelMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpFibreChannelMedia.setStatus("current")


class _SfpCompliance_Type(Bits):
    """Custom type sfpCompliance based on Bits"""
    namedValues = NamedValues(
        *(("sfpSonetReachSpecifier1", 0),
          ("sfpSonetReachSpecifier2", 1),
          ("sfpSonetOC48LongReach", 2),
          ("sfpSonetOC48IntermediateReach", 3),
          ("sfpSonetOC48ShortReach", 4),
          ("sfpSonetOC12LongReach", 5),
          ("sfpSonetOC12IntermediateReach", 6),
          ("sfpSonetOC12ShortReach", 7),
          ("sfpSonetOC3LongReach", 8),
          ("sfpSonetOC3IntermediateReach", 9),
          ("sfpSonetOC3ShortReach", 10),
          ("sfp1000BaseT", 11),
          ("sfp1000BaseCX", 12),
          ("sfp1000BaseLX", 13),
          ("sfp1000baseSX", 14),
          ("sfpBasePX", 15),
          ("sfpBaseBX10", 16),
          ("sfp100BaseFX", 17),
          ("sfp100BaseLX", 18))
    )

_SfpCompliance_Type.__name__ = "Bits"
_SfpCompliance_Object = MibTableColumn
sfpCompliance = _SfpCompliance_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 12),
    _SfpCompliance_Type()
)
sfpCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpCompliance.setStatus("current")
_SfpWavelength_Type = Integer32
_SfpWavelength_Object = MibTableColumn
sfpWavelength = _SfpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 13),
    _SfpWavelength_Type()
)
sfpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpWavelength.setStatus("current")
if mibBuilder.loadTexts:
    sfpWavelength.setUnits("nm")
_SfpNominalBitRate_Type = Integer32
_SfpNominalBitRate_Object = MibTableColumn
sfpNominalBitRate = _SfpNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 14),
    _SfpNominalBitRate_Type()
)
sfpNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpNominalBitRate.setStatus("current")
_SfpLinkLength9u_Type = Integer32
_SfpLinkLength9u_Object = MibTableColumn
sfpLinkLength9u = _SfpLinkLength9u_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 15),
    _SfpLinkLength9u_Type()
)
sfpLinkLength9u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLinkLength9u.setStatus("current")
if mibBuilder.loadTexts:
    sfpLinkLength9u.setUnits("m")
_SfpLinkLength50u_Type = Integer32
_SfpLinkLength50u_Object = MibTableColumn
sfpLinkLength50u = _SfpLinkLength50u_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 16),
    _SfpLinkLength50u_Type()
)
sfpLinkLength50u.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLinkLength50u.setStatus("current")
if mibBuilder.loadTexts:
    sfpLinkLength50u.setUnits("m")
_SfpLinkLength62u5_Type = Integer32
_SfpLinkLength62u5_Object = MibTableColumn
sfpLinkLength62u5 = _SfpLinkLength62u5_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 17),
    _SfpLinkLength62u5_Type()
)
sfpLinkLength62u5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLinkLength62u5.setStatus("current")
if mibBuilder.loadTexts:
    sfpLinkLength62u5.setUnits("m")
_SfpLinkLengthCopper_Type = Integer32
_SfpLinkLengthCopper_Object = MibTableColumn
sfpLinkLengthCopper = _SfpLinkLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 18),
    _SfpLinkLengthCopper_Type()
)
sfpLinkLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLinkLengthCopper.setStatus("current")
if mibBuilder.loadTexts:
    sfpLinkLengthCopper.setUnits("m")


class _SfpLabel_Type(DisplayString):
    """Custom type sfpLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpLabel_Type.__name__ = "DisplayString"
_SfpLabel_Object = MibTableColumn
sfpLabel = _SfpLabel_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 19),
    _SfpLabel_Type()
)
sfpLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLabel.setStatus("current")
_SfpFailAlarm_Type = AlarmStatus
_SfpFailAlarm_Object = MibTableColumn
sfpFailAlarm = _SfpFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 2, 1, 20),
    _SfpFailAlarm_Type()
)
sfpFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpFailAlarm.setStatus("current")


class _SfpFailAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type sfpFailAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_SfpFailAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_SfpFailAlarmSeverityCode_Object = MibScalar
sfpFailAlarmSeverityCode = _SfpFailAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 6),
    _SfpFailAlarmSeverityCode_Type()
)
sfpFailAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpFailAlarmSeverityCode.setStatus("current")
_SfpDiagnosticTable_Object = MibTable
sfpDiagnosticTable = _SfpDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7)
)
if mibBuilder.loadTexts:
    sfpDiagnosticTable.setStatus("current")
_SfpDiagnosticEntry_Object = MibTableRow
sfpDiagnosticEntry = _SfpDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1)
)
sfpDiagnosticEntry.setIndexNames(
    (0, "SIAE-SFP-MIB", "sfpModuleId"),
)
if mibBuilder.loadTexts:
    sfpDiagnosticEntry.setStatus("current")
_SfpDiagnosticValid_Type = TruthValue
_SfpDiagnosticValid_Object = MibTableColumn
sfpDiagnosticValid = _SfpDiagnosticValid_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 1),
    _SfpDiagnosticValid_Type()
)
sfpDiagnosticValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDiagnosticValid.setStatus("current")
_SfpLOSPinOut_Type = TruthValue
_SfpLOSPinOut_Object = MibTableColumn
sfpLOSPinOut = _SfpLOSPinOut_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 2),
    _SfpLOSPinOut_Type()
)
sfpLOSPinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLOSPinOut.setStatus("current")
_SfpTxFaultPinOut_Type = TruthValue
_SfpTxFaultPinOut_Object = MibTableColumn
sfpTxFaultPinOut = _SfpTxFaultPinOut_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 3),
    _SfpTxFaultPinOut_Type()
)
sfpTxFaultPinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxFaultPinOut.setStatus("current")
_SfpRateSelectPinIn_Type = TruthValue
_SfpRateSelectPinIn_Object = MibTableColumn
sfpRateSelectPinIn = _SfpRateSelectPinIn_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 4),
    _SfpRateSelectPinIn_Type()
)
sfpRateSelectPinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRateSelectPinIn.setStatus("current")
_SfpTxDisablePinIn_Type = TruthValue
_SfpTxDisablePinIn_Object = MibTableColumn
sfpTxDisablePinIn = _SfpTxDisablePinIn_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 5),
    _SfpTxDisablePinIn_Type()
)
sfpTxDisablePinIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxDisablePinIn.setStatus("current")
_SfpTemperature_Type = Temperature
_SfpTemperature_Object = MibTableColumn
sfpTemperature = _SfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 6),
    _SfpTemperature_Type()
)
sfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTemperature.setStatus("current")
if mibBuilder.loadTexts:
    sfpTemperature.setUnits("C/10")


class _SfpVoltage_Type(Integer32):
    """Custom type sfpVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpVoltage_Type.__name__ = "Integer32"
_SfpVoltage_Object = MibTableColumn
sfpVoltage = _SfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 7),
    _SfpVoltage_Type()
)
sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sfpVoltage.setUnits("milliVolts (mV)")


class _SfpTxBias_Type(Integer32):
    """Custom type sfpTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131000),
    )


_SfpTxBias_Type.__name__ = "Integer32"
_SfpTxBias_Object = MibTableColumn
sfpTxBias = _SfpTxBias_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 8),
    _SfpTxBias_Type()
)
sfpTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxBias.setStatus("current")
if mibBuilder.loadTexts:
    sfpTxBias.setUnits("microAmps (uA)")


class _SfpTxPower_Type(Integer32):
    """Custom type sfpTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpTxPower_Type.__name__ = "Integer32"
_SfpTxPower_Object = MibTableColumn
sfpTxPower = _SfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 9),
    _SfpTxPower_Type()
)
sfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    sfpTxPower.setUnits("microWatts (uW)")


class _SfpRxPower_Type(Integer32):
    """Custom type sfpRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpRxPower_Type.__name__ = "Integer32"
_SfpRxPower_Object = MibTableColumn
sfpRxPower = _SfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 10),
    _SfpRxPower_Type()
)
sfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRxPower.setStatus("current")
if mibBuilder.loadTexts:
    sfpRxPower.setUnits("microWatts (uW)")


class _SfpInternalAlarms_Type(Bits):
    """Custom type sfpInternalAlarms based on Bits"""
    namedValues = NamedValues(
        *(("sfpIntAlarmTempHigh", 0),
          ("sfpIntAlarmTempLow", 1),
          ("sfpIntAlarmVoltageHigh", 2),
          ("sfpIntAlarmVoltageLow", 3),
          ("sfpIntAlarmTxBiasHigh", 4),
          ("sfpIntAlarmTxBiasLow", 5),
          ("sfpIntAlarmTxPowerHigh", 6),
          ("sfpIntAlarmTxPowerLow", 7),
          ("sfpIntAlarmRxPowerHigh", 8),
          ("sfpIntAlarmRxPowerLow", 9))
    )

_SfpInternalAlarms_Type.__name__ = "Bits"
_SfpInternalAlarms_Object = MibTableColumn
sfpInternalAlarms = _SfpInternalAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 11),
    _SfpInternalAlarms_Type()
)
sfpInternalAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInternalAlarms.setStatus("current")


class _SfpInternalWarnings_Type(Bits):
    """Custom type sfpInternalWarnings based on Bits"""
    namedValues = NamedValues(
        *(("sfpIntWarnTempHigh", 0),
          ("sfpIntWarnTempLow", 1),
          ("sfpIntWarnVoltageHigh", 2),
          ("sfpIntWarnVoltageLow", 3),
          ("sfpIntWarnTxBiasHigh", 4),
          ("sfpIntWarnTxBiasLow", 5),
          ("sfpIntWarnTxPowerHigh", 6),
          ("sfpIntWarnTxPowerLow", 7),
          ("sfpIntWarnRxPowerHigh", 8),
          ("sfpIntWarnRxPowerLow", 9))
    )

_SfpInternalWarnings_Type.__name__ = "Bits"
_SfpInternalWarnings_Object = MibTableColumn
sfpInternalWarnings = _SfpInternalWarnings_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 7, 1, 12),
    _SfpInternalWarnings_Type()
)
sfpInternalWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInternalWarnings.setStatus("current")
_SfpAlarmTable_Object = MibTable
sfpAlarmTable = _SfpAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10)
)
if mibBuilder.loadTexts:
    sfpAlarmTable.setStatus("current")
_SfpAlarmEntry_Object = MibTableRow
sfpAlarmEntry = _SfpAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1)
)
sfpAlarmEntry.setIndexNames(
    (0, "SIAE-SFP-MIB", "sfpModuleId"),
    (0, "SIAE-SFP-MIB", "sfpPhysicalQuantity"),
)
if mibBuilder.loadTexts:
    sfpAlarmEntry.setStatus("current")
_SfpPhysicalQuantity_Type = PhysicalQuantity
_SfpPhysicalQuantity_Object = MibTableColumn
sfpPhysicalQuantity = _SfpPhysicalQuantity_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 1),
    _SfpPhysicalQuantity_Type()
)
sfpPhysicalQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPhysicalQuantity.setStatus("current")
_SfpThresholdHighAlarm_Type = Integer32
_SfpThresholdHighAlarm_Object = MibTableColumn
sfpThresholdHighAlarm = _SfpThresholdHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 2),
    _SfpThresholdHighAlarm_Type()
)
sfpThresholdHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpThresholdHighAlarm.setStatus("current")
_SfpThresholdHighWarning_Type = Integer32
_SfpThresholdHighWarning_Object = MibTableColumn
sfpThresholdHighWarning = _SfpThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 3),
    _SfpThresholdHighWarning_Type()
)
sfpThresholdHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpThresholdHighWarning.setStatus("current")
_SfpThresholdLowAlarm_Type = Integer32
_SfpThresholdLowAlarm_Object = MibTableColumn
sfpThresholdLowAlarm = _SfpThresholdLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 4),
    _SfpThresholdLowAlarm_Type()
)
sfpThresholdLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpThresholdLowAlarm.setStatus("current")
_SfpThresholdLowWarning_Type = Integer32
_SfpThresholdLowWarning_Object = MibTableColumn
sfpThresholdLowWarning = _SfpThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 5),
    _SfpThresholdLowWarning_Type()
)
sfpThresholdLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpThresholdLowWarning.setStatus("current")
_SfpHighAlarm_Type = AlarmStatus
_SfpHighAlarm_Object = MibTableColumn
sfpHighAlarm = _SfpHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 6),
    _SfpHighAlarm_Type()
)
sfpHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpHighAlarm.setStatus("current")
_SfpHighWarningAlarm_Type = AlarmStatus
_SfpHighWarningAlarm_Object = MibTableColumn
sfpHighWarningAlarm = _SfpHighWarningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 7),
    _SfpHighWarningAlarm_Type()
)
sfpHighWarningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpHighWarningAlarm.setStatus("current")
_SfpLowAlarm_Type = AlarmStatus
_SfpLowAlarm_Object = MibTableColumn
sfpLowAlarm = _SfpLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 8),
    _SfpLowAlarm_Type()
)
sfpLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLowAlarm.setStatus("current")
_SfpLowWarningAlarm_Type = AlarmStatus
_SfpLowWarningAlarm_Object = MibTableColumn
sfpLowWarningAlarm = _SfpLowWarningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 10, 1, 9),
    _SfpLowWarningAlarm_Type()
)
sfpLowWarningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLowWarningAlarm.setStatus("current")


class _SfpHighAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type sfpHighAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_SfpHighAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_SfpHighAlarmSeverityCode_Object = MibScalar
sfpHighAlarmSeverityCode = _SfpHighAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 11),
    _SfpHighAlarmSeverityCode_Type()
)
sfpHighAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpHighAlarmSeverityCode.setStatus("current")


class _SfpHighWarningAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type sfpHighWarningAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_SfpHighWarningAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_SfpHighWarningAlarmSeverityCode_Object = MibScalar
sfpHighWarningAlarmSeverityCode = _SfpHighWarningAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 12),
    _SfpHighWarningAlarmSeverityCode_Type()
)
sfpHighWarningAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpHighWarningAlarmSeverityCode.setStatus("current")


class _SfpLowAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type sfpLowAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 5


_SfpLowAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_SfpLowAlarmSeverityCode_Object = MibScalar
sfpLowAlarmSeverityCode = _SfpLowAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 13),
    _SfpLowAlarmSeverityCode_Type()
)
sfpLowAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpLowAlarmSeverityCode.setStatus("current")


class _SfpLowWarningAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type sfpLowWarningAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 3


_SfpLowWarningAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_SfpLowWarningAlarmSeverityCode_Object = MibScalar
sfpLowWarningAlarmSeverityCode = _SfpLowWarningAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 74, 14),
    _SfpLowWarningAlarmSeverityCode_Type()
)
sfpLowWarningAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpLowWarningAlarmSeverityCode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-SFP-MIB",
    **{"Temperature": Temperature,
       "PhysicalQuantity": PhysicalQuantity,
       "sfp": sfp,
       "sfpMibVersion": sfpMibVersion,
       "sfpSerialIdTable": sfpSerialIdTable,
       "sfpSerialIdEntry": sfpSerialIdEntry,
       "sfpModuleId": sfpModuleId,
       "sfpSerialIdValid": sfpSerialIdValid,
       "sfpVendorName": sfpVendorName,
       "sfpVendorPartNumber": sfpVendorPartNumber,
       "sfpVendorRev": sfpVendorRev,
       "sfpVendorSN": sfpVendorSN,
       "sfpVendorDateCode": sfpVendorDateCode,
       "sfpDiagMonitorCode": sfpDiagMonitorCode,
       "sfpEnhancedOptionsCode": sfpEnhancedOptionsCode,
       "sfpOptions": sfpOptions,
       "sfpFibreChannelMedia": sfpFibreChannelMedia,
       "sfpCompliance": sfpCompliance,
       "sfpWavelength": sfpWavelength,
       "sfpNominalBitRate": sfpNominalBitRate,
       "sfpLinkLength9u": sfpLinkLength9u,
       "sfpLinkLength50u": sfpLinkLength50u,
       "sfpLinkLength62u5": sfpLinkLength62u5,
       "sfpLinkLengthCopper": sfpLinkLengthCopper,
       "sfpLabel": sfpLabel,
       "sfpFailAlarm": sfpFailAlarm,
       "sfpFailAlarmSeverityCode": sfpFailAlarmSeverityCode,
       "sfpDiagnosticTable": sfpDiagnosticTable,
       "sfpDiagnosticEntry": sfpDiagnosticEntry,
       "sfpDiagnosticValid": sfpDiagnosticValid,
       "sfpLOSPinOut": sfpLOSPinOut,
       "sfpTxFaultPinOut": sfpTxFaultPinOut,
       "sfpRateSelectPinIn": sfpRateSelectPinIn,
       "sfpTxDisablePinIn": sfpTxDisablePinIn,
       "sfpTemperature": sfpTemperature,
       "sfpVoltage": sfpVoltage,
       "sfpTxBias": sfpTxBias,
       "sfpTxPower": sfpTxPower,
       "sfpRxPower": sfpRxPower,
       "sfpInternalAlarms": sfpInternalAlarms,
       "sfpInternalWarnings": sfpInternalWarnings,
       "sfpAlarmTable": sfpAlarmTable,
       "sfpAlarmEntry": sfpAlarmEntry,
       "sfpPhysicalQuantity": sfpPhysicalQuantity,
       "sfpThresholdHighAlarm": sfpThresholdHighAlarm,
       "sfpThresholdHighWarning": sfpThresholdHighWarning,
       "sfpThresholdLowAlarm": sfpThresholdLowAlarm,
       "sfpThresholdLowWarning": sfpThresholdLowWarning,
       "sfpHighAlarm": sfpHighAlarm,
       "sfpHighWarningAlarm": sfpHighWarningAlarm,
       "sfpLowAlarm": sfpLowAlarm,
       "sfpLowWarningAlarm": sfpLowWarningAlarm,
       "sfpHighAlarmSeverityCode": sfpHighAlarmSeverityCode,
       "sfpHighWarningAlarmSeverityCode": sfpHighWarningAlarmSeverityCode,
       "sfpLowAlarmSeverityCode": sfpLowAlarmSeverityCode,
       "sfpLowWarningAlarmSeverityCode": sfpLowWarningAlarmSeverityCode}
)
