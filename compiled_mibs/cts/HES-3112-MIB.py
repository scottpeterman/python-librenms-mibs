# SNMP MIB module (HES-3112-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cts\HES-3112-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:38 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(etherStatsBroadcastPkts,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "etherStatsBroadcastPkts")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cts_ObjectIdentity = ObjectIdentity
cts = _Cts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304)
)
_Cvt_ObjectIdentity = ObjectIdentity
cvt = _Cvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300)
)
_Hes3112_ObjectIdentity = ObjectIdentity
hes3112 = _Hes3112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002)
)
_CvtSystemInformation_ObjectIdentity = ObjectIdentity
cvtSystemInformation = _CvtSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1)
)
_CvtCompanyInfo_ObjectIdentity = ObjectIdentity
cvtCompanyInfo = _CvtCompanyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 1)
)


class _CvtCompanyName_Type(DisplayString):
    """Custom type cvtCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtCompanyName_Type.__name__ = "DisplayString"
_CvtCompanyName_Object = MibScalar
cvtCompanyName = _CvtCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 1, 1),
    _CvtCompanyName_Type()
)
cvtCompanyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCompanyName.setStatus("mandatory")


class _CvtCLIHostname_Type(DisplayString):
    """Custom type cvtCLIHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtCLIHostname_Type.__name__ = "DisplayString"
_CvtCLIHostname_Object = MibScalar
cvtCLIHostname = _CvtCLIHostname_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 1, 6),
    _CvtCLIHostname_Type()
)
cvtCLIHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCLIHostname.setStatus("mandatory")


class _CvtDHCPVendorID_Type(DisplayString):
    """Custom type cvtDHCPVendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtDHCPVendorID_Type.__name__ = "DisplayString"
_CvtDHCPVendorID_Object = MibScalar
cvtDHCPVendorID = _CvtDHCPVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 1, 7),
    _CvtDHCPVendorID_Type()
)
cvtDHCPVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDHCPVendorID.setStatus("mandatory")
_CvtHardwareInfo_ObjectIdentity = ObjectIdentity
cvtHardwareInfo = _CvtHardwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2)
)


class _CvtModelName_Type(DisplayString):
    """Custom type cvtModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtModelName_Type.__name__ = "DisplayString"
_CvtModelName_Object = MibScalar
cvtModelName = _CvtModelName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 1),
    _CvtModelName_Type()
)
cvtModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtModelName.setStatus("mandatory")


class _CvtFirmwareVersion_Type(DisplayString):
    """Custom type cvtFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtFirmwareVersion_Type.__name__ = "DisplayString"
_CvtFirmwareVersion_Object = MibScalar
cvtFirmwareVersion = _CvtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 2),
    _CvtFirmwareVersion_Type()
)
cvtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtFirmwareVersion.setStatus("mandatory")


class _CvtGPortNum_Type(Integer32):
    """Custom type cvtGPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtGPortNum_Type.__name__ = "Integer32"
_CvtGPortNum_Object = MibScalar
cvtGPortNum = _CvtGPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 6),
    _CvtGPortNum_Type()
)
cvtGPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtGPortNum.setStatus("mandatory")


class _CvtMPortNum_Type(Integer32):
    """Custom type cvtMPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtMPortNum_Type.__name__ = "Integer32"
_CvtMPortNum_Object = MibScalar
cvtMPortNum = _CvtMPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 7),
    _CvtMPortNum_Type()
)
cvtMPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMPortNum.setStatus("mandatory")


class _CvtMBVersion_Type(DisplayString):
    """Custom type cvtMBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtMBVersion_Type.__name__ = "DisplayString"
_CvtMBVersion_Object = MibScalar
cvtMBVersion = _CvtMBVersion_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 9),
    _CvtMBVersion_Type()
)
cvtMBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMBVersion.setStatus("mandatory")


class _CvtLANFiberType_Type(DisplayString):
    """Custom type cvtLANFiberType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtLANFiberType_Type.__name__ = "DisplayString"
_CvtLANFiberType_Object = MibScalar
cvtLANFiberType = _CvtLANFiberType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 10),
    _CvtLANFiberType_Type()
)
cvtLANFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtLANFiberType.setStatus("mandatory")


class _CvtLANFiberWaveLength_Type(DisplayString):
    """Custom type cvtLANFiberWaveLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtLANFiberWaveLength_Type.__name__ = "DisplayString"
_CvtLANFiberWaveLength_Object = MibScalar
cvtLANFiberWaveLength = _CvtLANFiberWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 11),
    _CvtLANFiberWaveLength_Type()
)
cvtLANFiberWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtLANFiberWaveLength.setStatus("mandatory")


class _CvtWANFiberType_Type(DisplayString):
    """Custom type cvtWANFiberType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtWANFiberType_Type.__name__ = "DisplayString"
_CvtWANFiberType_Object = MibScalar
cvtWANFiberType = _CvtWANFiberType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 12),
    _CvtWANFiberType_Type()
)
cvtWANFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtWANFiberType.setStatus("mandatory")


class _CvtWANFiberWaveLength_Type(DisplayString):
    """Custom type cvtWANFiberWaveLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtWANFiberWaveLength_Type.__name__ = "DisplayString"
_CvtWANFiberWaveLength_Object = MibScalar
cvtWANFiberWaveLength = _CvtWANFiberWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 13),
    _CvtWANFiberWaveLength_Type()
)
cvtWANFiberWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtWANFiberWaveLength.setStatus("mandatory")


class _CvtSerialNumber_Type(DisplayString):
    """Custom type cvtSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtSerialNumber_Type.__name__ = "DisplayString"
_CvtSerialNumber_Object = MibScalar
cvtSerialNumber = _CvtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 14),
    _CvtSerialNumber_Type()
)
cvtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSerialNumber.setStatus("mandatory")


class _CvtDateCode_Type(DisplayString):
    """Custom type cvtDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtDateCode_Type.__name__ = "DisplayString"
_CvtDateCode_Object = MibScalar
cvtDateCode = _CvtDateCode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 2, 15),
    _CvtDateCode_Type()
)
cvtDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtDateCode.setStatus("mandatory")
_CvtCATVModuleInfo_ObjectIdentity = ObjectIdentity
cvtCATVModuleInfo = _CvtCATVModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 5)
)


class _CvtRFTVOutput_Type(Integer32):
    """Custom type cvtRFTVOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CvtRFTVOutput_Type.__name__ = "Integer32"
_CvtRFTVOutput_Object = MibScalar
cvtRFTVOutput = _CvtRFTVOutput_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 5, 2),
    _CvtRFTVOutput_Type()
)
cvtRFTVOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtRFTVOutput.setStatus("mandatory")


class _CvtRFTVState_Type(DisplayString):
    """Custom type cvtRFTVState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtRFTVState_Type.__name__ = "DisplayString"
_CvtRFTVState_Object = MibScalar
cvtRFTVState = _CvtRFTVState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 5, 4),
    _CvtRFTVState_Type()
)
cvtRFTVState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtRFTVState.setStatus("mandatory")
_CvtBatteryModuleInfo_ObjectIdentity = ObjectIdentity
cvtBatteryModuleInfo = _CvtBatteryModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 6)
)


class _CvtBatteryState_Type(DisplayString):
    """Custom type cvtBatteryState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtBatteryState_Type.__name__ = "DisplayString"
_CvtBatteryState_Object = MibScalar
cvtBatteryState = _CvtBatteryState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 1, 6, 1),
    _CvtBatteryState_Type()
)
cvtBatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtBatteryState.setStatus("mandatory")
_CvtUserAuthentication_ObjectIdentity = ObjectIdentity
cvtUserAuthentication = _CvtUserAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2)
)
_CvtUserTable_Object = MibTable
cvtUserTable = _CvtUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1)
)
if mibBuilder.loadTexts:
    cvtUserTable.setStatus("mandatory")
_CvtUserEntry_Object = MibTableRow
cvtUserEntry = _CvtUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1, 1)
)
cvtUserEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtUserIndex"),
)
if mibBuilder.loadTexts:
    cvtUserEntry.setStatus("mandatory")


class _CvtUserIndex_Type(Integer32):
    """Custom type cvtUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtUserIndex_Type.__name__ = "Integer32"
_CvtUserIndex_Object = MibTableColumn
cvtUserIndex = _CvtUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1, 1, 1),
    _CvtUserIndex_Type()
)
cvtUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtUserIndex.setStatus("mandatory")


class _CvtUserEnable_Type(Integer32):
    """Custom type cvtUserEnable based on Integer32"""
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


_CvtUserEnable_Type.__name__ = "Integer32"
_CvtUserEnable_Object = MibTableColumn
cvtUserEnable = _CvtUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1, 1, 3),
    _CvtUserEnable_Type()
)
cvtUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtUserEnable.setStatus("mandatory")


class _CvtUserName_Type(DisplayString):
    """Custom type cvtUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUserName_Type.__name__ = "DisplayString"
_CvtUserName_Object = MibTableColumn
cvtUserName = _CvtUserName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1, 1, 4),
    _CvtUserName_Type()
)
cvtUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtUserName.setStatus("mandatory")


class _CvtUserPassword_Type(DisplayString):
    """Custom type cvtUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUserPassword_Type.__name__ = "DisplayString"
_CvtUserPassword_Object = MibTableColumn
cvtUserPassword = _CvtUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1, 1, 5),
    _CvtUserPassword_Type()
)
cvtUserPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtUserPassword.setStatus("mandatory")


class _CvtUserDescription_Type(DisplayString):
    """Custom type cvtUserDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUserDescription_Type.__name__ = "DisplayString"
_CvtUserDescription_Object = MibTableColumn
cvtUserDescription = _CvtUserDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1, 1, 6),
    _CvtUserDescription_Type()
)
cvtUserDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtUserDescription.setStatus("mandatory")


class _CvtUserConsoleLevel_Type(Integer32):
    """Custom type cvtUserConsoleLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("administrator", 3))
    )


_CvtUserConsoleLevel_Type.__name__ = "Integer32"
_CvtUserConsoleLevel_Object = MibTableColumn
cvtUserConsoleLevel = _CvtUserConsoleLevel_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 2, 1, 1, 10),
    _CvtUserConsoleLevel_Type()
)
cvtUserConsoleLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtUserConsoleLevel.setStatus("mandatory")
_CvtNetworkManagement_ObjectIdentity = ObjectIdentity
cvtNetworkManagement = _CvtNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3)
)
_CvtNetworkConfiguration_ObjectIdentity = ObjectIdentity
cvtNetworkConfiguration = _CvtNetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1)
)
_CvtNetMacAddr_Type = MacAddress
_CvtNetMacAddr_Object = MibScalar
cvtNetMacAddr = _CvtNetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 1),
    _CvtNetMacAddr_Type()
)
cvtNetMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetMacAddr.setStatus("mandatory")


class _CvtNetType_Type(Integer32):
    """Custom type cvtNetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("manual", 1))
    )


_CvtNetType_Type.__name__ = "Integer32"
_CvtNetType_Object = MibScalar
cvtNetType = _CvtNetType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 2),
    _CvtNetType_Type()
)
cvtNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetType.setStatus("mandatory")
_CvtNetIPAddr_Type = IpAddress
_CvtNetIPAddr_Object = MibScalar
cvtNetIPAddr = _CvtNetIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 3),
    _CvtNetIPAddr_Type()
)
cvtNetIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPAddr.setStatus("mandatory")
_CvtNetIPMask_Type = IpAddress
_CvtNetIPMask_Object = MibScalar
cvtNetIPMask = _CvtNetIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 4),
    _CvtNetIPMask_Type()
)
cvtNetIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPMask.setStatus("mandatory")
_CvtNetGateway_Type = IpAddress
_CvtNetGateway_Object = MibScalar
cvtNetGateway = _CvtNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 5),
    _CvtNetGateway_Type()
)
cvtNetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetGateway.setStatus("mandatory")


class _CvtNetIPv4En_Type(Integer32):
    """Custom type cvtNetIPv4En based on Integer32"""
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


_CvtNetIPv4En_Type.__name__ = "Integer32"
_CvtNetIPv4En_Object = MibScalar
cvtNetIPv4En = _CvtNetIPv4En_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 8),
    _CvtNetIPv4En_Type()
)
cvtNetIPv4En.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPv4En.setStatus("mandatory")
_CvtNetCurrentIPAddr_Type = IpAddress
_CvtNetCurrentIPAddr_Object = MibScalar
cvtNetCurrentIPAddr = _CvtNetCurrentIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 10),
    _CvtNetCurrentIPAddr_Type()
)
cvtNetCurrentIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentIPAddr.setStatus("mandatory")
_CvtNetCurrentIPMask_Type = IpAddress
_CvtNetCurrentIPMask_Object = MibScalar
cvtNetCurrentIPMask = _CvtNetCurrentIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 11),
    _CvtNetCurrentIPMask_Type()
)
cvtNetCurrentIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentIPMask.setStatus("mandatory")
_CvtNetCurrentGateway_Type = IpAddress
_CvtNetCurrentGateway_Object = MibScalar
cvtNetCurrentGateway = _CvtNetCurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 12),
    _CvtNetCurrentGateway_Type()
)
cvtNetCurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentGateway.setStatus("mandatory")


class _CvtNetIPSourceBinding_Type(Integer32):
    """Custom type cvtNetIPSourceBinding based on Integer32"""
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


_CvtNetIPSourceBinding_Type.__name__ = "Integer32"
_CvtNetIPSourceBinding_Object = MibScalar
cvtNetIPSourceBinding = _CvtNetIPSourceBinding_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 20),
    _CvtNetIPSourceBinding_Type()
)
cvtNetIPSourceBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPSourceBinding.setStatus("mandatory")
_CvtNetIPSourceBindingTable_Object = MibTable
cvtNetIPSourceBindingTable = _CvtNetIPSourceBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 21)
)
if mibBuilder.loadTexts:
    cvtNetIPSourceBindingTable.setStatus("mandatory")
_CvtNetIPSourceBindingEntry_Object = MibTableRow
cvtNetIPSourceBindingEntry = _CvtNetIPSourceBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 21, 1)
)
cvtNetIPSourceBindingEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtNetIPSourceBindingIndex"),
)
if mibBuilder.loadTexts:
    cvtNetIPSourceBindingEntry.setStatus("mandatory")


class _CvtNetIPSourceBindingIndex_Type(Integer32):
    """Custom type cvtNetIPSourceBindingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtNetIPSourceBindingIndex_Type.__name__ = "Integer32"
_CvtNetIPSourceBindingIndex_Object = MibTableColumn
cvtNetIPSourceBindingIndex = _CvtNetIPSourceBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 21, 1, 1),
    _CvtNetIPSourceBindingIndex_Type()
)
cvtNetIPSourceBindingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtNetIPSourceBindingIndex.setStatus("mandatory")


class _CvtNetIPSourceBindingState_Type(Integer32):
    """Custom type cvtNetIPSourceBindingState based on Integer32"""
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


_CvtNetIPSourceBindingState_Type.__name__ = "Integer32"
_CvtNetIPSourceBindingState_Object = MibTableColumn
cvtNetIPSourceBindingState = _CvtNetIPSourceBindingState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 21, 1, 3),
    _CvtNetIPSourceBindingState_Type()
)
cvtNetIPSourceBindingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPSourceBindingState.setStatus("mandatory")
_CvtNetIPSourceBindingIPAddress_Type = IpAddress
_CvtNetIPSourceBindingIPAddress_Object = MibTableColumn
cvtNetIPSourceBindingIPAddress = _CvtNetIPSourceBindingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 21, 1, 4),
    _CvtNetIPSourceBindingIPAddress_Type()
)
cvtNetIPSourceBindingIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPSourceBindingIPAddress.setStatus("mandatory")


class _CvtNetIPSourceBindingIPv6Address_Type(DisplayString):
    """Custom type cvtNetIPSourceBindingIPv6Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtNetIPSourceBindingIPv6Address_Type.__name__ = "DisplayString"
_CvtNetIPSourceBindingIPv6Address_Object = MibTableColumn
cvtNetIPSourceBindingIPv6Address = _CvtNetIPSourceBindingIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 21, 1, 5),
    _CvtNetIPSourceBindingIPv6Address_Type()
)
cvtNetIPSourceBindingIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPSourceBindingIPv6Address.setStatus("mandatory")


class _CvtNetIPSourceBindingDelete_Type(Integer32):
    """Custom type cvtNetIPSourceBindingDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_CvtNetIPSourceBindingDelete_Type.__name__ = "Integer32"
_CvtNetIPSourceBindingDelete_Object = MibTableColumn
cvtNetIPSourceBindingDelete = _CvtNetIPSourceBindingDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 21, 1, 10),
    _CvtNetIPSourceBindingDelete_Type()
)
cvtNetIPSourceBindingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPSourceBindingDelete.setStatus("mandatory")


class _CvtNetIPv6En_Type(Integer32):
    """Custom type cvtNetIPv6En based on Integer32"""
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


_CvtNetIPv6En_Type.__name__ = "Integer32"
_CvtNetIPv6En_Object = MibScalar
cvtNetIPv6En = _CvtNetIPv6En_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 32),
    _CvtNetIPv6En_Type()
)
cvtNetIPv6En.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPv6En.setStatus("mandatory")


class _CvtNetIPv6AutoConfig_Type(Integer32):
    """Custom type cvtNetIPv6AutoConfig based on Integer32"""
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


_CvtNetIPv6AutoConfig_Type.__name__ = "Integer32"
_CvtNetIPv6AutoConfig_Object = MibScalar
cvtNetIPv6AutoConfig = _CvtNetIPv6AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 33),
    _CvtNetIPv6AutoConfig_Type()
)
cvtNetIPv6AutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPv6AutoConfig.setStatus("mandatory")


class _CvtNetIPv6LinkLocalAddr_Type(DisplayString):
    """Custom type cvtNetIPv6LinkLocalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtNetIPv6LinkLocalAddr_Type.__name__ = "DisplayString"
_CvtNetIPv6LinkLocalAddr_Object = MibScalar
cvtNetIPv6LinkLocalAddr = _CvtNetIPv6LinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 34),
    _CvtNetIPv6LinkLocalAddr_Type()
)
cvtNetIPv6LinkLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPv6LinkLocalAddr.setStatus("mandatory")


class _CvtNetIPv6GlobalAddr_Type(DisplayString):
    """Custom type cvtNetIPv6GlobalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtNetIPv6GlobalAddr_Type.__name__ = "DisplayString"
_CvtNetIPv6GlobalAddr_Object = MibScalar
cvtNetIPv6GlobalAddr = _CvtNetIPv6GlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 35),
    _CvtNetIPv6GlobalAddr_Type()
)
cvtNetIPv6GlobalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPv6GlobalAddr.setStatus("mandatory")


class _CvtNetIPv6Gateway_Type(DisplayString):
    """Custom type cvtNetIPv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtNetIPv6Gateway_Type.__name__ = "DisplayString"
_CvtNetIPv6Gateway_Object = MibScalar
cvtNetIPv6Gateway = _CvtNetIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 36),
    _CvtNetIPv6Gateway_Type()
)
cvtNetIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetIPv6Gateway.setStatus("mandatory")


class _CvtNetDHCPv6_Type(Integer32):
    """Custom type cvtNetDHCPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("auto", 1),
          ("force", 2))
    )


_CvtNetDHCPv6_Type.__name__ = "Integer32"
_CvtNetDHCPv6_Object = MibScalar
cvtNetDHCPv6 = _CvtNetDHCPv6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 37),
    _CvtNetDHCPv6_Type()
)
cvtNetDHCPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetDHCPv6.setStatus("mandatory")


class _CvtNetRapidCommit_Type(Integer32):
    """Custom type cvtNetRapidCommit based on Integer32"""
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


_CvtNetRapidCommit_Type.__name__ = "Integer32"
_CvtNetRapidCommit_Object = MibScalar
cvtNetRapidCommit = _CvtNetRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 38),
    _CvtNetRapidCommit_Type()
)
cvtNetRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtNetRapidCommit.setStatus("mandatory")


class _CvtNetCurrentIPv6LinklocalAddr_Type(DisplayString):
    """Custom type cvtNetCurrentIPv6LinklocalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtNetCurrentIPv6LinklocalAddr_Type.__name__ = "DisplayString"
_CvtNetCurrentIPv6LinklocalAddr_Object = MibScalar
cvtNetCurrentIPv6LinklocalAddr = _CvtNetCurrentIPv6LinklocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 39),
    _CvtNetCurrentIPv6LinklocalAddr_Type()
)
cvtNetCurrentIPv6LinklocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentIPv6LinklocalAddr.setStatus("mandatory")


class _CvtNetCurrentIPv6GatewayAddr_Type(DisplayString):
    """Custom type cvtNetCurrentIPv6GatewayAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtNetCurrentIPv6GatewayAddr_Type.__name__ = "DisplayString"
_CvtNetCurrentIPv6GatewayAddr_Object = MibScalar
cvtNetCurrentIPv6GatewayAddr = _CvtNetCurrentIPv6GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 40),
    _CvtNetCurrentIPv6GatewayAddr_Type()
)
cvtNetCurrentIPv6GatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentIPv6GatewayAddr.setStatus("mandatory")


class _CvtNetCurrentDHCPv6DUID_Type(DisplayString):
    """Custom type cvtNetCurrentDHCPv6DUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtNetCurrentDHCPv6DUID_Type.__name__ = "DisplayString"
_CvtNetCurrentDHCPv6DUID_Object = MibScalar
cvtNetCurrentDHCPv6DUID = _CvtNetCurrentDHCPv6DUID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 41),
    _CvtNetCurrentDHCPv6DUID_Type()
)
cvtNetCurrentDHCPv6DUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentDHCPv6DUID.setStatus("mandatory")
_CvtNetCurrentIPv6GlobalAddrTable_Object = MibTable
cvtNetCurrentIPv6GlobalAddrTable = _CvtNetCurrentIPv6GlobalAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 45)
)
if mibBuilder.loadTexts:
    cvtNetCurrentIPv6GlobalAddrTable.setStatus("mandatory")
_CvtNetCurrentIPv6GlobalAddrEntry_Object = MibTableRow
cvtNetCurrentIPv6GlobalAddrEntry = _CvtNetCurrentIPv6GlobalAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 45, 1)
)
cvtNetCurrentIPv6GlobalAddrEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtNetCurrentIPv6GlobalAddrIndex"),
)
if mibBuilder.loadTexts:
    cvtNetCurrentIPv6GlobalAddrEntry.setStatus("mandatory")


class _CvtNetCurrentIPv6GlobalAddrIndex_Type(Integer32):
    """Custom type cvtNetCurrentIPv6GlobalAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtNetCurrentIPv6GlobalAddrIndex_Type.__name__ = "Integer32"
_CvtNetCurrentIPv6GlobalAddrIndex_Object = MibTableColumn
cvtNetCurrentIPv6GlobalAddrIndex = _CvtNetCurrentIPv6GlobalAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 45, 1, 1),
    _CvtNetCurrentIPv6GlobalAddrIndex_Type()
)
cvtNetCurrentIPv6GlobalAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentIPv6GlobalAddrIndex.setStatus("mandatory")
_CvtNetCurrentIPv6GlobalAddrState_Type = DisplayString
_CvtNetCurrentIPv6GlobalAddrState_Object = MibTableColumn
cvtNetCurrentIPv6GlobalAddrState = _CvtNetCurrentIPv6GlobalAddrState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 1, 45, 1, 2),
    _CvtNetCurrentIPv6GlobalAddrState_Type()
)
cvtNetCurrentIPv6GlobalAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtNetCurrentIPv6GlobalAddrState.setStatus("mandatory")
_CvtSystemServiceConfiguration_ObjectIdentity = ObjectIdentity
cvtSystemServiceConfiguration = _CvtSystemServiceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 2)
)


class _CvtServiceWebThreadEn_Type(Integer32):
    """Custom type cvtServiceWebThreadEn based on Integer32"""
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


_CvtServiceWebThreadEn_Type.__name__ = "Integer32"
_CvtServiceWebThreadEn_Object = MibScalar
cvtServiceWebThreadEn = _CvtServiceWebThreadEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 2, 4),
    _CvtServiceWebThreadEn_Type()
)
cvtServiceWebThreadEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtServiceWebThreadEn.setStatus("mandatory")


class _CvtServiceTypeThread_Type(Integer32):
    """Custom type cvtServiceTypeThread based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("telnet", 1),
          ("ssh", 2))
    )


_CvtServiceTypeThread_Type.__name__ = "Integer32"
_CvtServiceTypeThread_Object = MibScalar
cvtServiceTypeThread = _CvtServiceTypeThread_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 2, 11),
    _CvtServiceTypeThread_Type()
)
cvtServiceTypeThread.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtServiceTypeThread.setStatus("mandatory")
_CvtDeviceCommunity_ObjectIdentity = ObjectIdentity
cvtDeviceCommunity = _CvtDeviceCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4)
)
_CvtAgentTable_Object = MibTable
cvtAgentTable = _CvtAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cvtAgentTable.setStatus("mandatory")
_CvtAgentEntry_Object = MibTableRow
cvtAgentEntry = _CvtAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1)
)
cvtAgentEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtAgentIndex"),
)
if mibBuilder.loadTexts:
    cvtAgentEntry.setStatus("mandatory")


class _CvtAgentIndex_Type(Integer32):
    """Custom type cvtAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtAgentIndex_Type.__name__ = "Integer32"
_CvtAgentIndex_Object = MibTableColumn
cvtAgentIndex = _CvtAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1, 1),
    _CvtAgentIndex_Type()
)
cvtAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtAgentIndex.setStatus("mandatory")


class _CvtAgentValid_Type(Integer32):
    """Custom type cvtAgentValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_CvtAgentValid_Type.__name__ = "Integer32"
_CvtAgentValid_Object = MibTableColumn
cvtAgentValid = _CvtAgentValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1, 2),
    _CvtAgentValid_Type()
)
cvtAgentValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtAgentValid.setStatus("mandatory")


class _CvtAgentEnable_Type(Integer32):
    """Custom type cvtAgentEnable based on Integer32"""
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


_CvtAgentEnable_Type.__name__ = "Integer32"
_CvtAgentEnable_Object = MibTableColumn
cvtAgentEnable = _CvtAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1, 3),
    _CvtAgentEnable_Type()
)
cvtAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtAgentEnable.setStatus("mandatory")


class _CvtAgentCommunity_Type(DisplayString):
    """Custom type cvtAgentCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtAgentCommunity_Type.__name__ = "DisplayString"
_CvtAgentCommunity_Object = MibTableColumn
cvtAgentCommunity = _CvtAgentCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1, 4),
    _CvtAgentCommunity_Type()
)
cvtAgentCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtAgentCommunity.setStatus("mandatory")


class _CvtAgentDescription_Type(DisplayString):
    """Custom type cvtAgentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtAgentDescription_Type.__name__ = "DisplayString"
_CvtAgentDescription_Object = MibTableColumn
cvtAgentDescription = _CvtAgentDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1, 6),
    _CvtAgentDescription_Type()
)
cvtAgentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtAgentDescription.setStatus("mandatory")


class _CvtAgentSNMPLevel_Type(Integer32):
    """Custom type cvtAgentSNMPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("administrator", 3))
    )


_CvtAgentSNMPLevel_Type.__name__ = "Integer32"
_CvtAgentSNMPLevel_Object = MibTableColumn
cvtAgentSNMPLevel = _CvtAgentSNMPLevel_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1, 9),
    _CvtAgentSNMPLevel_Type()
)
cvtAgentSNMPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtAgentSNMPLevel.setStatus("mandatory")


class _CvtAgentDelete_Type(Integer32):
    """Custom type cvtAgentDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_CvtAgentDelete_Type.__name__ = "Integer32"
_CvtAgentDelete_Object = MibTableColumn
cvtAgentDelete = _CvtAgentDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 4, 1, 1, 10),
    _CvtAgentDelete_Type()
)
cvtAgentDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtAgentDelete.setStatus("mandatory")
_CvtTrapDestination_ObjectIdentity = ObjectIdentity
cvtTrapDestination = _CvtTrapDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5)
)
_CvtTrapDestTable_Object = MibTable
cvtTrapDestTable = _CvtTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5, 1)
)
if mibBuilder.loadTexts:
    cvtTrapDestTable.setStatus("mandatory")
_CvtTrapDestEntry_Object = MibTableRow
cvtTrapDestEntry = _CvtTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5, 1, 1)
)
cvtTrapDestEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtTrapDestIndex"),
)
if mibBuilder.loadTexts:
    cvtTrapDestEntry.setStatus("mandatory")


class _CvtTrapDestIndex_Type(Integer32):
    """Custom type cvtTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtTrapDestIndex_Type.__name__ = "Integer32"
_CvtTrapDestIndex_Object = MibTableColumn
cvtTrapDestIndex = _CvtTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5, 1, 1, 1),
    _CvtTrapDestIndex_Type()
)
cvtTrapDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtTrapDestIndex.setStatus("mandatory")


class _CvtTrapDestEnable_Type(Integer32):
    """Custom type cvtTrapDestEnable based on Integer32"""
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


_CvtTrapDestEnable_Type.__name__ = "Integer32"
_CvtTrapDestEnable_Object = MibTableColumn
cvtTrapDestEnable = _CvtTrapDestEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5, 1, 1, 3),
    _CvtTrapDestEnable_Type()
)
cvtTrapDestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapDestEnable.setStatus("mandatory")


class _CvtTrapDestCommunity_Type(DisplayString):
    """Custom type cvtTrapDestCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtTrapDestCommunity_Type.__name__ = "DisplayString"
_CvtTrapDestCommunity_Object = MibTableColumn
cvtTrapDestCommunity = _CvtTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5, 1, 1, 4),
    _CvtTrapDestCommunity_Type()
)
cvtTrapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapDestCommunity.setStatus("mandatory")
_CvtTrapDestIPAddr_Type = IpAddress
_CvtTrapDestIPAddr_Object = MibTableColumn
cvtTrapDestIPAddr = _CvtTrapDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5, 1, 1, 8),
    _CvtTrapDestIPAddr_Type()
)
cvtTrapDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapDestIPAddr.setStatus("mandatory")


class _CvtTrapDestIPv6Addr_Type(DisplayString):
    """Custom type cvtTrapDestIPv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtTrapDestIPv6Addr_Type.__name__ = "DisplayString"
_CvtTrapDestIPv6Addr_Object = MibTableColumn
cvtTrapDestIPv6Addr = _CvtTrapDestIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 5, 1, 1, 9),
    _CvtTrapDestIPv6Addr_Type()
)
cvtTrapDestIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapDestIPv6Addr.setStatus("mandatory")
_CvtTrapConfiguration_ObjectIdentity = ObjectIdentity
cvtTrapConfiguration = _CvtTrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6)
)


class _CvtTrapColdStart_Type(Integer32):
    """Custom type cvtTrapColdStart based on Integer32"""
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


_CvtTrapColdStart_Type.__name__ = "Integer32"
_CvtTrapColdStart_Object = MibScalar
cvtTrapColdStart = _CvtTrapColdStart_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6, 1),
    _CvtTrapColdStart_Type()
)
cvtTrapColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapColdStart.setStatus("mandatory")


class _CvtTrapWarmStart_Type(Integer32):
    """Custom type cvtTrapWarmStart based on Integer32"""
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


_CvtTrapWarmStart_Type.__name__ = "Integer32"
_CvtTrapWarmStart_Object = MibScalar
cvtTrapWarmStart = _CvtTrapWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6, 2),
    _CvtTrapWarmStart_Type()
)
cvtTrapWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapWarmStart.setStatus("mandatory")


class _CvtTrapAuthenticationFailure_Type(Integer32):
    """Custom type cvtTrapAuthenticationFailure based on Integer32"""
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


_CvtTrapAuthenticationFailure_Type.__name__ = "Integer32"
_CvtTrapAuthenticationFailure_Object = MibScalar
cvtTrapAuthenticationFailure = _CvtTrapAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6, 3),
    _CvtTrapAuthenticationFailure_Type()
)
cvtTrapAuthenticationFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapAuthenticationFailure.setStatus("mandatory")


class _CvtTrapPortLink_Type(Integer32):
    """Custom type cvtTrapPortLink based on Integer32"""
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


_CvtTrapPortLink_Type.__name__ = "Integer32"
_CvtTrapPortLink_Object = MibScalar
cvtTrapPortLink = _CvtTrapPortLink_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6, 4),
    _CvtTrapPortLink_Type()
)
cvtTrapPortLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapPortLink.setStatus("mandatory")


class _CvtTrapSystemPowerDown_Type(Integer32):
    """Custom type cvtTrapSystemPowerDown based on Integer32"""
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


_CvtTrapSystemPowerDown_Type.__name__ = "Integer32"
_CvtTrapSystemPowerDown_Object = MibScalar
cvtTrapSystemPowerDown = _CvtTrapSystemPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6, 5),
    _CvtTrapSystemPowerDown_Type()
)
cvtTrapSystemPowerDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapSystemPowerDown.setStatus("mandatory")


class _CvtTrapCATVState_Type(Integer32):
    """Custom type cvtTrapCATVState based on Integer32"""
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


_CvtTrapCATVState_Type.__name__ = "Integer32"
_CvtTrapCATVState_Object = MibScalar
cvtTrapCATVState = _CvtTrapCATVState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6, 8),
    _CvtTrapCATVState_Type()
)
cvtTrapCATVState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapCATVState.setStatus("mandatory")


class _CvtTrapBatteryMode_Type(Integer32):
    """Custom type cvtTrapBatteryMode based on Integer32"""
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


_CvtTrapBatteryMode_Type.__name__ = "Integer32"
_CvtTrapBatteryMode_Object = MibScalar
cvtTrapBatteryMode = _CvtTrapBatteryMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 6, 56),
    _CvtTrapBatteryMode_Type()
)
cvtTrapBatteryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTrapBatteryMode.setStatus("mandatory")
_CvtTimeServerConfiguration_ObjectIdentity = ObjectIdentity
cvtTimeServerConfiguration = _CvtTimeServerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7)
)


class _CvtTimeSync_Type(Integer32):
    """Custom type cvtTimeSync based on Integer32"""
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


_CvtTimeSync_Type.__name__ = "Integer32"
_CvtTimeSync_Object = MibScalar
cvtTimeSync = _CvtTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 1),
    _CvtTimeSync_Type()
)
cvtTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTimeSync.setStatus("mandatory")
_CvtTimeServerIPAddr_Type = IpAddress
_CvtTimeServerIPAddr_Object = MibScalar
cvtTimeServerIPAddr = _CvtTimeServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 2),
    _CvtTimeServerIPAddr_Type()
)
cvtTimeServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTimeServerIPAddr.setStatus("mandatory")
_CvtTimeServerIPAddr2_Type = IpAddress
_CvtTimeServerIPAddr2_Object = MibScalar
cvtTimeServerIPAddr2 = _CvtTimeServerIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 3),
    _CvtTimeServerIPAddr2_Type()
)
cvtTimeServerIPAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTimeServerIPAddr2.setStatus("mandatory")


class _CvtTimeSyncInterval_Type(Integer32):
    """Custom type cvtTimeSyncInterval based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("hour1", 1),
          ("hour2", 2),
          ("hour3", 3),
          ("hour4", 4),
          ("hour6", 5),
          ("hour8", 6),
          ("hour12", 7),
          ("hour24", 8))
    )


_CvtTimeSyncInterval_Type.__name__ = "Integer32"
_CvtTimeSyncInterval_Object = MibScalar
cvtTimeSyncInterval = _CvtTimeSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 4),
    _CvtTimeSyncInterval_Type()
)
cvtTimeSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTimeSyncInterval.setStatus("mandatory")


class _CvtTimeZoneIndex_Type(Integer32):
    """Custom type cvtTimeZoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtTimeZoneIndex_Type.__name__ = "Integer32"
_CvtTimeZoneIndex_Object = MibScalar
cvtTimeZoneIndex = _CvtTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 5),
    _CvtTimeZoneIndex_Type()
)
cvtTimeZoneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTimeZoneIndex.setStatus("mandatory")
_CvtTimeZone_Type = DisplayString
_CvtTimeZone_Object = MibScalar
cvtTimeZone = _CvtTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 6),
    _CvtTimeZone_Type()
)
cvtTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtTimeZone.setStatus("mandatory")
_CvtTimeServerIPv6Addr_Type = DisplayString
_CvtTimeServerIPv6Addr_Object = MibScalar
cvtTimeServerIPv6Addr = _CvtTimeServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 20),
    _CvtTimeServerIPv6Addr_Type()
)
cvtTimeServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTimeServerIPv6Addr.setStatus("mandatory")
_CvtTimeServerIPv6Addr2_Type = DisplayString
_CvtTimeServerIPv6Addr2_Object = MibScalar
cvtTimeServerIPv6Addr2 = _CvtTimeServerIPv6Addr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 7, 21),
    _CvtTimeServerIPv6Addr2_Type()
)
cvtTimeServerIPv6Addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtTimeServerIPv6Addr2.setStatus("mandatory")
_CvtCWMPConfiguration_ObjectIdentity = ObjectIdentity
cvtCWMPConfiguration = _CvtCWMPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11)
)


class _CvtCWMPConfigurationCWMPAgent_Type(Integer32):
    """Custom type cvtCWMPConfigurationCWMPAgent based on Integer32"""
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


_CvtCWMPConfigurationCWMPAgent_Type.__name__ = "Integer32"
_CvtCWMPConfigurationCWMPAgent_Object = MibScalar
cvtCWMPConfigurationCWMPAgent = _CvtCWMPConfigurationCWMPAgent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 1),
    _CvtCWMPConfigurationCWMPAgent_Type()
)
cvtCWMPConfigurationCWMPAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationCWMPAgent.setStatus("mandatory")
_CvtCWMPConfigurationServerURL_Type = DisplayString
_CvtCWMPConfigurationServerURL_Object = MibScalar
cvtCWMPConfigurationServerURL = _CvtCWMPConfigurationServerURL_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 2),
    _CvtCWMPConfigurationServerURL_Type()
)
cvtCWMPConfigurationServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationServerURL.setStatus("mandatory")
_CvtCWMPConfigurationServerUsername_Type = DisplayString
_CvtCWMPConfigurationServerUsername_Object = MibScalar
cvtCWMPConfigurationServerUsername = _CvtCWMPConfigurationServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 3),
    _CvtCWMPConfigurationServerUsername_Type()
)
cvtCWMPConfigurationServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationServerUsername.setStatus("mandatory")
_CvtCWMPConfigurationServerPasswrod_Type = DisplayString
_CvtCWMPConfigurationServerPasswrod_Object = MibScalar
cvtCWMPConfigurationServerPasswrod = _CvtCWMPConfigurationServerPasswrod_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 4),
    _CvtCWMPConfigurationServerPasswrod_Type()
)
cvtCWMPConfigurationServerPasswrod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationServerPasswrod.setStatus("mandatory")


class _CvtCWMPConfigurationParameterChangeNotifications_Type(Integer32):
    """Custom type cvtCWMPConfigurationParameterChangeNotifications based on Integer32"""
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


_CvtCWMPConfigurationParameterChangeNotifications_Type.__name__ = "Integer32"
_CvtCWMPConfigurationParameterChangeNotifications_Object = MibScalar
cvtCWMPConfigurationParameterChangeNotifications = _CvtCWMPConfigurationParameterChangeNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 5),
    _CvtCWMPConfigurationParameterChangeNotifications_Type()
)
cvtCWMPConfigurationParameterChangeNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationParameterChangeNotifications.setStatus("mandatory")


class _CvtCWMPConfigurationPeriodicallyInterval_Type(Integer32):
    """Custom type cvtCWMPConfigurationPeriodicallyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtCWMPConfigurationPeriodicallyInterval_Type.__name__ = "Integer32"
_CvtCWMPConfigurationPeriodicallyInterval_Object = MibScalar
cvtCWMPConfigurationPeriodicallyInterval = _CvtCWMPConfigurationPeriodicallyInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 6),
    _CvtCWMPConfigurationPeriodicallyInterval_Type()
)
cvtCWMPConfigurationPeriodicallyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationPeriodicallyInterval.setStatus("mandatory")
_CvtCWMPConfigurationConnectionRequestUsername_Type = DisplayString
_CvtCWMPConfigurationConnectionRequestUsername_Object = MibScalar
cvtCWMPConfigurationConnectionRequestUsername = _CvtCWMPConfigurationConnectionRequestUsername_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 7),
    _CvtCWMPConfigurationConnectionRequestUsername_Type()
)
cvtCWMPConfigurationConnectionRequestUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationConnectionRequestUsername.setStatus("mandatory")
_CvtCWMPConfigurationConnectionRequestPassword_Type = DisplayString
_CvtCWMPConfigurationConnectionRequestPassword_Object = MibScalar
cvtCWMPConfigurationConnectionRequestPassword = _CvtCWMPConfigurationConnectionRequestPassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 8),
    _CvtCWMPConfigurationConnectionRequestPassword_Type()
)
cvtCWMPConfigurationConnectionRequestPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationConnectionRequestPassword.setStatus("mandatory")


class _CvtCWMPConfigurationApply_Type(Integer32):
    """Custom type cvtCWMPConfigurationApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("apply", 1))
    )


_CvtCWMPConfigurationApply_Type.__name__ = "Integer32"
_CvtCWMPConfigurationApply_Object = MibScalar
cvtCWMPConfigurationApply = _CvtCWMPConfigurationApply_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 3, 11, 9),
    _CvtCWMPConfigurationApply_Type()
)
cvtCWMPConfigurationApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtCWMPConfigurationApply.setStatus("mandatory")
_CvtConverterManagement_ObjectIdentity = ObjectIdentity
cvtConverterManagement = _CvtConverterManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4)
)
_CvtConverterConfiguration_ObjectIdentity = ObjectIdentity
cvtConverterConfiguration = _CvtConverterConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 1)
)


class _CvtConverterAgingTime_Type(Integer32):
    """Custom type cvtConverterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 600000),
    )


_CvtConverterAgingTime_Type.__name__ = "Integer32"
_CvtConverterAgingTime_Object = MibScalar
cvtConverterAgingTime = _CvtConverterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 1, 3),
    _CvtConverterAgingTime_Type()
)
cvtConverterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtConverterAgingTime.setStatus("mandatory")


class _CvtConverterSFPPolling_Type(Integer32):
    """Custom type cvtConverterSFPPolling based on Integer32"""
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


_CvtConverterSFPPolling_Type.__name__ = "Integer32"
_CvtConverterSFPPolling_Object = MibScalar
cvtConverterSFPPolling = _CvtConverterSFPPolling_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 1, 51),
    _CvtConverterSFPPolling_Type()
)
cvtConverterSFPPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtConverterSFPPolling.setStatus("mandatory")


class _CvtConverterStatisticsPolling_Type(Integer32):
    """Custom type cvtConverterStatisticsPolling based on Integer32"""
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


_CvtConverterStatisticsPolling_Type.__name__ = "Integer32"
_CvtConverterStatisticsPolling_Object = MibScalar
cvtConverterStatisticsPolling = _CvtConverterStatisticsPolling_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 1, 52),
    _CvtConverterStatisticsPolling_Type()
)
cvtConverterStatisticsPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtConverterStatisticsPolling.setStatus("mandatory")
_CvtPortConfiguration_ObjectIdentity = ObjectIdentity
cvtPortConfiguration = _CvtPortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2)
)
_CvtPortConfigTable_Object = MibTable
cvtPortConfigTable = _CvtPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cvtPortConfigTable.setStatus("mandatory")
_CvtPortConfigEntry_Object = MibTableRow
cvtPortConfigEntry = _CvtPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1)
)
cvtPortConfigEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtPortConfigIndex"),
)
if mibBuilder.loadTexts:
    cvtPortConfigEntry.setStatus("mandatory")


class _CvtPortConfigIndex_Type(Integer32):
    """Custom type cvtPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtPortConfigIndex_Type.__name__ = "Integer32"
_CvtPortConfigIndex_Object = MibTableColumn
cvtPortConfigIndex = _CvtPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 1),
    _CvtPortConfigIndex_Type()
)
cvtPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtPortConfigIndex.setStatus("mandatory")


class _CvtPortConfigState_Type(Integer32):
    """Custom type cvtPortConfigState based on Integer32"""
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


_CvtPortConfigState_Type.__name__ = "Integer32"
_CvtPortConfigState_Object = MibTableColumn
cvtPortConfigState = _CvtPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 2),
    _CvtPortConfigState_Type()
)
cvtPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortConfigState.setStatus("mandatory")


class _CvtPortConfigType_Type(Integer32):
    """Custom type cvtPortConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiation", 0),
          ("manual", 1))
    )


_CvtPortConfigType_Type.__name__ = "Integer32"
_CvtPortConfigType_Object = MibTableColumn
cvtPortConfigType = _CvtPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 3),
    _CvtPortConfigType_Type()
)
cvtPortConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortConfigType.setStatus("mandatory")


class _CvtPortConfigSpeed_Type(Integer32):
    """Custom type cvtPortConfigSpeed based on Integer32"""
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
        *(("speed10M", 0),
          ("speed100M", 1),
          ("speed1000M", 2),
          ("auto-sense", 3))
    )


_CvtPortConfigSpeed_Type.__name__ = "Integer32"
_CvtPortConfigSpeed_Object = MibTableColumn
cvtPortConfigSpeed = _CvtPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 4),
    _CvtPortConfigSpeed_Type()
)
cvtPortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortConfigSpeed.setStatus("mandatory")


class _CvtPortConfigDuplex_Type(Integer32):
    """Custom type cvtPortConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 0),
          ("fullDuplex", 1))
    )


_CvtPortConfigDuplex_Type.__name__ = "Integer32"
_CvtPortConfigDuplex_Object = MibTableColumn
cvtPortConfigDuplex = _CvtPortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 5),
    _CvtPortConfigDuplex_Type()
)
cvtPortConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortConfigDuplex.setStatus("mandatory")


class _CvtPortConfigFlowControl_Type(Integer32):
    """Custom type cvtPortConfigFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CvtPortConfigFlowControl_Type.__name__ = "Integer32"
_CvtPortConfigFlowControl_Object = MibTableColumn
cvtPortConfigFlowControl = _CvtPortConfigFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 6),
    _CvtPortConfigFlowControl_Type()
)
cvtPortConfigFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortConfigFlowControl.setStatus("mandatory")
_CvtPortConfigDescription_Type = DisplayString
_CvtPortConfigDescription_Object = MibTableColumn
cvtPortConfigDescription = _CvtPortConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 7),
    _CvtPortConfigDescription_Type()
)
cvtPortConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortConfigDescription.setStatus("mandatory")


class _CvtPortConfigMediaType_Type(Integer32):
    """Custom type cvtPortConfigMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 0),
          ("fiber", 1),
          ("auto-media", 2))
    )


_CvtPortConfigMediaType_Type.__name__ = "Integer32"
_CvtPortConfigMediaType_Object = MibTableColumn
cvtPortConfigMediaType = _CvtPortConfigMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 8),
    _CvtPortConfigMediaType_Type()
)
cvtPortConfigMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortConfigMediaType.setStatus("mandatory")


class _CvtPortConfigComboMode_Type(Integer32):
    """Custom type cvtPortConfigComboMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("fiber-priority", 1),
          ("copper-priority", 2),
          ("fiber-only", 3),
          ("copper-only", 4))
    )


_CvtPortConfigComboMode_Type.__name__ = "Integer32"
_CvtPortConfigComboMode_Object = MibTableColumn
cvtPortConfigComboMode = _CvtPortConfigComboMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 2, 1, 1, 9),
    _CvtPortConfigComboMode_Type()
)
cvtPortConfigComboMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortConfigComboMode.setStatus("mandatory")
_CvtVLANConfiguration_ObjectIdentity = ObjectIdentity
cvtVLANConfiguration = _CvtVLANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4)
)
_CvtPortVLANConfiguration_ObjectIdentity = ObjectIdentity
cvtPortVLANConfiguration = _CvtPortVLANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1)
)
_CvtPortVLANConfigTable_Object = MibTable
cvtPortVLANConfigTable = _CvtPortVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cvtPortVLANConfigTable.setStatus("mandatory")
_CvtPortVLANConfigEntry_Object = MibTableRow
cvtPortVLANConfigEntry = _CvtPortVLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1)
)
cvtPortVLANConfigEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtPortVLANConfigIndex"),
)
if mibBuilder.loadTexts:
    cvtPortVLANConfigEntry.setStatus("mandatory")


class _CvtPortVLANConfigIndex_Type(Integer32):
    """Custom type cvtPortVLANConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtPortVLANConfigIndex_Type.__name__ = "Integer32"
_CvtPortVLANConfigIndex_Object = MibTableColumn
cvtPortVLANConfigIndex = _CvtPortVLANConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1, 1),
    _CvtPortVLANConfigIndex_Type()
)
cvtPortVLANConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtPortVLANConfigIndex.setStatus("mandatory")


class _CvtPortVLANConfigValid_Type(Integer32):
    """Custom type cvtPortVLANConfigValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_CvtPortVLANConfigValid_Type.__name__ = "Integer32"
_CvtPortVLANConfigValid_Object = MibTableColumn
cvtPortVLANConfigValid = _CvtPortVLANConfigValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1, 2),
    _CvtPortVLANConfigValid_Type()
)
cvtPortVLANConfigValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortVLANConfigValid.setStatus("mandatory")
_CvtPortVLANConfigName_Type = DisplayString
_CvtPortVLANConfigName_Object = MibTableColumn
cvtPortVLANConfigName = _CvtPortVLANConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1, 4),
    _CvtPortVLANConfigName_Type()
)
cvtPortVLANConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortVLANConfigName.setStatus("mandatory")


class _CvtPortVLANConfigPort1_Type(Integer32):
    """Custom type cvtPortVLANConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_CvtPortVLANConfigPort1_Type.__name__ = "Integer32"
_CvtPortVLANConfigPort1_Object = MibTableColumn
cvtPortVLANConfigPort1 = _CvtPortVLANConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1, 5),
    _CvtPortVLANConfigPort1_Type()
)
cvtPortVLANConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortVLANConfigPort1.setStatus("mandatory")


class _CvtPortVLANConfigPort2_Type(Integer32):
    """Custom type cvtPortVLANConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_CvtPortVLANConfigPort2_Type.__name__ = "Integer32"
_CvtPortVLANConfigPort2_Object = MibTableColumn
cvtPortVLANConfigPort2 = _CvtPortVLANConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1, 6),
    _CvtPortVLANConfigPort2_Type()
)
cvtPortVLANConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortVLANConfigPort2.setStatus("mandatory")


class _CvtPortVLANConfigCPU_Type(Integer32):
    """Custom type cvtPortVLANConfigCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_CvtPortVLANConfigCPU_Type.__name__ = "Integer32"
_CvtPortVLANConfigCPU_Object = MibTableColumn
cvtPortVLANConfigCPU = _CvtPortVLANConfigCPU_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1, 55),
    _CvtPortVLANConfigCPU_Type()
)
cvtPortVLANConfigCPU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortVLANConfigCPU.setStatus("mandatory")


class _CvtPortVLANConfigDelete_Type(Integer32):
    """Custom type cvtPortVLANConfigDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_CvtPortVLANConfigDelete_Type.__name__ = "Integer32"
_CvtPortVLANConfigDelete_Object = MibTableColumn
cvtPortVLANConfigDelete = _CvtPortVLANConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 1, 1, 1, 56),
    _CvtPortVLANConfigDelete_Type()
)
cvtPortVLANConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtPortVLANConfigDelete.setStatus("mandatory")
_Cvt8021QVLANConfiguration_ObjectIdentity = ObjectIdentity
cvt8021QVLANConfiguration = _Cvt8021QVLANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2)
)
_Cvt8021QVLANConfig_ObjectIdentity = ObjectIdentity
cvt8021QVLANConfig = _Cvt8021QVLANConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1)
)
_Cvt8021QVLANConfigTable_Object = MibTable
cvt8021QVLANConfigTable = _Cvt8021QVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvt8021QVLANConfigTable.setStatus("mandatory")
_Cvt8021QVLANConfigEntry_Object = MibTableRow
cvt8021QVLANConfigEntry = _Cvt8021QVLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1)
)
cvt8021QVLANConfigEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvt8021QVLANConfigIndex"),
)
if mibBuilder.loadTexts:
    cvt8021QVLANConfigEntry.setStatus("mandatory")


class _Cvt8021QVLANConfigIndex_Type(Integer32):
    """Custom type cvt8021QVLANConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cvt8021QVLANConfigIndex_Type.__name__ = "Integer32"
_Cvt8021QVLANConfigIndex_Object = MibTableColumn
cvt8021QVLANConfigIndex = _Cvt8021QVLANConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 1),
    _Cvt8021QVLANConfigIndex_Type()
)
cvt8021QVLANConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigIndex.setStatus("mandatory")


class _Cvt8021QVLANConfigValid_Type(Integer32):
    """Custom type cvt8021QVLANConfigValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_Cvt8021QVLANConfigValid_Type.__name__ = "Integer32"
_Cvt8021QVLANConfigValid_Object = MibTableColumn
cvt8021QVLANConfigValid = _Cvt8021QVLANConfigValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 2),
    _Cvt8021QVLANConfigValid_Type()
)
cvt8021QVLANConfigValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigValid.setStatus("mandatory")


class _Cvt8021QVLANConfigVID_Type(Integer32):
    """Custom type cvt8021QVLANConfigVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QVLANConfigVID_Type.__name__ = "Integer32"
_Cvt8021QVLANConfigVID_Object = MibTableColumn
cvt8021QVLANConfigVID = _Cvt8021QVLANConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 3),
    _Cvt8021QVLANConfigVID_Type()
)
cvt8021QVLANConfigVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigVID.setStatus("mandatory")
_Cvt8021QVLANConfigName_Type = DisplayString
_Cvt8021QVLANConfigName_Object = MibTableColumn
cvt8021QVLANConfigName = _Cvt8021QVLANConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 4),
    _Cvt8021QVLANConfigName_Type()
)
cvt8021QVLANConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigName.setStatus("mandatory")


class _Cvt8021QVLANConfigPort1_Type(Integer32):
    """Custom type cvt8021QVLANConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Cvt8021QVLANConfigPort1_Type.__name__ = "Integer32"
_Cvt8021QVLANConfigPort1_Object = MibTableColumn
cvt8021QVLANConfigPort1 = _Cvt8021QVLANConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 5),
    _Cvt8021QVLANConfigPort1_Type()
)
cvt8021QVLANConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigPort1.setStatus("mandatory")


class _Cvt8021QVLANConfigPort2_Type(Integer32):
    """Custom type cvt8021QVLANConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Cvt8021QVLANConfigPort2_Type.__name__ = "Integer32"
_Cvt8021QVLANConfigPort2_Object = MibTableColumn
cvt8021QVLANConfigPort2 = _Cvt8021QVLANConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 6),
    _Cvt8021QVLANConfigPort2_Type()
)
cvt8021QVLANConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigPort2.setStatus("mandatory")


class _Cvt8021QVLANConfigCPU_Type(Integer32):
    """Custom type cvt8021QVLANConfigCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Cvt8021QVLANConfigCPU_Type.__name__ = "Integer32"
_Cvt8021QVLANConfigCPU_Object = MibTableColumn
cvt8021QVLANConfigCPU = _Cvt8021QVLANConfigCPU_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 55),
    _Cvt8021QVLANConfigCPU_Type()
)
cvt8021QVLANConfigCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigCPU.setStatus("mandatory")


class _Cvt8021QVLANConfigDelete_Type(Integer32):
    """Custom type cvt8021QVLANConfigDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_Cvt8021QVLANConfigDelete_Type.__name__ = "Integer32"
_Cvt8021QVLANConfigDelete_Object = MibTableColumn
cvt8021QVLANConfigDelete = _Cvt8021QVLANConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 1, 1, 1, 56),
    _Cvt8021QVLANConfigDelete_Type()
)
cvt8021QVLANConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QVLANConfigDelete.setStatus("mandatory")
_Cvt8021QPortVLANConfig_ObjectIdentity = ObjectIdentity
cvt8021QPortVLANConfig = _Cvt8021QPortVLANConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2)
)


class _Cvt8021QCPUPVID_Type(Integer32):
    """Custom type cvt8021QCPUPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QCPUPVID_Type.__name__ = "Integer32"
_Cvt8021QCPUPVID_Object = MibScalar
cvt8021QCPUPVID = _Cvt8021QCPUPVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 1),
    _Cvt8021QCPUPVID_Type()
)
cvt8021QCPUPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvt8021QCPUPVID.setStatus("mandatory")
_Cvt8021QPortVLANConfigTable_Object = MibTable
cvt8021QPortVLANConfigTable = _Cvt8021QPortVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cvt8021QPortVLANConfigTable.setStatus("mandatory")
_Cvt8021QPortVLANConfigEntry_Object = MibTableRow
cvt8021QPortVLANConfigEntry = _Cvt8021QPortVLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 2, 1)
)
cvt8021QPortVLANConfigEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvt8021QPortIndex"),
)
if mibBuilder.loadTexts:
    cvt8021QPortVLANConfigEntry.setStatus("mandatory")


class _Cvt8021QPortIndex_Type(Integer32):
    """Custom type cvt8021QPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cvt8021QPortIndex_Type.__name__ = "Integer32"
_Cvt8021QPortIndex_Object = MibTableColumn
cvt8021QPortIndex = _Cvt8021QPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 2, 1, 1),
    _Cvt8021QPortIndex_Type()
)
cvt8021QPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvt8021QPortIndex.setStatus("mandatory")


class _Cvt8021QPortPVID_Type(Integer32):
    """Custom type cvt8021QPortPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QPortPVID_Type.__name__ = "Integer32"
_Cvt8021QPortPVID_Object = MibTableColumn
cvt8021QPortPVID = _Cvt8021QPortPVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 2, 1, 2),
    _Cvt8021QPortPVID_Type()
)
cvt8021QPortPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPortPVID.setStatus("mandatory")


class _Cvt8021QPortVLANMode_Type(Integer32):
    """Custom type cvt8021QPortVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("trunk", 1),
          ("trunknative", 2))
    )


_Cvt8021QPortVLANMode_Type.__name__ = "Integer32"
_Cvt8021QPortVLANMode_Object = MibTableColumn
cvt8021QPortVLANMode = _Cvt8021QPortVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 2, 1, 20),
    _Cvt8021QPortVLANMode_Type()
)
cvt8021QPortVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPortVLANMode.setStatus("mandatory")


class _Cvt8021QPortUserPriority_Type(Integer32):
    """Custom type cvt8021QPortUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cvt8021QPortUserPriority_Type.__name__ = "Integer32"
_Cvt8021QPortUserPriority_Object = MibTableColumn
cvt8021QPortUserPriority = _Cvt8021QPortUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 2, 1, 21),
    _Cvt8021QPortUserPriority_Type()
)
cvt8021QPortUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPortUserPriority.setStatus("mandatory")


class _Cvt8021QVLANMode_Type(Integer32):
    """Custom type cvt8021QVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("portbase", 1),
          ("tagvlan", 2),
          ("bypassctag", 4))
    )


_Cvt8021QVLANMode_Type.__name__ = "Integer32"
_Cvt8021QVLANMode_Object = MibScalar
cvt8021QVLANMode = _Cvt8021QVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 3),
    _Cvt8021QVLANMode_Type()
)
cvt8021QVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QVLANMode.setStatus("mandatory")


class _Cvt8021QManagementVLAN_Type(Integer32):
    """Custom type cvt8021QManagementVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QManagementVLAN_Type.__name__ = "Integer32"
_Cvt8021QManagementVLAN_Object = MibScalar
cvt8021QManagementVLAN = _Cvt8021QManagementVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 10),
    _Cvt8021QManagementVLAN_Type()
)
cvt8021QManagementVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QManagementVLAN.setStatus("mandatory")


class _Cvt8021QManagementPriority_Type(Integer32):
    """Custom type cvt8021QManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cvt8021QManagementPriority_Type.__name__ = "Integer32"
_Cvt8021QManagementPriority_Object = MibScalar
cvt8021QManagementPriority = _Cvt8021QManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 2, 2, 11),
    _Cvt8021QManagementPriority_Type()
)
cvt8021QManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QManagementPriority.setStatus("mandatory")
_CvtQinQVLANConfiguration_ObjectIdentity = ObjectIdentity
cvtQinQVLANConfiguration = _CvtQinQVLANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5)
)


class _CvtQinQVLANMode_Type(Integer32):
    """Custom type cvtQinQVLANMode based on Integer32"""
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


_CvtQinQVLANMode_Type.__name__ = "Integer32"
_CvtQinQVLANMode_Object = MibScalar
cvtQinQVLANMode = _CvtQinQVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 1),
    _CvtQinQVLANMode_Type()
)
cvtQinQVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQinQVLANMode.setStatus("mandatory")
_CvtQinQVLANEtherType_Type = DisplayString
_CvtQinQVLANEtherType_Object = MibScalar
cvtQinQVLANEtherType = _CvtQinQVLANEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 2),
    _CvtQinQVLANEtherType_Type()
)
cvtQinQVLANEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQinQVLANEtherType.setStatus("mandatory")


class _CvtQinQVLANPassThroughMode_Type(Integer32):
    """Custom type cvtQinQVLANPassThroughMode based on Integer32"""
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


_CvtQinQVLANPassThroughMode_Type.__name__ = "Integer32"
_CvtQinQVLANPassThroughMode_Object = MibScalar
cvtQinQVLANPassThroughMode = _CvtQinQVLANPassThroughMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 57),
    _CvtQinQVLANPassThroughMode_Type()
)
cvtQinQVLANPassThroughMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQinQVLANPassThroughMode.setStatus("mandatory")


class _CvtQinQVLANPassThroughVID_Type(Integer32):
    """Custom type cvtQinQVLANPassThroughVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CvtQinQVLANPassThroughVID_Type.__name__ = "Integer32"
_CvtQinQVLANPassThroughVID_Object = MibScalar
cvtQinQVLANPassThroughVID = _CvtQinQVLANPassThroughVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 59),
    _CvtQinQVLANPassThroughVID_Type()
)
cvtQinQVLANPassThroughVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQinQVLANPassThroughVID.setStatus("mandatory")
_CvtQinQVLANConfigTable_Object = MibTable
cvtQinQVLANConfigTable = _CvtQinQVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 60)
)
if mibBuilder.loadTexts:
    cvtQinQVLANConfigTable.setStatus("mandatory")
_CvtQinQVLANConfigEntry_Object = MibTableRow
cvtQinQVLANConfigEntry = _CvtQinQVLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 60, 1)
)
cvtQinQVLANConfigEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtQinQVLANPortIndex"),
)
if mibBuilder.loadTexts:
    cvtQinQVLANConfigEntry.setStatus("mandatory")


class _CvtQinQVLANPortIndex_Type(Integer32):
    """Custom type cvtQinQVLANPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtQinQVLANPortIndex_Type.__name__ = "Integer32"
_CvtQinQVLANPortIndex_Object = MibTableColumn
cvtQinQVLANPortIndex = _CvtQinQVLANPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 60, 1, 1),
    _CvtQinQVLANPortIndex_Type()
)
cvtQinQVLANPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtQinQVLANPortIndex.setStatus("mandatory")
_CvtQinQVLANPortName_Type = DisplayString
_CvtQinQVLANPortName_Object = MibTableColumn
cvtQinQVLANPortName = _CvtQinQVLANPortName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 60, 1, 3),
    _CvtQinQVLANPortName_Type()
)
cvtQinQVLANPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtQinQVLANPortName.setStatus("mandatory")


class _CvtQinQVLANPortStagVID_Type(Integer32):
    """Custom type cvtQinQVLANPortStagVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CvtQinQVLANPortStagVID_Type.__name__ = "Integer32"
_CvtQinQVLANPortStagVID_Object = MibTableColumn
cvtQinQVLANPortStagVID = _CvtQinQVLANPortStagVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 60, 1, 6),
    _CvtQinQVLANPortStagVID_Type()
)
cvtQinQVLANPortStagVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQinQVLANPortStagVID.setStatus("mandatory")


class _CvtQinQVLANPortISPPort_Type(Integer32):
    """Custom type cvtQinQVLANPortISPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_CvtQinQVLANPortISPPort_Type.__name__ = "Integer32"
_CvtQinQVLANPortISPPort_Object = MibTableColumn
cvtQinQVLANPortISPPort = _CvtQinQVLANPortISPPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 60, 1, 7),
    _CvtQinQVLANPortISPPort_Type()
)
cvtQinQVLANPortISPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQinQVLANPortISPPort.setStatus("mandatory")


class _CvtQinQVLANManagementStag_Type(Integer32):
    """Custom type cvtQinQVLANManagementStag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CvtQinQVLANManagementStag_Type.__name__ = "Integer32"
_CvtQinQVLANManagementStag_Object = MibScalar
cvtQinQVLANManagementStag = _CvtQinQVLANManagementStag_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 5, 61),
    _CvtQinQVLANManagementStag_Type()
)
cvtQinQVLANManagementStag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQinQVLANManagementStag.setStatus("mandatory")
_CvtVLANTranslationConfiguration_ObjectIdentity = ObjectIdentity
cvtVLANTranslationConfiguration = _CvtVLANTranslationConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7)
)


class _CvtVLANTranslationConfigVLANTranslation_Type(Integer32):
    """Custom type cvtVLANTranslationConfigVLANTranslation based on Integer32"""
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


_CvtVLANTranslationConfigVLANTranslation_Type.__name__ = "Integer32"
_CvtVLANTranslationConfigVLANTranslation_Object = MibScalar
cvtVLANTranslationConfigVLANTranslation = _CvtVLANTranslationConfigVLANTranslation_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 1),
    _CvtVLANTranslationConfigVLANTranslation_Type()
)
cvtVLANTranslationConfigVLANTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtVLANTranslationConfigVLANTranslation.setStatus("mandatory")
_Cvt8021QPort1VLANTranslationTable_Object = MibTable
cvt8021QPort1VLANTranslationTable = _Cvt8021QPort1VLANTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 11)
)
if mibBuilder.loadTexts:
    cvt8021QPort1VLANTranslationTable.setStatus("mandatory")
_Cvt8021QPort1VLANTranslationEntry_Object = MibTableRow
cvt8021QPort1VLANTranslationEntry = _Cvt8021QPort1VLANTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 11, 1)
)
cvt8021QPort1VLANTranslationEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvt8021QPort1VLANTranslationIndex"),
)
if mibBuilder.loadTexts:
    cvt8021QPort1VLANTranslationEntry.setStatus("mandatory")


class _Cvt8021QPort1VLANTranslationIndex_Type(Integer32):
    """Custom type cvt8021QPort1VLANTranslationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cvt8021QPort1VLANTranslationIndex_Type.__name__ = "Integer32"
_Cvt8021QPort1VLANTranslationIndex_Object = MibTableColumn
cvt8021QPort1VLANTranslationIndex = _Cvt8021QPort1VLANTranslationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 11, 1, 1),
    _Cvt8021QPort1VLANTranslationIndex_Type()
)
cvt8021QPort1VLANTranslationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvt8021QPort1VLANTranslationIndex.setStatus("mandatory")


class _Cvt8021QPort1VLANTranslationState_Type(Integer32):
    """Custom type cvt8021QPort1VLANTranslationState based on Integer32"""
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


_Cvt8021QPort1VLANTranslationState_Type.__name__ = "Integer32"
_Cvt8021QPort1VLANTranslationState_Object = MibTableColumn
cvt8021QPort1VLANTranslationState = _Cvt8021QPort1VLANTranslationState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 11, 1, 3),
    _Cvt8021QPort1VLANTranslationState_Type()
)
cvt8021QPort1VLANTranslationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort1VLANTranslationState.setStatus("mandatory")


class _Cvt8021QPort1VLANTranslationOriginalVID_Type(Integer32):
    """Custom type cvt8021QPort1VLANTranslationOriginalVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QPort1VLANTranslationOriginalVID_Type.__name__ = "Integer32"
_Cvt8021QPort1VLANTranslationOriginalVID_Object = MibTableColumn
cvt8021QPort1VLANTranslationOriginalVID = _Cvt8021QPort1VLANTranslationOriginalVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 11, 1, 4),
    _Cvt8021QPort1VLANTranslationOriginalVID_Type()
)
cvt8021QPort1VLANTranslationOriginalVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort1VLANTranslationOriginalVID.setStatus("mandatory")


class _Cvt8021QPort1VLANTranslationTranslatedVID_Type(Integer32):
    """Custom type cvt8021QPort1VLANTranslationTranslatedVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QPort1VLANTranslationTranslatedVID_Type.__name__ = "Integer32"
_Cvt8021QPort1VLANTranslationTranslatedVID_Object = MibTableColumn
cvt8021QPort1VLANTranslationTranslatedVID = _Cvt8021QPort1VLANTranslationTranslatedVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 11, 1, 5),
    _Cvt8021QPort1VLANTranslationTranslatedVID_Type()
)
cvt8021QPort1VLANTranslationTranslatedVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort1VLANTranslationTranslatedVID.setStatus("mandatory")


class _Cvt8021QPort1VLANTranslationDelete_Type(Integer32):
    """Custom type cvt8021QPort1VLANTranslationDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_Cvt8021QPort1VLANTranslationDelete_Type.__name__ = "Integer32"
_Cvt8021QPort1VLANTranslationDelete_Object = MibTableColumn
cvt8021QPort1VLANTranslationDelete = _Cvt8021QPort1VLANTranslationDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 11, 1, 10),
    _Cvt8021QPort1VLANTranslationDelete_Type()
)
cvt8021QPort1VLANTranslationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort1VLANTranslationDelete.setStatus("mandatory")
_Cvt8021QPort2VLANTranslationTable_Object = MibTable
cvt8021QPort2VLANTranslationTable = _Cvt8021QPort2VLANTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 12)
)
if mibBuilder.loadTexts:
    cvt8021QPort2VLANTranslationTable.setStatus("mandatory")
_Cvt8021QPort2VLANTranslationEntry_Object = MibTableRow
cvt8021QPort2VLANTranslationEntry = _Cvt8021QPort2VLANTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 12, 1)
)
cvt8021QPort2VLANTranslationEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvt8021QPort2VLANTranslationIndex"),
)
if mibBuilder.loadTexts:
    cvt8021QPort2VLANTranslationEntry.setStatus("mandatory")


class _Cvt8021QPort2VLANTranslationIndex_Type(Integer32):
    """Custom type cvt8021QPort2VLANTranslationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cvt8021QPort2VLANTranslationIndex_Type.__name__ = "Integer32"
_Cvt8021QPort2VLANTranslationIndex_Object = MibTableColumn
cvt8021QPort2VLANTranslationIndex = _Cvt8021QPort2VLANTranslationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 12, 1, 1),
    _Cvt8021QPort2VLANTranslationIndex_Type()
)
cvt8021QPort2VLANTranslationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvt8021QPort2VLANTranslationIndex.setStatus("mandatory")


class _Cvt8021QPort2VLANTranslationState_Type(Integer32):
    """Custom type cvt8021QPort2VLANTranslationState based on Integer32"""
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


_Cvt8021QPort2VLANTranslationState_Type.__name__ = "Integer32"
_Cvt8021QPort2VLANTranslationState_Object = MibTableColumn
cvt8021QPort2VLANTranslationState = _Cvt8021QPort2VLANTranslationState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 12, 1, 3),
    _Cvt8021QPort2VLANTranslationState_Type()
)
cvt8021QPort2VLANTranslationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort2VLANTranslationState.setStatus("mandatory")


class _Cvt8021QPort2VLANTranslationOriginalVID_Type(Integer32):
    """Custom type cvt8021QPort2VLANTranslationOriginalVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QPort2VLANTranslationOriginalVID_Type.__name__ = "Integer32"
_Cvt8021QPort2VLANTranslationOriginalVID_Object = MibTableColumn
cvt8021QPort2VLANTranslationOriginalVID = _Cvt8021QPort2VLANTranslationOriginalVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 12, 1, 4),
    _Cvt8021QPort2VLANTranslationOriginalVID_Type()
)
cvt8021QPort2VLANTranslationOriginalVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort2VLANTranslationOriginalVID.setStatus("mandatory")


class _Cvt8021QPort2VLANTranslationTranslatedVID_Type(Integer32):
    """Custom type cvt8021QPort2VLANTranslationTranslatedVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Cvt8021QPort2VLANTranslationTranslatedVID_Type.__name__ = "Integer32"
_Cvt8021QPort2VLANTranslationTranslatedVID_Object = MibTableColumn
cvt8021QPort2VLANTranslationTranslatedVID = _Cvt8021QPort2VLANTranslationTranslatedVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 12, 1, 5),
    _Cvt8021QPort2VLANTranslationTranslatedVID_Type()
)
cvt8021QPort2VLANTranslationTranslatedVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort2VLANTranslationTranslatedVID.setStatus("mandatory")


class _Cvt8021QPort2VLANTranslationDelete_Type(Integer32):
    """Custom type cvt8021QPort2VLANTranslationDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_Cvt8021QPort2VLANTranslationDelete_Type.__name__ = "Integer32"
_Cvt8021QPort2VLANTranslationDelete_Object = MibTableColumn
cvt8021QPort2VLANTranslationDelete = _Cvt8021QPort2VLANTranslationDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 4, 7, 12, 1, 10),
    _Cvt8021QPort2VLANTranslationDelete_Type()
)
cvt8021QPort2VLANTranslationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021QPort2VLANTranslationDelete.setStatus("mandatory")
_CvtRateLimiting_ObjectIdentity = ObjectIdentity
cvtRateLimiting = _CvtRateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10)
)
_CvtRateLimitingTable_Object = MibTable
cvtRateLimitingTable = _CvtRateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2)
)
if mibBuilder.loadTexts:
    cvtRateLimitingTable.setStatus("mandatory")
_CvtRateLimitingEntry_Object = MibTableRow
cvtRateLimitingEntry = _CvtRateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1)
)
cvtRateLimitingEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtRateLimitingIndex"),
)
if mibBuilder.loadTexts:
    cvtRateLimitingEntry.setStatus("mandatory")


class _CvtRateLimitingIndex_Type(Integer32):
    """Custom type cvtRateLimitingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtRateLimitingIndex_Type.__name__ = "Integer32"
_CvtRateLimitingIndex_Object = MibTableColumn
cvtRateLimitingIndex = _CvtRateLimitingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1, 1),
    _CvtRateLimitingIndex_Type()
)
cvtRateLimitingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtRateLimitingIndex.setStatus("mandatory")


class _CvtRateLimitingIngress_Type(Integer32):
    """Custom type cvtRateLimitingIngress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CvtRateLimitingIngress_Type.__name__ = "Integer32"
_CvtRateLimitingIngress_Object = MibTableColumn
cvtRateLimitingIngress = _CvtRateLimitingIngress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1, 2),
    _CvtRateLimitingIngress_Type()
)
cvtRateLimitingIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtRateLimitingIngress.setStatus("mandatory")


class _CvtRateLimitingIngressBW_Type(Integer32):
    """Custom type cvtRateLimitingIngressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtRateLimitingIngressBW_Type.__name__ = "Integer32"
_CvtRateLimitingIngressBW_Object = MibTableColumn
cvtRateLimitingIngressBW = _CvtRateLimitingIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1, 4),
    _CvtRateLimitingIngressBW_Type()
)
cvtRateLimitingIngressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtRateLimitingIngressBW.setStatus("mandatory")


class _CvtRateLimitingEgress_Type(Integer32):
    """Custom type cvtRateLimitingEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CvtRateLimitingEgress_Type.__name__ = "Integer32"
_CvtRateLimitingEgress_Object = MibTableColumn
cvtRateLimitingEgress = _CvtRateLimitingEgress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1, 5),
    _CvtRateLimitingEgress_Type()
)
cvtRateLimitingEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtRateLimitingEgress.setStatus("mandatory")


class _CvtRateLimitingEgressBW_Type(Integer32):
    """Custom type cvtRateLimitingEgressBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtRateLimitingEgressBW_Type.__name__ = "Integer32"
_CvtRateLimitingEgressBW_Object = MibTableColumn
cvtRateLimitingEgressBW = _CvtRateLimitingEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1, 7),
    _CvtRateLimitingEgressBW_Type()
)
cvtRateLimitingEgressBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtRateLimitingEgressBW.setStatus("mandatory")
_CvtRateLimitingIngressBandwidth_Type = DisplayString
_CvtRateLimitingIngressBandwidth_Object = MibTableColumn
cvtRateLimitingIngressBandwidth = _CvtRateLimitingIngressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1, 40),
    _CvtRateLimitingIngressBandwidth_Type()
)
cvtRateLimitingIngressBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtRateLimitingIngressBandwidth.setStatus("mandatory")
_CvtRateLimitingEgressBandwidth_Type = DisplayString
_CvtRateLimitingEgressBandwidth_Object = MibTableColumn
cvtRateLimitingEgressBandwidth = _CvtRateLimitingEgressBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 10, 2, 1, 41),
    _CvtRateLimitingEgressBandwidth_Type()
)
cvtRateLimitingEgressBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtRateLimitingEgressBandwidth.setStatus("mandatory")
_CvtStormControl_ObjectIdentity = ObjectIdentity
cvtStormControl = _CvtStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 16)
)


class _CvtStormControlMode_Type(Integer32):
    """Custom type cvtStormControlMode based on Integer32"""
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


_CvtStormControlMode_Type.__name__ = "Integer32"
_CvtStormControlMode_Object = MibScalar
cvtStormControlMode = _CvtStormControlMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 16, 20),
    _CvtStormControlMode_Type()
)
cvtStormControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtStormControlMode.setStatus("mandatory")


class _CvtStormControlRates_Type(Integer32):
    """Custom type cvtStormControlRates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1000000),
    )


_CvtStormControlRates_Type.__name__ = "Integer32"
_CvtStormControlRates_Object = MibScalar
cvtStormControlRates = _CvtStormControlRates_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 16, 21),
    _CvtStormControlRates_Type()
)
cvtStormControlRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtStormControlRates.setStatus("mandatory")
_CvtStormControlRatesBandwidth_Type = DisplayString
_CvtStormControlRatesBandwidth_Object = MibScalar
cvtStormControlRatesBandwidth = _CvtStormControlRatesBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 16, 22),
    _CvtStormControlRatesBandwidth_Type()
)
cvtStormControlRatesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtStormControlRatesBandwidth.setStatus("mandatory")
_CvtQoSPriority_ObjectIdentity = ObjectIdentity
cvtQoSPriority = _CvtQoSPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30)
)


class _CvtQoSMode_Type(Integer32):
    """Custom type cvtQoSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("ieee8021p", 2),
          ("dscp", 3))
    )


_CvtQoSMode_Type.__name__ = "Integer32"
_CvtQoSMode_Object = MibScalar
cvtQoSMode = _CvtQoSMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 1),
    _CvtQoSMode_Type()
)
cvtQoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQoSMode.setStatus("mandatory")


class _CvtQueuingMode_Type(Integer32):
    """Custom type cvtQueuingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("weight", 0),
          ("strict", 1))
    )


_CvtQueuingMode_Type.__name__ = "Integer32"
_CvtQueuingMode_Object = MibScalar
cvtQueuingMode = _CvtQueuingMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 2),
    _CvtQueuingMode_Type()
)
cvtQueuingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQueuingMode.setStatus("mandatory")
_Cvt8021pPriorityTable_Object = MibTable
cvt8021pPriorityTable = _Cvt8021pPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 5)
)
if mibBuilder.loadTexts:
    cvt8021pPriorityTable.setStatus("mandatory")
_Cvt8021pPriorityEntry_Object = MibTableRow
cvt8021pPriorityEntry = _Cvt8021pPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 5, 1)
)
cvt8021pPriorityEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvt8021pPriorityIndex"),
)
if mibBuilder.loadTexts:
    cvt8021pPriorityEntry.setStatus("mandatory")


class _Cvt8021pPriorityIndex_Type(Integer32):
    """Custom type cvt8021pPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cvt8021pPriorityIndex_Type.__name__ = "Integer32"
_Cvt8021pPriorityIndex_Object = MibTableColumn
cvt8021pPriorityIndex = _Cvt8021pPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 5, 1, 1),
    _Cvt8021pPriorityIndex_Type()
)
cvt8021pPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvt8021pPriorityIndex.setStatus("mandatory")


class _Cvt8021pPriorityPriority_Type(Integer32):
    """Custom type cvt8021pPriorityPriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021p-0", 0),
          ("ieee8021p-1", 1),
          ("ieee8021p-2", 2),
          ("ieee8021p-3", 3),
          ("ieee8021p-4", 4),
          ("ieee8021p-5", 5),
          ("ieee8021p-6", 6),
          ("ieee8021p-7", 7))
    )


_Cvt8021pPriorityPriority_Type.__name__ = "Integer32"
_Cvt8021pPriorityPriority_Object = MibTableColumn
cvt8021pPriorityPriority = _Cvt8021pPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 5, 1, 2),
    _Cvt8021pPriorityPriority_Type()
)
cvt8021pPriorityPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvt8021pPriorityPriority.setStatus("mandatory")


class _Cvt8021pPriorityQueue_Type(Integer32):
    """Custom type cvt8021pPriorityQueue based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3))
    )


_Cvt8021pPriorityQueue_Type.__name__ = "Integer32"
_Cvt8021pPriorityQueue_Object = MibTableColumn
cvt8021pPriorityQueue = _Cvt8021pPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 5, 1, 3),
    _Cvt8021pPriorityQueue_Type()
)
cvt8021pPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021pPriorityQueue.setStatus("mandatory")
_CvtDSCPPriorityTable_Object = MibTable
cvtDSCPPriorityTable = _CvtDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 6)
)
if mibBuilder.loadTexts:
    cvtDSCPPriorityTable.setStatus("mandatory")
_CvtDSCPPriorityEntry_Object = MibTableRow
cvtDSCPPriorityEntry = _CvtDSCPPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 6, 1)
)
cvtDSCPPriorityEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtDSCPPriorityIndex"),
)
if mibBuilder.loadTexts:
    cvtDSCPPriorityEntry.setStatus("mandatory")


class _CvtDSCPPriorityIndex_Type(Integer32):
    """Custom type cvtDSCPPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtDSCPPriorityIndex_Type.__name__ = "Integer32"
_CvtDSCPPriorityIndex_Object = MibTableColumn
cvtDSCPPriorityIndex = _CvtDSCPPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 6, 1, 1),
    _CvtDSCPPriorityIndex_Type()
)
cvtDSCPPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtDSCPPriorityIndex.setStatus("mandatory")


class _CvtDSCPPriorityPriority_Type(Integer32):
    """Custom type cvtDSCPPriorityPriority based on Integer32"""
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
              63)
        )
    )
    namedValues = NamedValues(
        *(("dscp-0", 0),
          ("dscp-1", 1),
          ("dscp-2", 2),
          ("dscp-3", 3),
          ("dscp-4", 4),
          ("dscp-5", 5),
          ("dscp-6", 6),
          ("dscp-7", 7),
          ("dscp-8", 8),
          ("dscp-9", 9),
          ("dscp-10", 10),
          ("dscp-11", 11),
          ("dscp-12", 12),
          ("dscp-13", 13),
          ("dscp-14", 14),
          ("dscp-15", 15),
          ("dscp-16", 16),
          ("dscp-17", 17),
          ("dscp-18", 18),
          ("dscp-19", 19),
          ("dscp-20", 20),
          ("dscp-21", 21),
          ("dscp-22", 22),
          ("dscp-23", 23),
          ("dscp-24", 24),
          ("dscp-25", 25),
          ("dscp-26", 26),
          ("dscp-27", 27),
          ("dscp-28", 28),
          ("dscp-29", 29),
          ("dscp-30", 30),
          ("dscp-31", 31),
          ("dscp-32", 32),
          ("dscp-33", 33),
          ("dscp-34", 34),
          ("dscp-35", 35),
          ("dscp-36", 36),
          ("dscp-37", 37),
          ("dscp-38", 38),
          ("dscp-39", 39),
          ("dscp-40", 40),
          ("dscp-41", 41),
          ("dscp-42", 42),
          ("dscp-43", 43),
          ("dscp-44", 44),
          ("dscp-45", 45),
          ("dscp-46", 46),
          ("dscp-47", 47),
          ("dscp-48", 48),
          ("dscp-49", 49),
          ("dscp-50", 50),
          ("dscp-51", 51),
          ("dscp-52", 52),
          ("dscp-53", 53),
          ("dscp-54", 54),
          ("dscp-55", 55),
          ("dscp-56", 56),
          ("dscp-57", 57),
          ("dscp-58", 58),
          ("dscp-59", 59),
          ("dscp-60", 60),
          ("dscp-61", 61),
          ("dscp-62", 62),
          ("dscp-63", 63))
    )


_CvtDSCPPriorityPriority_Type.__name__ = "Integer32"
_CvtDSCPPriorityPriority_Object = MibTableColumn
cvtDSCPPriorityPriority = _CvtDSCPPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 6, 1, 2),
    _CvtDSCPPriorityPriority_Type()
)
cvtDSCPPriorityPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtDSCPPriorityPriority.setStatus("mandatory")


class _CvtDSCPPriorityQueue_Type(Integer32):
    """Custom type cvtDSCPPriorityQueue based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3))
    )


_CvtDSCPPriorityQueue_Type.__name__ = "Integer32"
_CvtDSCPPriorityQueue_Object = MibTableColumn
cvtDSCPPriorityQueue = _CvtDSCPPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 6, 1, 3),
    _CvtDSCPPriorityQueue_Type()
)
cvtDSCPPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDSCPPriorityQueue.setStatus("mandatory")


class _CvtQueueWeighted_Type(DisplayString):
    """Custom type cvtQueueWeighted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtQueueWeighted_Type.__name__ = "DisplayString"
_CvtQueueWeighted_Object = MibScalar
cvtQueueWeighted = _CvtQueueWeighted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 11),
    _CvtQueueWeighted_Type()
)
cvtQueueWeighted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtQueueWeighted.setStatus("mandatory")


class _Cvt8021pRemarking_Type(Integer32):
    """Custom type cvt8021pRemarking based on Integer32"""
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


_Cvt8021pRemarking_Type.__name__ = "Integer32"
_Cvt8021pRemarking_Object = MibScalar
cvt8021pRemarking = _Cvt8021pRemarking_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 30),
    _Cvt8021pRemarking_Type()
)
cvt8021pRemarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021pRemarking.setStatus("mandatory")
_Cvt8021pRemarkingTable_Object = MibTable
cvt8021pRemarkingTable = _Cvt8021pRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 31)
)
if mibBuilder.loadTexts:
    cvt8021pRemarkingTable.setStatus("mandatory")
_Cvt8021pRemarkingEntry_Object = MibTableRow
cvt8021pRemarkingEntry = _Cvt8021pRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 31, 1)
)
cvt8021pRemarkingEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvt8021pRemarkingIndex"),
)
if mibBuilder.loadTexts:
    cvt8021pRemarkingEntry.setStatus("mandatory")


class _Cvt8021pRemarkingIndex_Type(Integer32):
    """Custom type cvt8021pRemarkingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cvt8021pRemarkingIndex_Type.__name__ = "Integer32"
_Cvt8021pRemarkingIndex_Object = MibTableColumn
cvt8021pRemarkingIndex = _Cvt8021pRemarkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 31, 1, 1),
    _Cvt8021pRemarkingIndex_Type()
)
cvt8021pRemarkingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvt8021pRemarkingIndex.setStatus("mandatory")


class _Cvt8021pRemarkingNew8021p_Type(Integer32):
    """Custom type cvt8021pRemarkingNew8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cvt8021pRemarkingNew8021p_Type.__name__ = "Integer32"
_Cvt8021pRemarkingNew8021p_Object = MibTableColumn
cvt8021pRemarkingNew8021p = _Cvt8021pRemarkingNew8021p_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 31, 1, 3),
    _Cvt8021pRemarkingNew8021p_Type()
)
cvt8021pRemarkingNew8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021pRemarkingNew8021p.setStatus("mandatory")


class _Cvt8021pRemarkingState_Type(Integer32):
    """Custom type cvt8021pRemarkingState based on Integer32"""
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


_Cvt8021pRemarkingState_Type.__name__ = "Integer32"
_Cvt8021pRemarkingState_Object = MibTableColumn
cvt8021pRemarkingState = _Cvt8021pRemarkingState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 31, 1, 4),
    _Cvt8021pRemarkingState_Type()
)
cvt8021pRemarkingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021pRemarkingState.setStatus("mandatory")


class _Cvt8021pRemarkingRx8021p_Type(Integer32):
    """Custom type cvt8021pRemarkingRx8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cvt8021pRemarkingRx8021p_Type.__name__ = "Integer32"
_Cvt8021pRemarkingRx8021p_Object = MibTableColumn
cvt8021pRemarkingRx8021p = _Cvt8021pRemarkingRx8021p_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 31, 1, 5),
    _Cvt8021pRemarkingRx8021p_Type()
)
cvt8021pRemarkingRx8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvt8021pRemarkingRx8021p.setStatus("mandatory")


class _CvtDSCPRemarking_Type(Integer32):
    """Custom type cvtDSCPRemarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("by-dscp", 1))
    )


_CvtDSCPRemarking_Type.__name__ = "Integer32"
_CvtDSCPRemarking_Object = MibScalar
cvtDSCPRemarking = _CvtDSCPRemarking_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 40),
    _CvtDSCPRemarking_Type()
)
cvtDSCPRemarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDSCPRemarking.setStatus("mandatory")
_CvtDSCPRemarkingTable_Object = MibTable
cvtDSCPRemarkingTable = _CvtDSCPRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 41)
)
if mibBuilder.loadTexts:
    cvtDSCPRemarkingTable.setStatus("mandatory")
_CvtDSCPRemarkingEntry_Object = MibTableRow
cvtDSCPRemarkingEntry = _CvtDSCPRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 41, 1)
)
cvtDSCPRemarkingEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtDSCPRemarkingIndex"),
)
if mibBuilder.loadTexts:
    cvtDSCPRemarkingEntry.setStatus("mandatory")


class _CvtDSCPRemarkingIndex_Type(Integer32):
    """Custom type cvtDSCPRemarkingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtDSCPRemarkingIndex_Type.__name__ = "Integer32"
_CvtDSCPRemarkingIndex_Object = MibTableColumn
cvtDSCPRemarkingIndex = _CvtDSCPRemarkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 41, 1, 1),
    _CvtDSCPRemarkingIndex_Type()
)
cvtDSCPRemarkingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtDSCPRemarkingIndex.setStatus("mandatory")


class _CvtDSCPRemarkingNewDSCP_Type(Integer32):
    """Custom type cvtDSCPRemarkingNewDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CvtDSCPRemarkingNewDSCP_Type.__name__ = "Integer32"
_CvtDSCPRemarkingNewDSCP_Object = MibTableColumn
cvtDSCPRemarkingNewDSCP = _CvtDSCPRemarkingNewDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 41, 1, 3),
    _CvtDSCPRemarkingNewDSCP_Type()
)
cvtDSCPRemarkingNewDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDSCPRemarkingNewDSCP.setStatus("mandatory")


class _CvtDSCPRemarkingState_Type(Integer32):
    """Custom type cvtDSCPRemarkingState based on Integer32"""
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


_CvtDSCPRemarkingState_Type.__name__ = "Integer32"
_CvtDSCPRemarkingState_Object = MibTableColumn
cvtDSCPRemarkingState = _CvtDSCPRemarkingState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 41, 1, 4),
    _CvtDSCPRemarkingState_Type()
)
cvtDSCPRemarkingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDSCPRemarkingState.setStatus("mandatory")


class _CvtDSCPRemarkingRxDSCP_Type(Integer32):
    """Custom type cvtDSCPRemarkingRxDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CvtDSCPRemarkingRxDSCP_Type.__name__ = "Integer32"
_CvtDSCPRemarkingRxDSCP_Object = MibTableColumn
cvtDSCPRemarkingRxDSCP = _CvtDSCPRemarkingRxDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 41, 1, 5),
    _CvtDSCPRemarkingRxDSCP_Type()
)
cvtDSCPRemarkingRxDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDSCPRemarkingRxDSCP.setStatus("mandatory")


class _CvtDSCPRemarkingManagementState_Type(Integer32):
    """Custom type cvtDSCPRemarkingManagementState based on Integer32"""
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


_CvtDSCPRemarkingManagementState_Type.__name__ = "Integer32"
_CvtDSCPRemarkingManagementState_Object = MibScalar
cvtDSCPRemarkingManagementState = _CvtDSCPRemarkingManagementState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 43),
    _CvtDSCPRemarkingManagementState_Type()
)
cvtDSCPRemarkingManagementState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDSCPRemarkingManagementState.setStatus("mandatory")


class _CvtDSCPRemarkingManagementNewDSCP_Type(Integer32):
    """Custom type cvtDSCPRemarkingManagementNewDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CvtDSCPRemarkingManagementNewDSCP_Type.__name__ = "Integer32"
_CvtDSCPRemarkingManagementNewDSCP_Object = MibScalar
cvtDSCPRemarkingManagementNewDSCP = _CvtDSCPRemarkingManagementNewDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 44),
    _CvtDSCPRemarkingManagementNewDSCP_Type()
)
cvtDSCPRemarkingManagementNewDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtDSCPRemarkingManagementNewDSCP.setStatus("mandatory")


class _CvtVIDRemarking_Type(Integer32):
    """Custom type cvtVIDRemarking based on Integer32"""
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


_CvtVIDRemarking_Type.__name__ = "Integer32"
_CvtVIDRemarking_Object = MibScalar
cvtVIDRemarking = _CvtVIDRemarking_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 50),
    _CvtVIDRemarking_Type()
)
cvtVIDRemarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtVIDRemarking.setStatus("mandatory")
_CvtVIDRemarkingTable_Object = MibTable
cvtVIDRemarkingTable = _CvtVIDRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 51)
)
if mibBuilder.loadTexts:
    cvtVIDRemarkingTable.setStatus("mandatory")
_CvtVIDRemarkingEntry_Object = MibTableRow
cvtVIDRemarkingEntry = _CvtVIDRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 51, 1)
)
cvtVIDRemarkingEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtVIDRemarkingIndex"),
)
if mibBuilder.loadTexts:
    cvtVIDRemarkingEntry.setStatus("mandatory")


class _CvtVIDRemarkingIndex_Type(Integer32):
    """Custom type cvtVIDRemarkingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtVIDRemarkingIndex_Type.__name__ = "Integer32"
_CvtVIDRemarkingIndex_Object = MibTableColumn
cvtVIDRemarkingIndex = _CvtVIDRemarkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 51, 1, 1),
    _CvtVIDRemarkingIndex_Type()
)
cvtVIDRemarkingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtVIDRemarkingIndex.setStatus("mandatory")


class _CvtVIDRemarkingPriority_Type(Integer32):
    """Custom type cvtVIDRemarkingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CvtVIDRemarkingPriority_Type.__name__ = "Integer32"
_CvtVIDRemarkingPriority_Object = MibTableColumn
cvtVIDRemarkingPriority = _CvtVIDRemarkingPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 51, 1, 3),
    _CvtVIDRemarkingPriority_Type()
)
cvtVIDRemarkingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtVIDRemarkingPriority.setStatus("mandatory")


class _CvtVIDRemarkingState_Type(Integer32):
    """Custom type cvtVIDRemarkingState based on Integer32"""
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


_CvtVIDRemarkingState_Type.__name__ = "Integer32"
_CvtVIDRemarkingState_Object = MibTableColumn
cvtVIDRemarkingState = _CvtVIDRemarkingState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 51, 1, 4),
    _CvtVIDRemarkingState_Type()
)
cvtVIDRemarkingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtVIDRemarkingState.setStatus("mandatory")


class _CvtVIDRemarkingVID_Type(Integer32):
    """Custom type cvtVIDRemarkingVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CvtVIDRemarkingVID_Type.__name__ = "Integer32"
_CvtVIDRemarkingVID_Object = MibTableColumn
cvtVIDRemarkingVID = _CvtVIDRemarkingVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 4, 30, 51, 1, 5),
    _CvtVIDRemarkingVID_Type()
)
cvtVIDRemarkingVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtVIDRemarkingVID.setStatus("mandatory")
_CvtConverterMonitor_ObjectIdentity = ObjectIdentity
cvtConverterMonitor = _CvtConverterMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5)
)
_CvtPortStatus_ObjectIdentity = ObjectIdentity
cvtPortStatus = _CvtPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1)
)
_CvtPortStatusTable_Object = MibTable
cvtPortStatusTable = _CvtPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cvtPortStatusTable.setStatus("mandatory")
_CvtPortStatusEntry_Object = MibTableRow
cvtPortStatusEntry = _CvtPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1)
)
cvtPortStatusEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtPortStatusIndex"),
)
if mibBuilder.loadTexts:
    cvtPortStatusEntry.setStatus("mandatory")


class _CvtPortStatusIndex_Type(Integer32):
    """Custom type cvtPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtPortStatusIndex_Type.__name__ = "Integer32"
_CvtPortStatusIndex_Object = MibTableColumn
cvtPortStatusIndex = _CvtPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1, 1),
    _CvtPortStatusIndex_Type()
)
cvtPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtPortStatusIndex.setStatus("mandatory")


class _CvtPortStatusPortMedia_Type(Integer32):
    """Custom type cvtPortStatusPortMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("copper", 1),
          ("fiber", 2))
    )


_CvtPortStatusPortMedia_Type.__name__ = "Integer32"
_CvtPortStatusPortMedia_Object = MibTableColumn
cvtPortStatusPortMedia = _CvtPortStatusPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1, 3),
    _CvtPortStatusPortMedia_Type()
)
cvtPortStatusPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortStatusPortMedia.setStatus("mandatory")


class _CvtPortStatusPortState_Type(Integer32):
    """Custom type cvtPortStatusPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("disable", 0),
          ("blocking-listening", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("enable", 4))
    )


_CvtPortStatusPortState_Type.__name__ = "Integer32"
_CvtPortStatusPortState_Object = MibTableColumn
cvtPortStatusPortState = _CvtPortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1, 4),
    _CvtPortStatusPortState_Type()
)
cvtPortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortStatusPortState.setStatus("mandatory")


class _CvtPortStatusPortLink_Type(Integer32):
    """Custom type cvtPortStatusPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("up", 1),
          ("down", 2))
    )


_CvtPortStatusPortLink_Type.__name__ = "Integer32"
_CvtPortStatusPortLink_Object = MibTableColumn
cvtPortStatusPortLink = _CvtPortStatusPortLink_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1, 5),
    _CvtPortStatusPortLink_Type()
)
cvtPortStatusPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortStatusPortLink.setStatus("mandatory")


class _CvtPortStatusPortSpeed_Type(Integer32):
    """Custom type cvtPortStatusPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1))
    )


_CvtPortStatusPortSpeed_Type.__name__ = "Integer32"
_CvtPortStatusPortSpeed_Object = MibTableColumn
cvtPortStatusPortSpeed = _CvtPortStatusPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1, 6),
    _CvtPortStatusPortSpeed_Type()
)
cvtPortStatusPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortStatusPortSpeed.setStatus("mandatory")


class _CvtPortStatusPortDuplex_Type(Integer32):
    """Custom type cvtPortStatusPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("full", 1),
          ("half", 2))
    )


_CvtPortStatusPortDuplex_Type.__name__ = "Integer32"
_CvtPortStatusPortDuplex_Object = MibTableColumn
cvtPortStatusPortDuplex = _CvtPortStatusPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1, 7),
    _CvtPortStatusPortDuplex_Type()
)
cvtPortStatusPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortStatusPortDuplex.setStatus("mandatory")


class _CvtPortStatusPortFlowCtrl_Type(Integer32):
    """Custom type cvtPortStatusPortFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("enable", 1),
          ("disable", 2))
    )


_CvtPortStatusPortFlowCtrl_Type.__name__ = "Integer32"
_CvtPortStatusPortFlowCtrl_Object = MibTableColumn
cvtPortStatusPortFlowCtrl = _CvtPortStatusPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 1, 1, 1, 8),
    _CvtPortStatusPortFlowCtrl_Type()
)
cvtPortStatusPortFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtPortStatusPortFlowCtrl.setStatus("mandatory")
_CvtPortCountersRates_ObjectIdentity = ObjectIdentity
cvtPortCountersRates = _CvtPortCountersRates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5)
)
_CvtCountersRatesTable_Object = MibTable
cvtCountersRatesTable = _CvtCountersRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1)
)
if mibBuilder.loadTexts:
    cvtCountersRatesTable.setStatus("mandatory")
_CvtCountersRatesEntry_Object = MibTableRow
cvtCountersRatesEntry = _CvtCountersRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1)
)
cvtCountersRatesEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtCountersRatesIndex"),
)
if mibBuilder.loadTexts:
    cvtCountersRatesEntry.setStatus("mandatory")


class _CvtCountersRatesIndex_Type(Integer32):
    """Custom type cvtCountersRatesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtCountersRatesIndex_Type.__name__ = "Integer32"
_CvtCountersRatesIndex_Object = MibTableColumn
cvtCountersRatesIndex = _CvtCountersRatesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 1),
    _CvtCountersRatesIndex_Type()
)
cvtCountersRatesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtCountersRatesIndex.setStatus("mandatory")
_CvtCountersRatesBytesReceived_Type = Counter32
_CvtCountersRatesBytesReceived_Object = MibTableColumn
cvtCountersRatesBytesReceived = _CvtCountersRatesBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 2),
    _CvtCountersRatesBytesReceived_Type()
)
cvtCountersRatesBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesBytesReceived.setStatus("mandatory")
_CvtCountersRatesFramesReceived_Type = Counter32
_CvtCountersRatesFramesReceived_Object = MibTableColumn
cvtCountersRatesFramesReceived = _CvtCountersRatesFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 3),
    _CvtCountersRatesFramesReceived_Type()
)
cvtCountersRatesFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesFramesReceived.setStatus("mandatory")
_CvtCountersRatesReceivedUtilization_Type = DisplayString
_CvtCountersRatesReceivedUtilization_Object = MibTableColumn
cvtCountersRatesReceivedUtilization = _CvtCountersRatesReceivedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 4),
    _CvtCountersRatesReceivedUtilization_Type()
)
cvtCountersRatesReceivedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesReceivedUtilization.setStatus("mandatory")
_CvtCountersRatesBytesSent_Type = Counter32
_CvtCountersRatesBytesSent_Object = MibTableColumn
cvtCountersRatesBytesSent = _CvtCountersRatesBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 5),
    _CvtCountersRatesBytesSent_Type()
)
cvtCountersRatesBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesBytesSent.setStatus("mandatory")
_CvtCountersRatesFramesSent_Type = Counter32
_CvtCountersRatesFramesSent_Object = MibTableColumn
cvtCountersRatesFramesSent = _CvtCountersRatesFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 6),
    _CvtCountersRatesFramesSent_Type()
)
cvtCountersRatesFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesFramesSent.setStatus("mandatory")
_CvtCountersRatesSentUtilization_Type = DisplayString
_CvtCountersRatesSentUtilization_Object = MibTableColumn
cvtCountersRatesSentUtilization = _CvtCountersRatesSentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 7),
    _CvtCountersRatesSentUtilization_Type()
)
cvtCountersRatesSentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesSentUtilization.setStatus("mandatory")
_CvtCountersRatesTotalBytes_Type = Counter32
_CvtCountersRatesTotalBytes_Object = MibTableColumn
cvtCountersRatesTotalBytes = _CvtCountersRatesTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 8),
    _CvtCountersRatesTotalBytes_Type()
)
cvtCountersRatesTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTotalBytes.setStatus("mandatory")
_CvtCountersRatesTotalUtilization_Type = DisplayString
_CvtCountersRatesTotalUtilization_Object = MibTableColumn
cvtCountersRatesTotalUtilization = _CvtCountersRatesTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 9),
    _CvtCountersRatesTotalUtilization_Type()
)
cvtCountersRatesTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTotalUtilization.setStatus("mandatory")
_CvtCountersRatesRxCRCError_Type = Counter32
_CvtCountersRatesRxCRCError_Object = MibTableColumn
cvtCountersRatesRxCRCError = _CvtCountersRatesRxCRCError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 10),
    _CvtCountersRatesRxCRCError_Type()
)
cvtCountersRatesRxCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxCRCError.setStatus("mandatory")
_CvtCountersRatesRxFragments_Type = Counter32
_CvtCountersRatesRxFragments_Object = MibTableColumn
cvtCountersRatesRxFragments = _CvtCountersRatesRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 11),
    _CvtCountersRatesRxFragments_Type()
)
cvtCountersRatesRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFragments.setStatus("mandatory")
_CvtCountersRatesRxFilteredFrames_Type = Counter32
_CvtCountersRatesRxFilteredFrames_Object = MibTableColumn
cvtCountersRatesRxFilteredFrames = _CvtCountersRatesRxFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 12),
    _CvtCountersRatesRxFilteredFrames_Type()
)
cvtCountersRatesRxFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFilteredFrames.setStatus("mandatory")
_CvtCountersRatesRxAlignError_Type = Counter32
_CvtCountersRatesRxAlignError_Object = MibTableColumn
cvtCountersRatesRxAlignError = _CvtCountersRatesRxAlignError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 13),
    _CvtCountersRatesRxAlignError_Type()
)
cvtCountersRatesRxAlignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxAlignError.setStatus("mandatory")
_CvtCountersRatesRxUndersizeFrames_Type = Counter32
_CvtCountersRatesRxUndersizeFrames_Object = MibTableColumn
cvtCountersRatesRxUndersizeFrames = _CvtCountersRatesRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 14),
    _CvtCountersRatesRxUndersizeFrames_Type()
)
cvtCountersRatesRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxUndersizeFrames.setStatus("mandatory")
_CvtCountersRatesTxLateCollision_Type = Counter32
_CvtCountersRatesTxLateCollision_Object = MibTableColumn
cvtCountersRatesTxLateCollision = _CvtCountersRatesTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 19),
    _CvtCountersRatesTxLateCollision_Type()
)
cvtCountersRatesTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTxLateCollision.setStatus("mandatory")
_CvtCountersRatesTxDeferred_Type = Counter32
_CvtCountersRatesTxDeferred_Object = MibTableColumn
cvtCountersRatesTxDeferred = _CvtCountersRatesTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 20),
    _CvtCountersRatesTxDeferred_Type()
)
cvtCountersRatesTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTxDeferred.setStatus("mandatory")
_CvtCountersRatesRxFrames64_Type = Counter32
_CvtCountersRatesRxFrames64_Object = MibTableColumn
cvtCountersRatesRxFrames64 = _CvtCountersRatesRxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 22),
    _CvtCountersRatesRxFrames64_Type()
)
cvtCountersRatesRxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFrames64.setStatus("mandatory")
_CvtCountersRatesRxFrames65to127_Type = Counter32
_CvtCountersRatesRxFrames65to127_Object = MibTableColumn
cvtCountersRatesRxFrames65to127 = _CvtCountersRatesRxFrames65to127_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 23),
    _CvtCountersRatesRxFrames65to127_Type()
)
cvtCountersRatesRxFrames65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFrames65to127.setStatus("mandatory")
_CvtCountersRatesRxFrames128to255_Type = Counter32
_CvtCountersRatesRxFrames128to255_Object = MibTableColumn
cvtCountersRatesRxFrames128to255 = _CvtCountersRatesRxFrames128to255_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 24),
    _CvtCountersRatesRxFrames128to255_Type()
)
cvtCountersRatesRxFrames128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFrames128to255.setStatus("mandatory")
_CvtCountersRatesRxFrames256to511_Type = Counter32
_CvtCountersRatesRxFrames256to511_Object = MibTableColumn
cvtCountersRatesRxFrames256to511 = _CvtCountersRatesRxFrames256to511_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 25),
    _CvtCountersRatesRxFrames256to511_Type()
)
cvtCountersRatesRxFrames256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFrames256to511.setStatus("mandatory")
_CvtCountersRatesRxFrames512to1023_Type = Counter32
_CvtCountersRatesRxFrames512to1023_Object = MibTableColumn
cvtCountersRatesRxFrames512to1023 = _CvtCountersRatesRxFrames512to1023_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 26),
    _CvtCountersRatesRxFrames512to1023_Type()
)
cvtCountersRatesRxFrames512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFrames512to1023.setStatus("mandatory")
_CvtCountersRatesRxMulticastFrames_Type = Counter32
_CvtCountersRatesRxMulticastFrames_Object = MibTableColumn
cvtCountersRatesRxMulticastFrames = _CvtCountersRatesRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 29),
    _CvtCountersRatesRxMulticastFrames_Type()
)
cvtCountersRatesRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxMulticastFrames.setStatus("mandatory")
_CvtCountersRatesRxBroadcastFrames_Type = Counter32
_CvtCountersRatesRxBroadcastFrames_Object = MibTableColumn
cvtCountersRatesRxBroadcastFrames = _CvtCountersRatesRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 30),
    _CvtCountersRatesRxBroadcastFrames_Type()
)
cvtCountersRatesRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxBroadcastFrames.setStatus("mandatory")
_CvtCountersRatesTxMulticastFrames_Type = Counter32
_CvtCountersRatesTxMulticastFrames_Object = MibTableColumn
cvtCountersRatesTxMulticastFrames = _CvtCountersRatesTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 32),
    _CvtCountersRatesTxMulticastFrames_Type()
)
cvtCountersRatesTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTxMulticastFrames.setStatus("mandatory")
_CvtCountersRatesTxBroadcastFrames_Type = Counter32
_CvtCountersRatesTxBroadcastFrames_Object = MibTableColumn
cvtCountersRatesTxBroadcastFrames = _CvtCountersRatesTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 33),
    _CvtCountersRatesTxBroadcastFrames_Type()
)
cvtCountersRatesTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTxBroadcastFrames.setStatus("mandatory")
_CvtCountersRatesTxCollision_Type = Counter32
_CvtCountersRatesTxCollision_Object = MibTableColumn
cvtCountersRatesTxCollision = _CvtCountersRatesTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 38),
    _CvtCountersRatesTxCollision_Type()
)
cvtCountersRatesTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTxCollision.setStatus("mandatory")
_CvtCountersRatesTotalErrors_Type = Counter32
_CvtCountersRatesTotalErrors_Object = MibTableColumn
cvtCountersRatesTotalErrors = _CvtCountersRatesTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 39),
    _CvtCountersRatesTotalErrors_Type()
)
cvtCountersRatesTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesTotalErrors.setStatus("mandatory")
_CvtCountersRatesRxFrames1024to1518_Type = Counter32
_CvtCountersRatesRxFrames1024to1518_Object = MibTableColumn
cvtCountersRatesRxFrames1024to1518 = _CvtCountersRatesRxFrames1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 5, 1, 1, 40),
    _CvtCountersRatesRxFrames1024to1518_Type()
)
cvtCountersRatesRxFrames1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersRatesRxFrames1024to1518.setStatus("mandatory")
_CvtPortCountersEvents_ObjectIdentity = ObjectIdentity
cvtPortCountersEvents = _CvtPortCountersEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6)
)
_CvtCountersEventsTable_Object = MibTable
cvtCountersEventsTable = _CvtCountersEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1)
)
if mibBuilder.loadTexts:
    cvtCountersEventsTable.setStatus("mandatory")
_CvtCountersEventsEntry_Object = MibTableRow
cvtCountersEventsEntry = _CvtCountersEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1)
)
cvtCountersEventsEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtCountersEventsIndex"),
)
if mibBuilder.loadTexts:
    cvtCountersEventsEntry.setStatus("mandatory")


class _CvtCountersEventsIndex_Type(Integer32):
    """Custom type cvtCountersEventsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtCountersEventsIndex_Type.__name__ = "Integer32"
_CvtCountersEventsIndex_Object = MibTableColumn
cvtCountersEventsIndex = _CvtCountersEventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 1),
    _CvtCountersEventsIndex_Type()
)
cvtCountersEventsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtCountersEventsIndex.setStatus("mandatory")
_CvtCountersEventsBytesReceived_Type = Counter64
_CvtCountersEventsBytesReceived_Object = MibTableColumn
cvtCountersEventsBytesReceived = _CvtCountersEventsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 2),
    _CvtCountersEventsBytesReceived_Type()
)
cvtCountersEventsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsBytesReceived.setStatus("mandatory")
_CvtCountersEventsFramesReceived_Type = Counter64
_CvtCountersEventsFramesReceived_Object = MibTableColumn
cvtCountersEventsFramesReceived = _CvtCountersEventsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 3),
    _CvtCountersEventsFramesReceived_Type()
)
cvtCountersEventsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsFramesReceived.setStatus("mandatory")
_CvtCountersEventsBytesSent_Type = Counter64
_CvtCountersEventsBytesSent_Object = MibTableColumn
cvtCountersEventsBytesSent = _CvtCountersEventsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 5),
    _CvtCountersEventsBytesSent_Type()
)
cvtCountersEventsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsBytesSent.setStatus("mandatory")
_CvtCountersEventsFramesSent_Type = Counter64
_CvtCountersEventsFramesSent_Object = MibTableColumn
cvtCountersEventsFramesSent = _CvtCountersEventsFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 6),
    _CvtCountersEventsFramesSent_Type()
)
cvtCountersEventsFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsFramesSent.setStatus("mandatory")
_CvtCountersEventsTotalBytes_Type = Counter64
_CvtCountersEventsTotalBytes_Object = MibTableColumn
cvtCountersEventsTotalBytes = _CvtCountersEventsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 8),
    _CvtCountersEventsTotalBytes_Type()
)
cvtCountersEventsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsTotalBytes.setStatus("mandatory")
_CvtCountersEventsRxCRCError_Type = Counter64
_CvtCountersEventsRxCRCError_Object = MibTableColumn
cvtCountersEventsRxCRCError = _CvtCountersEventsRxCRCError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 10),
    _CvtCountersEventsRxCRCError_Type()
)
cvtCountersEventsRxCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxCRCError.setStatus("mandatory")
_CvtCountersEventsRxFragments_Type = Counter64
_CvtCountersEventsRxFragments_Object = MibTableColumn
cvtCountersEventsRxFragments = _CvtCountersEventsRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 11),
    _CvtCountersEventsRxFragments_Type()
)
cvtCountersEventsRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFragments.setStatus("mandatory")
_CvtCountersEventsRxFilteredFrames_Type = Counter64
_CvtCountersEventsRxFilteredFrames_Object = MibTableColumn
cvtCountersEventsRxFilteredFrames = _CvtCountersEventsRxFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 12),
    _CvtCountersEventsRxFilteredFrames_Type()
)
cvtCountersEventsRxFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFilteredFrames.setStatus("mandatory")
_CvtCountersEventsRxAlignError_Type = Counter64
_CvtCountersEventsRxAlignError_Object = MibTableColumn
cvtCountersEventsRxAlignError = _CvtCountersEventsRxAlignError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 13),
    _CvtCountersEventsRxAlignError_Type()
)
cvtCountersEventsRxAlignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxAlignError.setStatus("mandatory")
_CvtCountersEventsRxUndersizeFrames_Type = Counter64
_CvtCountersEventsRxUndersizeFrames_Object = MibTableColumn
cvtCountersEventsRxUndersizeFrames = _CvtCountersEventsRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 14),
    _CvtCountersEventsRxUndersizeFrames_Type()
)
cvtCountersEventsRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxUndersizeFrames.setStatus("mandatory")
_CvtCountersEventsTxLateCollision_Type = Counter64
_CvtCountersEventsTxLateCollision_Object = MibTableColumn
cvtCountersEventsTxLateCollision = _CvtCountersEventsTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 19),
    _CvtCountersEventsTxLateCollision_Type()
)
cvtCountersEventsTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsTxLateCollision.setStatus("mandatory")
_CvtCountersEventsTxDeferred_Type = Counter64
_CvtCountersEventsTxDeferred_Object = MibTableColumn
cvtCountersEventsTxDeferred = _CvtCountersEventsTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 20),
    _CvtCountersEventsTxDeferred_Type()
)
cvtCountersEventsTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsTxDeferred.setStatus("mandatory")
_CvtCountersEventsRxFrames64_Type = Counter64
_CvtCountersEventsRxFrames64_Object = MibTableColumn
cvtCountersEventsRxFrames64 = _CvtCountersEventsRxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 22),
    _CvtCountersEventsRxFrames64_Type()
)
cvtCountersEventsRxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFrames64.setStatus("mandatory")
_CvtCountersEventsRxFrames65to127_Type = Counter64
_CvtCountersEventsRxFrames65to127_Object = MibTableColumn
cvtCountersEventsRxFrames65to127 = _CvtCountersEventsRxFrames65to127_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 23),
    _CvtCountersEventsRxFrames65to127_Type()
)
cvtCountersEventsRxFrames65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFrames65to127.setStatus("mandatory")
_CvtCountersEventsRxFrames128to255_Type = Counter64
_CvtCountersEventsRxFrames128to255_Object = MibTableColumn
cvtCountersEventsRxFrames128to255 = _CvtCountersEventsRxFrames128to255_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 24),
    _CvtCountersEventsRxFrames128to255_Type()
)
cvtCountersEventsRxFrames128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFrames128to255.setStatus("mandatory")
_CvtCountersEventsRxFrames256to511_Type = Counter64
_CvtCountersEventsRxFrames256to511_Object = MibTableColumn
cvtCountersEventsRxFrames256to511 = _CvtCountersEventsRxFrames256to511_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 25),
    _CvtCountersEventsRxFrames256to511_Type()
)
cvtCountersEventsRxFrames256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFrames256to511.setStatus("mandatory")
_CvtCountersEventsRxFrames512to1023_Type = Counter64
_CvtCountersEventsRxFrames512to1023_Object = MibTableColumn
cvtCountersEventsRxFrames512to1023 = _CvtCountersEventsRxFrames512to1023_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 26),
    _CvtCountersEventsRxFrames512to1023_Type()
)
cvtCountersEventsRxFrames512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFrames512to1023.setStatus("mandatory")
_CvtCountersEventsRxMulticastFrames_Type = Counter64
_CvtCountersEventsRxMulticastFrames_Object = MibTableColumn
cvtCountersEventsRxMulticastFrames = _CvtCountersEventsRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 29),
    _CvtCountersEventsRxMulticastFrames_Type()
)
cvtCountersEventsRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxMulticastFrames.setStatus("mandatory")
_CvtCountersEventsRxBroadcastFrames_Type = Counter64
_CvtCountersEventsRxBroadcastFrames_Object = MibTableColumn
cvtCountersEventsRxBroadcastFrames = _CvtCountersEventsRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 30),
    _CvtCountersEventsRxBroadcastFrames_Type()
)
cvtCountersEventsRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxBroadcastFrames.setStatus("mandatory")
_CvtCountersEventsTxMulticastFrames_Type = Counter64
_CvtCountersEventsTxMulticastFrames_Object = MibTableColumn
cvtCountersEventsTxMulticastFrames = _CvtCountersEventsTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 32),
    _CvtCountersEventsTxMulticastFrames_Type()
)
cvtCountersEventsTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsTxMulticastFrames.setStatus("mandatory")
_CvtCountersEventsTxBroadcastFrames_Type = Counter64
_CvtCountersEventsTxBroadcastFrames_Object = MibTableColumn
cvtCountersEventsTxBroadcastFrames = _CvtCountersEventsTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 33),
    _CvtCountersEventsTxBroadcastFrames_Type()
)
cvtCountersEventsTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsTxBroadcastFrames.setStatus("mandatory")
_CvtCountersEventsTxCollision_Type = Counter64
_CvtCountersEventsTxCollision_Object = MibTableColumn
cvtCountersEventsTxCollision = _CvtCountersEventsTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 39),
    _CvtCountersEventsTxCollision_Type()
)
cvtCountersEventsTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsTxCollision.setStatus("mandatory")
_CvtCountersEventsRxFrames1024to1518_Type = Counter64
_CvtCountersEventsRxFrames1024to1518_Object = MibTableColumn
cvtCountersEventsRxFrames1024to1518 = _CvtCountersEventsRxFrames1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 40),
    _CvtCountersEventsRxFrames1024to1518_Type()
)
cvtCountersEventsRxFrames1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsRxFrames1024to1518.setStatus("mandatory")
_CvtCountersEventsTotalErrors_Type = Counter64
_CvtCountersEventsTotalErrors_Object = MibTableColumn
cvtCountersEventsTotalErrors = _CvtCountersEventsTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 1, 1, 42),
    _CvtCountersEventsTotalErrors_Type()
)
cvtCountersEventsTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtCountersEventsTotalErrors.setStatus("mandatory")


class _CvtClearCountersOfAllPort_Type(Integer32):
    """Custom type cvtClearCountersOfAllPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_CvtClearCountersOfAllPort_Type.__name__ = "Integer32"
_CvtClearCountersOfAllPort_Object = MibScalar
cvtClearCountersOfAllPort = _CvtClearCountersOfAllPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 6, 2),
    _CvtClearCountersOfAllPort_Type()
)
cvtClearCountersOfAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtClearCountersOfAllPort.setStatus("mandatory")
_CvtMacAddressTable_ObjectIdentity = ObjectIdentity
cvtMacAddressTable = _CvtMacAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7)
)


class _CvtMacAddressPortSelect_Type(Integer32):
    """Custom type cvtMacAddressPortSelect based on Integer32"""
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
        *(("all", 0),
          ("port1", 1),
          ("port2", 2),
          ("cpu", 3))
    )


_CvtMacAddressPortSelect_Type.__name__ = "Integer32"
_CvtMacAddressPortSelect_Object = MibScalar
cvtMacAddressPortSelect = _CvtMacAddressPortSelect_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 1),
    _CvtMacAddressPortSelect_Type()
)
cvtMacAddressPortSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtMacAddressPortSelect.setStatus("mandatory")


class _CvtMacAddressTotal_Type(Integer32):
    """Custom type cvtMacAddressTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtMacAddressTotal_Type.__name__ = "Integer32"
_CvtMacAddressTotal_Object = MibScalar
cvtMacAddressTotal = _CvtMacAddressTotal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 4),
    _CvtMacAddressTotal_Type()
)
cvtMacAddressTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMacAddressTotal.setStatus("mandatory")
_CvtMacAddressState_Type = DisplayString
_CvtMacAddressState_Object = MibScalar
cvtMacAddressState = _CvtMacAddressState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 5),
    _CvtMacAddressState_Type()
)
cvtMacAddressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMacAddressState.setStatus("mandatory")
_CvtMacTable_Object = MibTable
cvtMacTable = _CvtMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 6)
)
if mibBuilder.loadTexts:
    cvtMacTable.setStatus("mandatory")
_CvtMacTableEntry_Object = MibTableRow
cvtMacTableEntry = _CvtMacTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 6, 1)
)
cvtMacTableEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtMacTableIndex"),
)
if mibBuilder.loadTexts:
    cvtMacTableEntry.setStatus("mandatory")


class _CvtMacTableIndex_Type(Integer32):
    """Custom type cvtMacTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtMacTableIndex_Type.__name__ = "Integer32"
_CvtMacTableIndex_Object = MibTableColumn
cvtMacTableIndex = _CvtMacTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 6, 1, 1),
    _CvtMacTableIndex_Type()
)
cvtMacTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtMacTableIndex.setStatus("mandatory")
_CvtMacTableAddr_Type = MacAddress
_CvtMacTableAddr_Object = MibTableColumn
cvtMacTableAddr = _CvtMacTableAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 6, 1, 2),
    _CvtMacTableAddr_Type()
)
cvtMacTableAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMacTableAddr.setStatus("mandatory")


class _CvtMacTableVID_Type(Integer32):
    """Custom type cvtMacTableVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtMacTableVID_Type.__name__ = "Integer32"
_CvtMacTableVID_Object = MibTableColumn
cvtMacTableVID = _CvtMacTableVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 6, 1, 3),
    _CvtMacTableVID_Type()
)
cvtMacTableVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMacTableVID.setStatus("mandatory")
_CvtMacTablePort_Type = DisplayString
_CvtMacTablePort_Object = MibTableColumn
cvtMacTablePort = _CvtMacTablePort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 6, 1, 4),
    _CvtMacTablePort_Type()
)
cvtMacTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMacTablePort.setStatus("mandatory")
_CvtMacTableType_Type = DisplayString
_CvtMacTableType_Object = MibTableColumn
cvtMacTableType = _CvtMacTableType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 6, 1, 5),
    _CvtMacTableType_Type()
)
cvtMacTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtMacTableType.setStatus("mandatory")


class _CvtMacAddressTop_Type(Integer32):
    """Custom type cvtMacAddressTop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("top", 1))
    )


_CvtMacAddressTop_Type.__name__ = "Integer32"
_CvtMacAddressTop_Object = MibScalar
cvtMacAddressTop = _CvtMacAddressTop_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 7),
    _CvtMacAddressTop_Type()
)
cvtMacAddressTop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtMacAddressTop.setStatus("mandatory")


class _CvtMacAddressNext_Type(Integer32):
    """Custom type cvtMacAddressNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("next", 1))
    )


_CvtMacAddressNext_Type.__name__ = "Integer32"
_CvtMacAddressNext_Object = MibScalar
cvtMacAddressNext = _CvtMacAddressNext_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 7, 8),
    _CvtMacAddressNext_Type()
)
cvtMacAddressNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtMacAddressNext.setStatus("mandatory")
_CvtSFPInformation_ObjectIdentity = ObjectIdentity
cvtSFPInformation = _CvtSFPInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34)
)
_CvtSFPPortInfo_ObjectIdentity = ObjectIdentity
cvtSFPPortInfo = _CvtSFPPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1)
)
_CvtSFPPortInfoTable_Object = MibTable
cvtSFPPortInfoTable = _CvtSFPPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1)
)
if mibBuilder.loadTexts:
    cvtSFPPortInfoTable.setStatus("mandatory")
_CvtSFPPortInfoEntry_Object = MibTableRow
cvtSFPPortInfoEntry = _CvtSFPPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1)
)
cvtSFPPortInfoEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtSFPPortInfoIndex"),
)
if mibBuilder.loadTexts:
    cvtSFPPortInfoEntry.setStatus("mandatory")


class _CvtSFPPortInfoIndex_Type(Integer32):
    """Custom type cvtSFPPortInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtSFPPortInfoIndex_Type.__name__ = "Integer32"
_CvtSFPPortInfoIndex_Object = MibTableColumn
cvtSFPPortInfoIndex = _CvtSFPPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1, 1),
    _CvtSFPPortInfoIndex_Type()
)
cvtSFPPortInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtSFPPortInfoIndex.setStatus("mandatory")
_CvtSFPPortInfoPortName_Type = DisplayString
_CvtSFPPortInfoPortName_Object = MibTableColumn
cvtSFPPortInfoPortName = _CvtSFPPortInfoPortName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1, 3),
    _CvtSFPPortInfoPortName_Type()
)
cvtSFPPortInfoPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortInfoPortName.setStatus("mandatory")
_CvtSFPPortInfoSpeed_Type = DisplayString
_CvtSFPPortInfoSpeed_Object = MibTableColumn
cvtSFPPortInfoSpeed = _CvtSFPPortInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1, 5),
    _CvtSFPPortInfoSpeed_Type()
)
cvtSFPPortInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortInfoSpeed.setStatus("mandatory")
_CvtSFPPortInfoDistance_Type = DisplayString
_CvtSFPPortInfoDistance_Object = MibTableColumn
cvtSFPPortInfoDistance = _CvtSFPPortInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1, 7),
    _CvtSFPPortInfoDistance_Type()
)
cvtSFPPortInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortInfoDistance.setStatus("mandatory")
_CvtSFPPortInfoVendorName_Type = DisplayString
_CvtSFPPortInfoVendorName_Object = MibTableColumn
cvtSFPPortInfoVendorName = _CvtSFPPortInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1, 9),
    _CvtSFPPortInfoVendorName_Type()
)
cvtSFPPortInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortInfoVendorName.setStatus("mandatory")
_CvtSFPPortInfoVendorPN_Type = DisplayString
_CvtSFPPortInfoVendorPN_Object = MibTableColumn
cvtSFPPortInfoVendorPN = _CvtSFPPortInfoVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1, 11),
    _CvtSFPPortInfoVendorPN_Type()
)
cvtSFPPortInfoVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortInfoVendorPN.setStatus("mandatory")
_CvtSFPPortInfoVendorSN_Type = DisplayString
_CvtSFPPortInfoVendorSN_Object = MibTableColumn
cvtSFPPortInfoVendorSN = _CvtSFPPortInfoVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 1, 1, 1, 13),
    _CvtSFPPortInfoVendorSN_Type()
)
cvtSFPPortInfoVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortInfoVendorSN.setStatus("mandatory")
_CvtSFPPortState_ObjectIdentity = ObjectIdentity
cvtSFPPortState = _CvtSFPPortState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2)
)
_CvtSFPPortStateTable_Object = MibTable
cvtSFPPortStateTable = _CvtSFPPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1)
)
if mibBuilder.loadTexts:
    cvtSFPPortStateTable.setStatus("mandatory")
_CvtSFPPortStateEntry_Object = MibTableRow
cvtSFPPortStateEntry = _CvtSFPPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1)
)
cvtSFPPortStateEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtSFPPortStateIndex"),
)
if mibBuilder.loadTexts:
    cvtSFPPortStateEntry.setStatus("mandatory")


class _CvtSFPPortStateIndex_Type(Integer32):
    """Custom type cvtSFPPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtSFPPortStateIndex_Type.__name__ = "Integer32"
_CvtSFPPortStateIndex_Object = MibTableColumn
cvtSFPPortStateIndex = _CvtSFPPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1, 1),
    _CvtSFPPortStateIndex_Type()
)
cvtSFPPortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtSFPPortStateIndex.setStatus("mandatory")
_CvtSFPPortStatePortName_Type = DisplayString
_CvtSFPPortStatePortName_Object = MibTableColumn
cvtSFPPortStatePortName = _CvtSFPPortStatePortName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1, 3),
    _CvtSFPPortStatePortName_Type()
)
cvtSFPPortStatePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortStatePortName.setStatus("mandatory")
_CvtSFPPortStateTemperature_Type = DisplayString
_CvtSFPPortStateTemperature_Object = MibTableColumn
cvtSFPPortStateTemperature = _CvtSFPPortStateTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1, 5),
    _CvtSFPPortStateTemperature_Type()
)
cvtSFPPortStateTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortStateTemperature.setStatus("mandatory")
_CvtSFPPortStateVoltage_Type = DisplayString
_CvtSFPPortStateVoltage_Object = MibTableColumn
cvtSFPPortStateVoltage = _CvtSFPPortStateVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1, 7),
    _CvtSFPPortStateVoltage_Type()
)
cvtSFPPortStateVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortStateVoltage.setStatus("mandatory")
_CvtSFPPortStateTXBias_Type = DisplayString
_CvtSFPPortStateTXBias_Object = MibTableColumn
cvtSFPPortStateTXBias = _CvtSFPPortStateTXBias_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1, 9),
    _CvtSFPPortStateTXBias_Type()
)
cvtSFPPortStateTXBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortStateTXBias.setStatus("mandatory")
_CvtSFPPortStateTXPower_Type = DisplayString
_CvtSFPPortStateTXPower_Object = MibTableColumn
cvtSFPPortStateTXPower = _CvtSFPPortStateTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1, 11),
    _CvtSFPPortStateTXPower_Type()
)
cvtSFPPortStateTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortStateTXPower.setStatus("mandatory")
_CvtSFPPortStateRXPower_Type = DisplayString
_CvtSFPPortStateRXPower_Object = MibTableColumn
cvtSFPPortStateRXPower = _CvtSFPPortStateRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 5, 34, 2, 1, 1, 13),
    _CvtSFPPortStateRXPower_Type()
)
cvtSFPPortStateRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtSFPPortStateRXPower.setStatus("mandatory")
_CvtSystemUtility_ObjectIdentity = ObjectIdentity
cvtSystemUtility = _CvtSystemUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6)
)


class _CvtLoadFactorySetting_Type(Integer32):
    """Custom type cvtLoadFactorySetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("load", 1))
    )


_CvtLoadFactorySetting_Type.__name__ = "Integer32"
_CvtLoadFactorySetting_Object = MibScalar
cvtLoadFactorySetting = _CvtLoadFactorySetting_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 1),
    _CvtLoadFactorySetting_Type()
)
cvtLoadFactorySetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtLoadFactorySetting.setStatus("mandatory")


class _CvtLoadFactorySettingExceptNetworkConfiguration_Type(Integer32):
    """Custom type cvtLoadFactorySettingExceptNetworkConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("load", 1))
    )


_CvtLoadFactorySettingExceptNetworkConfiguration_Type.__name__ = "Integer32"
_CvtLoadFactorySettingExceptNetworkConfiguration_Object = MibScalar
cvtLoadFactorySettingExceptNetworkConfiguration = _CvtLoadFactorySettingExceptNetworkConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 2),
    _CvtLoadFactorySettingExceptNetworkConfiguration_Type()
)
cvtLoadFactorySettingExceptNetworkConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtLoadFactorySettingExceptNetworkConfiguration.setStatus("mandatory")
_CvtEventLog_ObjectIdentity = ObjectIdentity
cvtEventLog = _CvtEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3)
)
_CvtEventLogTable_Object = MibTable
cvtEventLogTable = _CvtEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1)
)
if mibBuilder.loadTexts:
    cvtEventLogTable.setStatus("mandatory")
_CvtEventLogEntry_Object = MibTableRow
cvtEventLogEntry = _CvtEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1)
)
cvtEventLogEntry.setIndexNames(
    (0, "HES-3112-MIB", "cvtEventLogIndex"),
)
if mibBuilder.loadTexts:
    cvtEventLogEntry.setStatus("mandatory")


class _CvtEventLogIndex_Type(Integer32):
    """Custom type cvtEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CvtEventLogIndex_Type.__name__ = "Integer32"
_CvtEventLogIndex_Object = MibTableColumn
cvtEventLogIndex = _CvtEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 1),
    _CvtEventLogIndex_Type()
)
cvtEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtEventLogIndex.setStatus("mandatory")


class _CvtEventLogType_Type(Integer32):
    """Custom type cvtEventLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1000,
              2000,
              3000)
        )
    )
    namedValues = NamedValues(
        *(("error", 1000),
          ("warning", 2000),
          ("information", 3000))
    )


_CvtEventLogType_Type.__name__ = "Integer32"
_CvtEventLogType_Object = MibTableColumn
cvtEventLogType = _CvtEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 2),
    _CvtEventLogType_Type()
)
cvtEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogType.setStatus("mandatory")
_CvtEventLogTime_Type = DisplayString
_CvtEventLogTime_Object = MibTableColumn
cvtEventLogTime = _CvtEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 3),
    _CvtEventLogTime_Type()
)
cvtEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogTime.setStatus("mandatory")
_CvtEventLogUpTime_Type = DisplayString
_CvtEventLogUpTime_Object = MibTableColumn
cvtEventLogUpTime = _CvtEventLogUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 4),
    _CvtEventLogUpTime_Type()
)
cvtEventLogUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogUpTime.setStatus("mandatory")
_CvtEventLogDescription_Type = DisplayString
_CvtEventLogDescription_Object = MibTableColumn
cvtEventLogDescription = _CvtEventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 5),
    _CvtEventLogDescription_Type()
)
cvtEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogDescription.setStatus("mandatory")


class _CvtEventLogSource_Type(Integer32):
    """Custom type cvtEventLogSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4000,
              4001,
              4002,
              4003,
              4004,
              4005,
              4006,
              4007,
              4008,
              4009,
              4010,
              4011,
              4012,
              4013,
              4014,
              4015,
              4016)
        )
    )
    namedValues = NamedValues(
        *(("local-machine", 4000),
          ("rs232d", 4001),
          ("rs232", 4002),
          ("telnetd", 4003),
          ("telnet", 4004),
          ("tftpd", 4005),
          ("tftp", 4006),
          ("ftpd", 4007),
          ("ftp", 4008),
          ("snmpd", 4009),
          ("snmp", 4010),
          ("webd", 4011),
          ("web", 4012),
          ("ping", 4013),
          ("watch-dog", 4014),
          ("remote-machine", 4015),
          ("catv-module", 4016))
    )


_CvtEventLogSource_Type.__name__ = "Integer32"
_CvtEventLogSource_Object = MibTableColumn
cvtEventLogSource = _CvtEventLogSource_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 6),
    _CvtEventLogSource_Type()
)
cvtEventLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogSource.setStatus("mandatory")


class _CvtEventLogEvent_Type(Integer32):
    """Custom type cvtEventLogEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1001,
              1002,
              1003,
              1004,
              1005,
              2001,
              2002,
              2003,
              2004,
              2005,
              2007,
              2008,
              2009,
              2010,
              2011,
              2012,
              2013,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3022)
        )
    )
    namedValues = NamedValues(
        *(("boot-failed", 1001),
          ("load-config-failed", 1002),
          ("load-default-config-failed", 1003),
          ("save-config-failed", 1004),
          ("save-default-config-failed", 1005),
          ("login-failed", 2001),
          ("module-down", 2002),
          ("module-power-down", 2003),
          ("power-module-down", 2004),
          ("power-fan-failed", 2005),
          ("auto-provision", 2007),
          ("fan-failed", 2008),
          ("temperature-abnormality", 2009),
          ("voltage-abnormality", 2010),
          ("tx-bias-abnormality", 2011),
          ("loop", 2012),
          ("upgrade", 2013),
          ("cold-start", 3001),
          ("warm-start", 3002),
          ("login", 3003),
          ("logout", 3004),
          ("timeout", 3005),
          ("disconnected", 3006),
          ("link-up", 3007),
          ("link-down", 3008),
          ("fan-ok", 3022))
    )


_CvtEventLogEvent_Type.__name__ = "Integer32"
_CvtEventLogEvent_Object = MibTableColumn
cvtEventLogEvent = _CvtEventLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 7),
    _CvtEventLogEvent_Type()
)
cvtEventLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogEvent.setStatus("mandatory")
_CvtEventLogNameCommunity_Type = DisplayString
_CvtEventLogNameCommunity_Object = MibTableColumn
cvtEventLogNameCommunity = _CvtEventLogNameCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 8),
    _CvtEventLogNameCommunity_Type()
)
cvtEventLogNameCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogNameCommunity.setStatus("mandatory")
_CvtEventLogIPAddr_Type = IpAddress
_CvtEventLogIPAddr_Object = MibTableColumn
cvtEventLogIPAddr = _CvtEventLogIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 1, 1, 9),
    _CvtEventLogIPAddr_Type()
)
cvtEventLogIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtEventLogIPAddr.setStatus("mandatory")


class _CvtEventLogClear_Type(Integer32):
    """Custom type cvtEventLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_CvtEventLogClear_Type.__name__ = "Integer32"
_CvtEventLogClear_Object = MibScalar
cvtEventLogClear = _CvtEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 3, 2),
    _CvtEventLogClear_Type()
)
cvtEventLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtEventLogClear.setStatus("mandatory")
_CvtUpdateFirmware_ObjectIdentity = ObjectIdentity
cvtUpdateFirmware = _CvtUpdateFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4)
)


class _CvtUpdateProtocol_Type(Integer32):
    """Custom type cvtUpdateProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 0),
          ("ftp", 1))
    )


_CvtUpdateProtocol_Type.__name__ = "Integer32"
_CvtUpdateProtocol_Object = MibScalar
cvtUpdateProtocol = _CvtUpdateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 1),
    _CvtUpdateProtocol_Type()
)
cvtUpdateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateProtocol.setStatus("mandatory")


class _CvtUpdateFileType_Type(Integer32):
    """Custom type cvtUpdateFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("firmware", 0),
          ("configuration", 1))
    )


_CvtUpdateFileType_Type.__name__ = "Integer32"
_CvtUpdateFileType_Object = MibScalar
cvtUpdateFileType = _CvtUpdateFileType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 2),
    _CvtUpdateFileType_Type()
)
cvtUpdateFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateFileType.setStatus("mandatory")
_CvtUpdateServerIPAddr_Type = IpAddress
_CvtUpdateServerIPAddr_Object = MibScalar
cvtUpdateServerIPAddr = _CvtUpdateServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 3),
    _CvtUpdateServerIPAddr_Type()
)
cvtUpdateServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateServerIPAddr.setStatus("mandatory")


class _CvtUpdateUserName_Type(DisplayString):
    """Custom type cvtUpdateUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUpdateUserName_Type.__name__ = "DisplayString"
_CvtUpdateUserName_Object = MibScalar
cvtUpdateUserName = _CvtUpdateUserName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 4),
    _CvtUpdateUserName_Type()
)
cvtUpdateUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateUserName.setStatus("mandatory")


class _CvtUpdatePassword_Type(DisplayString):
    """Custom type cvtUpdatePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUpdatePassword_Type.__name__ = "DisplayString"
_CvtUpdatePassword_Object = MibScalar
cvtUpdatePassword = _CvtUpdatePassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 5),
    _CvtUpdatePassword_Type()
)
cvtUpdatePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdatePassword.setStatus("mandatory")


class _CvtUpdateFileLocation_Type(DisplayString):
    """Custom type cvtUpdateFileLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUpdateFileLocation_Type.__name__ = "DisplayString"
_CvtUpdateFileLocation_Object = MibScalar
cvtUpdateFileLocation = _CvtUpdateFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 6),
    _CvtUpdateFileLocation_Type()
)
cvtUpdateFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateFileLocation.setStatus("mandatory")


class _CvtUpdateBackup_Type(Integer32):
    """Custom type cvtUpdateBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("backup", 1))
    )


_CvtUpdateBackup_Type.__name__ = "Integer32"
_CvtUpdateBackup_Object = MibScalar
cvtUpdateBackup = _CvtUpdateBackup_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 8),
    _CvtUpdateBackup_Type()
)
cvtUpdateBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateBackup.setStatus("mandatory")


class _CvtUpdateUpdate_Type(Integer32):
    """Custom type cvtUpdateUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("update", 1))
    )


_CvtUpdateUpdate_Type.__name__ = "Integer32"
_CvtUpdateUpdate_Object = MibScalar
cvtUpdateUpdate = _CvtUpdateUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 10),
    _CvtUpdateUpdate_Type()
)
cvtUpdateUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateUpdate.setStatus("mandatory")


class _CvtUpdateState_Type(DisplayString):
    """Custom type cvtUpdateState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUpdateState_Type.__name__ = "DisplayString"
_CvtUpdateState_Object = MibScalar
cvtUpdateState = _CvtUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 12),
    _CvtUpdateState_Type()
)
cvtUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtUpdateState.setStatus("mandatory")


class _CvtUpdateServerIPv6Addr_Type(DisplayString):
    """Custom type cvtUpdateServerIPv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvtUpdateServerIPv6Addr_Type.__name__ = "DisplayString"
_CvtUpdateServerIPv6Addr_Object = MibScalar
cvtUpdateServerIPv6Addr = _CvtUpdateServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 6, 4, 13),
    _CvtUpdateServerIPv6Addr_Type()
)
cvtUpdateServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtUpdateServerIPv6Addr.setStatus("mandatory")


class _CvtSaveConfiguration_Type(Integer32):
    """Custom type cvtSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("save", 1))
    )


_CvtSaveConfiguration_Type.__name__ = "Integer32"
_CvtSaveConfiguration_Object = MibScalar
cvtSaveConfiguration = _CvtSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 7),
    _CvtSaveConfiguration_Type()
)
cvtSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtSaveConfiguration.setStatus("mandatory")


class _CvtResetSystem_Type(Integer32):
    """Custom type cvtResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_CvtResetSystem_Type.__name__ = "Integer32"
_CvtResetSystem_Object = MibScalar
cvtResetSystem = _CvtResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 8),
    _CvtResetSystem_Type()
)
cvtResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvtResetSystem.setStatus("mandatory")
_ConverterTraps_ObjectIdentity = ObjectIdentity
converterTraps = _ConverterTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9)
)

# Managed Objects groups


# Notification objects

cvtSystemPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 1)
)
if mibBuilder.loadTexts:
    cvtSystemPowerDown.setStatus(
        ""
    )

cvtBroadcastStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 2)
)
cvtBroadcastStorm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RMON-MIB", "etherStatsBroadcastPkts"))
)
if mibBuilder.loadTexts:
    cvtBroadcastStorm.setStatus(
        ""
    )

cvtBroadcastNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 3)
)
cvtBroadcastNormal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RMON-MIB", "etherStatsBroadcastPkts"))
)
if mibBuilder.loadTexts:
    cvtBroadcastNormal.setStatus(
        ""
    )

cvtFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 8)
)
cvtFaultAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cvtFaultAlarm.setStatus(
        ""
    )

cvtWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 9)
)
cvtWarningAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cvtWarningAlarm.setStatus(
        ""
    )

cvtMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 10)
)
cvtMinorAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cvtMinorAlarm.setStatus(
        ""
    )

cvtLoopBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 13)
)
cvtLoopBack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cvtLoopBack.setStatus(
        ""
    )

cvtBatteryMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 14)
)
cvtBatteryMode.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cvtBatteryMode.setStatus(
        ""
    )

cvtCATVPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 15)
)
cvtCATVPower.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cvtCATVPower.setStatus(
        ""
    )

cvtPowerExceptional = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 300, 3002, 9, 0, 17)
)
cvtPowerExceptional.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    cvtPowerExceptional.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HES-3112-MIB",
    **{"MacAddress": MacAddress,
       "cts": cts,
       "cvt": cvt,
       "hes3112": hes3112,
       "cvtSystemInformation": cvtSystemInformation,
       "cvtCompanyInfo": cvtCompanyInfo,
       "cvtCompanyName": cvtCompanyName,
       "cvtCLIHostname": cvtCLIHostname,
       "cvtDHCPVendorID": cvtDHCPVendorID,
       "cvtHardwareInfo": cvtHardwareInfo,
       "cvtModelName": cvtModelName,
       "cvtFirmwareVersion": cvtFirmwareVersion,
       "cvtGPortNum": cvtGPortNum,
       "cvtMPortNum": cvtMPortNum,
       "cvtMBVersion": cvtMBVersion,
       "cvtLANFiberType": cvtLANFiberType,
       "cvtLANFiberWaveLength": cvtLANFiberWaveLength,
       "cvtWANFiberType": cvtWANFiberType,
       "cvtWANFiberWaveLength": cvtWANFiberWaveLength,
       "cvtSerialNumber": cvtSerialNumber,
       "cvtDateCode": cvtDateCode,
       "cvtCATVModuleInfo": cvtCATVModuleInfo,
       "cvtRFTVOutput": cvtRFTVOutput,
       "cvtRFTVState": cvtRFTVState,
       "cvtBatteryModuleInfo": cvtBatteryModuleInfo,
       "cvtBatteryState": cvtBatteryState,
       "cvtUserAuthentication": cvtUserAuthentication,
       "cvtUserTable": cvtUserTable,
       "cvtUserEntry": cvtUserEntry,
       "cvtUserIndex": cvtUserIndex,
       "cvtUserEnable": cvtUserEnable,
       "cvtUserName": cvtUserName,
       "cvtUserPassword": cvtUserPassword,
       "cvtUserDescription": cvtUserDescription,
       "cvtUserConsoleLevel": cvtUserConsoleLevel,
       "cvtNetworkManagement": cvtNetworkManagement,
       "cvtNetworkConfiguration": cvtNetworkConfiguration,
       "cvtNetMacAddr": cvtNetMacAddr,
       "cvtNetType": cvtNetType,
       "cvtNetIPAddr": cvtNetIPAddr,
       "cvtNetIPMask": cvtNetIPMask,
       "cvtNetGateway": cvtNetGateway,
       "cvtNetIPv4En": cvtNetIPv4En,
       "cvtNetCurrentIPAddr": cvtNetCurrentIPAddr,
       "cvtNetCurrentIPMask": cvtNetCurrentIPMask,
       "cvtNetCurrentGateway": cvtNetCurrentGateway,
       "cvtNetIPSourceBinding": cvtNetIPSourceBinding,
       "cvtNetIPSourceBindingTable": cvtNetIPSourceBindingTable,
       "cvtNetIPSourceBindingEntry": cvtNetIPSourceBindingEntry,
       "cvtNetIPSourceBindingIndex": cvtNetIPSourceBindingIndex,
       "cvtNetIPSourceBindingState": cvtNetIPSourceBindingState,
       "cvtNetIPSourceBindingIPAddress": cvtNetIPSourceBindingIPAddress,
       "cvtNetIPSourceBindingIPv6Address": cvtNetIPSourceBindingIPv6Address,
       "cvtNetIPSourceBindingDelete": cvtNetIPSourceBindingDelete,
       "cvtNetIPv6En": cvtNetIPv6En,
       "cvtNetIPv6AutoConfig": cvtNetIPv6AutoConfig,
       "cvtNetIPv6LinkLocalAddr": cvtNetIPv6LinkLocalAddr,
       "cvtNetIPv6GlobalAddr": cvtNetIPv6GlobalAddr,
       "cvtNetIPv6Gateway": cvtNetIPv6Gateway,
       "cvtNetDHCPv6": cvtNetDHCPv6,
       "cvtNetRapidCommit": cvtNetRapidCommit,
       "cvtNetCurrentIPv6LinklocalAddr": cvtNetCurrentIPv6LinklocalAddr,
       "cvtNetCurrentIPv6GatewayAddr": cvtNetCurrentIPv6GatewayAddr,
       "cvtNetCurrentDHCPv6DUID": cvtNetCurrentDHCPv6DUID,
       "cvtNetCurrentIPv6GlobalAddrTable": cvtNetCurrentIPv6GlobalAddrTable,
       "cvtNetCurrentIPv6GlobalAddrEntry": cvtNetCurrentIPv6GlobalAddrEntry,
       "cvtNetCurrentIPv6GlobalAddrIndex": cvtNetCurrentIPv6GlobalAddrIndex,
       "cvtNetCurrentIPv6GlobalAddrState": cvtNetCurrentIPv6GlobalAddrState,
       "cvtSystemServiceConfiguration": cvtSystemServiceConfiguration,
       "cvtServiceWebThreadEn": cvtServiceWebThreadEn,
       "cvtServiceTypeThread": cvtServiceTypeThread,
       "cvtDeviceCommunity": cvtDeviceCommunity,
       "cvtAgentTable": cvtAgentTable,
       "cvtAgentEntry": cvtAgentEntry,
       "cvtAgentIndex": cvtAgentIndex,
       "cvtAgentValid": cvtAgentValid,
       "cvtAgentEnable": cvtAgentEnable,
       "cvtAgentCommunity": cvtAgentCommunity,
       "cvtAgentDescription": cvtAgentDescription,
       "cvtAgentSNMPLevel": cvtAgentSNMPLevel,
       "cvtAgentDelete": cvtAgentDelete,
       "cvtTrapDestination": cvtTrapDestination,
       "cvtTrapDestTable": cvtTrapDestTable,
       "cvtTrapDestEntry": cvtTrapDestEntry,
       "cvtTrapDestIndex": cvtTrapDestIndex,
       "cvtTrapDestEnable": cvtTrapDestEnable,
       "cvtTrapDestCommunity": cvtTrapDestCommunity,
       "cvtTrapDestIPAddr": cvtTrapDestIPAddr,
       "cvtTrapDestIPv6Addr": cvtTrapDestIPv6Addr,
       "cvtTrapConfiguration": cvtTrapConfiguration,
       "cvtTrapColdStart": cvtTrapColdStart,
       "cvtTrapWarmStart": cvtTrapWarmStart,
       "cvtTrapAuthenticationFailure": cvtTrapAuthenticationFailure,
       "cvtTrapPortLink": cvtTrapPortLink,
       "cvtTrapSystemPowerDown": cvtTrapSystemPowerDown,
       "cvtTrapCATVState": cvtTrapCATVState,
       "cvtTrapBatteryMode": cvtTrapBatteryMode,
       "cvtTimeServerConfiguration": cvtTimeServerConfiguration,
       "cvtTimeSync": cvtTimeSync,
       "cvtTimeServerIPAddr": cvtTimeServerIPAddr,
       "cvtTimeServerIPAddr2": cvtTimeServerIPAddr2,
       "cvtTimeSyncInterval": cvtTimeSyncInterval,
       "cvtTimeZoneIndex": cvtTimeZoneIndex,
       "cvtTimeZone": cvtTimeZone,
       "cvtTimeServerIPv6Addr": cvtTimeServerIPv6Addr,
       "cvtTimeServerIPv6Addr2": cvtTimeServerIPv6Addr2,
       "cvtCWMPConfiguration": cvtCWMPConfiguration,
       "cvtCWMPConfigurationCWMPAgent": cvtCWMPConfigurationCWMPAgent,
       "cvtCWMPConfigurationServerURL": cvtCWMPConfigurationServerURL,
       "cvtCWMPConfigurationServerUsername": cvtCWMPConfigurationServerUsername,
       "cvtCWMPConfigurationServerPasswrod": cvtCWMPConfigurationServerPasswrod,
       "cvtCWMPConfigurationParameterChangeNotifications": cvtCWMPConfigurationParameterChangeNotifications,
       "cvtCWMPConfigurationPeriodicallyInterval": cvtCWMPConfigurationPeriodicallyInterval,
       "cvtCWMPConfigurationConnectionRequestUsername": cvtCWMPConfigurationConnectionRequestUsername,
       "cvtCWMPConfigurationConnectionRequestPassword": cvtCWMPConfigurationConnectionRequestPassword,
       "cvtCWMPConfigurationApply": cvtCWMPConfigurationApply,
       "cvtConverterManagement": cvtConverterManagement,
       "cvtConverterConfiguration": cvtConverterConfiguration,
       "cvtConverterAgingTime": cvtConverterAgingTime,
       "cvtConverterSFPPolling": cvtConverterSFPPolling,
       "cvtConverterStatisticsPolling": cvtConverterStatisticsPolling,
       "cvtPortConfiguration": cvtPortConfiguration,
       "cvtPortConfigTable": cvtPortConfigTable,
       "cvtPortConfigEntry": cvtPortConfigEntry,
       "cvtPortConfigIndex": cvtPortConfigIndex,
       "cvtPortConfigState": cvtPortConfigState,
       "cvtPortConfigType": cvtPortConfigType,
       "cvtPortConfigSpeed": cvtPortConfigSpeed,
       "cvtPortConfigDuplex": cvtPortConfigDuplex,
       "cvtPortConfigFlowControl": cvtPortConfigFlowControl,
       "cvtPortConfigDescription": cvtPortConfigDescription,
       "cvtPortConfigMediaType": cvtPortConfigMediaType,
       "cvtPortConfigComboMode": cvtPortConfigComboMode,
       "cvtVLANConfiguration": cvtVLANConfiguration,
       "cvtPortVLANConfiguration": cvtPortVLANConfiguration,
       "cvtPortVLANConfigTable": cvtPortVLANConfigTable,
       "cvtPortVLANConfigEntry": cvtPortVLANConfigEntry,
       "cvtPortVLANConfigIndex": cvtPortVLANConfigIndex,
       "cvtPortVLANConfigValid": cvtPortVLANConfigValid,
       "cvtPortVLANConfigName": cvtPortVLANConfigName,
       "cvtPortVLANConfigPort1": cvtPortVLANConfigPort1,
       "cvtPortVLANConfigPort2": cvtPortVLANConfigPort2,
       "cvtPortVLANConfigCPU": cvtPortVLANConfigCPU,
       "cvtPortVLANConfigDelete": cvtPortVLANConfigDelete,
       "cvt8021QVLANConfiguration": cvt8021QVLANConfiguration,
       "cvt8021QVLANConfig": cvt8021QVLANConfig,
       "cvt8021QVLANConfigTable": cvt8021QVLANConfigTable,
       "cvt8021QVLANConfigEntry": cvt8021QVLANConfigEntry,
       "cvt8021QVLANConfigIndex": cvt8021QVLANConfigIndex,
       "cvt8021QVLANConfigValid": cvt8021QVLANConfigValid,
       "cvt8021QVLANConfigVID": cvt8021QVLANConfigVID,
       "cvt8021QVLANConfigName": cvt8021QVLANConfigName,
       "cvt8021QVLANConfigPort1": cvt8021QVLANConfigPort1,
       "cvt8021QVLANConfigPort2": cvt8021QVLANConfigPort2,
       "cvt8021QVLANConfigCPU": cvt8021QVLANConfigCPU,
       "cvt8021QVLANConfigDelete": cvt8021QVLANConfigDelete,
       "cvt8021QPortVLANConfig": cvt8021QPortVLANConfig,
       "cvt8021QCPUPVID": cvt8021QCPUPVID,
       "cvt8021QPortVLANConfigTable": cvt8021QPortVLANConfigTable,
       "cvt8021QPortVLANConfigEntry": cvt8021QPortVLANConfigEntry,
       "cvt8021QPortIndex": cvt8021QPortIndex,
       "cvt8021QPortPVID": cvt8021QPortPVID,
       "cvt8021QPortVLANMode": cvt8021QPortVLANMode,
       "cvt8021QPortUserPriority": cvt8021QPortUserPriority,
       "cvt8021QVLANMode": cvt8021QVLANMode,
       "cvt8021QManagementVLAN": cvt8021QManagementVLAN,
       "cvt8021QManagementPriority": cvt8021QManagementPriority,
       "cvtQinQVLANConfiguration": cvtQinQVLANConfiguration,
       "cvtQinQVLANMode": cvtQinQVLANMode,
       "cvtQinQVLANEtherType": cvtQinQVLANEtherType,
       "cvtQinQVLANPassThroughMode": cvtQinQVLANPassThroughMode,
       "cvtQinQVLANPassThroughVID": cvtQinQVLANPassThroughVID,
       "cvtQinQVLANConfigTable": cvtQinQVLANConfigTable,
       "cvtQinQVLANConfigEntry": cvtQinQVLANConfigEntry,
       "cvtQinQVLANPortIndex": cvtQinQVLANPortIndex,
       "cvtQinQVLANPortName": cvtQinQVLANPortName,
       "cvtQinQVLANPortStagVID": cvtQinQVLANPortStagVID,
       "cvtQinQVLANPortISPPort": cvtQinQVLANPortISPPort,
       "cvtQinQVLANManagementStag": cvtQinQVLANManagementStag,
       "cvtVLANTranslationConfiguration": cvtVLANTranslationConfiguration,
       "cvtVLANTranslationConfigVLANTranslation": cvtVLANTranslationConfigVLANTranslation,
       "cvt8021QPort1VLANTranslationTable": cvt8021QPort1VLANTranslationTable,
       "cvt8021QPort1VLANTranslationEntry": cvt8021QPort1VLANTranslationEntry,
       "cvt8021QPort1VLANTranslationIndex": cvt8021QPort1VLANTranslationIndex,
       "cvt8021QPort1VLANTranslationState": cvt8021QPort1VLANTranslationState,
       "cvt8021QPort1VLANTranslationOriginalVID": cvt8021QPort1VLANTranslationOriginalVID,
       "cvt8021QPort1VLANTranslationTranslatedVID": cvt8021QPort1VLANTranslationTranslatedVID,
       "cvt8021QPort1VLANTranslationDelete": cvt8021QPort1VLANTranslationDelete,
       "cvt8021QPort2VLANTranslationTable": cvt8021QPort2VLANTranslationTable,
       "cvt8021QPort2VLANTranslationEntry": cvt8021QPort2VLANTranslationEntry,
       "cvt8021QPort2VLANTranslationIndex": cvt8021QPort2VLANTranslationIndex,
       "cvt8021QPort2VLANTranslationState": cvt8021QPort2VLANTranslationState,
       "cvt8021QPort2VLANTranslationOriginalVID": cvt8021QPort2VLANTranslationOriginalVID,
       "cvt8021QPort2VLANTranslationTranslatedVID": cvt8021QPort2VLANTranslationTranslatedVID,
       "cvt8021QPort2VLANTranslationDelete": cvt8021QPort2VLANTranslationDelete,
       "cvtRateLimiting": cvtRateLimiting,
       "cvtRateLimitingTable": cvtRateLimitingTable,
       "cvtRateLimitingEntry": cvtRateLimitingEntry,
       "cvtRateLimitingIndex": cvtRateLimitingIndex,
       "cvtRateLimitingIngress": cvtRateLimitingIngress,
       "cvtRateLimitingIngressBW": cvtRateLimitingIngressBW,
       "cvtRateLimitingEgress": cvtRateLimitingEgress,
       "cvtRateLimitingEgressBW": cvtRateLimitingEgressBW,
       "cvtRateLimitingIngressBandwidth": cvtRateLimitingIngressBandwidth,
       "cvtRateLimitingEgressBandwidth": cvtRateLimitingEgressBandwidth,
       "cvtStormControl": cvtStormControl,
       "cvtStormControlMode": cvtStormControlMode,
       "cvtStormControlRates": cvtStormControlRates,
       "cvtStormControlRatesBandwidth": cvtStormControlRatesBandwidth,
       "cvtQoSPriority": cvtQoSPriority,
       "cvtQoSMode": cvtQoSMode,
       "cvtQueuingMode": cvtQueuingMode,
       "cvt8021pPriorityTable": cvt8021pPriorityTable,
       "cvt8021pPriorityEntry": cvt8021pPriorityEntry,
       "cvt8021pPriorityIndex": cvt8021pPriorityIndex,
       "cvt8021pPriorityPriority": cvt8021pPriorityPriority,
       "cvt8021pPriorityQueue": cvt8021pPriorityQueue,
       "cvtDSCPPriorityTable": cvtDSCPPriorityTable,
       "cvtDSCPPriorityEntry": cvtDSCPPriorityEntry,
       "cvtDSCPPriorityIndex": cvtDSCPPriorityIndex,
       "cvtDSCPPriorityPriority": cvtDSCPPriorityPriority,
       "cvtDSCPPriorityQueue": cvtDSCPPriorityQueue,
       "cvtQueueWeighted": cvtQueueWeighted,
       "cvt8021pRemarking": cvt8021pRemarking,
       "cvt8021pRemarkingTable": cvt8021pRemarkingTable,
       "cvt8021pRemarkingEntry": cvt8021pRemarkingEntry,
       "cvt8021pRemarkingIndex": cvt8021pRemarkingIndex,
       "cvt8021pRemarkingNew8021p": cvt8021pRemarkingNew8021p,
       "cvt8021pRemarkingState": cvt8021pRemarkingState,
       "cvt8021pRemarkingRx8021p": cvt8021pRemarkingRx8021p,
       "cvtDSCPRemarking": cvtDSCPRemarking,
       "cvtDSCPRemarkingTable": cvtDSCPRemarkingTable,
       "cvtDSCPRemarkingEntry": cvtDSCPRemarkingEntry,
       "cvtDSCPRemarkingIndex": cvtDSCPRemarkingIndex,
       "cvtDSCPRemarkingNewDSCP": cvtDSCPRemarkingNewDSCP,
       "cvtDSCPRemarkingState": cvtDSCPRemarkingState,
       "cvtDSCPRemarkingRxDSCP": cvtDSCPRemarkingRxDSCP,
       "cvtDSCPRemarkingManagementState": cvtDSCPRemarkingManagementState,
       "cvtDSCPRemarkingManagementNewDSCP": cvtDSCPRemarkingManagementNewDSCP,
       "cvtVIDRemarking": cvtVIDRemarking,
       "cvtVIDRemarkingTable": cvtVIDRemarkingTable,
       "cvtVIDRemarkingEntry": cvtVIDRemarkingEntry,
       "cvtVIDRemarkingIndex": cvtVIDRemarkingIndex,
       "cvtVIDRemarkingPriority": cvtVIDRemarkingPriority,
       "cvtVIDRemarkingState": cvtVIDRemarkingState,
       "cvtVIDRemarkingVID": cvtVIDRemarkingVID,
       "cvtConverterMonitor": cvtConverterMonitor,
       "cvtPortStatus": cvtPortStatus,
       "cvtPortStatusTable": cvtPortStatusTable,
       "cvtPortStatusEntry": cvtPortStatusEntry,
       "cvtPortStatusIndex": cvtPortStatusIndex,
       "cvtPortStatusPortMedia": cvtPortStatusPortMedia,
       "cvtPortStatusPortState": cvtPortStatusPortState,
       "cvtPortStatusPortLink": cvtPortStatusPortLink,
       "cvtPortStatusPortSpeed": cvtPortStatusPortSpeed,
       "cvtPortStatusPortDuplex": cvtPortStatusPortDuplex,
       "cvtPortStatusPortFlowCtrl": cvtPortStatusPortFlowCtrl,
       "cvtPortCountersRates": cvtPortCountersRates,
       "cvtCountersRatesTable": cvtCountersRatesTable,
       "cvtCountersRatesEntry": cvtCountersRatesEntry,
       "cvtCountersRatesIndex": cvtCountersRatesIndex,
       "cvtCountersRatesBytesReceived": cvtCountersRatesBytesReceived,
       "cvtCountersRatesFramesReceived": cvtCountersRatesFramesReceived,
       "cvtCountersRatesReceivedUtilization": cvtCountersRatesReceivedUtilization,
       "cvtCountersRatesBytesSent": cvtCountersRatesBytesSent,
       "cvtCountersRatesFramesSent": cvtCountersRatesFramesSent,
       "cvtCountersRatesSentUtilization": cvtCountersRatesSentUtilization,
       "cvtCountersRatesTotalBytes": cvtCountersRatesTotalBytes,
       "cvtCountersRatesTotalUtilization": cvtCountersRatesTotalUtilization,
       "cvtCountersRatesRxCRCError": cvtCountersRatesRxCRCError,
       "cvtCountersRatesRxFragments": cvtCountersRatesRxFragments,
       "cvtCountersRatesRxFilteredFrames": cvtCountersRatesRxFilteredFrames,
       "cvtCountersRatesRxAlignError": cvtCountersRatesRxAlignError,
       "cvtCountersRatesRxUndersizeFrames": cvtCountersRatesRxUndersizeFrames,
       "cvtCountersRatesTxLateCollision": cvtCountersRatesTxLateCollision,
       "cvtCountersRatesTxDeferred": cvtCountersRatesTxDeferred,
       "cvtCountersRatesRxFrames64": cvtCountersRatesRxFrames64,
       "cvtCountersRatesRxFrames65to127": cvtCountersRatesRxFrames65to127,
       "cvtCountersRatesRxFrames128to255": cvtCountersRatesRxFrames128to255,
       "cvtCountersRatesRxFrames256to511": cvtCountersRatesRxFrames256to511,
       "cvtCountersRatesRxFrames512to1023": cvtCountersRatesRxFrames512to1023,
       "cvtCountersRatesRxMulticastFrames": cvtCountersRatesRxMulticastFrames,
       "cvtCountersRatesRxBroadcastFrames": cvtCountersRatesRxBroadcastFrames,
       "cvtCountersRatesTxMulticastFrames": cvtCountersRatesTxMulticastFrames,
       "cvtCountersRatesTxBroadcastFrames": cvtCountersRatesTxBroadcastFrames,
       "cvtCountersRatesTxCollision": cvtCountersRatesTxCollision,
       "cvtCountersRatesTotalErrors": cvtCountersRatesTotalErrors,
       "cvtCountersRatesRxFrames1024to1518": cvtCountersRatesRxFrames1024to1518,
       "cvtPortCountersEvents": cvtPortCountersEvents,
       "cvtCountersEventsTable": cvtCountersEventsTable,
       "cvtCountersEventsEntry": cvtCountersEventsEntry,
       "cvtCountersEventsIndex": cvtCountersEventsIndex,
       "cvtCountersEventsBytesReceived": cvtCountersEventsBytesReceived,
       "cvtCountersEventsFramesReceived": cvtCountersEventsFramesReceived,
       "cvtCountersEventsBytesSent": cvtCountersEventsBytesSent,
       "cvtCountersEventsFramesSent": cvtCountersEventsFramesSent,
       "cvtCountersEventsTotalBytes": cvtCountersEventsTotalBytes,
       "cvtCountersEventsRxCRCError": cvtCountersEventsRxCRCError,
       "cvtCountersEventsRxFragments": cvtCountersEventsRxFragments,
       "cvtCountersEventsRxFilteredFrames": cvtCountersEventsRxFilteredFrames,
       "cvtCountersEventsRxAlignError": cvtCountersEventsRxAlignError,
       "cvtCountersEventsRxUndersizeFrames": cvtCountersEventsRxUndersizeFrames,
       "cvtCountersEventsTxLateCollision": cvtCountersEventsTxLateCollision,
       "cvtCountersEventsTxDeferred": cvtCountersEventsTxDeferred,
       "cvtCountersEventsRxFrames64": cvtCountersEventsRxFrames64,
       "cvtCountersEventsRxFrames65to127": cvtCountersEventsRxFrames65to127,
       "cvtCountersEventsRxFrames128to255": cvtCountersEventsRxFrames128to255,
       "cvtCountersEventsRxFrames256to511": cvtCountersEventsRxFrames256to511,
       "cvtCountersEventsRxFrames512to1023": cvtCountersEventsRxFrames512to1023,
       "cvtCountersEventsRxMulticastFrames": cvtCountersEventsRxMulticastFrames,
       "cvtCountersEventsRxBroadcastFrames": cvtCountersEventsRxBroadcastFrames,
       "cvtCountersEventsTxMulticastFrames": cvtCountersEventsTxMulticastFrames,
       "cvtCountersEventsTxBroadcastFrames": cvtCountersEventsTxBroadcastFrames,
       "cvtCountersEventsTxCollision": cvtCountersEventsTxCollision,
       "cvtCountersEventsRxFrames1024to1518": cvtCountersEventsRxFrames1024to1518,
       "cvtCountersEventsTotalErrors": cvtCountersEventsTotalErrors,
       "cvtClearCountersOfAllPort": cvtClearCountersOfAllPort,
       "cvtMacAddressTable": cvtMacAddressTable,
       "cvtMacAddressPortSelect": cvtMacAddressPortSelect,
       "cvtMacAddressTotal": cvtMacAddressTotal,
       "cvtMacAddressState": cvtMacAddressState,
       "cvtMacTable": cvtMacTable,
       "cvtMacTableEntry": cvtMacTableEntry,
       "cvtMacTableIndex": cvtMacTableIndex,
       "cvtMacTableAddr": cvtMacTableAddr,
       "cvtMacTableVID": cvtMacTableVID,
       "cvtMacTablePort": cvtMacTablePort,
       "cvtMacTableType": cvtMacTableType,
       "cvtMacAddressTop": cvtMacAddressTop,
       "cvtMacAddressNext": cvtMacAddressNext,
       "cvtSFPInformation": cvtSFPInformation,
       "cvtSFPPortInfo": cvtSFPPortInfo,
       "cvtSFPPortInfoTable": cvtSFPPortInfoTable,
       "cvtSFPPortInfoEntry": cvtSFPPortInfoEntry,
       "cvtSFPPortInfoIndex": cvtSFPPortInfoIndex,
       "cvtSFPPortInfoPortName": cvtSFPPortInfoPortName,
       "cvtSFPPortInfoSpeed": cvtSFPPortInfoSpeed,
       "cvtSFPPortInfoDistance": cvtSFPPortInfoDistance,
       "cvtSFPPortInfoVendorName": cvtSFPPortInfoVendorName,
       "cvtSFPPortInfoVendorPN": cvtSFPPortInfoVendorPN,
       "cvtSFPPortInfoVendorSN": cvtSFPPortInfoVendorSN,
       "cvtSFPPortState": cvtSFPPortState,
       "cvtSFPPortStateTable": cvtSFPPortStateTable,
       "cvtSFPPortStateEntry": cvtSFPPortStateEntry,
       "cvtSFPPortStateIndex": cvtSFPPortStateIndex,
       "cvtSFPPortStatePortName": cvtSFPPortStatePortName,
       "cvtSFPPortStateTemperature": cvtSFPPortStateTemperature,
       "cvtSFPPortStateVoltage": cvtSFPPortStateVoltage,
       "cvtSFPPortStateTXBias": cvtSFPPortStateTXBias,
       "cvtSFPPortStateTXPower": cvtSFPPortStateTXPower,
       "cvtSFPPortStateRXPower": cvtSFPPortStateRXPower,
       "cvtSystemUtility": cvtSystemUtility,
       "cvtLoadFactorySetting": cvtLoadFactorySetting,
       "cvtLoadFactorySettingExceptNetworkConfiguration": cvtLoadFactorySettingExceptNetworkConfiguration,
       "cvtEventLog": cvtEventLog,
       "cvtEventLogTable": cvtEventLogTable,
       "cvtEventLogEntry": cvtEventLogEntry,
       "cvtEventLogIndex": cvtEventLogIndex,
       "cvtEventLogType": cvtEventLogType,
       "cvtEventLogTime": cvtEventLogTime,
       "cvtEventLogUpTime": cvtEventLogUpTime,
       "cvtEventLogDescription": cvtEventLogDescription,
       "cvtEventLogSource": cvtEventLogSource,
       "cvtEventLogEvent": cvtEventLogEvent,
       "cvtEventLogNameCommunity": cvtEventLogNameCommunity,
       "cvtEventLogIPAddr": cvtEventLogIPAddr,
       "cvtEventLogClear": cvtEventLogClear,
       "cvtUpdateFirmware": cvtUpdateFirmware,
       "cvtUpdateProtocol": cvtUpdateProtocol,
       "cvtUpdateFileType": cvtUpdateFileType,
       "cvtUpdateServerIPAddr": cvtUpdateServerIPAddr,
       "cvtUpdateUserName": cvtUpdateUserName,
       "cvtUpdatePassword": cvtUpdatePassword,
       "cvtUpdateFileLocation": cvtUpdateFileLocation,
       "cvtUpdateBackup": cvtUpdateBackup,
       "cvtUpdateUpdate": cvtUpdateUpdate,
       "cvtUpdateState": cvtUpdateState,
       "cvtUpdateServerIPv6Addr": cvtUpdateServerIPv6Addr,
       "cvtSaveConfiguration": cvtSaveConfiguration,
       "cvtResetSystem": cvtResetSystem,
       "converterTraps": converterTraps,
       "cvtSystemPowerDown": cvtSystemPowerDown,
       "cvtBroadcastStorm": cvtBroadcastStorm,
       "cvtBroadcastNormal": cvtBroadcastNormal,
       "cvtFaultAlarm": cvtFaultAlarm,
       "cvtWarningAlarm": cvtWarningAlarm,
       "cvtMinorAlarm": cvtMinorAlarm,
       "cvtLoopBack": cvtLoopBack,
       "cvtBatteryMode": cvtBatteryMode,
       "cvtCATVPower": cvtCATVPower,
       "cvtPowerExceptional": cvtPowerExceptional}
)
