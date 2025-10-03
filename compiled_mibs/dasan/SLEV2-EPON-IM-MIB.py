# SNMP MIB module (SLEV2-EPON-IM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLEV2-EPON-IM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:09 2025
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

(sleV2Mgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleV2Mgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleV2EponIM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15)
)


# Types definitions



class EponOnuState(Integer32):
    """Custom type EponOnuState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )





class EponPortType(Integer32):
    """Custom type EponPortType based on Integer32"""
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
        *(("nni", 1),
          ("mgmt", 2),
          ("uni", 3),
          ("pon", 4),
          ("aggr", 5),
          ("llid", 6))
    )





class EponOnuLinkStatus(Integer32):
    """Custom type EponOnuLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )





class EponOnuStatus(Integer32):
    """Custom type EponOnuStatus based on Integer32"""
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
        *(("registered", 1),
          ("deregistered", 2),
          ("discovered", 3),
          ("lost", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleV2EponIMOnu_ObjectIdentity = ObjectIdentity
sleV2EponIMOnu = _SleV2EponIMOnu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1)
)
_SleV2EponIMOnuBase_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuBase = _SleV2EponIMOnuBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1)
)
_SleV2EponIMOnuInfo_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuInfo = _SleV2EponIMOnuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1)
)
_SleV2EponIMOnuConfigMask_Type = Integer32
_SleV2EponIMOnuConfigMask_Object = MibScalar
sleV2EponIMOnuConfigMask = _SleV2EponIMOnuConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 1),
    _SleV2EponIMOnuConfigMask_Type()
)
sleV2EponIMOnuConfigMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuConfigMask.setStatus("current")
_SleV2EponIMOnuConfigData_Type = OctetString
_SleV2EponIMOnuConfigData_Object = MibScalar
sleV2EponIMOnuConfigData = _SleV2EponIMOnuConfigData_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 2),
    _SleV2EponIMOnuConfigData_Type()
)
sleV2EponIMOnuConfigData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuConfigData.setStatus("current")
_SleV2EponIMOnuRegistered_Type = EponOnuState
_SleV2EponIMOnuRegistered_Object = MibScalar
sleV2EponIMOnuRegistered = _SleV2EponIMOnuRegistered_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 3),
    _SleV2EponIMOnuRegistered_Type()
)
sleV2EponIMOnuRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuRegistered.setStatus("current")
_SleV2EponIMOnuAuthenticated_Type = EponOnuState
_SleV2EponIMOnuAuthenticated_Object = MibScalar
sleV2EponIMOnuAuthenticated = _SleV2EponIMOnuAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 4),
    _SleV2EponIMOnuAuthenticated_Type()
)
sleV2EponIMOnuAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuAuthenticated.setStatus("current")
_SleV2EponIMOnuImageVersion_Type = OctetString
_SleV2EponIMOnuImageVersion_Object = MibScalar
sleV2EponIMOnuImageVersion = _SleV2EponIMOnuImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 5),
    _SleV2EponIMOnuImageVersion_Type()
)
sleV2EponIMOnuImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuImageVersion.setStatus("current")
_SleV2EponIMOnuLoadVersion_Type = OctetString
_SleV2EponIMOnuLoadVersion_Object = MibScalar
sleV2EponIMOnuLoadVersion = _SleV2EponIMOnuLoadVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 6),
    _SleV2EponIMOnuLoadVersion_Type()
)
sleV2EponIMOnuLoadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLoadVersion.setStatus("current")
_SleV2EponIMOnuChipVersion_Type = OctetString
_SleV2EponIMOnuChipVersion_Object = MibScalar
sleV2EponIMOnuChipVersion = _SleV2EponIMOnuChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 7),
    _SleV2EponIMOnuChipVersion_Type()
)
sleV2EponIMOnuChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuChipVersion.setStatus("current")
_SleV2EponIMOnuSerialNumber_Type = OctetString
_SleV2EponIMOnuSerialNumber_Object = MibScalar
sleV2EponIMOnuSerialNumber = _SleV2EponIMOnuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 8),
    _SleV2EponIMOnuSerialNumber_Type()
)
sleV2EponIMOnuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuSerialNumber.setStatus("current")
_SleV2EponIMOnuRxOpticPower_Type = OctetString
_SleV2EponIMOnuRxOpticPower_Object = MibScalar
sleV2EponIMOnuRxOpticPower = _SleV2EponIMOnuRxOpticPower_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 9),
    _SleV2EponIMOnuRxOpticPower_Type()
)
sleV2EponIMOnuRxOpticPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuRxOpticPower.setStatus("current")
_SleV2EponIMRegInfoOltId_Type = Integer32
_SleV2EponIMRegInfoOltId_Object = MibScalar
sleV2EponIMRegInfoOltId = _SleV2EponIMRegInfoOltId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 10),
    _SleV2EponIMRegInfoOltId_Type()
)
sleV2EponIMRegInfoOltId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMRegInfoOltId.setStatus("current")


class _SleV2EponIMRegInfoOltLlidPort_Type(Integer32):
    """Custom type sleV2EponIMRegInfoOltLlidPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SleV2EponIMRegInfoOltLlidPort_Type.__name__ = "Integer32"
_SleV2EponIMRegInfoOltLlidPort_Object = MibScalar
sleV2EponIMRegInfoOltLlidPort = _SleV2EponIMRegInfoOltLlidPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 11),
    _SleV2EponIMRegInfoOltLlidPort_Type()
)
sleV2EponIMRegInfoOltLlidPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMRegInfoOltLlidPort.setStatus("current")
_SleV2EponIMRegInfoOltPonPort_Type = Integer32
_SleV2EponIMRegInfoOltPonPort_Object = MibScalar
sleV2EponIMRegInfoOltPonPort = _SleV2EponIMRegInfoOltPonPort_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 12),
    _SleV2EponIMRegInfoOltPonPort_Type()
)
sleV2EponIMRegInfoOltPonPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMRegInfoOltPonPort.setStatus("current")
_SleV2EponIMRegInfoOnuMacAddress_Type = OctetString
_SleV2EponIMRegInfoOnuMacAddress_Object = MibScalar
sleV2EponIMRegInfoOnuMacAddress = _SleV2EponIMRegInfoOnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 13),
    _SleV2EponIMRegInfoOnuMacAddress_Type()
)
sleV2EponIMRegInfoOnuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMRegInfoOnuMacAddress.setStatus("current")
_SleV2EponIMRegInfoOnuLlid_Type = Integer32
_SleV2EponIMRegInfoOnuLlid_Object = MibScalar
sleV2EponIMRegInfoOnuLlid = _SleV2EponIMRegInfoOnuLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 14),
    _SleV2EponIMRegInfoOnuLlid_Type()
)
sleV2EponIMRegInfoOnuLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMRegInfoOnuLlid.setStatus("current")
_SleV2EponIMOnuId_Type = OctetString
_SleV2EponIMOnuId_Object = MibScalar
sleV2EponIMOnuId = _SleV2EponIMOnuId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 15),
    _SleV2EponIMOnuId_Type()
)
sleV2EponIMOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuId.setStatus("current")
_SleV2EponIMOnuSecret_Type = OctetString
_SleV2EponIMOnuSecret_Object = MibScalar
sleV2EponIMOnuSecret = _SleV2EponIMOnuSecret_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 16),
    _SleV2EponIMOnuSecret_Type()
)
sleV2EponIMOnuSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuSecret.setStatus("current")
_SleV2EponIMOnuVendorCode_Type = Integer32
_SleV2EponIMOnuVendorCode_Object = MibScalar
sleV2EponIMOnuVendorCode = _SleV2EponIMOnuVendorCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 17),
    _SleV2EponIMOnuVendorCode_Type()
)
sleV2EponIMOnuVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuVendorCode.setStatus("current")


class _SleV2EponIMOnuAuthTimer_Type(Integer32):
    """Custom type sleV2EponIMOnuAuthTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_SleV2EponIMOnuAuthTimer_Type.__name__ = "Integer32"
_SleV2EponIMOnuAuthTimer_Object = MibScalar
sleV2EponIMOnuAuthTimer = _SleV2EponIMOnuAuthTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 18),
    _SleV2EponIMOnuAuthTimer_Type()
)
sleV2EponIMOnuAuthTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuAuthTimer.setStatus("current")


class _SleV2EponIMOnuAuthTimeoutTimer_Type(Integer32):
    """Custom type sleV2EponIMOnuAuthTimeoutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15360),
    )


_SleV2EponIMOnuAuthTimeoutTimer_Type.__name__ = "Integer32"
_SleV2EponIMOnuAuthTimeoutTimer_Object = MibScalar
sleV2EponIMOnuAuthTimeoutTimer = _SleV2EponIMOnuAuthTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 19),
    _SleV2EponIMOnuAuthTimeoutTimer_Type()
)
sleV2EponIMOnuAuthTimeoutTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuAuthTimeoutTimer.setStatus("current")


class _SleV2EponIMOnuAuthRejectTimer_Type(Integer32):
    """Custom type sleV2EponIMOnuAuthRejectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15360),
    )


_SleV2EponIMOnuAuthRejectTimer_Type.__name__ = "Integer32"
_SleV2EponIMOnuAuthRejectTimer_Object = MibScalar
sleV2EponIMOnuAuthRejectTimer = _SleV2EponIMOnuAuthRejectTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 20),
    _SleV2EponIMOnuAuthRejectTimer_Type()
)
sleV2EponIMOnuAuthRejectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuAuthRejectTimer.setStatus("current")
_SleV2EponIMOnuAutoUpgrade_Type = EponOnuState
_SleV2EponIMOnuAutoUpgrade_Object = MibScalar
sleV2EponIMOnuAutoUpgrade = _SleV2EponIMOnuAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 21),
    _SleV2EponIMOnuAutoUpgrade_Type()
)
sleV2EponIMOnuAutoUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuAutoUpgrade.setStatus("current")
_SleV2EponIMOnuForceOpticPowerOff_Type = EponOnuState
_SleV2EponIMOnuForceOpticPowerOff_Object = MibScalar
sleV2EponIMOnuForceOpticPowerOff = _SleV2EponIMOnuForceOpticPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 22),
    _SleV2EponIMOnuForceOpticPowerOff_Type()
)
sleV2EponIMOnuForceOpticPowerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuForceOpticPowerOff.setStatus("current")
_SleV2EponIMOnuOpticButtonPushed_Type = EponOnuState
_SleV2EponIMOnuOpticButtonPushed_Object = MibScalar
sleV2EponIMOnuOpticButtonPushed = _SleV2EponIMOnuOpticButtonPushed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 1, 23),
    _SleV2EponIMOnuOpticButtonPushed_Type()
)
sleV2EponIMOnuOpticButtonPushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuOpticButtonPushed.setStatus("current")
_SleV2EponIMOnuControl_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuControl = _SleV2EponIMOnuControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2)
)


class _SleV2EponIMOnuControlRequest_Type(Integer32):
    """Custom type sleV2EponIMOnuControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("setOnuSecret", 1),
          ("setOnuVendorCode", 2),
          ("setOnuAuthTimer", 3),
          ("setOnuConfigApply", 4),
          ("setOnuAutoUpgrade", 5),
          ("setOnuForcePowerOff", 6),
          ("setOnuReset", 7))
    )


_SleV2EponIMOnuControlRequest_Type.__name__ = "Integer32"
_SleV2EponIMOnuControlRequest_Object = MibScalar
sleV2EponIMOnuControlRequest = _SleV2EponIMOnuControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 1),
    _SleV2EponIMOnuControlRequest_Type()
)
sleV2EponIMOnuControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlRequest.setStatus("current")
_SleV2EponIMOnuControlStatus_Type = SleControlStatusType
_SleV2EponIMOnuControlStatus_Object = MibScalar
sleV2EponIMOnuControlStatus = _SleV2EponIMOnuControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 2),
    _SleV2EponIMOnuControlStatus_Type()
)
sleV2EponIMOnuControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlStatus.setStatus("current")
_SleV2EponIMOnuControlTimer_Type = Gauge32
_SleV2EponIMOnuControlTimer_Object = MibScalar
sleV2EponIMOnuControlTimer = _SleV2EponIMOnuControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 3),
    _SleV2EponIMOnuControlTimer_Type()
)
sleV2EponIMOnuControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlTimer.setStatus("current")
_SleV2EponIMOnuControlTimeStamp_Type = TimeTicks
_SleV2EponIMOnuControlTimeStamp_Object = MibScalar
sleV2EponIMOnuControlTimeStamp = _SleV2EponIMOnuControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 4),
    _SleV2EponIMOnuControlTimeStamp_Type()
)
sleV2EponIMOnuControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlTimeStamp.setStatus("current")
_SleV2EponIMOnuControlReqResult_Type = SleControlRequestResultType
_SleV2EponIMOnuControlReqResult_Object = MibScalar
sleV2EponIMOnuControlReqResult = _SleV2EponIMOnuControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 5),
    _SleV2EponIMOnuControlReqResult_Type()
)
sleV2EponIMOnuControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlReqResult.setStatus("current")


class _SleV2EponIMOnuControlSecret_Type(OctetString):
    """Custom type sleV2EponIMOnuControlSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SleV2EponIMOnuControlSecret_Type.__name__ = "OctetString"
_SleV2EponIMOnuControlSecret_Object = MibScalar
sleV2EponIMOnuControlSecret = _SleV2EponIMOnuControlSecret_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 6),
    _SleV2EponIMOnuControlSecret_Type()
)
sleV2EponIMOnuControlSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlSecret.setStatus("current")


class _SleV2EponIMOnuControlOnuVendorCode_Type(Integer32):
    """Custom type sleV2EponIMOnuControlOnuVendorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleV2EponIMOnuControlOnuVendorCode_Type.__name__ = "Integer32"
_SleV2EponIMOnuControlOnuVendorCode_Object = MibScalar
sleV2EponIMOnuControlOnuVendorCode = _SleV2EponIMOnuControlOnuVendorCode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 7),
    _SleV2EponIMOnuControlOnuVendorCode_Type()
)
sleV2EponIMOnuControlOnuVendorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlOnuVendorCode.setStatus("current")


class _SleV2EponIMOnuControlAuthTimer_Type(Integer32):
    """Custom type sleV2EponIMOnuControlAuthTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_SleV2EponIMOnuControlAuthTimer_Type.__name__ = "Integer32"
_SleV2EponIMOnuControlAuthTimer_Object = MibScalar
sleV2EponIMOnuControlAuthTimer = _SleV2EponIMOnuControlAuthTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 8),
    _SleV2EponIMOnuControlAuthTimer_Type()
)
sleV2EponIMOnuControlAuthTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlAuthTimer.setStatus("current")


class _SleV2EponIMOnuControlAuthTimeoutTimer_Type(Integer32):
    """Custom type sleV2EponIMOnuControlAuthTimeoutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15360),
    )


_SleV2EponIMOnuControlAuthTimeoutTimer_Type.__name__ = "Integer32"
_SleV2EponIMOnuControlAuthTimeoutTimer_Object = MibScalar
sleV2EponIMOnuControlAuthTimeoutTimer = _SleV2EponIMOnuControlAuthTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 9),
    _SleV2EponIMOnuControlAuthTimeoutTimer_Type()
)
sleV2EponIMOnuControlAuthTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlAuthTimeoutTimer.setStatus("current")


class _SleV2EponIMOnuControlAuthRejectTimer_Type(Integer32):
    """Custom type sleV2EponIMOnuControlAuthRejectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15360),
    )


_SleV2EponIMOnuControlAuthRejectTimer_Type.__name__ = "Integer32"
_SleV2EponIMOnuControlAuthRejectTimer_Object = MibScalar
sleV2EponIMOnuControlAuthRejectTimer = _SleV2EponIMOnuControlAuthRejectTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 10),
    _SleV2EponIMOnuControlAuthRejectTimer_Type()
)
sleV2EponIMOnuControlAuthRejectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlAuthRejectTimer.setStatus("current")
_SleV2EponIMOnuControlAutoUpgrade_Type = EponOnuState
_SleV2EponIMOnuControlAutoUpgrade_Object = MibScalar
sleV2EponIMOnuControlAutoUpgrade = _SleV2EponIMOnuControlAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 11),
    _SleV2EponIMOnuControlAutoUpgrade_Type()
)
sleV2EponIMOnuControlAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlAutoUpgrade.setStatus("current")
_SleV2EponIMOnuControlForceOpticPowerOff_Type = EponOnuState
_SleV2EponIMOnuControlForceOpticPowerOff_Object = MibScalar
sleV2EponIMOnuControlForceOpticPowerOff = _SleV2EponIMOnuControlForceOpticPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 2, 12),
    _SleV2EponIMOnuControlForceOpticPowerOff_Type()
)
sleV2EponIMOnuControlForceOpticPowerOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuControlForceOpticPowerOff.setStatus("current")
_SleV2EponIMOnuNotification_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuNotification = _SleV2EponIMOnuNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3)
)
_SleV2EponIMOnuFW_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuFW = _SleV2EponIMOnuFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2)
)
_SleV2EponIMOnuFWTable_Object = MibTable
sleV2EponIMOnuFWTable = _SleV2EponIMOnuFWTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWTable.setStatus("current")
_SleV2EponIMOnuFWEntry_Object = MibTableRow
sleV2EponIMOnuFWEntry = _SleV2EponIMOnuFWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 1, 1)
)
sleV2EponIMOnuFWEntry.setIndexNames(
    (0, "SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWName"),
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWEntry.setStatus("current")
_SleV2EponIMOnuFWName_Type = OctetString
_SleV2EponIMOnuFWName_Object = MibTableColumn
sleV2EponIMOnuFWName = _SleV2EponIMOnuFWName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 1, 1, 1),
    _SleV2EponIMOnuFWName_Type()
)
sleV2EponIMOnuFWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWName.setStatus("current")
_SleV2EponIMOnuFWControl_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuFWControl = _SleV2EponIMOnuFWControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2)
)


class _SleV2EponIMOnuFWControlRequest_Type(Integer32):
    """Custom type sleV2EponIMOnuFWControlRequest based on Integer32"""
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
        *(("copyFirmware", 1),
          ("destroyFirmware", 2),
          ("updateFirmware", 3),
          ("commitFirmware", 4))
    )


_SleV2EponIMOnuFWControlRequest_Type.__name__ = "Integer32"
_SleV2EponIMOnuFWControlRequest_Object = MibScalar
sleV2EponIMOnuFWControlRequest = _SleV2EponIMOnuFWControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 1),
    _SleV2EponIMOnuFWControlRequest_Type()
)
sleV2EponIMOnuFWControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlRequest.setStatus("current")
_SleV2EponIMOnuFWControlStatus_Type = SleControlStatusType
_SleV2EponIMOnuFWControlStatus_Object = MibScalar
sleV2EponIMOnuFWControlStatus = _SleV2EponIMOnuFWControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 2),
    _SleV2EponIMOnuFWControlStatus_Type()
)
sleV2EponIMOnuFWControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlStatus.setStatus("current")
_SleV2EponIMOnuFWControlTimer_Type = Gauge32
_SleV2EponIMOnuFWControlTimer_Object = MibScalar
sleV2EponIMOnuFWControlTimer = _SleV2EponIMOnuFWControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 3),
    _SleV2EponIMOnuFWControlTimer_Type()
)
sleV2EponIMOnuFWControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlTimer.setStatus("current")
_SleV2EponIMOnuFWControlTimeStamp_Type = TimeTicks
_SleV2EponIMOnuFWControlTimeStamp_Object = MibScalar
sleV2EponIMOnuFWControlTimeStamp = _SleV2EponIMOnuFWControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 4),
    _SleV2EponIMOnuFWControlTimeStamp_Type()
)
sleV2EponIMOnuFWControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlTimeStamp.setStatus("current")
_SleV2EponIMOnuFWControlReqResult_Type = SleControlRequestResultType
_SleV2EponIMOnuFWControlReqResult_Object = MibScalar
sleV2EponIMOnuFWControlReqResult = _SleV2EponIMOnuFWControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 5),
    _SleV2EponIMOnuFWControlReqResult_Type()
)
sleV2EponIMOnuFWControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlReqResult.setStatus("current")
_SleV2EponIMOnuFWControlServerIp_Type = OctetString
_SleV2EponIMOnuFWControlServerIp_Object = MibScalar
sleV2EponIMOnuFWControlServerIp = _SleV2EponIMOnuFWControlServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 6),
    _SleV2EponIMOnuFWControlServerIp_Type()
)
sleV2EponIMOnuFWControlServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlServerIp.setStatus("current")


class _SleV2EponIMOnuFWControlUpDownFlag_Type(Integer32):
    """Custom type sleV2EponIMOnuFWControlUpDownFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upload", 1),
          ("download", 2))
    )


_SleV2EponIMOnuFWControlUpDownFlag_Type.__name__ = "Integer32"
_SleV2EponIMOnuFWControlUpDownFlag_Object = MibScalar
sleV2EponIMOnuFWControlUpDownFlag = _SleV2EponIMOnuFWControlUpDownFlag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 7),
    _SleV2EponIMOnuFWControlUpDownFlag_Type()
)
sleV2EponIMOnuFWControlUpDownFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlUpDownFlag.setStatus("current")
_SleV2EponIMOnuFWControlUserId_Type = OctetString
_SleV2EponIMOnuFWControlUserId_Object = MibScalar
sleV2EponIMOnuFWControlUserId = _SleV2EponIMOnuFWControlUserId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 8),
    _SleV2EponIMOnuFWControlUserId_Type()
)
sleV2EponIMOnuFWControlUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlUserId.setStatus("current")
_SleV2EponIMOnuFWControlPassword_Type = OctetString
_SleV2EponIMOnuFWControlPassword_Object = MibScalar
sleV2EponIMOnuFWControlPassword = _SleV2EponIMOnuFWControlPassword_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 9),
    _SleV2EponIMOnuFWControlPassword_Type()
)
sleV2EponIMOnuFWControlPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlPassword.setStatus("current")
_SleV2EponIMOnuFWControlFileName_Type = OctetString
_SleV2EponIMOnuFWControlFileName_Object = MibScalar
sleV2EponIMOnuFWControlFileName = _SleV2EponIMOnuFWControlFileName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 10),
    _SleV2EponIMOnuFWControlFileName_Type()
)
sleV2EponIMOnuFWControlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlFileName.setStatus("current")


class _SleV2EponIMOnuFWControlUpdateCommitTime_Type(Integer32):
    """Custom type sleV2EponIMOnuFWControlUpdateCommitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_SleV2EponIMOnuFWControlUpdateCommitTime_Type.__name__ = "Integer32"
_SleV2EponIMOnuFWControlUpdateCommitTime_Object = MibScalar
sleV2EponIMOnuFWControlUpdateCommitTime = _SleV2EponIMOnuFWControlUpdateCommitTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 2, 11),
    _SleV2EponIMOnuFWControlUpdateCommitTime_Type()
)
sleV2EponIMOnuFWControlUpdateCommitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWControlUpdateCommitTime.setStatus("current")
_SleV2EponIMOnuFWNotification_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuFWNotification = _SleV2EponIMOnuFWNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 3)
)
_SleV2EponIMOnuBridge_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuBridge = _SleV2EponIMOnuBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2)
)
_SleV2EponIMOnuPort_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuPort = _SleV2EponIMOnuPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1)
)
_SleV2EponIMOnuPortTable_Object = MibTable
sleV2EponIMOnuPortTable = _SleV2EponIMOnuPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortTable.setStatus("current")
_SleV2EponIMOnuPortEntry_Object = MibTableRow
sleV2EponIMOnuPortEntry = _SleV2EponIMOnuPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1)
)
sleV2EponIMOnuPortEntry.setIndexNames(
    (0, "SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIndex"),
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEntry.setStatus("current")


class _SleV2EponIMOnuPortIndex_Type(Integer32):
    """Custom type sleV2EponIMOnuPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SleV2EponIMOnuPortIndex_Type.__name__ = "Integer32"
_SleV2EponIMOnuPortIndex_Object = MibTableColumn
sleV2EponIMOnuPortIndex = _SleV2EponIMOnuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 1),
    _SleV2EponIMOnuPortIndex_Type()
)
sleV2EponIMOnuPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIndex.setStatus("current")
_SleV2EponIMOnuPortId_Type = Integer32
_SleV2EponIMOnuPortId_Object = MibTableColumn
sleV2EponIMOnuPortId = _SleV2EponIMOnuPortId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 2),
    _SleV2EponIMOnuPortId_Type()
)
sleV2EponIMOnuPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortId.setStatus("current")
_SleV2EponIMOnuPortType_Type = EponPortType
_SleV2EponIMOnuPortType_Object = MibTableColumn
sleV2EponIMOnuPortType = _SleV2EponIMOnuPortType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 3),
    _SleV2EponIMOnuPortType_Type()
)
sleV2EponIMOnuPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortType.setStatus("current")
_SleV2EponIMOnuPortAdminStatus_Type = EponOnuLinkStatus
_SleV2EponIMOnuPortAdminStatus_Object = MibTableColumn
sleV2EponIMOnuPortAdminStatus = _SleV2EponIMOnuPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 4),
    _SleV2EponIMOnuPortAdminStatus_Type()
)
sleV2EponIMOnuPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortAdminStatus.setStatus("current")
_SleV2EponIMOnuPortOperStatus_Type = EponOnuLinkStatus
_SleV2EponIMOnuPortOperStatus_Object = MibTableColumn
sleV2EponIMOnuPortOperStatus = _SleV2EponIMOnuPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 5),
    _SleV2EponIMOnuPortOperStatus_Type()
)
sleV2EponIMOnuPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortOperStatus.setStatus("current")
_SleV2EponIMOnuPortLinkupTime_Type = OctetString
_SleV2EponIMOnuPortLinkupTime_Object = MibTableColumn
sleV2EponIMOnuPortLinkupTime = _SleV2EponIMOnuPortLinkupTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 6),
    _SleV2EponIMOnuPortLinkupTime_Type()
)
sleV2EponIMOnuPortLinkupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortLinkupTime.setStatus("current")
_SleV2EponIMOnuPortUpTime_Type = TimeTicks
_SleV2EponIMOnuPortUpTime_Object = MibTableColumn
sleV2EponIMOnuPortUpTime = _SleV2EponIMOnuPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 7),
    _SleV2EponIMOnuPortUpTime_Type()
)
sleV2EponIMOnuPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortUpTime.setStatus("current")
_SleV2EponIMOnuPortFECtxEnable_Type = EponOnuState
_SleV2EponIMOnuPortFECtxEnable_Object = MibTableColumn
sleV2EponIMOnuPortFECtxEnable = _SleV2EponIMOnuPortFECtxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 8),
    _SleV2EponIMOnuPortFECtxEnable_Type()
)
sleV2EponIMOnuPortFECtxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortFECtxEnable.setStatus("current")
_SleV2EponIMOnuPortFECrxEnable_Type = EponOnuState
_SleV2EponIMOnuPortFECrxEnable_Object = MibTableColumn
sleV2EponIMOnuPortFECrxEnable = _SleV2EponIMOnuPortFECrxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 9),
    _SleV2EponIMOnuPortFECrxEnable_Type()
)
sleV2EponIMOnuPortFECrxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortFECrxEnable.setStatus("current")
_SleV2EponIMOnuPortLaserAlwaysOn_Type = EponOnuState
_SleV2EponIMOnuPortLaserAlwaysOn_Object = MibTableColumn
sleV2EponIMOnuPortLaserAlwaysOn = _SleV2EponIMOnuPortLaserAlwaysOn_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 10),
    _SleV2EponIMOnuPortLaserAlwaysOn_Type()
)
sleV2EponIMOnuPortLaserAlwaysOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortLaserAlwaysOn.setStatus("current")
_SleV2EponIMOnuPortDropInMcastTraffic_Type = EponOnuState
_SleV2EponIMOnuPortDropInMcastTraffic_Object = MibTableColumn
sleV2EponIMOnuPortDropInMcastTraffic = _SleV2EponIMOnuPortDropInMcastTraffic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 11),
    _SleV2EponIMOnuPortDropInMcastTraffic_Type()
)
sleV2EponIMOnuPortDropInMcastTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortDropInMcastTraffic.setStatus("current")
_SleV2EponIMOnuPortDropInBcastTraffic_Type = EponOnuState
_SleV2EponIMOnuPortDropInBcastTraffic_Object = MibTableColumn
sleV2EponIMOnuPortDropInBcastTraffic = _SleV2EponIMOnuPortDropInBcastTraffic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 12),
    _SleV2EponIMOnuPortDropInBcastTraffic_Type()
)
sleV2EponIMOnuPortDropInBcastTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortDropInBcastTraffic.setStatus("current")
_SleV2EponIMOnuPortBlockDataTraffic_Type = EponOnuState
_SleV2EponIMOnuPortBlockDataTraffic_Object = MibTableColumn
sleV2EponIMOnuPortBlockDataTraffic = _SleV2EponIMOnuPortBlockDataTraffic_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 1, 1, 13),
    _SleV2EponIMOnuPortBlockDataTraffic_Type()
)
sleV2EponIMOnuPortBlockDataTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortBlockDataTraffic.setStatus("current")
_SleV2EponIMOnuPortControl_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuPortControl = _SleV2EponIMOnuPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 2)
)


class _SleV2EponIMOnuPortControlRequest_Type(Integer32):
    """Custom type sleV2EponIMOnuPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("changeAdminStatus", 1)
    )


_SleV2EponIMOnuPortControlRequest_Type.__name__ = "Integer32"
_SleV2EponIMOnuPortControlRequest_Object = MibScalar
sleV2EponIMOnuPortControlRequest = _SleV2EponIMOnuPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 2, 1),
    _SleV2EponIMOnuPortControlRequest_Type()
)
sleV2EponIMOnuPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortControlRequest.setStatus("current")
_SleV2EponIMOnuPortControlStatus_Type = SleControlStatusType
_SleV2EponIMOnuPortControlStatus_Object = MibScalar
sleV2EponIMOnuPortControlStatus = _SleV2EponIMOnuPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 2, 2),
    _SleV2EponIMOnuPortControlStatus_Type()
)
sleV2EponIMOnuPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortControlStatus.setStatus("current")
_SleV2EponIMOnuPortControlTimer_Type = Gauge32
_SleV2EponIMOnuPortControlTimer_Object = MibScalar
sleV2EponIMOnuPortControlTimer = _SleV2EponIMOnuPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 2, 3),
    _SleV2EponIMOnuPortControlTimer_Type()
)
sleV2EponIMOnuPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortControlTimer.setStatus("current")
_SleV2EponIMOnuPortControlTimeStamp_Type = TimeTicks
_SleV2EponIMOnuPortControlTimeStamp_Object = MibScalar
sleV2EponIMOnuPortControlTimeStamp = _SleV2EponIMOnuPortControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 2, 4),
    _SleV2EponIMOnuPortControlTimeStamp_Type()
)
sleV2EponIMOnuPortControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortControlTimeStamp.setStatus("current")
_SleV2EponIMOnuPortControlReqResult_Type = SleControlRequestResultType
_SleV2EponIMOnuPortControlReqResult_Object = MibScalar
sleV2EponIMOnuPortControlReqResult = _SleV2EponIMOnuPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 2, 5),
    _SleV2EponIMOnuPortControlReqResult_Type()
)
sleV2EponIMOnuPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortControlReqResult.setStatus("current")
_SleV2EponIMOnuPortControlAdminState_Type = EponOnuState
_SleV2EponIMOnuPortControlAdminState_Object = MibScalar
sleV2EponIMOnuPortControlAdminState = _SleV2EponIMOnuPortControlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 2, 6),
    _SleV2EponIMOnuPortControlAdminState_Type()
)
sleV2EponIMOnuPortControlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortControlAdminState.setStatus("current")
_SleV2EponIMOnuPortNotification_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuPortNotification = _SleV2EponIMOnuPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 3)
)
_SleV2EponIMOnuBridgeBase_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuBridgeBase = _SleV2EponIMOnuBridgeBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2)
)
_SleV2EponIMOnuBridgeInfo_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuBridgeInfo = _SleV2EponIMOnuBridgeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 1)
)
_SleV2EponIMOnuRxFlowCtrl_Type = EponOnuState
_SleV2EponIMOnuRxFlowCtrl_Object = MibScalar
sleV2EponIMOnuRxFlowCtrl = _SleV2EponIMOnuRxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 1, 1),
    _SleV2EponIMOnuRxFlowCtrl_Type()
)
sleV2EponIMOnuRxFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuRxFlowCtrl.setStatus("current")
_SleV2EponIMOnuTxFlowCtrl_Type = EponOnuState
_SleV2EponIMOnuTxFlowCtrl_Object = MibScalar
sleV2EponIMOnuTxFlowCtrl = _SleV2EponIMOnuTxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 1, 2),
    _SleV2EponIMOnuTxFlowCtrl_Type()
)
sleV2EponIMOnuTxFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuTxFlowCtrl.setStatus("current")


class _SleV2EponIMOnuFlowCtrlLowThreshold_Type(Integer32):
    """Custom type sleV2EponIMOnuFlowCtrlLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleV2EponIMOnuFlowCtrlLowThreshold_Type.__name__ = "Integer32"
_SleV2EponIMOnuFlowCtrlLowThreshold_Object = MibScalar
sleV2EponIMOnuFlowCtrlLowThreshold = _SleV2EponIMOnuFlowCtrlLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 1, 3),
    _SleV2EponIMOnuFlowCtrlLowThreshold_Type()
)
sleV2EponIMOnuFlowCtrlLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFlowCtrlLowThreshold.setStatus("current")


class _SleV2EponIMOnuFlowCtrlHighThreshold_Type(Integer32):
    """Custom type sleV2EponIMOnuFlowCtrlHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleV2EponIMOnuFlowCtrlHighThreshold_Type.__name__ = "Integer32"
_SleV2EponIMOnuFlowCtrlHighThreshold_Object = MibScalar
sleV2EponIMOnuFlowCtrlHighThreshold = _SleV2EponIMOnuFlowCtrlHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 1, 4),
    _SleV2EponIMOnuFlowCtrlHighThreshold_Type()
)
sleV2EponIMOnuFlowCtrlHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuFlowCtrlHighThreshold.setStatus("current")
_SleV2EponIMOnuBridgeControl_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuBridgeControl = _SleV2EponIMOnuBridgeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2)
)


class _SleV2EponIMOnuBridgeControlRequest_Type(Integer32):
    """Custom type sleV2EponIMOnuBridgeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setFlowControl", 1)
    )


_SleV2EponIMOnuBridgeControlRequest_Type.__name__ = "Integer32"
_SleV2EponIMOnuBridgeControlRequest_Object = MibScalar
sleV2EponIMOnuBridgeControlRequest = _SleV2EponIMOnuBridgeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 1),
    _SleV2EponIMOnuBridgeControlRequest_Type()
)
sleV2EponIMOnuBridgeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlRequest.setStatus("current")
_SleV2EponIMOnuBridgeControlStatus_Type = SleControlStatusType
_SleV2EponIMOnuBridgeControlStatus_Object = MibScalar
sleV2EponIMOnuBridgeControlStatus = _SleV2EponIMOnuBridgeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 2),
    _SleV2EponIMOnuBridgeControlStatus_Type()
)
sleV2EponIMOnuBridgeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlStatus.setStatus("current")
_SleV2EponIMOnuBridgeControlTimer_Type = Gauge32
_SleV2EponIMOnuBridgeControlTimer_Object = MibScalar
sleV2EponIMOnuBridgeControlTimer = _SleV2EponIMOnuBridgeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 3),
    _SleV2EponIMOnuBridgeControlTimer_Type()
)
sleV2EponIMOnuBridgeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlTimer.setStatus("current")
_SleV2EponIMOnuBridgeControlTimeStamp_Type = TimeTicks
_SleV2EponIMOnuBridgeControlTimeStamp_Object = MibScalar
sleV2EponIMOnuBridgeControlTimeStamp = _SleV2EponIMOnuBridgeControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 4),
    _SleV2EponIMOnuBridgeControlTimeStamp_Type()
)
sleV2EponIMOnuBridgeControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlTimeStamp.setStatus("current")
_SleV2EponIMOnuBridgeControlReqResult_Type = SleControlRequestResultType
_SleV2EponIMOnuBridgeControlReqResult_Object = MibScalar
sleV2EponIMOnuBridgeControlReqResult = _SleV2EponIMOnuBridgeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 5),
    _SleV2EponIMOnuBridgeControlReqResult_Type()
)
sleV2EponIMOnuBridgeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlReqResult.setStatus("current")
_SleV2EponIMOnuBridgeControlRxFlowCtrl_Type = EponOnuState
_SleV2EponIMOnuBridgeControlRxFlowCtrl_Object = MibScalar
sleV2EponIMOnuBridgeControlRxFlowCtrl = _SleV2EponIMOnuBridgeControlRxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 6),
    _SleV2EponIMOnuBridgeControlRxFlowCtrl_Type()
)
sleV2EponIMOnuBridgeControlRxFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlRxFlowCtrl.setStatus("current")
_SleV2EponIMOnuBridgeControlTxFlowCtrl_Type = EponOnuState
_SleV2EponIMOnuBridgeControlTxFlowCtrl_Object = MibScalar
sleV2EponIMOnuBridgeControlTxFlowCtrl = _SleV2EponIMOnuBridgeControlTxFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 7),
    _SleV2EponIMOnuBridgeControlTxFlowCtrl_Type()
)
sleV2EponIMOnuBridgeControlTxFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlTxFlowCtrl.setStatus("current")


class _SleV2EponIMOnuBridgeControlFlowCtrlLowThreshold_Type(Integer32):
    """Custom type sleV2EponIMOnuBridgeControlFlowCtrlLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleV2EponIMOnuBridgeControlFlowCtrlLowThreshold_Type.__name__ = "Integer32"
_SleV2EponIMOnuBridgeControlFlowCtrlLowThreshold_Object = MibScalar
sleV2EponIMOnuBridgeControlFlowCtrlLowThreshold = _SleV2EponIMOnuBridgeControlFlowCtrlLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 8),
    _SleV2EponIMOnuBridgeControlFlowCtrlLowThreshold_Type()
)
sleV2EponIMOnuBridgeControlFlowCtrlLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlFlowCtrlLowThreshold.setStatus("current")


class _SleV2EponIMOnuBridgeControlFlowCtrlHighThreshold_Type(Integer32):
    """Custom type sleV2EponIMOnuBridgeControlFlowCtrlHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SleV2EponIMOnuBridgeControlFlowCtrlHighThreshold_Type.__name__ = "Integer32"
_SleV2EponIMOnuBridgeControlFlowCtrlHighThreshold_Object = MibScalar
sleV2EponIMOnuBridgeControlFlowCtrlHighThreshold = _SleV2EponIMOnuBridgeControlFlowCtrlHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 2, 9),
    _SleV2EponIMOnuBridgeControlFlowCtrlHighThreshold_Type()
)
sleV2EponIMOnuBridgeControlFlowCtrlHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeControlFlowCtrlHighThreshold.setStatus("current")
_SleV2EponIMOnuBridgeNotification_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuBridgeNotification = _SleV2EponIMOnuBridgeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 3)
)
_SleV2EponIMOnuStats_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuStats = _SleV2EponIMOnuStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3)
)
_SleV2EponIMOnuPortStats_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuPortStats = _SleV2EponIMOnuPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1)
)
_SleV2EponIMOnuPortIfStatsTable_Object = MibTable
sleV2EponIMOnuPortIfStatsTable = _SleV2EponIMOnuPortIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfStatsTable.setStatus("current")
_SleV2EponIMOnuPortIfStatsEntry_Object = MibTableRow
sleV2EponIMOnuPortIfStatsEntry = _SleV2EponIMOnuPortIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1)
)
sleV2EponIMOnuPortIfStatsEntry.setIndexNames(
    (0, "SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIndex"),
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfStatsEntry.setStatus("current")
_SleV2EponIMOnuPortIfInOctets_Type = Counter64
_SleV2EponIMOnuPortIfInOctets_Object = MibTableColumn
sleV2EponIMOnuPortIfInOctets = _SleV2EponIMOnuPortIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 1),
    _SleV2EponIMOnuPortIfInOctets_Type()
)
sleV2EponIMOnuPortIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfInOctets.setStatus("current")
_SleV2EponIMOnuPortIfInUnicast_Type = Counter64
_SleV2EponIMOnuPortIfInUnicast_Object = MibTableColumn
sleV2EponIMOnuPortIfInUnicast = _SleV2EponIMOnuPortIfInUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 2),
    _SleV2EponIMOnuPortIfInUnicast_Type()
)
sleV2EponIMOnuPortIfInUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfInUnicast.setStatus("current")
_SleV2EponIMOnuPortIfInMulticast_Type = Counter64
_SleV2EponIMOnuPortIfInMulticast_Object = MibTableColumn
sleV2EponIMOnuPortIfInMulticast = _SleV2EponIMOnuPortIfInMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 3),
    _SleV2EponIMOnuPortIfInMulticast_Type()
)
sleV2EponIMOnuPortIfInMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfInMulticast.setStatus("current")
_SleV2EponIMOnuPortIfInBroadcast_Type = Counter64
_SleV2EponIMOnuPortIfInBroadcast_Object = MibTableColumn
sleV2EponIMOnuPortIfInBroadcast = _SleV2EponIMOnuPortIfInBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 4),
    _SleV2EponIMOnuPortIfInBroadcast_Type()
)
sleV2EponIMOnuPortIfInBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfInBroadcast.setStatus("current")
_SleV2EponIMOnuPortIfInDiscards_Type = Counter64
_SleV2EponIMOnuPortIfInDiscards_Object = MibTableColumn
sleV2EponIMOnuPortIfInDiscards = _SleV2EponIMOnuPortIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 5),
    _SleV2EponIMOnuPortIfInDiscards_Type()
)
sleV2EponIMOnuPortIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfInDiscards.setStatus("current")
_SleV2EponIMOnuPortIfInErrors_Type = Counter64
_SleV2EponIMOnuPortIfInErrors_Object = MibTableColumn
sleV2EponIMOnuPortIfInErrors = _SleV2EponIMOnuPortIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 6),
    _SleV2EponIMOnuPortIfInErrors_Type()
)
sleV2EponIMOnuPortIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfInErrors.setStatus("current")
_SleV2EponIMOnuPortIfInUnknownProtos_Type = Counter64
_SleV2EponIMOnuPortIfInUnknownProtos_Object = MibTableColumn
sleV2EponIMOnuPortIfInUnknownProtos = _SleV2EponIMOnuPortIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 7),
    _SleV2EponIMOnuPortIfInUnknownProtos_Type()
)
sleV2EponIMOnuPortIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfInUnknownProtos.setStatus("current")
_SleV2EponIMOnuPortIfOutOctets_Type = Counter64
_SleV2EponIMOnuPortIfOutOctets_Object = MibTableColumn
sleV2EponIMOnuPortIfOutOctets = _SleV2EponIMOnuPortIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 8),
    _SleV2EponIMOnuPortIfOutOctets_Type()
)
sleV2EponIMOnuPortIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfOutOctets.setStatus("current")
_SleV2EponIMOnuPortIfOutUnicast_Type = Counter64
_SleV2EponIMOnuPortIfOutUnicast_Object = MibTableColumn
sleV2EponIMOnuPortIfOutUnicast = _SleV2EponIMOnuPortIfOutUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 9),
    _SleV2EponIMOnuPortIfOutUnicast_Type()
)
sleV2EponIMOnuPortIfOutUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfOutUnicast.setStatus("current")
_SleV2EponIMOnuPortIfOutMulticast_Type = Counter64
_SleV2EponIMOnuPortIfOutMulticast_Object = MibTableColumn
sleV2EponIMOnuPortIfOutMulticast = _SleV2EponIMOnuPortIfOutMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 10),
    _SleV2EponIMOnuPortIfOutMulticast_Type()
)
sleV2EponIMOnuPortIfOutMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfOutMulticast.setStatus("current")
_SleV2EponIMOnuPortIfOutBroadcast_Type = Counter64
_SleV2EponIMOnuPortIfOutBroadcast_Object = MibTableColumn
sleV2EponIMOnuPortIfOutBroadcast = _SleV2EponIMOnuPortIfOutBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 11),
    _SleV2EponIMOnuPortIfOutBroadcast_Type()
)
sleV2EponIMOnuPortIfOutBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfOutBroadcast.setStatus("current")
_SleV2EponIMOnuPortIfOutDiscards_Type = Counter64
_SleV2EponIMOnuPortIfOutDiscards_Object = MibTableColumn
sleV2EponIMOnuPortIfOutDiscards = _SleV2EponIMOnuPortIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 12),
    _SleV2EponIMOnuPortIfOutDiscards_Type()
)
sleV2EponIMOnuPortIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfOutDiscards.setStatus("current")
_SleV2EponIMOnuPortIfOutErrors_Type = Counter64
_SleV2EponIMOnuPortIfOutErrors_Object = MibTableColumn
sleV2EponIMOnuPortIfOutErrors = _SleV2EponIMOnuPortIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 1, 1, 13),
    _SleV2EponIMOnuPortIfOutErrors_Type()
)
sleV2EponIMOnuPortIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortIfOutErrors.setStatus("current")
_SleV2EponIMOnuPortEtherStatsTable_Object = MibTable
sleV2EponIMOnuPortEtherStatsTable = _SleV2EponIMOnuPortEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherStatsTable.setStatus("current")
_SleV2EponIMOnuPortEtherStatsEntry_Object = MibTableRow
sleV2EponIMOnuPortEtherStatsEntry = _SleV2EponIMOnuPortEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1)
)
sleV2EponIMOnuPortEtherStatsEntry.setIndexNames(
    (0, "SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIndex"),
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherStatsEntry.setStatus("current")
_SleV2EponIMOnuPortEtherAlignmentErrors_Type = Counter64
_SleV2EponIMOnuPortEtherAlignmentErrors_Object = MibTableColumn
sleV2EponIMOnuPortEtherAlignmentErrors = _SleV2EponIMOnuPortEtherAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 1),
    _SleV2EponIMOnuPortEtherAlignmentErrors_Type()
)
sleV2EponIMOnuPortEtherAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherAlignmentErrors.setStatus("current")
_SleV2EponIMOnuPortEtherFcsErrors_Type = Counter64
_SleV2EponIMOnuPortEtherFcsErrors_Object = MibTableColumn
sleV2EponIMOnuPortEtherFcsErrors = _SleV2EponIMOnuPortEtherFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 2),
    _SleV2EponIMOnuPortEtherFcsErrors_Type()
)
sleV2EponIMOnuPortEtherFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherFcsErrors.setStatus("current")
_SleV2EponIMOnuPortEtherSingleCollision_Type = Counter32
_SleV2EponIMOnuPortEtherSingleCollision_Object = MibTableColumn
sleV2EponIMOnuPortEtherSingleCollision = _SleV2EponIMOnuPortEtherSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 3),
    _SleV2EponIMOnuPortEtherSingleCollision_Type()
)
sleV2EponIMOnuPortEtherSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherSingleCollision.setStatus("current")
_SleV2EponIMOnuPortEtherMultipleCollision_Type = Counter32
_SleV2EponIMOnuPortEtherMultipleCollision_Object = MibTableColumn
sleV2EponIMOnuPortEtherMultipleCollision = _SleV2EponIMOnuPortEtherMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 4),
    _SleV2EponIMOnuPortEtherMultipleCollision_Type()
)
sleV2EponIMOnuPortEtherMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherMultipleCollision.setStatus("current")
_SleV2EponIMOnuPortEtherSqeTestErrors_Type = Counter32
_SleV2EponIMOnuPortEtherSqeTestErrors_Object = MibTableColumn
sleV2EponIMOnuPortEtherSqeTestErrors = _SleV2EponIMOnuPortEtherSqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 5),
    _SleV2EponIMOnuPortEtherSqeTestErrors_Type()
)
sleV2EponIMOnuPortEtherSqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherSqeTestErrors.setStatus("current")
_SleV2EponIMOnuPortEtherDeferredTransmissions_Type = Counter32
_SleV2EponIMOnuPortEtherDeferredTransmissions_Object = MibTableColumn
sleV2EponIMOnuPortEtherDeferredTransmissions = _SleV2EponIMOnuPortEtherDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 6),
    _SleV2EponIMOnuPortEtherDeferredTransmissions_Type()
)
sleV2EponIMOnuPortEtherDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherDeferredTransmissions.setStatus("current")
_SleV2EponIMOnuPortEtherLateCollisions_Type = Counter32
_SleV2EponIMOnuPortEtherLateCollisions_Object = MibTableColumn
sleV2EponIMOnuPortEtherLateCollisions = _SleV2EponIMOnuPortEtherLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 7),
    _SleV2EponIMOnuPortEtherLateCollisions_Type()
)
sleV2EponIMOnuPortEtherLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherLateCollisions.setStatus("current")
_SleV2EponIMOnuPortEtherExcessiveCollisions_Type = Counter32
_SleV2EponIMOnuPortEtherExcessiveCollisions_Object = MibTableColumn
sleV2EponIMOnuPortEtherExcessiveCollisions = _SleV2EponIMOnuPortEtherExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 8),
    _SleV2EponIMOnuPortEtherExcessiveCollisions_Type()
)
sleV2EponIMOnuPortEtherExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherExcessiveCollisions.setStatus("current")
_SleV2EponIMOnuPortEtherInternalMacTxErrors_Type = Counter64
_SleV2EponIMOnuPortEtherInternalMacTxErrors_Object = MibTableColumn
sleV2EponIMOnuPortEtherInternalMacTxErrors = _SleV2EponIMOnuPortEtherInternalMacTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 9),
    _SleV2EponIMOnuPortEtherInternalMacTxErrors_Type()
)
sleV2EponIMOnuPortEtherInternalMacTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherInternalMacTxErrors.setStatus("current")
_SleV2EponIMOnuPortEtherCarrierSenseErrors_Type = Counter32
_SleV2EponIMOnuPortEtherCarrierSenseErrors_Object = MibTableColumn
sleV2EponIMOnuPortEtherCarrierSenseErrors = _SleV2EponIMOnuPortEtherCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 10),
    _SleV2EponIMOnuPortEtherCarrierSenseErrors_Type()
)
sleV2EponIMOnuPortEtherCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherCarrierSenseErrors.setStatus("current")
_SleV2EponIMOnuPortEtherFrameTooLongs_Type = Counter64
_SleV2EponIMOnuPortEtherFrameTooLongs_Object = MibTableColumn
sleV2EponIMOnuPortEtherFrameTooLongs = _SleV2EponIMOnuPortEtherFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 11),
    _SleV2EponIMOnuPortEtherFrameTooLongs_Type()
)
sleV2EponIMOnuPortEtherFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherFrameTooLongs.setStatus("current")
_SleV2EponIMOnuPortEtherInternalMacRxErrors_Type = Counter64
_SleV2EponIMOnuPortEtherInternalMacRxErrors_Object = MibTableColumn
sleV2EponIMOnuPortEtherInternalMacRxErrors = _SleV2EponIMOnuPortEtherInternalMacRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 12),
    _SleV2EponIMOnuPortEtherInternalMacRxErrors_Type()
)
sleV2EponIMOnuPortEtherInternalMacRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherInternalMacRxErrors.setStatus("current")
_SleV2EponIMOnuPortEtherSymbolErrors_Type = Counter64
_SleV2EponIMOnuPortEtherSymbolErrors_Object = MibTableColumn
sleV2EponIMOnuPortEtherSymbolErrors = _SleV2EponIMOnuPortEtherSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 13),
    _SleV2EponIMOnuPortEtherSymbolErrors_Type()
)
sleV2EponIMOnuPortEtherSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherSymbolErrors.setStatus("current")
_SleV2EponIMOnuPortEtherInUnknownOpcode_Type = Counter64
_SleV2EponIMOnuPortEtherInUnknownOpcode_Object = MibTableColumn
sleV2EponIMOnuPortEtherInUnknownOpcode = _SleV2EponIMOnuPortEtherInUnknownOpcode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 14),
    _SleV2EponIMOnuPortEtherInUnknownOpcode_Type()
)
sleV2EponIMOnuPortEtherInUnknownOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherInUnknownOpcode.setStatus("current")
_SleV2EponIMOnuPortEtherInPauseFrames_Type = Counter64
_SleV2EponIMOnuPortEtherInPauseFrames_Object = MibTableColumn
sleV2EponIMOnuPortEtherInPauseFrames = _SleV2EponIMOnuPortEtherInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 15),
    _SleV2EponIMOnuPortEtherInPauseFrames_Type()
)
sleV2EponIMOnuPortEtherInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherInPauseFrames.setStatus("current")
_SleV2EponIMOnuPortEtherOutPauseFrames_Type = Counter64
_SleV2EponIMOnuPortEtherOutPauseFrames_Object = MibTableColumn
sleV2EponIMOnuPortEtherOutPauseFrames = _SleV2EponIMOnuPortEtherOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 2, 1, 16),
    _SleV2EponIMOnuPortEtherOutPauseFrames_Type()
)
sleV2EponIMOnuPortEtherOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEtherOutPauseFrames.setStatus("current")
_SleV2EponIMOnuPortEponStatsTable_Object = MibTable
sleV2EponIMOnuPortEponStatsTable = _SleV2EponIMOnuPortEponStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3)
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponStatsTable.setStatus("current")
_SleV2EponIMOnuPortEponStatsEntry_Object = MibTableRow
sleV2EponIMOnuPortEponStatsEntry = _SleV2EponIMOnuPortEponStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1)
)
sleV2EponIMOnuPortEponStatsEntry.setIndexNames(
    (0, "SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIndex"),
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponStatsEntry.setStatus("current")
_SleV2EponIMOnuPortEponMacCtrlFrameRx_Type = Counter32
_SleV2EponIMOnuPortEponMacCtrlFrameRx_Object = MibTableColumn
sleV2EponIMOnuPortEponMacCtrlFrameRx = _SleV2EponIMOnuPortEponMacCtrlFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 1),
    _SleV2EponIMOnuPortEponMacCtrlFrameRx_Type()
)
sleV2EponIMOnuPortEponMacCtrlFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponMacCtrlFrameRx.setStatus("current")
_SleV2EponIMOnuPortEponDiscWindowsSent_Type = Counter32
_SleV2EponIMOnuPortEponDiscWindowsSent_Object = MibTableColumn
sleV2EponIMOnuPortEponDiscWindowsSent = _SleV2EponIMOnuPortEponDiscWindowsSent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 2),
    _SleV2EponIMOnuPortEponDiscWindowsSent_Type()
)
sleV2EponIMOnuPortEponDiscWindowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponDiscWindowsSent.setStatus("current")
_SleV2EponIMOnuPortEponDiscTimeout_Type = Counter32
_SleV2EponIMOnuPortEponDiscTimeout_Object = MibTableColumn
sleV2EponIMOnuPortEponDiscTimeout = _SleV2EponIMOnuPortEponDiscTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 3),
    _SleV2EponIMOnuPortEponDiscTimeout_Type()
)
sleV2EponIMOnuPortEponDiscTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponDiscTimeout.setStatus("current")
_SleV2EponIMOnuPortEponTxRegRequest_Type = Counter32
_SleV2EponIMOnuPortEponTxRegRequest_Object = MibTableColumn
sleV2EponIMOnuPortEponTxRegRequest = _SleV2EponIMOnuPortEponTxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 4),
    _SleV2EponIMOnuPortEponTxRegRequest_Type()
)
sleV2EponIMOnuPortEponTxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponTxRegRequest.setStatus("current")
_SleV2EponIMOnuPortEponRxReqRequest_Type = Counter32
_SleV2EponIMOnuPortEponRxReqRequest_Object = MibTableColumn
sleV2EponIMOnuPortEponRxReqRequest = _SleV2EponIMOnuPortEponRxReqRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 5),
    _SleV2EponIMOnuPortEponRxReqRequest_Type()
)
sleV2EponIMOnuPortEponRxReqRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponRxReqRequest.setStatus("current")
_SleV2EponIMOnuPortEponTxReqAck_Type = Counter32
_SleV2EponIMOnuPortEponTxReqAck_Object = MibTableColumn
sleV2EponIMOnuPortEponTxReqAck = _SleV2EponIMOnuPortEponTxReqAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 6),
    _SleV2EponIMOnuPortEponTxReqAck_Type()
)
sleV2EponIMOnuPortEponTxReqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponTxReqAck.setStatus("current")
_SleV2EponIMOnuPortEponRxReqAck_Type = Counter32
_SleV2EponIMOnuPortEponRxReqAck_Object = MibTableColumn
sleV2EponIMOnuPortEponRxReqAck = _SleV2EponIMOnuPortEponRxReqAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 7),
    _SleV2EponIMOnuPortEponRxReqAck_Type()
)
sleV2EponIMOnuPortEponRxReqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponRxReqAck.setStatus("current")
_SleV2EponIMOnuPortEponTxReport_Type = Counter32
_SleV2EponIMOnuPortEponTxReport_Object = MibTableColumn
sleV2EponIMOnuPortEponTxReport = _SleV2EponIMOnuPortEponTxReport_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 8),
    _SleV2EponIMOnuPortEponTxReport_Type()
)
sleV2EponIMOnuPortEponTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponTxReport.setStatus("current")
_SleV2EponIMOnuPortEponRxReport_Type = Counter32
_SleV2EponIMOnuPortEponRxReport_Object = MibTableColumn
sleV2EponIMOnuPortEponRxReport = _SleV2EponIMOnuPortEponRxReport_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 9),
    _SleV2EponIMOnuPortEponRxReport_Type()
)
sleV2EponIMOnuPortEponRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponRxReport.setStatus("current")
_SleV2EponIMOnuPortEponTxGate_Type = Counter32
_SleV2EponIMOnuPortEponTxGate_Object = MibTableColumn
sleV2EponIMOnuPortEponTxGate = _SleV2EponIMOnuPortEponTxGate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 10),
    _SleV2EponIMOnuPortEponTxGate_Type()
)
sleV2EponIMOnuPortEponTxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponTxGate.setStatus("current")
_SleV2EponIMOnuPortEponRxGate_Type = Counter32
_SleV2EponIMOnuPortEponRxGate_Object = MibTableColumn
sleV2EponIMOnuPortEponRxGate = _SleV2EponIMOnuPortEponRxGate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 11),
    _SleV2EponIMOnuPortEponRxGate_Type()
)
sleV2EponIMOnuPortEponRxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponRxGate.setStatus("current")
_SleV2EponIMOnuPortEponTxRegister_Type = Counter32
_SleV2EponIMOnuPortEponTxRegister_Object = MibTableColumn
sleV2EponIMOnuPortEponTxRegister = _SleV2EponIMOnuPortEponTxRegister_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 12),
    _SleV2EponIMOnuPortEponTxRegister_Type()
)
sleV2EponIMOnuPortEponTxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponTxRegister.setStatus("current")
_SleV2EponIMOnuPortEponRxRegister_Type = Counter32
_SleV2EponIMOnuPortEponRxRegister_Object = MibTableColumn
sleV2EponIMOnuPortEponRxRegister = _SleV2EponIMOnuPortEponRxRegister_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 13),
    _SleV2EponIMOnuPortEponRxRegister_Type()
)
sleV2EponIMOnuPortEponRxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponRxRegister.setStatus("current")
_SleV2EponIMOnuPortEponRxNotSupported_Type = Counter32
_SleV2EponIMOnuPortEponRxNotSupported_Object = MibTableColumn
sleV2EponIMOnuPortEponRxNotSupported = _SleV2EponIMOnuPortEponRxNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 14),
    _SleV2EponIMOnuPortEponRxNotSupported_Type()
)
sleV2EponIMOnuPortEponRxNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponRxNotSupported.setStatus("current")
_SleV2EponIMOnuPortEponSldErrors_Type = Counter32
_SleV2EponIMOnuPortEponSldErrors_Object = MibTableColumn
sleV2EponIMOnuPortEponSldErrors = _SleV2EponIMOnuPortEponSldErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 15),
    _SleV2EponIMOnuPortEponSldErrors_Type()
)
sleV2EponIMOnuPortEponSldErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponSldErrors.setStatus("current")
_SleV2EponIMOnuPortEponCrc8Errors_Type = Counter32
_SleV2EponIMOnuPortEponCrc8Errors_Object = MibTableColumn
sleV2EponIMOnuPortEponCrc8Errors = _SleV2EponIMOnuPortEponCrc8Errors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 16),
    _SleV2EponIMOnuPortEponCrc8Errors_Type()
)
sleV2EponIMOnuPortEponCrc8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponCrc8Errors.setStatus("current")
_SleV2EponIMOnuPortEponBadLlid_Type = Counter32
_SleV2EponIMOnuPortEponBadLlid_Object = MibTableColumn
sleV2EponIMOnuPortEponBadLlid = _SleV2EponIMOnuPortEponBadLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 17),
    _SleV2EponIMOnuPortEponBadLlid_Type()
)
sleV2EponIMOnuPortEponBadLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponBadLlid.setStatus("current")
_SleV2EponIMOnuPortEponGoodLlid_Type = Counter32
_SleV2EponIMOnuPortEponGoodLlid_Object = MibTableColumn
sleV2EponIMOnuPortEponGoodLlid = _SleV2EponIMOnuPortEponGoodLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 18),
    _SleV2EponIMOnuPortEponGoodLlid_Type()
)
sleV2EponIMOnuPortEponGoodLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponGoodLlid.setStatus("current")
_SleV2EponIMOnuPortEponOnuPonCastLlid_Type = Counter32
_SleV2EponIMOnuPortEponOnuPonCastLlid_Object = MibTableColumn
sleV2EponIMOnuPortEponOnuPonCastLlid = _SleV2EponIMOnuPortEponOnuPonCastLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 19),
    _SleV2EponIMOnuPortEponOnuPonCastLlid_Type()
)
sleV2EponIMOnuPortEponOnuPonCastLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponOnuPonCastLlid.setStatus("current")
_SleV2EponIMOnuPortEponOltPonCastLlid_Type = Counter32
_SleV2EponIMOnuPortEponOltPonCastLlid_Object = MibTableColumn
sleV2EponIMOnuPortEponOltPonCastLlid = _SleV2EponIMOnuPortEponOltPonCastLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 20),
    _SleV2EponIMOnuPortEponOltPonCastLlid_Type()
)
sleV2EponIMOnuPortEponOltPonCastLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponOltPonCastLlid.setStatus("current")
_SleV2EponIMOnuPortEponBcastLlidNotOnuId_Type = Counter32
_SleV2EponIMOnuPortEponBcastLlidNotOnuId_Object = MibTableColumn
sleV2EponIMOnuPortEponBcastLlidNotOnuId = _SleV2EponIMOnuPortEponBcastLlidNotOnuId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 21),
    _SleV2EponIMOnuPortEponBcastLlidNotOnuId_Type()
)
sleV2EponIMOnuPortEponBcastLlidNotOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponBcastLlidNotOnuId.setStatus("current")
_SleV2EponIMOnuPortEponOnuLlidNotBcast_Type = Counter32
_SleV2EponIMOnuPortEponOnuLlidNotBcast_Object = MibTableColumn
sleV2EponIMOnuPortEponOnuLlidNotBcast = _SleV2EponIMOnuPortEponOnuLlidNotBcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 22),
    _SleV2EponIMOnuPortEponOnuLlidNotBcast_Type()
)
sleV2EponIMOnuPortEponOnuLlidNotBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponOnuLlidNotBcast.setStatus("current")
_SleV2EponIMOnuPortEponBcastLlidPlusOnuId_Type = Counter32
_SleV2EponIMOnuPortEponBcastLlidPlusOnuId_Object = MibTableColumn
sleV2EponIMOnuPortEponBcastLlidPlusOnuId = _SleV2EponIMOnuPortEponBcastLlidPlusOnuId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 23),
    _SleV2EponIMOnuPortEponBcastLlidPlusOnuId_Type()
)
sleV2EponIMOnuPortEponBcastLlidPlusOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponBcastLlidPlusOnuId.setStatus("current")
_SleV2EponIMOnuPortEponNotBcastLlidNotOnuId_Type = Counter32
_SleV2EponIMOnuPortEponNotBcastLlidNotOnuId_Object = MibTableColumn
sleV2EponIMOnuPortEponNotBcastLlidNotOnuId = _SleV2EponIMOnuPortEponNotBcastLlidNotOnuId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 24),
    _SleV2EponIMOnuPortEponNotBcastLlidNotOnuId_Type()
)
sleV2EponIMOnuPortEponNotBcastLlidNotOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponNotBcastLlidNotOnuId.setStatus("current")
_SleV2EponIMOnuPortEponPcsCodingViolation_Type = Counter32
_SleV2EponIMOnuPortEponPcsCodingViolation_Object = MibTableColumn
sleV2EponIMOnuPortEponPcsCodingViolation = _SleV2EponIMOnuPortEponPcsCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 25),
    _SleV2EponIMOnuPortEponPcsCodingViolation_Type()
)
sleV2EponIMOnuPortEponPcsCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponPcsCodingViolation.setStatus("current")
_SleV2EponIMOnuPortEponFecCorrectedBlocks_Type = Counter32
_SleV2EponIMOnuPortEponFecCorrectedBlocks_Object = MibTableColumn
sleV2EponIMOnuPortEponFecCorrectedBlocks = _SleV2EponIMOnuPortEponFecCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 26),
    _SleV2EponIMOnuPortEponFecCorrectedBlocks_Type()
)
sleV2EponIMOnuPortEponFecCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponFecCorrectedBlocks.setStatus("current")
_SleV2EponIMOnuPortEponFecUnCorrectedBlocks_Type = Counter32
_SleV2EponIMOnuPortEponFecUnCorrectedBlocks_Object = MibTableColumn
sleV2EponIMOnuPortEponFecUnCorrectedBlocks = _SleV2EponIMOnuPortEponFecUnCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 27),
    _SleV2EponIMOnuPortEponFecUnCorrectedBlocks_Type()
)
sleV2EponIMOnuPortEponFecUnCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponFecUnCorrectedBlocks.setStatus("current")
_SleV2EponIMOnuPortEponBufferHeadCodingViolation_Type = Counter32
_SleV2EponIMOnuPortEponBufferHeadCodingViolation_Object = MibTableColumn
sleV2EponIMOnuPortEponBufferHeadCodingViolation = _SleV2EponIMOnuPortEponBufferHeadCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 3, 1, 28),
    _SleV2EponIMOnuPortEponBufferHeadCodingViolation_Type()
)
sleV2EponIMOnuPortEponBufferHeadCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortEponBufferHeadCodingViolation.setStatus("current")
_SleV2EponIMOnuPortStatsControl_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuPortStatsControl = _SleV2EponIMOnuPortStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 4)
)


class _SleV2EponIMOnuPortStatsControlRequest_Type(Integer32):
    """Custom type sleV2EponIMOnuPortStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearPortStats", 1)
    )


_SleV2EponIMOnuPortStatsControlRequest_Type.__name__ = "Integer32"
_SleV2EponIMOnuPortStatsControlRequest_Object = MibScalar
sleV2EponIMOnuPortStatsControlRequest = _SleV2EponIMOnuPortStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 4, 1),
    _SleV2EponIMOnuPortStatsControlRequest_Type()
)
sleV2EponIMOnuPortStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortStatsControlRequest.setStatus("current")
_SleV2EponIMOnuPortStatsControlStatus_Type = SleControlStatusType
_SleV2EponIMOnuPortStatsControlStatus_Object = MibScalar
sleV2EponIMOnuPortStatsControlStatus = _SleV2EponIMOnuPortStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 4, 2),
    _SleV2EponIMOnuPortStatsControlStatus_Type()
)
sleV2EponIMOnuPortStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortStatsControlStatus.setStatus("current")
_SleV2EponIMOnuPortStatsControlTimer_Type = Gauge32
_SleV2EponIMOnuPortStatsControlTimer_Object = MibScalar
sleV2EponIMOnuPortStatsControlTimer = _SleV2EponIMOnuPortStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 4, 3),
    _SleV2EponIMOnuPortStatsControlTimer_Type()
)
sleV2EponIMOnuPortStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortStatsControlTimer.setStatus("current")
_SleV2EponIMOnuPortStatsControlTimeStamp_Type = TimeTicks
_SleV2EponIMOnuPortStatsControlTimeStamp_Object = MibScalar
sleV2EponIMOnuPortStatsControlTimeStamp = _SleV2EponIMOnuPortStatsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 4, 4),
    _SleV2EponIMOnuPortStatsControlTimeStamp_Type()
)
sleV2EponIMOnuPortStatsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortStatsControlTimeStamp.setStatus("current")
_SleV2EponIMOnuPortStatsControlReqResult_Type = SleControlRequestResultType
_SleV2EponIMOnuPortStatsControlReqResult_Object = MibScalar
sleV2EponIMOnuPortStatsControlReqResult = _SleV2EponIMOnuPortStatsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 4, 5),
    _SleV2EponIMOnuPortStatsControlReqResult_Type()
)
sleV2EponIMOnuPortStatsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortStatsControlReqResult.setStatus("current")
_SleV2EponIMOnuPortStatsControlPortIndex_Type = Integer32
_SleV2EponIMOnuPortStatsControlPortIndex_Object = MibScalar
sleV2EponIMOnuPortStatsControlPortIndex = _SleV2EponIMOnuPortStatsControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 4, 6),
    _SleV2EponIMOnuPortStatsControlPortIndex_Type()
)
sleV2EponIMOnuPortStatsControlPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortStatsControlPortIndex.setStatus("current")
_SleV2EponIMOnuPortStatsNotification_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuPortStatsNotification = _SleV2EponIMOnuPortStatsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 5)
)
_SleV2EponIMOnuLlidStats_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuLlidStats = _SleV2EponIMOnuLlidStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2)
)
_SleV2EponIMOnuLlidIfStats_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuLlidIfStats = _SleV2EponIMOnuLlidIfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1)
)
_SleV2EponIMOnuLlidIfInOctets_Type = Counter64
_SleV2EponIMOnuLlidIfInOctets_Object = MibScalar
sleV2EponIMOnuLlidIfInOctets = _SleV2EponIMOnuLlidIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 1),
    _SleV2EponIMOnuLlidIfInOctets_Type()
)
sleV2EponIMOnuLlidIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfInOctets.setStatus("current")
_SleV2EponIMOnuLlidIfInUnicast_Type = Counter64
_SleV2EponIMOnuLlidIfInUnicast_Object = MibScalar
sleV2EponIMOnuLlidIfInUnicast = _SleV2EponIMOnuLlidIfInUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 2),
    _SleV2EponIMOnuLlidIfInUnicast_Type()
)
sleV2EponIMOnuLlidIfInUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfInUnicast.setStatus("current")
_SleV2EponIMOnuLlidIfInMulticast_Type = Counter64
_SleV2EponIMOnuLlidIfInMulticast_Object = MibScalar
sleV2EponIMOnuLlidIfInMulticast = _SleV2EponIMOnuLlidIfInMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 3),
    _SleV2EponIMOnuLlidIfInMulticast_Type()
)
sleV2EponIMOnuLlidIfInMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfInMulticast.setStatus("current")
_SleV2EponIMOnuLlidIfInBroadcast_Type = Counter64
_SleV2EponIMOnuLlidIfInBroadcast_Object = MibScalar
sleV2EponIMOnuLlidIfInBroadcast = _SleV2EponIMOnuLlidIfInBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 4),
    _SleV2EponIMOnuLlidIfInBroadcast_Type()
)
sleV2EponIMOnuLlidIfInBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfInBroadcast.setStatus("current")
_SleV2EponIMOnuLlidIfInDiscards_Type = Counter64
_SleV2EponIMOnuLlidIfInDiscards_Object = MibScalar
sleV2EponIMOnuLlidIfInDiscards = _SleV2EponIMOnuLlidIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 5),
    _SleV2EponIMOnuLlidIfInDiscards_Type()
)
sleV2EponIMOnuLlidIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfInDiscards.setStatus("current")
_SleV2EponIMOnuLlidIfInErrors_Type = Counter64
_SleV2EponIMOnuLlidIfInErrors_Object = MibScalar
sleV2EponIMOnuLlidIfInErrors = _SleV2EponIMOnuLlidIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 6),
    _SleV2EponIMOnuLlidIfInErrors_Type()
)
sleV2EponIMOnuLlidIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfInErrors.setStatus("current")
_SleV2EponIMOnuLlidIfInUnknownProtos_Type = Counter64
_SleV2EponIMOnuLlidIfInUnknownProtos_Object = MibScalar
sleV2EponIMOnuLlidIfInUnknownProtos = _SleV2EponIMOnuLlidIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 7),
    _SleV2EponIMOnuLlidIfInUnknownProtos_Type()
)
sleV2EponIMOnuLlidIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfInUnknownProtos.setStatus("current")
_SleV2EponIMOnuLlidIfOutOctets_Type = Counter64
_SleV2EponIMOnuLlidIfOutOctets_Object = MibScalar
sleV2EponIMOnuLlidIfOutOctets = _SleV2EponIMOnuLlidIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 8),
    _SleV2EponIMOnuLlidIfOutOctets_Type()
)
sleV2EponIMOnuLlidIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfOutOctets.setStatus("current")
_SleV2EponIMOnuLlidIfOutUnicast_Type = Counter64
_SleV2EponIMOnuLlidIfOutUnicast_Object = MibScalar
sleV2EponIMOnuLlidIfOutUnicast = _SleV2EponIMOnuLlidIfOutUnicast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 9),
    _SleV2EponIMOnuLlidIfOutUnicast_Type()
)
sleV2EponIMOnuLlidIfOutUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfOutUnicast.setStatus("current")
_SleV2EponIMOnuLlidIfOutMulticast_Type = Counter64
_SleV2EponIMOnuLlidIfOutMulticast_Object = MibScalar
sleV2EponIMOnuLlidIfOutMulticast = _SleV2EponIMOnuLlidIfOutMulticast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 10),
    _SleV2EponIMOnuLlidIfOutMulticast_Type()
)
sleV2EponIMOnuLlidIfOutMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfOutMulticast.setStatus("current")
_SleV2EponIMOnuLlidIfOutBroadcast_Type = Counter64
_SleV2EponIMOnuLlidIfOutBroadcast_Object = MibScalar
sleV2EponIMOnuLlidIfOutBroadcast = _SleV2EponIMOnuLlidIfOutBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 11),
    _SleV2EponIMOnuLlidIfOutBroadcast_Type()
)
sleV2EponIMOnuLlidIfOutBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfOutBroadcast.setStatus("current")
_SleV2EponIMOnuLlidIfOutDiscards_Type = Counter64
_SleV2EponIMOnuLlidIfOutDiscards_Object = MibScalar
sleV2EponIMOnuLlidIfOutDiscards = _SleV2EponIMOnuLlidIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 12),
    _SleV2EponIMOnuLlidIfOutDiscards_Type()
)
sleV2EponIMOnuLlidIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfOutDiscards.setStatus("current")
_SleV2EponIMOnuLlidIfOutErrors_Type = Counter64
_SleV2EponIMOnuLlidIfOutErrors_Object = MibScalar
sleV2EponIMOnuLlidIfOutErrors = _SleV2EponIMOnuLlidIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 1, 13),
    _SleV2EponIMOnuLlidIfOutErrors_Type()
)
sleV2EponIMOnuLlidIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidIfOutErrors.setStatus("current")
_SleV2EponIMOnuLlidEponStats_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuLlidEponStats = _SleV2EponIMOnuLlidEponStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2)
)
_SleV2EponIMOnuLlidEponMacCtrlFrameRx_Type = Counter32
_SleV2EponIMOnuLlidEponMacCtrlFrameRx_Object = MibScalar
sleV2EponIMOnuLlidEponMacCtrlFrameRx = _SleV2EponIMOnuLlidEponMacCtrlFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 1),
    _SleV2EponIMOnuLlidEponMacCtrlFrameRx_Type()
)
sleV2EponIMOnuLlidEponMacCtrlFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponMacCtrlFrameRx.setStatus("current")
_SleV2EponIMOnuLlidEponDiscWindowsSent_Type = Counter32
_SleV2EponIMOnuLlidEponDiscWindowsSent_Object = MibScalar
sleV2EponIMOnuLlidEponDiscWindowsSent = _SleV2EponIMOnuLlidEponDiscWindowsSent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 2),
    _SleV2EponIMOnuLlidEponDiscWindowsSent_Type()
)
sleV2EponIMOnuLlidEponDiscWindowsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponDiscWindowsSent.setStatus("current")
_SleV2EponIMOnuLlidEponDiscTimeout_Type = Counter32
_SleV2EponIMOnuLlidEponDiscTimeout_Object = MibScalar
sleV2EponIMOnuLlidEponDiscTimeout = _SleV2EponIMOnuLlidEponDiscTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 3),
    _SleV2EponIMOnuLlidEponDiscTimeout_Type()
)
sleV2EponIMOnuLlidEponDiscTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponDiscTimeout.setStatus("current")
_SleV2EponIMOnuLlidEponTxRegRequest_Type = Counter32
_SleV2EponIMOnuLlidEponTxRegRequest_Object = MibScalar
sleV2EponIMOnuLlidEponTxRegRequest = _SleV2EponIMOnuLlidEponTxRegRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 4),
    _SleV2EponIMOnuLlidEponTxRegRequest_Type()
)
sleV2EponIMOnuLlidEponTxRegRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponTxRegRequest.setStatus("current")
_SleV2EponIMOnuLlidEponRxReqRequest_Type = Counter32
_SleV2EponIMOnuLlidEponRxReqRequest_Object = MibScalar
sleV2EponIMOnuLlidEponRxReqRequest = _SleV2EponIMOnuLlidEponRxReqRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 5),
    _SleV2EponIMOnuLlidEponRxReqRequest_Type()
)
sleV2EponIMOnuLlidEponRxReqRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponRxReqRequest.setStatus("current")
_SleV2EponIMOnuLlidEponTxReqAck_Type = Counter32
_SleV2EponIMOnuLlidEponTxReqAck_Object = MibScalar
sleV2EponIMOnuLlidEponTxReqAck = _SleV2EponIMOnuLlidEponTxReqAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 6),
    _SleV2EponIMOnuLlidEponTxReqAck_Type()
)
sleV2EponIMOnuLlidEponTxReqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponTxReqAck.setStatus("current")
_SleV2EponIMOnuLlidEponRxReqAck_Type = Counter32
_SleV2EponIMOnuLlidEponRxReqAck_Object = MibScalar
sleV2EponIMOnuLlidEponRxReqAck = _SleV2EponIMOnuLlidEponRxReqAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 7),
    _SleV2EponIMOnuLlidEponRxReqAck_Type()
)
sleV2EponIMOnuLlidEponRxReqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponRxReqAck.setStatus("current")
_SleV2EponIMOnuLlidEponTxReport_Type = Counter32
_SleV2EponIMOnuLlidEponTxReport_Object = MibScalar
sleV2EponIMOnuLlidEponTxReport = _SleV2EponIMOnuLlidEponTxReport_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 8),
    _SleV2EponIMOnuLlidEponTxReport_Type()
)
sleV2EponIMOnuLlidEponTxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponTxReport.setStatus("current")
_SleV2EponIMOnuLlidEponRxReport_Type = Counter32
_SleV2EponIMOnuLlidEponRxReport_Object = MibScalar
sleV2EponIMOnuLlidEponRxReport = _SleV2EponIMOnuLlidEponRxReport_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 9),
    _SleV2EponIMOnuLlidEponRxReport_Type()
)
sleV2EponIMOnuLlidEponRxReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponRxReport.setStatus("current")
_SleV2EponIMOnuLlidEponTxGate_Type = Counter32
_SleV2EponIMOnuLlidEponTxGate_Object = MibScalar
sleV2EponIMOnuLlidEponTxGate = _SleV2EponIMOnuLlidEponTxGate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 10),
    _SleV2EponIMOnuLlidEponTxGate_Type()
)
sleV2EponIMOnuLlidEponTxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponTxGate.setStatus("current")
_SleV2EponIMOnuLlidEponRxGate_Type = Counter32
_SleV2EponIMOnuLlidEponRxGate_Object = MibScalar
sleV2EponIMOnuLlidEponRxGate = _SleV2EponIMOnuLlidEponRxGate_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 11),
    _SleV2EponIMOnuLlidEponRxGate_Type()
)
sleV2EponIMOnuLlidEponRxGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponRxGate.setStatus("current")
_SleV2EponIMOnuLlidEponTxRegister_Type = Counter32
_SleV2EponIMOnuLlidEponTxRegister_Object = MibScalar
sleV2EponIMOnuLlidEponTxRegister = _SleV2EponIMOnuLlidEponTxRegister_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 12),
    _SleV2EponIMOnuLlidEponTxRegister_Type()
)
sleV2EponIMOnuLlidEponTxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponTxRegister.setStatus("current")
_SleV2EponIMOnuLlidEponRxRegister_Type = Counter32
_SleV2EponIMOnuLlidEponRxRegister_Object = MibScalar
sleV2EponIMOnuLlidEponRxRegister = _SleV2EponIMOnuLlidEponRxRegister_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 13),
    _SleV2EponIMOnuLlidEponRxRegister_Type()
)
sleV2EponIMOnuLlidEponRxRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponRxRegister.setStatus("current")
_SleV2EponIMOnuLlidEponRxNotSupported_Type = Counter32
_SleV2EponIMOnuLlidEponRxNotSupported_Object = MibScalar
sleV2EponIMOnuLlidEponRxNotSupported = _SleV2EponIMOnuLlidEponRxNotSupported_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 14),
    _SleV2EponIMOnuLlidEponRxNotSupported_Type()
)
sleV2EponIMOnuLlidEponRxNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponRxNotSupported.setStatus("current")
_SleV2EponIMOnuLlidEponSldErrors_Type = Counter32
_SleV2EponIMOnuLlidEponSldErrors_Object = MibScalar
sleV2EponIMOnuLlidEponSldErrors = _SleV2EponIMOnuLlidEponSldErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 15),
    _SleV2EponIMOnuLlidEponSldErrors_Type()
)
sleV2EponIMOnuLlidEponSldErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponSldErrors.setStatus("current")
_SleV2EponIMOnuLlidEponCrc8Errors_Type = Counter32
_SleV2EponIMOnuLlidEponCrc8Errors_Object = MibScalar
sleV2EponIMOnuLlidEponCrc8Errors = _SleV2EponIMOnuLlidEponCrc8Errors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 16),
    _SleV2EponIMOnuLlidEponCrc8Errors_Type()
)
sleV2EponIMOnuLlidEponCrc8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponCrc8Errors.setStatus("current")
_SleV2EponIMOnuLlidEponBadLlid_Type = Counter32
_SleV2EponIMOnuLlidEponBadLlid_Object = MibScalar
sleV2EponIMOnuLlidEponBadLlid = _SleV2EponIMOnuLlidEponBadLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 17),
    _SleV2EponIMOnuLlidEponBadLlid_Type()
)
sleV2EponIMOnuLlidEponBadLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponBadLlid.setStatus("current")
_SleV2EponIMOnuLlidEponGoodLlid_Type = Counter32
_SleV2EponIMOnuLlidEponGoodLlid_Object = MibScalar
sleV2EponIMOnuLlidEponGoodLlid = _SleV2EponIMOnuLlidEponGoodLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 18),
    _SleV2EponIMOnuLlidEponGoodLlid_Type()
)
sleV2EponIMOnuLlidEponGoodLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponGoodLlid.setStatus("current")
_SleV2EponIMOnuLlidEponOnuPonCastLlid_Type = Counter32
_SleV2EponIMOnuLlidEponOnuPonCastLlid_Object = MibScalar
sleV2EponIMOnuLlidEponOnuPonCastLlid = _SleV2EponIMOnuLlidEponOnuPonCastLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 19),
    _SleV2EponIMOnuLlidEponOnuPonCastLlid_Type()
)
sleV2EponIMOnuLlidEponOnuPonCastLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponOnuPonCastLlid.setStatus("current")
_SleV2EponIMOnuLlidEponOltPonCastLlid_Type = Counter32
_SleV2EponIMOnuLlidEponOltPonCastLlid_Object = MibScalar
sleV2EponIMOnuLlidEponOltPonCastLlid = _SleV2EponIMOnuLlidEponOltPonCastLlid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 20),
    _SleV2EponIMOnuLlidEponOltPonCastLlid_Type()
)
sleV2EponIMOnuLlidEponOltPonCastLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponOltPonCastLlid.setStatus("current")
_SleV2EponIMOnuLlidEponBcastLlidNotOnuId_Type = Counter32
_SleV2EponIMOnuLlidEponBcastLlidNotOnuId_Object = MibScalar
sleV2EponIMOnuLlidEponBcastLlidNotOnuId = _SleV2EponIMOnuLlidEponBcastLlidNotOnuId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 21),
    _SleV2EponIMOnuLlidEponBcastLlidNotOnuId_Type()
)
sleV2EponIMOnuLlidEponBcastLlidNotOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponBcastLlidNotOnuId.setStatus("current")
_SleV2EponIMOnuLlidEponOnuLlidNotBcast_Type = Counter32
_SleV2EponIMOnuLlidEponOnuLlidNotBcast_Object = MibScalar
sleV2EponIMOnuLlidEponOnuLlidNotBcast = _SleV2EponIMOnuLlidEponOnuLlidNotBcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 22),
    _SleV2EponIMOnuLlidEponOnuLlidNotBcast_Type()
)
sleV2EponIMOnuLlidEponOnuLlidNotBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponOnuLlidNotBcast.setStatus("current")
_SleV2EponIMOnuLlidEponBcastLlidPlusOnuId_Type = Counter32
_SleV2EponIMOnuLlidEponBcastLlidPlusOnuId_Object = MibScalar
sleV2EponIMOnuLlidEponBcastLlidPlusOnuId = _SleV2EponIMOnuLlidEponBcastLlidPlusOnuId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 23),
    _SleV2EponIMOnuLlidEponBcastLlidPlusOnuId_Type()
)
sleV2EponIMOnuLlidEponBcastLlidPlusOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponBcastLlidPlusOnuId.setStatus("current")
_SleV2EponIMOnuLlidEponNotBcastLlidNotOnuId_Type = Counter32
_SleV2EponIMOnuLlidEponNotBcastLlidNotOnuId_Object = MibScalar
sleV2EponIMOnuLlidEponNotBcastLlidNotOnuId = _SleV2EponIMOnuLlidEponNotBcastLlidNotOnuId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 24),
    _SleV2EponIMOnuLlidEponNotBcastLlidNotOnuId_Type()
)
sleV2EponIMOnuLlidEponNotBcastLlidNotOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponNotBcastLlidNotOnuId.setStatus("current")
_SleV2EponIMOnuLlidEponPcsCodingViolation_Type = Counter32
_SleV2EponIMOnuLlidEponPcsCodingViolation_Object = MibScalar
sleV2EponIMOnuLlidEponPcsCodingViolation = _SleV2EponIMOnuLlidEponPcsCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 25),
    _SleV2EponIMOnuLlidEponPcsCodingViolation_Type()
)
sleV2EponIMOnuLlidEponPcsCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponPcsCodingViolation.setStatus("current")
_SleV2EponIMOnuLlidEponFecCorrectedBlocks_Type = Counter32
_SleV2EponIMOnuLlidEponFecCorrectedBlocks_Object = MibScalar
sleV2EponIMOnuLlidEponFecCorrectedBlocks = _SleV2EponIMOnuLlidEponFecCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 26),
    _SleV2EponIMOnuLlidEponFecCorrectedBlocks_Type()
)
sleV2EponIMOnuLlidEponFecCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponFecCorrectedBlocks.setStatus("current")
_SleV2EponIMOnuLlidEponFecUnCorrectedBlocks_Type = Counter32
_SleV2EponIMOnuLlidEponFecUnCorrectedBlocks_Object = MibScalar
sleV2EponIMOnuLlidEponFecUnCorrectedBlocks = _SleV2EponIMOnuLlidEponFecUnCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 27),
    _SleV2EponIMOnuLlidEponFecUnCorrectedBlocks_Type()
)
sleV2EponIMOnuLlidEponFecUnCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponFecUnCorrectedBlocks.setStatus("current")
_SleV2EponIMOnuLlidEponBufferHeadCodingViolation_Type = Counter32
_SleV2EponIMOnuLlidEponBufferHeadCodingViolation_Object = MibScalar
sleV2EponIMOnuLlidEponBufferHeadCodingViolation = _SleV2EponIMOnuLlidEponBufferHeadCodingViolation_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 2, 28),
    _SleV2EponIMOnuLlidEponBufferHeadCodingViolation_Type()
)
sleV2EponIMOnuLlidEponBufferHeadCodingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidEponBufferHeadCodingViolation.setStatus("current")
_SleV2EponIMOnuLlidStatsControl_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuLlidStatsControl = _SleV2EponIMOnuLlidStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 3)
)


class _SleV2EponIMOnuLlidStatsControlRequest_Type(Integer32):
    """Custom type sleV2EponIMOnuLlidStatsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearPortStats", 1)
    )


_SleV2EponIMOnuLlidStatsControlRequest_Type.__name__ = "Integer32"
_SleV2EponIMOnuLlidStatsControlRequest_Object = MibScalar
sleV2EponIMOnuLlidStatsControlRequest = _SleV2EponIMOnuLlidStatsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 3, 1),
    _SleV2EponIMOnuLlidStatsControlRequest_Type()
)
sleV2EponIMOnuLlidStatsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidStatsControlRequest.setStatus("current")
_SleV2EponIMOnuLlidStatsControlStatus_Type = SleControlStatusType
_SleV2EponIMOnuLlidStatsControlStatus_Object = MibScalar
sleV2EponIMOnuLlidStatsControlStatus = _SleV2EponIMOnuLlidStatsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 3, 2),
    _SleV2EponIMOnuLlidStatsControlStatus_Type()
)
sleV2EponIMOnuLlidStatsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidStatsControlStatus.setStatus("current")
_SleV2EponIMOnuLlidStatsControlTimer_Type = Gauge32
_SleV2EponIMOnuLlidStatsControlTimer_Object = MibScalar
sleV2EponIMOnuLlidStatsControlTimer = _SleV2EponIMOnuLlidStatsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 3, 3),
    _SleV2EponIMOnuLlidStatsControlTimer_Type()
)
sleV2EponIMOnuLlidStatsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidStatsControlTimer.setStatus("current")
_SleV2EponIMOnuLlidStatsControlTimeStamp_Type = TimeTicks
_SleV2EponIMOnuLlidStatsControlTimeStamp_Object = MibScalar
sleV2EponIMOnuLlidStatsControlTimeStamp = _SleV2EponIMOnuLlidStatsControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 3, 4),
    _SleV2EponIMOnuLlidStatsControlTimeStamp_Type()
)
sleV2EponIMOnuLlidStatsControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidStatsControlTimeStamp.setStatus("current")
_SleV2EponIMOnuLlidStatsControlReqResult_Type = SleControlRequestResultType
_SleV2EponIMOnuLlidStatsControlReqResult_Object = MibScalar
sleV2EponIMOnuLlidStatsControlReqResult = _SleV2EponIMOnuLlidStatsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 3, 5),
    _SleV2EponIMOnuLlidStatsControlReqResult_Type()
)
sleV2EponIMOnuLlidStatsControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidStatsControlReqResult.setStatus("current")
_SleV2EponIMOnuLlidStatsNotification_ObjectIdentity = ObjectIdentity
sleV2EponIMOnuLlidStatsNotification = _SleV2EponIMOnuLlidStatsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 4)
)
_SleV2EponIMAlarm_ObjectIdentity = ObjectIdentity
sleV2EponIMAlarm = _SleV2EponIMAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4)
)
_SleV2EponIMAlarmTable_Object = MibTable
sleV2EponIMAlarmTable = _SleV2EponIMAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 1)
)
if mibBuilder.loadTexts:
    sleV2EponIMAlarmTable.setStatus("current")
_SleV2EponIMAlarmEntry_Object = MibTableRow
sleV2EponIMAlarmEntry = _SleV2EponIMAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 1, 1)
)
sleV2EponIMAlarmEntry.setIndexNames(
    (0, "SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuPortIndex"),
    (0, "SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuAlarmIndex"),
)
if mibBuilder.loadTexts:
    sleV2EponIMAlarmEntry.setStatus("current")


class _SleV2EponIMAlarmOnuPortIndex_Type(Integer32):
    """Custom type sleV2EponIMAlarmOnuPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pon", 1),
          ("uni", 2),
          ("llid", 3))
    )


_SleV2EponIMAlarmOnuPortIndex_Type.__name__ = "Integer32"
_SleV2EponIMAlarmOnuPortIndex_Object = MibTableColumn
sleV2EponIMAlarmOnuPortIndex = _SleV2EponIMAlarmOnuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 1, 1, 1),
    _SleV2EponIMAlarmOnuPortIndex_Type()
)
sleV2EponIMAlarmOnuPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmOnuPortIndex.setStatus("current")


class _SleV2EponIMAlarmOnuAlarmIndex_Type(Integer32):
    """Custom type sleV2EponIMAlarmOnuAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("errFramePeriod", 1),
          ("errFrame", 2),
          ("errFrameSecond", 3))
    )


_SleV2EponIMAlarmOnuAlarmIndex_Type.__name__ = "Integer32"
_SleV2EponIMAlarmOnuAlarmIndex_Object = MibTableColumn
sleV2EponIMAlarmOnuAlarmIndex = _SleV2EponIMAlarmOnuAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 1, 1, 2),
    _SleV2EponIMAlarmOnuAlarmIndex_Type()
)
sleV2EponIMAlarmOnuAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmOnuAlarmIndex.setStatus("current")
_SleV2EponIMAlarmOnuAlarmStatus_Type = EponOnuState
_SleV2EponIMAlarmOnuAlarmStatus_Object = MibTableColumn
sleV2EponIMAlarmOnuAlarmStatus = _SleV2EponIMAlarmOnuAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 1, 1, 3),
    _SleV2EponIMAlarmOnuAlarmStatus_Type()
)
sleV2EponIMAlarmOnuAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmOnuAlarmStatus.setStatus("current")
_SleV2EponIMAlarmOnuWindow_Type = Integer32
_SleV2EponIMAlarmOnuWindow_Object = MibTableColumn
sleV2EponIMAlarmOnuWindow = _SleV2EponIMAlarmOnuWindow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 1, 1, 4),
    _SleV2EponIMAlarmOnuWindow_Type()
)
sleV2EponIMAlarmOnuWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmOnuWindow.setStatus("current")
_SleV2EponIMAlarmOnuThreshold_Type = Integer32
_SleV2EponIMAlarmOnuThreshold_Object = MibTableColumn
sleV2EponIMAlarmOnuThreshold = _SleV2EponIMAlarmOnuThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 1, 1, 5),
    _SleV2EponIMAlarmOnuThreshold_Type()
)
sleV2EponIMAlarmOnuThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmOnuThreshold.setStatus("current")
_SleV2EponIMAlarmControl_ObjectIdentity = ObjectIdentity
sleV2EponIMAlarmControl = _SleV2EponIMAlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2)
)


class _SleV2EponIMAlarmControlRequest_Type(Integer32):
    """Custom type sleV2EponIMAlarmControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setEponIMAlarmProfileChanged", 1)
    )


_SleV2EponIMAlarmControlRequest_Type.__name__ = "Integer32"
_SleV2EponIMAlarmControlRequest_Object = MibScalar
sleV2EponIMAlarmControlRequest = _SleV2EponIMAlarmControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 1),
    _SleV2EponIMAlarmControlRequest_Type()
)
sleV2EponIMAlarmControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlRequest.setStatus("current")
_SleV2EponIMAlarmControlStatus_Type = SleControlStatusType
_SleV2EponIMAlarmControlStatus_Object = MibScalar
sleV2EponIMAlarmControlStatus = _SleV2EponIMAlarmControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 2),
    _SleV2EponIMAlarmControlStatus_Type()
)
sleV2EponIMAlarmControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlStatus.setStatus("current")
_SleV2EponIMAlarmControlTimer_Type = Gauge32
_SleV2EponIMAlarmControlTimer_Object = MibScalar
sleV2EponIMAlarmControlTimer = _SleV2EponIMAlarmControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 3),
    _SleV2EponIMAlarmControlTimer_Type()
)
sleV2EponIMAlarmControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlTimer.setStatus("current")
_SleV2EponIMAlarmControlTimeStamp_Type = TimeTicks
_SleV2EponIMAlarmControlTimeStamp_Object = MibScalar
sleV2EponIMAlarmControlTimeStamp = _SleV2EponIMAlarmControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 4),
    _SleV2EponIMAlarmControlTimeStamp_Type()
)
sleV2EponIMAlarmControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlTimeStamp.setStatus("current")
_SleV2EponIMAlarmControlReqResult_Type = SleControlRequestResultType
_SleV2EponIMAlarmControlReqResult_Object = MibScalar
sleV2EponIMAlarmControlReqResult = _SleV2EponIMAlarmControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 5),
    _SleV2EponIMAlarmControlReqResult_Type()
)
sleV2EponIMAlarmControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlReqResult.setStatus("current")


class _SleV2EponIMAlarmControlOnuPortIndex_Type(Integer32):
    """Custom type sleV2EponIMAlarmControlOnuPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pon", 1),
          ("uni", 2),
          ("llid", 3))
    )


_SleV2EponIMAlarmControlOnuPortIndex_Type.__name__ = "Integer32"
_SleV2EponIMAlarmControlOnuPortIndex_Object = MibScalar
sleV2EponIMAlarmControlOnuPortIndex = _SleV2EponIMAlarmControlOnuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 6),
    _SleV2EponIMAlarmControlOnuPortIndex_Type()
)
sleV2EponIMAlarmControlOnuPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlOnuPortIndex.setStatus("current")


class _SleV2EponIMAlarmControlOnuAlarmIndex_Type(Integer32):
    """Custom type sleV2EponIMAlarmControlOnuAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("errFramePeriod", 1),
          ("errFrame", 2),
          ("errFrameSecond", 3))
    )


_SleV2EponIMAlarmControlOnuAlarmIndex_Type.__name__ = "Integer32"
_SleV2EponIMAlarmControlOnuAlarmIndex_Object = MibScalar
sleV2EponIMAlarmControlOnuAlarmIndex = _SleV2EponIMAlarmControlOnuAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 7),
    _SleV2EponIMAlarmControlOnuAlarmIndex_Type()
)
sleV2EponIMAlarmControlOnuAlarmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlOnuAlarmIndex.setStatus("current")
_SleV2EponIMAlarmControlOnuAlarmStatus_Type = EponOnuState
_SleV2EponIMAlarmControlOnuAlarmStatus_Object = MibScalar
sleV2EponIMAlarmControlOnuAlarmStatus = _SleV2EponIMAlarmControlOnuAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 8),
    _SleV2EponIMAlarmControlOnuAlarmStatus_Type()
)
sleV2EponIMAlarmControlOnuAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlOnuAlarmStatus.setStatus("current")
_SleV2EponIMAlarmControlWindow_Type = Integer32
_SleV2EponIMAlarmControlWindow_Object = MibScalar
sleV2EponIMAlarmControlWindow = _SleV2EponIMAlarmControlWindow_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 9),
    _SleV2EponIMAlarmControlWindow_Type()
)
sleV2EponIMAlarmControlWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlWindow.setStatus("current")
_SleV2EponIMAlarmControlThreshold_Type = Integer32
_SleV2EponIMAlarmControlThreshold_Object = MibScalar
sleV2EponIMAlarmControlThreshold = _SleV2EponIMAlarmControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 2, 10),
    _SleV2EponIMAlarmControlThreshold_Type()
)
sleV2EponIMAlarmControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleV2EponIMAlarmControlThreshold.setStatus("current")
_SleV2EponIMAlarmNotification_ObjectIdentity = ObjectIdentity
sleV2EponIMAlarmNotification = _SleV2EponIMAlarmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 4)
)

# Managed Objects groups

sleV2EponIMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 5)
)
sleV2EponIMGroup.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuConfigMask"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuConfigData"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuRegistered"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthenticated"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuImageVersion"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLoadVersion"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuChipVersion"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuSerialNumber"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuRxOpticPower"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMRegInfoOltId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMRegInfoOltLlidPort"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMRegInfoOltPonPort"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMRegInfoOnuMacAddress"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMRegInfoOnuLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuSecret"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuVendorCode"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthTimeoutTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthRejectTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlSecret"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlOnuVendorCode"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlAuthTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlAuthTimeoutTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlAuthRejectTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWName"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlServerIp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlUpDownFlag"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlUserId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlPassword"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlFileName"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlUpdateCommitTime"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIndex"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortType"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortAdminStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortOperStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortLinkupTime"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortUpTime"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlAdminState"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuRxFlowCtrl"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuTxFlowCtrl"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFlowCtrlLowThreshold"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFlowCtrlHighThreshold"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlRxFlowCtrl"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlTxFlowCtrl"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlFlowCtrlLowThreshold"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlFlowCtrlHighThreshold"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfInOctets"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfInUnicast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfInMulticast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfInBroadcast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfInDiscards"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfInErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfInUnknownProtos"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfOutOctets"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfOutUnicast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfOutMulticast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfOutBroadcast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfOutDiscards"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortIfOutErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherAlignmentErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherFcsErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherSingleCollision"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherMultipleCollision"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherSqeTestErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherDeferredTransmissions"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherLateCollisions"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherExcessiveCollisions"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherInternalMacTxErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherCarrierSenseErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherFrameTooLongs"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherInternalMacRxErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherSymbolErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherInUnknownOpcode"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherInPauseFrames"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEtherOutPauseFrames"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponMacCtrlFrameRx"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponDiscWindowsSent"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponDiscTimeout"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponTxRegRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponRxReqRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponTxReqAck"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponRxReqAck"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponTxReport"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponRxReport"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponTxGate"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponRxGate"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponTxRegister"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponRxRegister"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponRxNotSupported"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponSldErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponCrc8Errors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponBadLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponGoodLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponOnuPonCastLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponOltPonCastLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponBcastLlidNotOnuId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponOnuLlidNotBcast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponBcastLlidPlusOnuId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponNotBcastLlidNotOnuId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponPcsCodingViolation"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponFecCorrectedBlocks"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponFecUnCorrectedBlocks"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortEponBufferHeadCodingViolation"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlPortIndex"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfInOctets"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfInUnicast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfInMulticast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfInBroadcast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfInDiscards"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfInErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfInUnknownProtos"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfOutOctets"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfOutUnicast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfOutMulticast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfOutBroadcast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfOutDiscards"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidIfOutErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponMacCtrlFrameRx"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponDiscWindowsSent"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponDiscTimeout"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponTxRegRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponRxReqRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponTxReqAck"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponRxReqAck"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponTxReport"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponRxReport"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponTxGate"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponRxGate"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponTxRegister"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponRxRegister"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponRxNotSupported"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponSldErrors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponCrc8Errors"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponBadLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponGoodLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponOnuPonCastLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponOltPonCastLlid"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponBcastLlidNotOnuId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponOnuLlidNotBcast"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponBcastLlidPlusOnuId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponNotBcastLlidNotOnuId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponPcsCodingViolation"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponFecCorrectedBlocks"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponFecUnCorrectedBlocks"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidEponBufferHeadCodingViolation"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuPortIndex"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuAlarmIndex"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuAlarmStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuWindow"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuThreshold"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlOnuPortIndex"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlOnuAlarmIndex"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlOnuAlarmStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlWindow"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlForceOpticPowerOff"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuForceOpticPowerOff"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortFECtxEnable"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortFECrxEnable"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortLaserAlwaysOn"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortDropInMcastTraffic"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortDropInBcastTraffic"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortBlockDataTraffic"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuOpticButtonPushed"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlThreshold"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAutoUpgrade"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlAutoUpgrade"))
)
if mibBuilder.loadTexts:
    sleV2EponIMGroup.setStatus("current")


# Notification objects

sleV2EponIMOnuSecretChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3, 1)
)
sleV2EponIMOnuSecretChanged.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuSecret"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuSecretChanged.setStatus(
        "current"
    )

sleV2EponIMOnuVendorCodeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3, 2)
)
sleV2EponIMOnuVendorCodeChanged.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuVendorCode"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuVendorCodeChanged.setStatus(
        "current"
    )

sleV2EponIMOnuAuthTimerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3, 3)
)
sleV2EponIMOnuAuthTimerChanged.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthTimeoutTimer"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthRejectTimer"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuAuthTimerChanged.setStatus(
        "current"
    )

sleV2EponIMOnuConfigApplySetted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3, 4)
)
sleV2EponIMOnuConfigApplySetted.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuConfigApplySetted.setStatus(
        "current"
    )

sleV2EponIMOnuAutoUpgradeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3, 5)
)
sleV2EponIMOnuAutoUpgradeChanged.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlAuthRejectTimer"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuAutoUpgradeChanged.setStatus(
        "current"
    )

sleV2EponIMOnuForcePowerOffChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3, 6)
)
sleV2EponIMOnuForcePowerOffChanged.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuForceOpticPowerOff"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuForcePowerOffChanged.setStatus(
        "current"
    )

sleV2EponIMOnuReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 1, 3, 7)
)
sleV2EponIMOnuReset.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuReset.setStatus(
        "current"
    )

sleV2EponIMOnuFWFirmwareCpSetted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 3, 1)
)
sleV2EponIMOnuFWFirmwareCpSetted.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlServerIp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlUpDownFlag"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlUserId"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlPassword"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWFirmwareCpSetted.setStatus(
        "current"
    )

sleV2EponIMOnuFWFirmwareDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 3, 2)
)
sleV2EponIMOnuFWFirmwareDestroyed.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlFileName"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWFirmwareDestroyed.setStatus(
        "current"
    )

sleV2EponIMOnuFWFirmwareUpgradeSetted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 3, 3)
)
sleV2EponIMOnuFWFirmwareUpgradeSetted.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlUpdateCommitTime"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlFileName"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWFirmwareUpgradeSetted.setStatus(
        "current"
    )

sleV2EponIMOnuFWFirmwareCommitSetted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 1, 2, 3, 4)
)
sleV2EponIMOnuFWFirmwareCommitSetted.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuFWFirmwareCommitSetted.setStatus(
        "current"
    )

sleV2EponIMOnuPortAdminStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 1, 3, 1)
)
sleV2EponIMOnuPortAdminStateChanged.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortAdminStatus"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortAdminStateChanged.setStatus(
        "current"
    )

sleV2EponIMOnuBridgeFlowCtrlChagned = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 2, 2, 3, 1)
)
sleV2EponIMOnuBridgeFlowCtrlChagned.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuRxFlowCtrl"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuTxFlowCtrl"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFlowCtrlLowThreshold"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFlowCtrlHighThreshold"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuBridgeFlowCtrlChagned.setStatus(
        "current"
    )

sleV2EponIMOnuPortStatsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 1, 5, 1)
)
sleV2EponIMOnuPortStatsCleared.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsControlPortIndex"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuPortStatsCleared.setStatus(
        "current"
    )

sleV2EponIMOnuLlidStatsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 3, 2, 4, 1)
)
sleV2EponIMOnuLlidStatsCleared.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsControlReqResult"))
)
if mibBuilder.loadTexts:
    sleV2EponIMOnuLlidStatsCleared.setStatus(
        "current"
    )

sleV2EponIMAlarmProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 4, 4, 1)
)
sleV2EponIMAlarmProfileChanged.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlRequest"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlTimeStamp"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmControlReqResult"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuAlarmStatus"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuWindow"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmOnuThreshold"))
)
if mibBuilder.loadTexts:
    sleV2EponIMAlarmProfileChanged.setStatus(
        "current"
    )


# Notifications groups

sleV2EponIMNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 102, 15, 6)
)
sleV2EponIMNotificationGroup.setObjects(
      *(("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuSecretChanged"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuVendorCodeChanged"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAuthTimerChanged"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuConfigApplySetted"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWFirmwareCpSetted"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWFirmwareDestroyed"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWFirmwareUpgradeSetted"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuFWFirmwareCommitSetted"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortAdminStateChanged"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuBridgeFlowCtrlChagned"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuPortStatsCleared"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuLlidStatsCleared"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuForcePowerOffChanged"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMAlarmProfileChanged"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuAutoUpgradeChanged"),
        ("SLEV2-EPON-IM-MIB", "sleV2EponIMOnuReset"))
)
if mibBuilder.loadTexts:
    sleV2EponIMNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLEV2-EPON-IM-MIB",
    **{"EponOnuState": EponOnuState,
       "EponPortType": EponPortType,
       "EponOnuLinkStatus": EponOnuLinkStatus,
       "EponOnuStatus": EponOnuStatus,
       "sleV2EponIM": sleV2EponIM,
       "sleV2EponIMOnu": sleV2EponIMOnu,
       "sleV2EponIMOnuBase": sleV2EponIMOnuBase,
       "sleV2EponIMOnuInfo": sleV2EponIMOnuInfo,
       "sleV2EponIMOnuConfigMask": sleV2EponIMOnuConfigMask,
       "sleV2EponIMOnuConfigData": sleV2EponIMOnuConfigData,
       "sleV2EponIMOnuRegistered": sleV2EponIMOnuRegistered,
       "sleV2EponIMOnuAuthenticated": sleV2EponIMOnuAuthenticated,
       "sleV2EponIMOnuImageVersion": sleV2EponIMOnuImageVersion,
       "sleV2EponIMOnuLoadVersion": sleV2EponIMOnuLoadVersion,
       "sleV2EponIMOnuChipVersion": sleV2EponIMOnuChipVersion,
       "sleV2EponIMOnuSerialNumber": sleV2EponIMOnuSerialNumber,
       "sleV2EponIMOnuRxOpticPower": sleV2EponIMOnuRxOpticPower,
       "sleV2EponIMRegInfoOltId": sleV2EponIMRegInfoOltId,
       "sleV2EponIMRegInfoOltLlidPort": sleV2EponIMRegInfoOltLlidPort,
       "sleV2EponIMRegInfoOltPonPort": sleV2EponIMRegInfoOltPonPort,
       "sleV2EponIMRegInfoOnuMacAddress": sleV2EponIMRegInfoOnuMacAddress,
       "sleV2EponIMRegInfoOnuLlid": sleV2EponIMRegInfoOnuLlid,
       "sleV2EponIMOnuId": sleV2EponIMOnuId,
       "sleV2EponIMOnuSecret": sleV2EponIMOnuSecret,
       "sleV2EponIMOnuVendorCode": sleV2EponIMOnuVendorCode,
       "sleV2EponIMOnuAuthTimer": sleV2EponIMOnuAuthTimer,
       "sleV2EponIMOnuAuthTimeoutTimer": sleV2EponIMOnuAuthTimeoutTimer,
       "sleV2EponIMOnuAuthRejectTimer": sleV2EponIMOnuAuthRejectTimer,
       "sleV2EponIMOnuAutoUpgrade": sleV2EponIMOnuAutoUpgrade,
       "sleV2EponIMOnuForceOpticPowerOff": sleV2EponIMOnuForceOpticPowerOff,
       "sleV2EponIMOnuOpticButtonPushed": sleV2EponIMOnuOpticButtonPushed,
       "sleV2EponIMOnuControl": sleV2EponIMOnuControl,
       "sleV2EponIMOnuControlRequest": sleV2EponIMOnuControlRequest,
       "sleV2EponIMOnuControlStatus": sleV2EponIMOnuControlStatus,
       "sleV2EponIMOnuControlTimer": sleV2EponIMOnuControlTimer,
       "sleV2EponIMOnuControlTimeStamp": sleV2EponIMOnuControlTimeStamp,
       "sleV2EponIMOnuControlReqResult": sleV2EponIMOnuControlReqResult,
       "sleV2EponIMOnuControlSecret": sleV2EponIMOnuControlSecret,
       "sleV2EponIMOnuControlOnuVendorCode": sleV2EponIMOnuControlOnuVendorCode,
       "sleV2EponIMOnuControlAuthTimer": sleV2EponIMOnuControlAuthTimer,
       "sleV2EponIMOnuControlAuthTimeoutTimer": sleV2EponIMOnuControlAuthTimeoutTimer,
       "sleV2EponIMOnuControlAuthRejectTimer": sleV2EponIMOnuControlAuthRejectTimer,
       "sleV2EponIMOnuControlAutoUpgrade": sleV2EponIMOnuControlAutoUpgrade,
       "sleV2EponIMOnuControlForceOpticPowerOff": sleV2EponIMOnuControlForceOpticPowerOff,
       "sleV2EponIMOnuNotification": sleV2EponIMOnuNotification,
       "sleV2EponIMOnuSecretChanged": sleV2EponIMOnuSecretChanged,
       "sleV2EponIMOnuVendorCodeChanged": sleV2EponIMOnuVendorCodeChanged,
       "sleV2EponIMOnuAuthTimerChanged": sleV2EponIMOnuAuthTimerChanged,
       "sleV2EponIMOnuConfigApplySetted": sleV2EponIMOnuConfigApplySetted,
       "sleV2EponIMOnuAutoUpgradeChanged": sleV2EponIMOnuAutoUpgradeChanged,
       "sleV2EponIMOnuForcePowerOffChanged": sleV2EponIMOnuForcePowerOffChanged,
       "sleV2EponIMOnuReset": sleV2EponIMOnuReset,
       "sleV2EponIMOnuFW": sleV2EponIMOnuFW,
       "sleV2EponIMOnuFWTable": sleV2EponIMOnuFWTable,
       "sleV2EponIMOnuFWEntry": sleV2EponIMOnuFWEntry,
       "sleV2EponIMOnuFWName": sleV2EponIMOnuFWName,
       "sleV2EponIMOnuFWControl": sleV2EponIMOnuFWControl,
       "sleV2EponIMOnuFWControlRequest": sleV2EponIMOnuFWControlRequest,
       "sleV2EponIMOnuFWControlStatus": sleV2EponIMOnuFWControlStatus,
       "sleV2EponIMOnuFWControlTimer": sleV2EponIMOnuFWControlTimer,
       "sleV2EponIMOnuFWControlTimeStamp": sleV2EponIMOnuFWControlTimeStamp,
       "sleV2EponIMOnuFWControlReqResult": sleV2EponIMOnuFWControlReqResult,
       "sleV2EponIMOnuFWControlServerIp": sleV2EponIMOnuFWControlServerIp,
       "sleV2EponIMOnuFWControlUpDownFlag": sleV2EponIMOnuFWControlUpDownFlag,
       "sleV2EponIMOnuFWControlUserId": sleV2EponIMOnuFWControlUserId,
       "sleV2EponIMOnuFWControlPassword": sleV2EponIMOnuFWControlPassword,
       "sleV2EponIMOnuFWControlFileName": sleV2EponIMOnuFWControlFileName,
       "sleV2EponIMOnuFWControlUpdateCommitTime": sleV2EponIMOnuFWControlUpdateCommitTime,
       "sleV2EponIMOnuFWNotification": sleV2EponIMOnuFWNotification,
       "sleV2EponIMOnuFWFirmwareCpSetted": sleV2EponIMOnuFWFirmwareCpSetted,
       "sleV2EponIMOnuFWFirmwareDestroyed": sleV2EponIMOnuFWFirmwareDestroyed,
       "sleV2EponIMOnuFWFirmwareUpgradeSetted": sleV2EponIMOnuFWFirmwareUpgradeSetted,
       "sleV2EponIMOnuFWFirmwareCommitSetted": sleV2EponIMOnuFWFirmwareCommitSetted,
       "sleV2EponIMOnuBridge": sleV2EponIMOnuBridge,
       "sleV2EponIMOnuPort": sleV2EponIMOnuPort,
       "sleV2EponIMOnuPortTable": sleV2EponIMOnuPortTable,
       "sleV2EponIMOnuPortEntry": sleV2EponIMOnuPortEntry,
       "sleV2EponIMOnuPortIndex": sleV2EponIMOnuPortIndex,
       "sleV2EponIMOnuPortId": sleV2EponIMOnuPortId,
       "sleV2EponIMOnuPortType": sleV2EponIMOnuPortType,
       "sleV2EponIMOnuPortAdminStatus": sleV2EponIMOnuPortAdminStatus,
       "sleV2EponIMOnuPortOperStatus": sleV2EponIMOnuPortOperStatus,
       "sleV2EponIMOnuPortLinkupTime": sleV2EponIMOnuPortLinkupTime,
       "sleV2EponIMOnuPortUpTime": sleV2EponIMOnuPortUpTime,
       "sleV2EponIMOnuPortFECtxEnable": sleV2EponIMOnuPortFECtxEnable,
       "sleV2EponIMOnuPortFECrxEnable": sleV2EponIMOnuPortFECrxEnable,
       "sleV2EponIMOnuPortLaserAlwaysOn": sleV2EponIMOnuPortLaserAlwaysOn,
       "sleV2EponIMOnuPortDropInMcastTraffic": sleV2EponIMOnuPortDropInMcastTraffic,
       "sleV2EponIMOnuPortDropInBcastTraffic": sleV2EponIMOnuPortDropInBcastTraffic,
       "sleV2EponIMOnuPortBlockDataTraffic": sleV2EponIMOnuPortBlockDataTraffic,
       "sleV2EponIMOnuPortControl": sleV2EponIMOnuPortControl,
       "sleV2EponIMOnuPortControlRequest": sleV2EponIMOnuPortControlRequest,
       "sleV2EponIMOnuPortControlStatus": sleV2EponIMOnuPortControlStatus,
       "sleV2EponIMOnuPortControlTimer": sleV2EponIMOnuPortControlTimer,
       "sleV2EponIMOnuPortControlTimeStamp": sleV2EponIMOnuPortControlTimeStamp,
       "sleV2EponIMOnuPortControlReqResult": sleV2EponIMOnuPortControlReqResult,
       "sleV2EponIMOnuPortControlAdminState": sleV2EponIMOnuPortControlAdminState,
       "sleV2EponIMOnuPortNotification": sleV2EponIMOnuPortNotification,
       "sleV2EponIMOnuPortAdminStateChanged": sleV2EponIMOnuPortAdminStateChanged,
       "sleV2EponIMOnuBridgeBase": sleV2EponIMOnuBridgeBase,
       "sleV2EponIMOnuBridgeInfo": sleV2EponIMOnuBridgeInfo,
       "sleV2EponIMOnuRxFlowCtrl": sleV2EponIMOnuRxFlowCtrl,
       "sleV2EponIMOnuTxFlowCtrl": sleV2EponIMOnuTxFlowCtrl,
       "sleV2EponIMOnuFlowCtrlLowThreshold": sleV2EponIMOnuFlowCtrlLowThreshold,
       "sleV2EponIMOnuFlowCtrlHighThreshold": sleV2EponIMOnuFlowCtrlHighThreshold,
       "sleV2EponIMOnuBridgeControl": sleV2EponIMOnuBridgeControl,
       "sleV2EponIMOnuBridgeControlRequest": sleV2EponIMOnuBridgeControlRequest,
       "sleV2EponIMOnuBridgeControlStatus": sleV2EponIMOnuBridgeControlStatus,
       "sleV2EponIMOnuBridgeControlTimer": sleV2EponIMOnuBridgeControlTimer,
       "sleV2EponIMOnuBridgeControlTimeStamp": sleV2EponIMOnuBridgeControlTimeStamp,
       "sleV2EponIMOnuBridgeControlReqResult": sleV2EponIMOnuBridgeControlReqResult,
       "sleV2EponIMOnuBridgeControlRxFlowCtrl": sleV2EponIMOnuBridgeControlRxFlowCtrl,
       "sleV2EponIMOnuBridgeControlTxFlowCtrl": sleV2EponIMOnuBridgeControlTxFlowCtrl,
       "sleV2EponIMOnuBridgeControlFlowCtrlLowThreshold": sleV2EponIMOnuBridgeControlFlowCtrlLowThreshold,
       "sleV2EponIMOnuBridgeControlFlowCtrlHighThreshold": sleV2EponIMOnuBridgeControlFlowCtrlHighThreshold,
       "sleV2EponIMOnuBridgeNotification": sleV2EponIMOnuBridgeNotification,
       "sleV2EponIMOnuBridgeFlowCtrlChagned": sleV2EponIMOnuBridgeFlowCtrlChagned,
       "sleV2EponIMOnuStats": sleV2EponIMOnuStats,
       "sleV2EponIMOnuPortStats": sleV2EponIMOnuPortStats,
       "sleV2EponIMOnuPortIfStatsTable": sleV2EponIMOnuPortIfStatsTable,
       "sleV2EponIMOnuPortIfStatsEntry": sleV2EponIMOnuPortIfStatsEntry,
       "sleV2EponIMOnuPortIfInOctets": sleV2EponIMOnuPortIfInOctets,
       "sleV2EponIMOnuPortIfInUnicast": sleV2EponIMOnuPortIfInUnicast,
       "sleV2EponIMOnuPortIfInMulticast": sleV2EponIMOnuPortIfInMulticast,
       "sleV2EponIMOnuPortIfInBroadcast": sleV2EponIMOnuPortIfInBroadcast,
       "sleV2EponIMOnuPortIfInDiscards": sleV2EponIMOnuPortIfInDiscards,
       "sleV2EponIMOnuPortIfInErrors": sleV2EponIMOnuPortIfInErrors,
       "sleV2EponIMOnuPortIfInUnknownProtos": sleV2EponIMOnuPortIfInUnknownProtos,
       "sleV2EponIMOnuPortIfOutOctets": sleV2EponIMOnuPortIfOutOctets,
       "sleV2EponIMOnuPortIfOutUnicast": sleV2EponIMOnuPortIfOutUnicast,
       "sleV2EponIMOnuPortIfOutMulticast": sleV2EponIMOnuPortIfOutMulticast,
       "sleV2EponIMOnuPortIfOutBroadcast": sleV2EponIMOnuPortIfOutBroadcast,
       "sleV2EponIMOnuPortIfOutDiscards": sleV2EponIMOnuPortIfOutDiscards,
       "sleV2EponIMOnuPortIfOutErrors": sleV2EponIMOnuPortIfOutErrors,
       "sleV2EponIMOnuPortEtherStatsTable": sleV2EponIMOnuPortEtherStatsTable,
       "sleV2EponIMOnuPortEtherStatsEntry": sleV2EponIMOnuPortEtherStatsEntry,
       "sleV2EponIMOnuPortEtherAlignmentErrors": sleV2EponIMOnuPortEtherAlignmentErrors,
       "sleV2EponIMOnuPortEtherFcsErrors": sleV2EponIMOnuPortEtherFcsErrors,
       "sleV2EponIMOnuPortEtherSingleCollision": sleV2EponIMOnuPortEtherSingleCollision,
       "sleV2EponIMOnuPortEtherMultipleCollision": sleV2EponIMOnuPortEtherMultipleCollision,
       "sleV2EponIMOnuPortEtherSqeTestErrors": sleV2EponIMOnuPortEtherSqeTestErrors,
       "sleV2EponIMOnuPortEtherDeferredTransmissions": sleV2EponIMOnuPortEtherDeferredTransmissions,
       "sleV2EponIMOnuPortEtherLateCollisions": sleV2EponIMOnuPortEtherLateCollisions,
       "sleV2EponIMOnuPortEtherExcessiveCollisions": sleV2EponIMOnuPortEtherExcessiveCollisions,
       "sleV2EponIMOnuPortEtherInternalMacTxErrors": sleV2EponIMOnuPortEtherInternalMacTxErrors,
       "sleV2EponIMOnuPortEtherCarrierSenseErrors": sleV2EponIMOnuPortEtherCarrierSenseErrors,
       "sleV2EponIMOnuPortEtherFrameTooLongs": sleV2EponIMOnuPortEtherFrameTooLongs,
       "sleV2EponIMOnuPortEtherInternalMacRxErrors": sleV2EponIMOnuPortEtherInternalMacRxErrors,
       "sleV2EponIMOnuPortEtherSymbolErrors": sleV2EponIMOnuPortEtherSymbolErrors,
       "sleV2EponIMOnuPortEtherInUnknownOpcode": sleV2EponIMOnuPortEtherInUnknownOpcode,
       "sleV2EponIMOnuPortEtherInPauseFrames": sleV2EponIMOnuPortEtherInPauseFrames,
       "sleV2EponIMOnuPortEtherOutPauseFrames": sleV2EponIMOnuPortEtherOutPauseFrames,
       "sleV2EponIMOnuPortEponStatsTable": sleV2EponIMOnuPortEponStatsTable,
       "sleV2EponIMOnuPortEponStatsEntry": sleV2EponIMOnuPortEponStatsEntry,
       "sleV2EponIMOnuPortEponMacCtrlFrameRx": sleV2EponIMOnuPortEponMacCtrlFrameRx,
       "sleV2EponIMOnuPortEponDiscWindowsSent": sleV2EponIMOnuPortEponDiscWindowsSent,
       "sleV2EponIMOnuPortEponDiscTimeout": sleV2EponIMOnuPortEponDiscTimeout,
       "sleV2EponIMOnuPortEponTxRegRequest": sleV2EponIMOnuPortEponTxRegRequest,
       "sleV2EponIMOnuPortEponRxReqRequest": sleV2EponIMOnuPortEponRxReqRequest,
       "sleV2EponIMOnuPortEponTxReqAck": sleV2EponIMOnuPortEponTxReqAck,
       "sleV2EponIMOnuPortEponRxReqAck": sleV2EponIMOnuPortEponRxReqAck,
       "sleV2EponIMOnuPortEponTxReport": sleV2EponIMOnuPortEponTxReport,
       "sleV2EponIMOnuPortEponRxReport": sleV2EponIMOnuPortEponRxReport,
       "sleV2EponIMOnuPortEponTxGate": sleV2EponIMOnuPortEponTxGate,
       "sleV2EponIMOnuPortEponRxGate": sleV2EponIMOnuPortEponRxGate,
       "sleV2EponIMOnuPortEponTxRegister": sleV2EponIMOnuPortEponTxRegister,
       "sleV2EponIMOnuPortEponRxRegister": sleV2EponIMOnuPortEponRxRegister,
       "sleV2EponIMOnuPortEponRxNotSupported": sleV2EponIMOnuPortEponRxNotSupported,
       "sleV2EponIMOnuPortEponSldErrors": sleV2EponIMOnuPortEponSldErrors,
       "sleV2EponIMOnuPortEponCrc8Errors": sleV2EponIMOnuPortEponCrc8Errors,
       "sleV2EponIMOnuPortEponBadLlid": sleV2EponIMOnuPortEponBadLlid,
       "sleV2EponIMOnuPortEponGoodLlid": sleV2EponIMOnuPortEponGoodLlid,
       "sleV2EponIMOnuPortEponOnuPonCastLlid": sleV2EponIMOnuPortEponOnuPonCastLlid,
       "sleV2EponIMOnuPortEponOltPonCastLlid": sleV2EponIMOnuPortEponOltPonCastLlid,
       "sleV2EponIMOnuPortEponBcastLlidNotOnuId": sleV2EponIMOnuPortEponBcastLlidNotOnuId,
       "sleV2EponIMOnuPortEponOnuLlidNotBcast": sleV2EponIMOnuPortEponOnuLlidNotBcast,
       "sleV2EponIMOnuPortEponBcastLlidPlusOnuId": sleV2EponIMOnuPortEponBcastLlidPlusOnuId,
       "sleV2EponIMOnuPortEponNotBcastLlidNotOnuId": sleV2EponIMOnuPortEponNotBcastLlidNotOnuId,
       "sleV2EponIMOnuPortEponPcsCodingViolation": sleV2EponIMOnuPortEponPcsCodingViolation,
       "sleV2EponIMOnuPortEponFecCorrectedBlocks": sleV2EponIMOnuPortEponFecCorrectedBlocks,
       "sleV2EponIMOnuPortEponFecUnCorrectedBlocks": sleV2EponIMOnuPortEponFecUnCorrectedBlocks,
       "sleV2EponIMOnuPortEponBufferHeadCodingViolation": sleV2EponIMOnuPortEponBufferHeadCodingViolation,
       "sleV2EponIMOnuPortStatsControl": sleV2EponIMOnuPortStatsControl,
       "sleV2EponIMOnuPortStatsControlRequest": sleV2EponIMOnuPortStatsControlRequest,
       "sleV2EponIMOnuPortStatsControlStatus": sleV2EponIMOnuPortStatsControlStatus,
       "sleV2EponIMOnuPortStatsControlTimer": sleV2EponIMOnuPortStatsControlTimer,
       "sleV2EponIMOnuPortStatsControlTimeStamp": sleV2EponIMOnuPortStatsControlTimeStamp,
       "sleV2EponIMOnuPortStatsControlReqResult": sleV2EponIMOnuPortStatsControlReqResult,
       "sleV2EponIMOnuPortStatsControlPortIndex": sleV2EponIMOnuPortStatsControlPortIndex,
       "sleV2EponIMOnuPortStatsNotification": sleV2EponIMOnuPortStatsNotification,
       "sleV2EponIMOnuPortStatsCleared": sleV2EponIMOnuPortStatsCleared,
       "sleV2EponIMOnuLlidStats": sleV2EponIMOnuLlidStats,
       "sleV2EponIMOnuLlidIfStats": sleV2EponIMOnuLlidIfStats,
       "sleV2EponIMOnuLlidIfInOctets": sleV2EponIMOnuLlidIfInOctets,
       "sleV2EponIMOnuLlidIfInUnicast": sleV2EponIMOnuLlidIfInUnicast,
       "sleV2EponIMOnuLlidIfInMulticast": sleV2EponIMOnuLlidIfInMulticast,
       "sleV2EponIMOnuLlidIfInBroadcast": sleV2EponIMOnuLlidIfInBroadcast,
       "sleV2EponIMOnuLlidIfInDiscards": sleV2EponIMOnuLlidIfInDiscards,
       "sleV2EponIMOnuLlidIfInErrors": sleV2EponIMOnuLlidIfInErrors,
       "sleV2EponIMOnuLlidIfInUnknownProtos": sleV2EponIMOnuLlidIfInUnknownProtos,
       "sleV2EponIMOnuLlidIfOutOctets": sleV2EponIMOnuLlidIfOutOctets,
       "sleV2EponIMOnuLlidIfOutUnicast": sleV2EponIMOnuLlidIfOutUnicast,
       "sleV2EponIMOnuLlidIfOutMulticast": sleV2EponIMOnuLlidIfOutMulticast,
       "sleV2EponIMOnuLlidIfOutBroadcast": sleV2EponIMOnuLlidIfOutBroadcast,
       "sleV2EponIMOnuLlidIfOutDiscards": sleV2EponIMOnuLlidIfOutDiscards,
       "sleV2EponIMOnuLlidIfOutErrors": sleV2EponIMOnuLlidIfOutErrors,
       "sleV2EponIMOnuLlidEponStats": sleV2EponIMOnuLlidEponStats,
       "sleV2EponIMOnuLlidEponMacCtrlFrameRx": sleV2EponIMOnuLlidEponMacCtrlFrameRx,
       "sleV2EponIMOnuLlidEponDiscWindowsSent": sleV2EponIMOnuLlidEponDiscWindowsSent,
       "sleV2EponIMOnuLlidEponDiscTimeout": sleV2EponIMOnuLlidEponDiscTimeout,
       "sleV2EponIMOnuLlidEponTxRegRequest": sleV2EponIMOnuLlidEponTxRegRequest,
       "sleV2EponIMOnuLlidEponRxReqRequest": sleV2EponIMOnuLlidEponRxReqRequest,
       "sleV2EponIMOnuLlidEponTxReqAck": sleV2EponIMOnuLlidEponTxReqAck,
       "sleV2EponIMOnuLlidEponRxReqAck": sleV2EponIMOnuLlidEponRxReqAck,
       "sleV2EponIMOnuLlidEponTxReport": sleV2EponIMOnuLlidEponTxReport,
       "sleV2EponIMOnuLlidEponRxReport": sleV2EponIMOnuLlidEponRxReport,
       "sleV2EponIMOnuLlidEponTxGate": sleV2EponIMOnuLlidEponTxGate,
       "sleV2EponIMOnuLlidEponRxGate": sleV2EponIMOnuLlidEponRxGate,
       "sleV2EponIMOnuLlidEponTxRegister": sleV2EponIMOnuLlidEponTxRegister,
       "sleV2EponIMOnuLlidEponRxRegister": sleV2EponIMOnuLlidEponRxRegister,
       "sleV2EponIMOnuLlidEponRxNotSupported": sleV2EponIMOnuLlidEponRxNotSupported,
       "sleV2EponIMOnuLlidEponSldErrors": sleV2EponIMOnuLlidEponSldErrors,
       "sleV2EponIMOnuLlidEponCrc8Errors": sleV2EponIMOnuLlidEponCrc8Errors,
       "sleV2EponIMOnuLlidEponBadLlid": sleV2EponIMOnuLlidEponBadLlid,
       "sleV2EponIMOnuLlidEponGoodLlid": sleV2EponIMOnuLlidEponGoodLlid,
       "sleV2EponIMOnuLlidEponOnuPonCastLlid": sleV2EponIMOnuLlidEponOnuPonCastLlid,
       "sleV2EponIMOnuLlidEponOltPonCastLlid": sleV2EponIMOnuLlidEponOltPonCastLlid,
       "sleV2EponIMOnuLlidEponBcastLlidNotOnuId": sleV2EponIMOnuLlidEponBcastLlidNotOnuId,
       "sleV2EponIMOnuLlidEponOnuLlidNotBcast": sleV2EponIMOnuLlidEponOnuLlidNotBcast,
       "sleV2EponIMOnuLlidEponBcastLlidPlusOnuId": sleV2EponIMOnuLlidEponBcastLlidPlusOnuId,
       "sleV2EponIMOnuLlidEponNotBcastLlidNotOnuId": sleV2EponIMOnuLlidEponNotBcastLlidNotOnuId,
       "sleV2EponIMOnuLlidEponPcsCodingViolation": sleV2EponIMOnuLlidEponPcsCodingViolation,
       "sleV2EponIMOnuLlidEponFecCorrectedBlocks": sleV2EponIMOnuLlidEponFecCorrectedBlocks,
       "sleV2EponIMOnuLlidEponFecUnCorrectedBlocks": sleV2EponIMOnuLlidEponFecUnCorrectedBlocks,
       "sleV2EponIMOnuLlidEponBufferHeadCodingViolation": sleV2EponIMOnuLlidEponBufferHeadCodingViolation,
       "sleV2EponIMOnuLlidStatsControl": sleV2EponIMOnuLlidStatsControl,
       "sleV2EponIMOnuLlidStatsControlRequest": sleV2EponIMOnuLlidStatsControlRequest,
       "sleV2EponIMOnuLlidStatsControlStatus": sleV2EponIMOnuLlidStatsControlStatus,
       "sleV2EponIMOnuLlidStatsControlTimer": sleV2EponIMOnuLlidStatsControlTimer,
       "sleV2EponIMOnuLlidStatsControlTimeStamp": sleV2EponIMOnuLlidStatsControlTimeStamp,
       "sleV2EponIMOnuLlidStatsControlReqResult": sleV2EponIMOnuLlidStatsControlReqResult,
       "sleV2EponIMOnuLlidStatsNotification": sleV2EponIMOnuLlidStatsNotification,
       "sleV2EponIMOnuLlidStatsCleared": sleV2EponIMOnuLlidStatsCleared,
       "sleV2EponIMAlarm": sleV2EponIMAlarm,
       "sleV2EponIMAlarmTable": sleV2EponIMAlarmTable,
       "sleV2EponIMAlarmEntry": sleV2EponIMAlarmEntry,
       "sleV2EponIMAlarmOnuPortIndex": sleV2EponIMAlarmOnuPortIndex,
       "sleV2EponIMAlarmOnuAlarmIndex": sleV2EponIMAlarmOnuAlarmIndex,
       "sleV2EponIMAlarmOnuAlarmStatus": sleV2EponIMAlarmOnuAlarmStatus,
       "sleV2EponIMAlarmOnuWindow": sleV2EponIMAlarmOnuWindow,
       "sleV2EponIMAlarmOnuThreshold": sleV2EponIMAlarmOnuThreshold,
       "sleV2EponIMAlarmControl": sleV2EponIMAlarmControl,
       "sleV2EponIMAlarmControlRequest": sleV2EponIMAlarmControlRequest,
       "sleV2EponIMAlarmControlStatus": sleV2EponIMAlarmControlStatus,
       "sleV2EponIMAlarmControlTimer": sleV2EponIMAlarmControlTimer,
       "sleV2EponIMAlarmControlTimeStamp": sleV2EponIMAlarmControlTimeStamp,
       "sleV2EponIMAlarmControlReqResult": sleV2EponIMAlarmControlReqResult,
       "sleV2EponIMAlarmControlOnuPortIndex": sleV2EponIMAlarmControlOnuPortIndex,
       "sleV2EponIMAlarmControlOnuAlarmIndex": sleV2EponIMAlarmControlOnuAlarmIndex,
       "sleV2EponIMAlarmControlOnuAlarmStatus": sleV2EponIMAlarmControlOnuAlarmStatus,
       "sleV2EponIMAlarmControlWindow": sleV2EponIMAlarmControlWindow,
       "sleV2EponIMAlarmControlThreshold": sleV2EponIMAlarmControlThreshold,
       "sleV2EponIMAlarmNotification": sleV2EponIMAlarmNotification,
       "sleV2EponIMAlarmProfileChanged": sleV2EponIMAlarmProfileChanged,
       "sleV2EponIMGroup": sleV2EponIMGroup,
       "sleV2EponIMNotificationGroup": sleV2EponIMNotificationGroup}
)
