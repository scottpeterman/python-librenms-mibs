# SNMP MIB module (ICOTERA-I6800-SERIES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\icotera\ICOTERA-I6800-SERIES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:09 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

icotera = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29865)
)
if mibBuilder.loadTexts:
    icotera.setRevisions(
        ("2016-03-11 13:07",
         "2015-08-26 12:40",
         "2015-08-26 08:15",
         "2015-08-21 10:12",
         "2015-08-10 14:33",
         "2015-06-22 14:49",
         "2015-03-12 12:27")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IctIGW4k_ObjectIdentity = ObjectIdentity
ictIGW4k = _IctIGW4k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12)
)
if mibBuilder.loadTexts:
    ictIGW4k.setStatus("current")
_IctMgmt_ObjectIdentity = ObjectIdentity
ictMgmt = _IctMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 2)
)
_IctMgmtMib_ObjectIdentity = ObjectIdentity
ictMgmtMib = _IctMgmtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ictMgmtMib.setStatus("current")
_IctFwUpg_ObjectIdentity = ObjectIdentity
ictFwUpg = _IctFwUpg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 1, 3),
    _UpgStatus_Type()
)
upgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upgStatus.setStatus("current")
_IctCfgUpdate_ObjectIdentity = ObjectIdentity
ictCfgUpdate = _IctCfgUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 1),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("notUpdating", 0),
          ("startUpdate", 1),
          ("someErrorOccured", 3))
    )


_CfgExecute_Type.__name__ = "Integer32"
_CfgExecute_Object = MibScalar
cfgExecute = _CfgExecute_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 2, 3),
    _CfgStatus_Type()
)
cfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgStatus.setStatus("current")
_IctReboot_ObjectIdentity = ObjectIdentity
ictReboot = _IctReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 2, 1, 3, 2),
    _PerformCpeReboot_Type()
)
performCpeReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    performCpeReboot.setStatus("current")
_IctServices_ObjectIdentity = ObjectIdentity
ictServices = _IctServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3)
)
_IctCatv_ObjectIdentity = ObjectIdentity
ictCatv = _IctCatv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ictCatv.setStatus("current")
_IctCatvMib_ObjectIdentity = ObjectIdentity
ictCatvMib = _IctCatvMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ictCatvMib.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 3),
    _CatvModuleRflevel_Type()
)
catvModuleRflevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleRflevel.setStatus("current")
_CatvModuleLowSignal_Type = Integer32
_CatvModuleLowSignal_Object = MibScalar
catvModuleLowSignal = _CatvModuleLowSignal_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 5),
    _CatvModuleSignalDetected_Type()
)
catvModuleSignalDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleSignalDetected.setStatus("current")
_CatvModulePowerLevel_Type = Integer32
_CatvModulePowerLevel_Object = MibScalar
catvModulePowerLevel = _CatvModulePowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 6),
    _CatvModulePowerLevel_Type()
)
catvModulePowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModulePowerLevel.setStatus("current")
_CatvModuleRfOutputLevel_Type = Integer32
_CatvModuleRfOutputLevel_Object = MibScalar
catvModuleRfOutputLevel = _CatvModuleRfOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 7),
    _CatvModuleRfOutputLevel_Type()
)
catvModuleRfOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleRfOutputLevel.setStatus("current")
_CatvModuleOmi_Type = Integer32
_CatvModuleOmi_Object = MibScalar
catvModuleOmi = _CatvModuleOmi_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 1, 1, 8),
    _CatvModuleOmi_Type()
)
catvModuleOmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    catvModuleOmi.setStatus("current")
_IctVoip_ObjectIdentity = ObjectIdentity
ictVoip = _IctVoip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 2)
)
if mibBuilder.loadTexts:
    ictVoip.setStatus("current")
_IctVoipMib_ObjectIdentity = ObjectIdentity
ictVoipMib = _IctVoipMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ictVoipMib.setStatus("current")


class _VoipFXSport1_Type(OctetString):
    """Custom type voipFXSport1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoipFXSport1_Type.__name__ = "OctetString"
_VoipFXSport1_Object = MibScalar
voipFXSport1 = _VoipFXSport1_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1, 1),
    _VoipFXSport1_Type()
)
voipFXSport1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipFXSport1.setStatus("current")


class _VoipFXSport2_Type(OctetString):
    """Custom type voipFXSport2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoipFXSport2_Type.__name__ = "OctetString"
_VoipFXSport2_Object = MibScalar
voipFXSport2 = _VoipFXSport2_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 3, 2, 1, 2),
    _VoipFXSport2_Type()
)
voipFXSport2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipFXSport2.setStatus("current")
_IctDuplex_ObjectIdentity = ObjectIdentity
ictDuplex = _IctDuplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 4)
)
_IctDuplexMib_ObjectIdentity = ObjectIdentity
ictDuplexMib = _IctDuplexMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 4, 15)
)
if mibBuilder.loadTexts:
    ictDuplexMib.setStatus("current")
_DuplexConfig_ObjectIdentity = ObjectIdentity
duplexConfig = _DuplexConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1)
)
_IfDuplexTable_Object = MibTable
ifDuplexTable = _IfDuplexTable_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1)
)
if mibBuilder.loadTexts:
    ifDuplexTable.setStatus("current")
_IfDuplexEntry_Object = MibTableRow
ifDuplexEntry = _IfDuplexEntry_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1)
)
ifDuplexEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifDuplexEntry.setStatus("current")
_IfDuplexIndex_Type = InterfaceIndex
_IfDuplexIndex_Object = MibTableColumn
ifDuplexIndex = _IfDuplexIndex_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1, 1),
    _IfDuplexIndex_Type()
)
ifDuplexIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDuplexIndex.setStatus("current")


class _IfDuplexStatus_Type(Integer32):
    """Custom type ifDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_IfDuplexStatus_Type.__name__ = "Integer32"
_IfDuplexStatus_Object = MibTableColumn
ifDuplexStatus = _IfDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 4, 15, 1, 1, 1, 2),
    _IfDuplexStatus_Type()
)
ifDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDuplexStatus.setStatus("current")
_IctReset_ObjectIdentity = ObjectIdentity
ictReset = _IctReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 5)
)
_IctFacRst_ObjectIdentity = ObjectIdentity
ictFacRst = _IctFacRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 5, 1)
)
if mibBuilder.loadTexts:
    ictFacRst.setStatus("current")
_IctFacRstMib_ObjectIdentity = ObjectIdentity
ictFacRstMib = _IctFacRstMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 5, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 29865, 12, 5, 1, 1, 1),
    _PerformFactoryReset_Type()
)
performFactoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    performFactoryReset.setStatus("current")
_IctDhcp_ObjectIdentity = ObjectIdentity
ictDhcp = _IctDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6)
)
_IctDHCPsrv_Object = MibTable
ictDHCPsrv = _IctDHCPsrv_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6, 1)
)
if mibBuilder.loadTexts:
    ictDHCPsrv.setStatus("current")
_IctDHCPsrvLeases_Object = MibTableRow
ictDHCPsrvLeases = _IctDHCPsrvLeases_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1)
)
ictDHCPsrvLeases.setIndexNames(
    (0, "ICOTERA-I6800-SERIES", "ictDHCPsrvIndex"),
)
if mibBuilder.loadTexts:
    ictDHCPsrvLeases.setStatus("current")


class _IctDHCPsrvIndex_Type(Integer32):
    """Custom type ictDHCPsrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_IctDHCPsrvIndex_Type.__name__ = "Integer32"
_IctDHCPsrvIndex_Object = MibTableColumn
ictDHCPsrvIndex = _IctDHCPsrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 1),
    _IctDHCPsrvIndex_Type()
)
ictDHCPsrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ictDHCPsrvIndex.setStatus("current")
_IctMacAddress_Type = MacAddress
_IctMacAddress_Object = MibTableColumn
ictMacAddress = _IctMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 2),
    _IctMacAddress_Type()
)
ictMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ictMacAddress.setStatus("current")
_IctExpire_Type = Integer32
_IctExpire_Object = MibTableColumn
ictExpire = _IctExpire_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 3),
    _IctExpire_Type()
)
ictExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ictExpire.setStatus("current")
_IctIPaddress_Type = DisplayString
_IctIPaddress_Object = MibTableColumn
ictIPaddress = _IctIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 4),
    _IctIPaddress_Type()
)
ictIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ictIPaddress.setStatus("current")
_IctHostName_Type = DisplayString
_IctHostName_Object = MibTableColumn
ictHostName = _IctHostName_Object(
    (1, 3, 6, 1, 4, 1, 29865, 12, 6, 1, 1, 5),
    _IctHostName_Type()
)
ictHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ictHostName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICOTERA-I6800-SERIES",
    **{"icotera": icotera,
       "ictIGW4k": ictIGW4k,
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
       "ictCatv": ictCatv,
       "ictCatvMib": ictCatvMib,
       "catvModuleAdminStatus": catvModuleAdminStatus,
       "catvModuleFilter": catvModuleFilter,
       "catvModuleRflevel": catvModuleRflevel,
       "catvModuleLowSignal": catvModuleLowSignal,
       "catvModuleSignalDetected": catvModuleSignalDetected,
       "catvModulePowerLevel": catvModulePowerLevel,
       "catvModuleRfOutputLevel": catvModuleRfOutputLevel,
       "catvModuleOmi": catvModuleOmi,
       "ictVoip": ictVoip,
       "ictVoipMib": ictVoipMib,
       "voipFXSport1": voipFXSport1,
       "voipFXSport2": voipFXSport2,
       "ictDuplex": ictDuplex,
       "ictDuplexMib": ictDuplexMib,
       "duplexConfig": duplexConfig,
       "ifDuplexTable": ifDuplexTable,
       "ifDuplexEntry": ifDuplexEntry,
       "ifDuplexIndex": ifDuplexIndex,
       "ifDuplexStatus": ifDuplexStatus,
       "ictReset": ictReset,
       "ictFacRst": ictFacRst,
       "ictFacRstMib": ictFacRstMib,
       "performFactoryReset": performFactoryReset,
       "ictDhcp": ictDhcp,
       "ictDHCPsrv": ictDHCPsrv,
       "ictDHCPsrvLeases": ictDHCPsrvLeases,
       "ictDHCPsrvIndex": ictDHCPsrvIndex,
       "ictMacAddress": ictMacAddress,
       "ictExpire": ictExpire,
       "ictIPaddress": ictIPaddress,
       "ictHostName": ictHostName}
)
