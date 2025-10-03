# SNMP MIB module (SL-FT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-FT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:51 2025
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slMain,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slMain")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slFt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



class SftpUserLogin(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



class SftpUserPassword(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )



# MIB Managed Objects in the order of their OIDs

_SlFtGen_ObjectIdentity = ObjectIdentity
slFtGen = _SlFtGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1)
)
_SlFtSystems_ObjectIdentity = ObjectIdentity
slFtSystems = _SlFtSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1)
)
_SlFtSystemsEvents_ObjectIdentity = ObjectIdentity
slFtSystemsEvents = _SlFtSystemsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1, 0)
)
if mibBuilder.loadTexts:
    slFtSystemsEvents.setStatus("current")
_SlFtAgnt_ObjectIdentity = ObjectIdentity
slFtAgnt = _SlFtAgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2)
)
_SlFtFileTransfer_ObjectIdentity = ObjectIdentity
slFtFileTransfer = _SlFtFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12)
)
_SlFtFileServerIP_Type = IpAddress
_SlFtFileServerIP_Object = MibScalar
slFtFileServerIP = _SlFtFileServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 1),
    _SlFtFileServerIP_Type()
)
slFtFileServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtFileServerIP.setStatus("current")
_SlFtFileName_Type = DisplayString
_SlFtFileName_Object = MibScalar
slFtFileName = _SlFtFileName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 2),
    _SlFtFileName_Type()
)
slFtFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtFileName.setStatus("current")


class _SlFtFileTransCmd_Type(Integer32):
    """Custom type slFtFileTransCmd based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("swDwnLoad", 1),
          ("configDwnLoad", 2),
          ("configUpLoad", 3),
          ("coProcDwnLoad", 4),
          ("stateUpLoad", 5),
          ("dwnLoadUserFile", 6),
          ("upLoadUserFile", 7),
          ("swDwnLoadAndReset", 8),
          ("swUpLoad", 9),
          ("swDwnLoad2BkupStorage", 10),
          ("bootDwnLoad", 11),
          ("bootUpLoad", 12),
          ("swUpLoadFromBkupStorage", 13),
          ("licenseDwnLoad", 14),
          ("configDwnLoadToDefaultFile", 15),
          ("noOp", 255))
    )


_SlFtFileTransCmd_Type.__name__ = "Integer32"
_SlFtFileTransCmd_Object = MibScalar
slFtFileTransCmd = _SlFtFileTransCmd_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 3),
    _SlFtFileTransCmd_Type()
)
slFtFileTransCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtFileTransCmd.setStatus("current")
_SlFtTftpRetryTimeOut_Type = Integer32
_SlFtTftpRetryTimeOut_Object = MibScalar
slFtTftpRetryTimeOut = _SlFtTftpRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 4),
    _SlFtTftpRetryTimeOut_Type()
)
slFtTftpRetryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtTftpRetryTimeOut.setStatus("current")
_SlFtTftpTotalTimeOut_Type = Integer32
_SlFtTftpTotalTimeOut_Object = MibScalar
slFtTftpTotalTimeOut = _SlFtTftpTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 5),
    _SlFtTftpTotalTimeOut_Type()
)
slFtTftpTotalTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtTftpTotalTimeOut.setStatus("current")


class _SlFtTftpStatus_Type(Integer32):
    """Custom type slFtTftpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 2),
          ("connecting", 3),
          ("transferringData", 4),
          ("endedTimeOut", 5),
          ("endedOk", 6),
          ("error", 7))
    )


_SlFtTftpStatus_Type.__name__ = "Integer32"
_SlFtTftpStatus_Object = MibScalar
slFtTftpStatus = _SlFtTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 6),
    _SlFtTftpStatus_Type()
)
slFtTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtTftpStatus.setStatus("current")


class _SlFtTftpError_Type(OctetString):
    """Custom type slFtTftpError based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_SlFtTftpError_Type.__name__ = "OctetString"
_SlFtTftpError_Object = MibScalar
slFtTftpError = _SlFtTftpError_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 7),
    _SlFtTftpError_Type()
)
slFtTftpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slFtTftpError.setStatus("current")


class _SlFtFileTransferToSubSystems_Type(OctetString):
    """Custom type slFtFileTransferToSubSystems based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_SlFtFileTransferToSubSystems_Type.__name__ = "OctetString"
_SlFtFileTransferToSubSystems_Object = MibScalar
slFtFileTransferToSubSystems = _SlFtFileTransferToSubSystems_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 8),
    _SlFtFileTransferToSubSystems_Type()
)
slFtFileTransferToSubSystems.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtFileTransferToSubSystems.setStatus("current")
_SlFtFileNameWithinProduct_Type = DisplayString
_SlFtFileNameWithinProduct_Object = MibScalar
slFtFileNameWithinProduct = _SlFtFileNameWithinProduct_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 9),
    _SlFtFileNameWithinProduct_Type()
)
slFtFileNameWithinProduct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtFileNameWithinProduct.setStatus("current")
_SlFtFileTransferServerPort_Type = Unsigned32
_SlFtFileTransferServerPort_Object = MibScalar
slFtFileTransferServerPort = _SlFtFileTransferServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 14),
    _SlFtFileTransferServerPort_Type()
)
slFtFileTransferServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtFileTransferServerPort.setStatus("current")


class _SlFtFileTransferProtocol_Type(Integer32):
    """Custom type slFtFileTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("sftp", 2))
    )


_SlFtFileTransferProtocol_Type.__name__ = "Integer32"
_SlFtFileTransferProtocol_Object = MibScalar
slFtFileTransferProtocol = _SlFtFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 15),
    _SlFtFileTransferProtocol_Type()
)
slFtFileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtFileTransferProtocol.setStatus("current")
_SlFtSftpUserLogin_Type = SftpUserLogin
_SlFtSftpUserLogin_Object = MibScalar
slFtSftpUserLogin = _SlFtSftpUserLogin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 16),
    _SlFtSftpUserLogin_Type()
)
slFtSftpUserLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtSftpUserLogin.setStatus("current")
_SlFtSftpPasswordLogin_Type = SftpUserPassword
_SlFtSftpPasswordLogin_Object = MibScalar
slFtSftpPasswordLogin = _SlFtSftpPasswordLogin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 17),
    _SlFtSftpPasswordLogin_Type()
)
slFtSftpPasswordLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtSftpPasswordLogin.setStatus("current")


class _SlFtSystemReset_Type(Integer32):
    """Custom type slFtSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("resetConfig", 4),
          ("resetMapping", 5),
          ("resetStandby", 6))
    )


_SlFtSystemReset_Type.__name__ = "Integer32"
_SlFtSystemReset_Object = MibScalar
slFtSystemReset = _SlFtSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 13),
    _SlFtSystemReset_Type()
)
slFtSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtSystemReset.setStatus("current")


class _SlFtAgnSwVersionSwapCmd_Type(Integer32):
    """Custom type slFtAgnSwVersionSwapCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("mainAndBackup", 3))
    )


_SlFtAgnSwVersionSwapCmd_Type.__name__ = "Integer32"
_SlFtAgnSwVersionSwapCmd_Object = MibScalar
slFtAgnSwVersionSwapCmd = _SlFtAgnSwVersionSwapCmd_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 51),
    _SlFtAgnSwVersionSwapCmd_Type()
)
slFtAgnSwVersionSwapCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFtAgnSwVersionSwapCmd.setStatus("current")

# Managed Objects groups


# Notification objects

slFtTftpStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1, 0, 1)
)
slFtTftpStatusChangeTrap.setObjects(
    ("SL-FT-MIB", "slFtTftpStatus")
)
if mibBuilder.loadTexts:
    slFtTftpStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-FT-MIB",
    **{"MacAddress": MacAddress,
       "SftpUserLogin": SftpUserLogin,
       "SftpUserPassword": SftpUserPassword,
       "slFt": slFt,
       "slFtGen": slFtGen,
       "slFtSystems": slFtSystems,
       "slFtSystemsEvents": slFtSystemsEvents,
       "slFtTftpStatusChangeTrap": slFtTftpStatusChangeTrap,
       "slFtAgnt": slFtAgnt,
       "slFtFileTransfer": slFtFileTransfer,
       "slFtFileServerIP": slFtFileServerIP,
       "slFtFileName": slFtFileName,
       "slFtFileTransCmd": slFtFileTransCmd,
       "slFtTftpRetryTimeOut": slFtTftpRetryTimeOut,
       "slFtTftpTotalTimeOut": slFtTftpTotalTimeOut,
       "slFtTftpStatus": slFtTftpStatus,
       "slFtTftpError": slFtTftpError,
       "slFtFileTransferToSubSystems": slFtFileTransferToSubSystems,
       "slFtFileNameWithinProduct": slFtFileNameWithinProduct,
       "slFtFileTransferServerPort": slFtFileTransferServerPort,
       "slFtFileTransferProtocol": slFtFileTransferProtocol,
       "slFtSftpUserLogin": slFtSftpUserLogin,
       "slFtSftpPasswordLogin": slFtSftpPasswordLogin,
       "slFtSystemReset": slFtSystemReset,
       "slFtAgnSwVersionSwapCmd": slFtAgnSwVersionSwapCmd}
)
