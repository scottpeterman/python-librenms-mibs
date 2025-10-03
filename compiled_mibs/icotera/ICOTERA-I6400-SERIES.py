# SNMP MIB module (ICOTERA-I6400-SERIES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\icotera\ICOTERA-I6400-SERIES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:08 2025
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

icotera = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29865)
)
if mibBuilder.loadTexts:
    icotera.setRevisions(
        ("2017-03-01 16:46",
         "2017-02-09 14:27",
         "2017-01-16 10:32",
         "2016-08-26 09:24",
         "2016-08-24 09:04",
         "2015-04-01 13:57")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IctTimeStamp(TextualConvention, Counter32):
    status = "current"


class IctPortList(TextualConvention, OctetString):
    status = "current"


class IctJitter(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


class IctDelta(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_IctIGW1k_ObjectIdentity = ObjectIdentity
ictIGW1k = _IctIGW1k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11)
)
if mibBuilder.loadTexts:
    ictIGW1k.setStatus("current")
_IctMgmt_ObjectIdentity = ObjectIdentity
ictMgmt = _IctMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2)
)
_IctMgmtMib_ObjectIdentity = ObjectIdentity
ictMgmtMib = _IctMgmtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1)
)
if mibBuilder.loadTexts:
    ictMgmtMib.setStatus("current")
_IctFwUpg_ObjectIdentity = ObjectIdentity
ictFwUpg = _IctFwUpg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ictFwUpg.setStatus("current")


class _UpgUrl_Type(OctetString):
    """Custom type upgUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpgUrl_Type.__name__ = "OctetString"
_UpgUrl_Object = MibScalar
upgUrl = _UpgUrl_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1, 1),
    _UpgUrl_Type()
)
upgUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgUrl.setStatus("current")


class _UpgExecute_Type(Integer32):
    """Custom type upgExecute based on Integer32"""
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
        *(("notUpgrading", 0),
          ("startUpgrade", 1),
          ("validatingUpgrade-CheckErrorCodeIfFailed", 2),
          ("someErrorOccured", 3))
    )


_UpgExecute_Type.__name__ = "Integer32"
_UpgExecute_Object = MibScalar
upgExecute = _UpgExecute_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1, 2),
    _UpgExecute_Type()
)
upgExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upgExecute.setStatus("current")


class _UpgStatus_Type(OctetString):
    """Custom type upgStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpgStatus_Type.__name__ = "OctetString"
_UpgStatus_Object = MibScalar
upgStatus = _UpgStatus_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 1, 3),
    _UpgStatus_Type()
)
upgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgStatus.setStatus("current")
_IctCfgUpdate_ObjectIdentity = ObjectIdentity
ictCfgUpdate = _IctCfgUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ictCfgUpdate.setStatus("current")


class _CfgTftpPath_Type(OctetString):
    """Custom type cfgTftpPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfgTftpPath_Type.__name__ = "OctetString"
_CfgTftpPath_Object = MibScalar
cfgTftpPath = _CfgTftpPath_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2, 1),
    _CfgTftpPath_Type()
)
cfgTftpPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgTftpPath.setStatus("current")


class _CfgExecute_Type(Integer32):
    """Custom type cfgExecute based on Integer32"""
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
        *(("notUpdating", 0),
          ("startUpdate", 1),
          ("inProgress", 2),
          ("someErrorOccured", 3),
          ("resultOK", 4))
    )


_CfgExecute_Type.__name__ = "Integer32"
_CfgExecute_Object = MibScalar
cfgExecute = _CfgExecute_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2, 2),
    _CfgExecute_Type()
)
cfgExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgExecute.setStatus("current")


class _CfgStatus_Type(OctetString):
    """Custom type cfgStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfgStatus_Type.__name__ = "OctetString"
_CfgStatus_Object = MibScalar
cfgStatus = _CfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 2, 3),
    _CfgStatus_Type()
)
cfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgStatus.setStatus("current")
_IctReboot_ObjectIdentity = ObjectIdentity
ictReboot = _IctReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ictReboot.setStatus("current")


class _PerformCpeReboot_Type(Integer32):
    """Custom type performCpeReboot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noActionRequested", 0),
          ("makeReboot", 1),
          ("someErrorOccured", 3))
    )


_PerformCpeReboot_Type.__name__ = "Integer32"
_PerformCpeReboot_Object = MibScalar
performCpeReboot = _PerformCpeReboot_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 2, 1, 3, 2),
    _PerformCpeReboot_Type()
)
performCpeReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    performCpeReboot.setStatus("current")
_IctServices_ObjectIdentity = ObjectIdentity
ictServices = _IctServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3)
)
_IctServicesMibs_ObjectIdentity = ObjectIdentity
ictServicesMibs = _IctServicesMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1)
)
if mibBuilder.loadTexts:
    ictServicesMibs.setStatus("current")
_IctCatv_ObjectIdentity = ObjectIdentity
ictCatv = _IctCatv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ictCatv.setStatus("current")


class _CatvModuleAdminStatus_Type(Integer32):
    """Custom type catvModuleAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CatvModuleAdminStatus_Type.__name__ = "Integer32"
_CatvModuleAdminStatus_Object = MibScalar
catvModuleAdminStatus = _CatvModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 1),
    _CatvModuleAdminStatus_Type()
)
catvModuleAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleAdminStatus.setStatus("current")


class _CatvModuleFilter_Type(Integer32):
    """Custom type catvModuleFilter based on Integer32"""
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
          ("pkg1", 1),
          ("pkg2", 2),
          ("pkg3", 3),
          ("pkg4", 4))
    )


_CatvModuleFilter_Type.__name__ = "Integer32"
_CatvModuleFilter_Object = MibScalar
catvModuleFilter = _CatvModuleFilter_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 2),
    _CatvModuleFilter_Type()
)
catvModuleFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleFilter.setStatus("current")


class _CatvModuleRflevel_Type(Integer32):
    """Custom type catvModuleRflevel based on Integer32"""
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
        *(("auto", 0),
          ("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_CatvModuleRflevel_Type.__name__ = "Integer32"
_CatvModuleRflevel_Object = MibScalar
catvModuleRflevel = _CatvModuleRflevel_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 3),
    _CatvModuleRflevel_Type()
)
catvModuleRflevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleRflevel.setStatus("current")
_CatvModuleLowSignal_Type = Integer32
_CatvModuleLowSignal_Object = MibScalar
catvModuleLowSignal = _CatvModuleLowSignal_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 4),
    _CatvModuleLowSignal_Type()
)
catvModuleLowSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleLowSignal.setStatus("current")


class _CatvModuleSignalDetected_Type(Integer32):
    """Custom type catvModuleSignalDetected based on Integer32"""
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


_CatvModuleSignalDetected_Type.__name__ = "Integer32"
_CatvModuleSignalDetected_Object = MibScalar
catvModuleSignalDetected = _CatvModuleSignalDetected_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 5),
    _CatvModuleSignalDetected_Type()
)
catvModuleSignalDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleSignalDetected.setStatus("current")
_CatvModulePowerLevel_Type = Integer32
_CatvModulePowerLevel_Object = MibScalar
catvModulePowerLevel = _CatvModulePowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 1, 6),
    _CatvModulePowerLevel_Type()
)
catvModulePowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModulePowerLevel.setStatus("current")
_IctTransceiver_ObjectIdentity = ObjectIdentity
ictTransceiver = _IctTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ictTransceiver.setStatus("current")
_TransceiverDdmTemperature_Type = Integer32
_TransceiverDdmTemperature_Object = MibScalar
transceiverDdmTemperature = _TransceiverDdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 1),
    _TransceiverDdmTemperature_Type()
)
transceiverDdmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmTemperature.setStatus("current")
_TransceiverDdmTxPower_Type = Integer32
_TransceiverDdmTxPower_Object = MibScalar
transceiverDdmTxPower = _TransceiverDdmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 2),
    _TransceiverDdmTxPower_Type()
)
transceiverDdmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmTxPower.setStatus("current")
_TransceiverDdmRxPower_Type = Integer32
_TransceiverDdmRxPower_Object = MibScalar
transceiverDdmRxPower = _TransceiverDdmRxPower_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 3),
    _TransceiverDdmRxPower_Type()
)
transceiverDdmRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmRxPower.setStatus("current")
_TransceiverDdmVoltage_Type = Integer32
_TransceiverDdmVoltage_Object = MibScalar
transceiverDdmVoltage = _TransceiverDdmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 4),
    _TransceiverDdmVoltage_Type()
)
transceiverDdmVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmVoltage.setStatus("current")
_TransceiverDdmTxBiasCurrent_Type = Integer32
_TransceiverDdmTxBiasCurrent_Object = MibScalar
transceiverDdmTxBiasCurrent = _TransceiverDdmTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 5),
    _TransceiverDdmTxBiasCurrent_Type()
)
transceiverDdmTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDdmTxBiasCurrent.setStatus("current")


class _TransceiverTransceiverType_Type(Integer32):
    """Custom type transceiverTransceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("gbic", 1),
          ("moduleSolderedToMotherboard", 2),
          ("sfp", 3),
          ("type300pinXbi", 4),
          ("xenpak", 5),
          ("xfp", 6),
          ("xff", 7),
          ("xfpE", 8),
          ("xPak", 9),
          ("x2", 10),
          ("dWdmSfp", 11),
          ("qSfp", 12))
    )


_TransceiverTransceiverType_Type.__name__ = "Integer32"
_TransceiverTransceiverType_Object = MibScalar
transceiverTransceiverType = _TransceiverTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 6),
    _TransceiverTransceiverType_Type()
)
transceiverTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverTransceiverType.setStatus("current")
_TransceiverLaserWavelength_Type = Integer32
_TransceiverLaserWavelength_Object = MibScalar
transceiverLaserWavelength = _TransceiverLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 7),
    _TransceiverLaserWavelength_Type()
)
transceiverLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverLaserWavelength.setStatus("current")


class _TransceiverConnectorType_Type(Integer32):
    """Custom type transceiverConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sc", 1),
          ("fibreChannelStyle1CopperConnector", 2),
          ("fibreChannelStyle2CopperConnector", 3),
          ("bncTnc", 4),
          ("fibreChannelCoaxialHeaders", 5),
          ("fiberJack", 6),
          ("lc", 7),
          ("mtRj", 8),
          ("mu", 9),
          ("sg", 10),
          ("opticalPigtail", 11),
          ("mpoParallelOptic", 12),
          ("hssdcII", 32),
          ("copperPigtail", 33),
          ("rj45", 34))
    )


_TransceiverConnectorType_Type.__name__ = "Integer32"
_TransceiverConnectorType_Object = MibScalar
transceiverConnectorType = _TransceiverConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 8),
    _TransceiverConnectorType_Type()
)
transceiverConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverConnectorType.setStatus("current")
_TransceiverEthernetCompliance_Type = Integer32
_TransceiverEthernetCompliance_Object = MibScalar
transceiverEthernetCompliance = _TransceiverEthernetCompliance_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 9),
    _TransceiverEthernetCompliance_Type()
)
transceiverEthernetCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverEthernetCompliance.setStatus("current")
_TransceiverLinkLength_Type = Integer32
_TransceiverLinkLength_Object = MibScalar
transceiverLinkLength = _TransceiverLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 10),
    _TransceiverLinkLength_Type()
)
transceiverLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverLinkLength.setStatus("current")


class _TransceiverDiagCapable_Type(Integer32):
    """Custom type transceiverDiagCapable based on Integer32"""
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


_TransceiverDiagCapable_Type.__name__ = "Integer32"
_TransceiverDiagCapable_Object = MibScalar
transceiverDiagCapable = _TransceiverDiagCapable_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 3, 1, 3, 11),
    _TransceiverDiagCapable_Type()
)
transceiverDiagCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverDiagCapable.setStatus("current")
_IctReset_ObjectIdentity = ObjectIdentity
ictReset = _IctReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 5)
)
_IctFacRst_ObjectIdentity = ObjectIdentity
ictFacRst = _IctFacRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 5, 1)
)
if mibBuilder.loadTexts:
    ictFacRst.setStatus("current")
_IctFacRstMib_ObjectIdentity = ObjectIdentity
ictFacRstMib = _IctFacRstMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ictFacRstMib.setStatus("current")


class _PerformFactoryReset_Type(Integer32):
    """Custom type performFactoryReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noActionRequested", 0),
          ("makeFactoryreset", 1),
          ("someErrorOccured", 3))
    )


_PerformFactoryReset_Type.__name__ = "Integer32"
_PerformFactoryReset_Object = MibScalar
performFactoryReset = _PerformFactoryReset_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 5, 1, 1, 1),
    _PerformFactoryReset_Type()
)
performFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    performFactoryReset.setStatus("current")
_IctMcastAnalyzer_ObjectIdentity = ObjectIdentity
ictMcastAnalyzer = _IctMcastAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7)
)
_IctMcastAnalyzerCurrent_ObjectIdentity = ObjectIdentity
ictMcastAnalyzerCurrent = _IctMcastAnalyzerCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1)
)
_IctMcastAnalyzerCurrentList_Object = MibTable
ictMcastAnalyzerCurrentList = _IctMcastAnalyzerCurrentList_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ictMcastAnalyzerCurrentList.setStatus("current")
_CurrentListEntry_Object = MibTableRow
currentListEntry = _CurrentListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1, 1)
)
currentListEntry.setIndexNames(
    (0, "ICOTERA-I6400-SERIES", "curGroupIndex"),
)
if mibBuilder.loadTexts:
    currentListEntry.setStatus("current")


class _CurGroupIndex_Type(Integer32):
    """Custom type curGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CurGroupIndex_Type.__name__ = "Integer32"
_CurGroupIndex_Object = MibTableColumn
curGroupIndex = _CurGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1, 1, 1),
    _CurGroupIndex_Type()
)
curGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curGroupIndex.setStatus("current")
_CurGroupAddr_Type = IpAddress
_CurGroupAddr_Object = MibTableColumn
curGroupAddr = _CurGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 1, 1, 2),
    _CurGroupAddr_Type()
)
curGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curGroupAddr.setStatus("current")
_IctMcastAnalyzerCurrentMetrics_Object = MibTable
ictMcastAnalyzerCurrentMetrics = _IctMcastAnalyzerCurrentMetrics_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ictMcastAnalyzerCurrentMetrics.setStatus("current")
_CurrentMetricsEntry_Object = MibTableRow
currentMetricsEntry = _CurrentMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1)
)
currentMetricsEntry.setIndexNames(
    (0, "ICOTERA-I6400-SERIES", "curMetrGroupAddr"),
)
if mibBuilder.loadTexts:
    currentMetricsEntry.setStatus("current")
_CurMetrGroupAddr_Type = IpAddress
_CurMetrGroupAddr_Object = MibTableColumn
curMetrGroupAddr = _CurMetrGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 1),
    _CurMetrGroupAddr_Type()
)
curMetrGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrGroupAddr.setStatus("current")
_CurMetrSourceAddr_Type = IpAddress
_CurMetrSourceAddr_Object = MibTableColumn
curMetrSourceAddr = _CurMetrSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 2),
    _CurMetrSourceAddr_Type()
)
curMetrSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrSourceAddr.setStatus("current")


class _CurMetrDstPort_Type(Integer32):
    """Custom type curMetrDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CurMetrDstPort_Type.__name__ = "Integer32"
_CurMetrDstPort_Object = MibTableColumn
curMetrDstPort = _CurMetrDstPort_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 3),
    _CurMetrDstPort_Type()
)
curMetrDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrDstPort.setStatus("current")


class _CurMetrSrcPort_Type(Integer32):
    """Custom type curMetrSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CurMetrSrcPort_Type.__name__ = "Integer32"
_CurMetrSrcPort_Object = MibTableColumn
curMetrSrcPort = _CurMetrSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 4),
    _CurMetrSrcPort_Type()
)
curMetrSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrSrcPort.setStatus("current")
_CurMetrTotalBytes_Type = Counter64
_CurMetrTotalBytes_Object = MibTableColumn
curMetrTotalBytes = _CurMetrTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 5),
    _CurMetrTotalBytes_Type()
)
curMetrTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalBytes.setStatus("current")
_CurMetrTotalPackets_Type = Counter64
_CurMetrTotalPackets_Object = MibTableColumn
curMetrTotalPackets = _CurMetrTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 6),
    _CurMetrTotalPackets_Type()
)
curMetrTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalPackets.setStatus("current")
_CurMetrKbps_Type = Gauge32
_CurMetrKbps_Object = MibTableColumn
curMetrKbps = _CurMetrKbps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 7),
    _CurMetrKbps_Type()
)
curMetrKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrKbps.setStatus("current")
_CurMetrPps_Type = Gauge32
_CurMetrPps_Object = MibTableColumn
curMetrPps = _CurMetrPps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 8),
    _CurMetrPps_Type()
)
curMetrPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrPps.setStatus("current")
_CurMetrAvgKbps_Type = Gauge32
_CurMetrAvgKbps_Object = MibTableColumn
curMetrAvgKbps = _CurMetrAvgKbps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 9),
    _CurMetrAvgKbps_Type()
)
curMetrAvgKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrAvgKbps.setStatus("current")
_CurMetrAvgPps_Type = Gauge32
_CurMetrAvgPps_Object = MibTableColumn
curMetrAvgPps = _CurMetrAvgPps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 10),
    _CurMetrAvgPps_Type()
)
curMetrAvgPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrAvgPps.setStatus("current")
_CurMetrMaxDelta_Type = IctDelta
_CurMetrMaxDelta_Object = MibTableColumn
curMetrMaxDelta = _CurMetrMaxDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 11),
    _CurMetrMaxDelta_Type()
)
curMetrMaxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrMaxDelta.setStatus("current")
_CurMetrAvgDelta_Type = IctDelta
_CurMetrAvgDelta_Object = MibTableColumn
curMetrAvgDelta = _CurMetrAvgDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 12),
    _CurMetrAvgDelta_Type()
)
curMetrAvgDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrAvgDelta.setStatus("current")
_CurMetrTotalMaxDelta_Type = IctDelta
_CurMetrTotalMaxDelta_Object = MibTableColumn
curMetrTotalMaxDelta = _CurMetrTotalMaxDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 13),
    _CurMetrTotalMaxDelta_Type()
)
curMetrTotalMaxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalMaxDelta.setStatus("current")
_CurMetrTotalAvgDelta_Type = IctDelta
_CurMetrTotalAvgDelta_Object = MibTableColumn
curMetrTotalAvgDelta = _CurMetrTotalAvgDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 14),
    _CurMetrTotalAvgDelta_Type()
)
curMetrTotalAvgDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalAvgDelta.setStatus("current")
_CurMetrStartTimestamp_Type = IctTimeStamp
_CurMetrStartTimestamp_Object = MibTableColumn
curMetrStartTimestamp = _CurMetrStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 15),
    _CurMetrStartTimestamp_Type()
)
curMetrStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrStartTimestamp.setStatus("current")
_CurMetrStopTimestamp_Type = IctTimeStamp
_CurMetrStopTimestamp_Object = MibTableColumn
curMetrStopTimestamp = _CurMetrStopTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 16),
    _CurMetrStopTimestamp_Type()
)
curMetrStopTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrStopTimestamp.setStatus("current")
_CurMetrMemberPorts_Type = IctPortList
_CurMetrMemberPorts_Object = MibTableColumn
curMetrMemberPorts = _CurMetrMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 17),
    _CurMetrMemberPorts_Type()
)
curMetrMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrMemberPorts.setStatus("current")
_CurMetrStreamType_Type = OctetString
_CurMetrStreamType_Object = MibTableColumn
curMetrStreamType = _CurMetrStreamType_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 18),
    _CurMetrStreamType_Type()
)
curMetrStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrStreamType.setStatus("current")
_CurMetrSkips_Type = Counter32
_CurMetrSkips_Object = MibTableColumn
curMetrSkips = _CurMetrSkips_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 19),
    _CurMetrSkips_Type()
)
curMetrSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrSkips.setStatus("current")
_CurMetrDiscontinuities_Type = Counter32
_CurMetrDiscontinuities_Object = MibTableColumn
curMetrDiscontinuities = _CurMetrDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 20),
    _CurMetrDiscontinuities_Type()
)
curMetrDiscontinuities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrDiscontinuities.setStatus("current")
_CurMetrLost_Type = Counter32
_CurMetrLost_Object = MibTableColumn
curMetrLost = _CurMetrLost_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 21),
    _CurMetrLost_Type()
)
curMetrLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrLost.setStatus("current")
_CurMetrReordered_Type = Counter32
_CurMetrReordered_Object = MibTableColumn
curMetrReordered = _CurMetrReordered_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 22),
    _CurMetrReordered_Type()
)
curMetrReordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrReordered.setStatus("current")
_CurMetrTotalSkips_Type = Counter32
_CurMetrTotalSkips_Object = MibTableColumn
curMetrTotalSkips = _CurMetrTotalSkips_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 23),
    _CurMetrTotalSkips_Type()
)
curMetrTotalSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalSkips.setStatus("current")
_CurMetrTotalDiscontinuities_Type = Counter32
_CurMetrTotalDiscontinuities_Object = MibTableColumn
curMetrTotalDiscontinuities = _CurMetrTotalDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 24),
    _CurMetrTotalDiscontinuities_Type()
)
curMetrTotalDiscontinuities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalDiscontinuities.setStatus("current")
_CurMetrTotalLost_Type = Counter32
_CurMetrTotalLost_Object = MibTableColumn
curMetrTotalLost = _CurMetrTotalLost_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 25),
    _CurMetrTotalLost_Type()
)
curMetrTotalLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalLost.setStatus("current")
_CurMetrTotalReordered_Type = Counter32
_CurMetrTotalReordered_Object = MibTableColumn
curMetrTotalReordered = _CurMetrTotalReordered_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 26),
    _CurMetrTotalReordered_Type()
)
curMetrTotalReordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrTotalReordered.setStatus("current")
_CurMetrAvgLostPps_Type = Gauge32
_CurMetrAvgLostPps_Object = MibTableColumn
curMetrAvgLostPps = _CurMetrAvgLostPps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 27),
    _CurMetrAvgLostPps_Type()
)
curMetrAvgLostPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrAvgLostPps.setStatus("current")
_CurMetrJitter_Type = IctJitter
_CurMetrJitter_Object = MibTableColumn
curMetrJitter = _CurMetrJitter_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 1, 2, 1, 28),
    _CurMetrJitter_Type()
)
curMetrJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curMetrJitter.setStatus("current")
_IctMcastAnalyzerHistory_ObjectIdentity = ObjectIdentity
ictMcastAnalyzerHistory = _IctMcastAnalyzerHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2)
)
_IctMcastAnalyzerHistoryList_Object = MibTable
ictMcastAnalyzerHistoryList = _IctMcastAnalyzerHistoryList_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1)
)
if mibBuilder.loadTexts:
    ictMcastAnalyzerHistoryList.setStatus("current")
_HistoryListEntry_Object = MibTableRow
historyListEntry = _HistoryListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1, 1)
)
historyListEntry.setIndexNames(
    (0, "ICOTERA-I6400-SERIES", "histGroupIndex"),
)
if mibBuilder.loadTexts:
    historyListEntry.setStatus("current")


class _HistGroupIndex_Type(Integer32):
    """Custom type histGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HistGroupIndex_Type.__name__ = "Integer32"
_HistGroupIndex_Object = MibTableColumn
histGroupIndex = _HistGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1, 1, 1),
    _HistGroupIndex_Type()
)
histGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histGroupIndex.setStatus("current")
_HistGroupAddr_Type = IpAddress
_HistGroupAddr_Object = MibTableColumn
histGroupAddr = _HistGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 1, 1, 2),
    _HistGroupAddr_Type()
)
histGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histGroupAddr.setStatus("current")
_IctMcastAnalyzerHistoryMetrics_Object = MibTable
ictMcastAnalyzerHistoryMetrics = _IctMcastAnalyzerHistoryMetrics_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2)
)
if mibBuilder.loadTexts:
    ictMcastAnalyzerHistoryMetrics.setStatus("current")
_HistoryMetricsEntry_Object = MibTableRow
historyMetricsEntry = _HistoryMetricsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1)
)
historyMetricsEntry.setIndexNames(
    (0, "ICOTERA-I6400-SERIES", "histMetrGroupAddr"),
)
if mibBuilder.loadTexts:
    historyMetricsEntry.setStatus("current")
_HistMetrGroupAddr_Type = IpAddress
_HistMetrGroupAddr_Object = MibTableColumn
histMetrGroupAddr = _HistMetrGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 1),
    _HistMetrGroupAddr_Type()
)
histMetrGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrGroupAddr.setStatus("current")
_HistMetrSourceAddr_Type = IpAddress
_HistMetrSourceAddr_Object = MibTableColumn
histMetrSourceAddr = _HistMetrSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 2),
    _HistMetrSourceAddr_Type()
)
histMetrSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrSourceAddr.setStatus("current")


class _HistMetrDstPort_Type(Integer32):
    """Custom type histMetrDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HistMetrDstPort_Type.__name__ = "Integer32"
_HistMetrDstPort_Object = MibTableColumn
histMetrDstPort = _HistMetrDstPort_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 3),
    _HistMetrDstPort_Type()
)
histMetrDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrDstPort.setStatus("current")


class _HistMetrSrcPort_Type(Integer32):
    """Custom type histMetrSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HistMetrSrcPort_Type.__name__ = "Integer32"
_HistMetrSrcPort_Object = MibTableColumn
histMetrSrcPort = _HistMetrSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 4),
    _HistMetrSrcPort_Type()
)
histMetrSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrSrcPort.setStatus("current")
_HistMetrTotalBytes_Type = Counter64
_HistMetrTotalBytes_Object = MibTableColumn
histMetrTotalBytes = _HistMetrTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 5),
    _HistMetrTotalBytes_Type()
)
histMetrTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalBytes.setStatus("current")
_HistMetrTotalPackets_Type = Counter64
_HistMetrTotalPackets_Object = MibTableColumn
histMetrTotalPackets = _HistMetrTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 6),
    _HistMetrTotalPackets_Type()
)
histMetrTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalPackets.setStatus("current")
_HistMetrKbps_Type = Gauge32
_HistMetrKbps_Object = MibTableColumn
histMetrKbps = _HistMetrKbps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 7),
    _HistMetrKbps_Type()
)
histMetrKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrKbps.setStatus("current")
_HistMetrPps_Type = Gauge32
_HistMetrPps_Object = MibTableColumn
histMetrPps = _HistMetrPps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 8),
    _HistMetrPps_Type()
)
histMetrPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrPps.setStatus("current")
_HistMetrAvgKbps_Type = Gauge32
_HistMetrAvgKbps_Object = MibTableColumn
histMetrAvgKbps = _HistMetrAvgKbps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 9),
    _HistMetrAvgKbps_Type()
)
histMetrAvgKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrAvgKbps.setStatus("current")
_HistMetrAvgPps_Type = Gauge32
_HistMetrAvgPps_Object = MibTableColumn
histMetrAvgPps = _HistMetrAvgPps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 10),
    _HistMetrAvgPps_Type()
)
histMetrAvgPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrAvgPps.setStatus("current")
_HistMetrMaxDelta_Type = IctDelta
_HistMetrMaxDelta_Object = MibTableColumn
histMetrMaxDelta = _HistMetrMaxDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 11),
    _HistMetrMaxDelta_Type()
)
histMetrMaxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrMaxDelta.setStatus("current")
_HistMetrAvgDelta_Type = IctDelta
_HistMetrAvgDelta_Object = MibTableColumn
histMetrAvgDelta = _HistMetrAvgDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 12),
    _HistMetrAvgDelta_Type()
)
histMetrAvgDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrAvgDelta.setStatus("current")
_HistMetrTotalMaxDelta_Type = IctDelta
_HistMetrTotalMaxDelta_Object = MibTableColumn
histMetrTotalMaxDelta = _HistMetrTotalMaxDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 13),
    _HistMetrTotalMaxDelta_Type()
)
histMetrTotalMaxDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalMaxDelta.setStatus("current")
_HistMetrTotalAvgDelta_Type = IctDelta
_HistMetrTotalAvgDelta_Object = MibTableColumn
histMetrTotalAvgDelta = _HistMetrTotalAvgDelta_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 14),
    _HistMetrTotalAvgDelta_Type()
)
histMetrTotalAvgDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalAvgDelta.setStatus("current")
_HistMetrStartTimestamp_Type = IctTimeStamp
_HistMetrStartTimestamp_Object = MibTableColumn
histMetrStartTimestamp = _HistMetrStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 15),
    _HistMetrStartTimestamp_Type()
)
histMetrStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrStartTimestamp.setStatus("current")
_HistMetrStopTimestamp_Type = IctTimeStamp
_HistMetrStopTimestamp_Object = MibTableColumn
histMetrStopTimestamp = _HistMetrStopTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 16),
    _HistMetrStopTimestamp_Type()
)
histMetrStopTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrStopTimestamp.setStatus("current")
_HistMetrMemberPorts_Type = IctPortList
_HistMetrMemberPorts_Object = MibTableColumn
histMetrMemberPorts = _HistMetrMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 17),
    _HistMetrMemberPorts_Type()
)
histMetrMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrMemberPorts.setStatus("current")
_HistMetrStreamType_Type = OctetString
_HistMetrStreamType_Object = MibTableColumn
histMetrStreamType = _HistMetrStreamType_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 18),
    _HistMetrStreamType_Type()
)
histMetrStreamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrStreamType.setStatus("current")
_HistMetrSkips_Type = Counter32
_HistMetrSkips_Object = MibTableColumn
histMetrSkips = _HistMetrSkips_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 19),
    _HistMetrSkips_Type()
)
histMetrSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrSkips.setStatus("current")
_HistMetrDiscontinuities_Type = Counter32
_HistMetrDiscontinuities_Object = MibTableColumn
histMetrDiscontinuities = _HistMetrDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 20),
    _HistMetrDiscontinuities_Type()
)
histMetrDiscontinuities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrDiscontinuities.setStatus("current")
_HistMetrLost_Type = Counter32
_HistMetrLost_Object = MibTableColumn
histMetrLost = _HistMetrLost_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 21),
    _HistMetrLost_Type()
)
histMetrLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrLost.setStatus("current")
_HistMetrReordered_Type = Counter32
_HistMetrReordered_Object = MibTableColumn
histMetrReordered = _HistMetrReordered_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 22),
    _HistMetrReordered_Type()
)
histMetrReordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrReordered.setStatus("current")
_HistMetrTotalSkips_Type = Counter32
_HistMetrTotalSkips_Object = MibTableColumn
histMetrTotalSkips = _HistMetrTotalSkips_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 23),
    _HistMetrTotalSkips_Type()
)
histMetrTotalSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalSkips.setStatus("current")
_HistMetrTotalDiscontinuities_Type = Counter32
_HistMetrTotalDiscontinuities_Object = MibTableColumn
histMetrTotalDiscontinuities = _HistMetrTotalDiscontinuities_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 24),
    _HistMetrTotalDiscontinuities_Type()
)
histMetrTotalDiscontinuities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalDiscontinuities.setStatus("current")
_HistMetrTotalLost_Type = Counter32
_HistMetrTotalLost_Object = MibTableColumn
histMetrTotalLost = _HistMetrTotalLost_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 25),
    _HistMetrTotalLost_Type()
)
histMetrTotalLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalLost.setStatus("current")
_HistMetrTotalReordered_Type = Counter32
_HistMetrTotalReordered_Object = MibTableColumn
histMetrTotalReordered = _HistMetrTotalReordered_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 26),
    _HistMetrTotalReordered_Type()
)
histMetrTotalReordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrTotalReordered.setStatus("current")
_HistMetrAvgLostPps_Type = Gauge32
_HistMetrAvgLostPps_Object = MibTableColumn
histMetrAvgLostPps = _HistMetrAvgLostPps_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 27),
    _HistMetrAvgLostPps_Type()
)
histMetrAvgLostPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrAvgLostPps.setStatus("current")
_HistMetrJitter_Type = IctJitter
_HistMetrJitter_Object = MibTableColumn
histMetrJitter = _HistMetrJitter_Object(
    (1, 3, 6, 1, 4, 1, 29865, 11, 7, 2, 2, 1, 28),
    _HistMetrJitter_Type()
)
histMetrJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histMetrJitter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICOTERA-I6400-SERIES",
    **{"IctTimeStamp": IctTimeStamp,
       "IctPortList": IctPortList,
       "IctJitter": IctJitter,
       "IctDelta": IctDelta,
       "icotera": icotera,
       "ictIGW1k": ictIGW1k,
       "ictMgmt": ictMgmt,
       "ictMgmtMib": ictMgmtMib,
       "ictFwUpg": ictFwUpg,
       "upgUrl": upgUrl,
       "upgExecute": upgExecute,
       "upgStatus": upgStatus,
       "ictCfgUpdate": ictCfgUpdate,
       "cfgTftpPath": cfgTftpPath,
       "cfgExecute": cfgExecute,
       "cfgStatus": cfgStatus,
       "ictReboot": ictReboot,
       "performCpeReboot": performCpeReboot,
       "ictServices": ictServices,
       "ictServicesMibs": ictServicesMibs,
       "ictCatv": ictCatv,
       "catvModuleAdminStatus": catvModuleAdminStatus,
       "catvModuleFilter": catvModuleFilter,
       "catvModuleRflevel": catvModuleRflevel,
       "catvModuleLowSignal": catvModuleLowSignal,
       "catvModuleSignalDetected": catvModuleSignalDetected,
       "catvModulePowerLevel": catvModulePowerLevel,
       "ictTransceiver": ictTransceiver,
       "transceiverDdmTemperature": transceiverDdmTemperature,
       "transceiverDdmTxPower": transceiverDdmTxPower,
       "transceiverDdmRxPower": transceiverDdmRxPower,
       "transceiverDdmVoltage": transceiverDdmVoltage,
       "transceiverDdmTxBiasCurrent": transceiverDdmTxBiasCurrent,
       "transceiverTransceiverType": transceiverTransceiverType,
       "transceiverLaserWavelength": transceiverLaserWavelength,
       "transceiverConnectorType": transceiverConnectorType,
       "transceiverEthernetCompliance": transceiverEthernetCompliance,
       "transceiverLinkLength": transceiverLinkLength,
       "transceiverDiagCapable": transceiverDiagCapable,
       "ictReset": ictReset,
       "ictFacRst": ictFacRst,
       "ictFacRstMib": ictFacRstMib,
       "performFactoryReset": performFactoryReset,
       "ictMcastAnalyzer": ictMcastAnalyzer,
       "ictMcastAnalyzerCurrent": ictMcastAnalyzerCurrent,
       "ictMcastAnalyzerCurrentList": ictMcastAnalyzerCurrentList,
       "currentListEntry": currentListEntry,
       "curGroupIndex": curGroupIndex,
       "curGroupAddr": curGroupAddr,
       "ictMcastAnalyzerCurrentMetrics": ictMcastAnalyzerCurrentMetrics,
       "currentMetricsEntry": currentMetricsEntry,
       "curMetrGroupAddr": curMetrGroupAddr,
       "curMetrSourceAddr": curMetrSourceAddr,
       "curMetrDstPort": curMetrDstPort,
       "curMetrSrcPort": curMetrSrcPort,
       "curMetrTotalBytes": curMetrTotalBytes,
       "curMetrTotalPackets": curMetrTotalPackets,
       "curMetrKbps": curMetrKbps,
       "curMetrPps": curMetrPps,
       "curMetrAvgKbps": curMetrAvgKbps,
       "curMetrAvgPps": curMetrAvgPps,
       "curMetrMaxDelta": curMetrMaxDelta,
       "curMetrAvgDelta": curMetrAvgDelta,
       "curMetrTotalMaxDelta": curMetrTotalMaxDelta,
       "curMetrTotalAvgDelta": curMetrTotalAvgDelta,
       "curMetrStartTimestamp": curMetrStartTimestamp,
       "curMetrStopTimestamp": curMetrStopTimestamp,
       "curMetrMemberPorts": curMetrMemberPorts,
       "curMetrStreamType": curMetrStreamType,
       "curMetrSkips": curMetrSkips,
       "curMetrDiscontinuities": curMetrDiscontinuities,
       "curMetrLost": curMetrLost,
       "curMetrReordered": curMetrReordered,
       "curMetrTotalSkips": curMetrTotalSkips,
       "curMetrTotalDiscontinuities": curMetrTotalDiscontinuities,
       "curMetrTotalLost": curMetrTotalLost,
       "curMetrTotalReordered": curMetrTotalReordered,
       "curMetrAvgLostPps": curMetrAvgLostPps,
       "curMetrJitter": curMetrJitter,
       "ictMcastAnalyzerHistory": ictMcastAnalyzerHistory,
       "ictMcastAnalyzerHistoryList": ictMcastAnalyzerHistoryList,
       "historyListEntry": historyListEntry,
       "histGroupIndex": histGroupIndex,
       "histGroupAddr": histGroupAddr,
       "ictMcastAnalyzerHistoryMetrics": ictMcastAnalyzerHistoryMetrics,
       "historyMetricsEntry": historyMetricsEntry,
       "histMetrGroupAddr": histMetrGroupAddr,
       "histMetrSourceAddr": histMetrSourceAddr,
       "histMetrDstPort": histMetrDstPort,
       "histMetrSrcPort": histMetrSrcPort,
       "histMetrTotalBytes": histMetrTotalBytes,
       "histMetrTotalPackets": histMetrTotalPackets,
       "histMetrKbps": histMetrKbps,
       "histMetrPps": histMetrPps,
       "histMetrAvgKbps": histMetrAvgKbps,
       "histMetrAvgPps": histMetrAvgPps,
       "histMetrMaxDelta": histMetrMaxDelta,
       "histMetrAvgDelta": histMetrAvgDelta,
       "histMetrTotalMaxDelta": histMetrTotalMaxDelta,
       "histMetrTotalAvgDelta": histMetrTotalAvgDelta,
       "histMetrStartTimestamp": histMetrStartTimestamp,
       "histMetrStopTimestamp": histMetrStopTimestamp,
       "histMetrMemberPorts": histMetrMemberPorts,
       "histMetrStreamType": histMetrStreamType,
       "histMetrSkips": histMetrSkips,
       "histMetrDiscontinuities": histMetrDiscontinuities,
       "histMetrLost": histMetrLost,
       "histMetrReordered": histMetrReordered,
       "histMetrTotalSkips": histMetrTotalSkips,
       "histMetrTotalDiscontinuities": histMetrTotalDiscontinuities,
       "histMetrTotalLost": histMetrTotalLost,
       "histMetrTotalReordered": histMetrTotalReordered,
       "histMetrAvgLostPps": histMetrAvgLostPps,
       "histMetrJitter": histMetrJitter}
)
