# SNMP MIB module (RAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\RAD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:40 2025
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

_Rad_ObjectIdentity = ObjectIdentity
rad = _Rad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164)
)
_RadGen_ObjectIdentity = ObjectIdentity
radGen = _RadGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1)
)
_SystemsEvents_ObjectIdentity = ObjectIdentity
systemsEvents = _SystemsEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0)
)
if mibBuilder.loadTexts:
    systemsEvents.setStatus("current")
_Agnt_ObjectIdentity = ObjectIdentity
agnt = _Agnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2)
)
_AgnHwVersion_Type = DisplayString
_AgnHwVersion_Object = MibScalar
agnHwVersion = _AgnHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 1),
    _AgnHwVersion_Type()
)
agnHwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnHwVersion.setStatus("current")
_AgnTrapMask_Type = Integer32
_AgnTrapMask_Object = MibScalar
agnTrapMask = _AgnTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 2),
    _AgnTrapMask_Type()
)
agnTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnTrapMask.setStatus("current")


class _AgnTrapValue_Type(OctetString):
    """Custom type agnTrapValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )
    fixed_length = 100


_AgnTrapValue_Type.__name__ = "OctetString"
_AgnTrapValue_Object = MibScalar
agnTrapValue = _AgnTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 3),
    _AgnTrapValue_Type()
)
agnTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTrapValue.setStatus("deprecated")
_AgnChangeCnt_Type = Counter32
_AgnChangeCnt_Object = MibScalar
agnChangeCnt = _AgnChangeCnt_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 4),
    _AgnChangeCnt_Type()
)
agnChangeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnChangeCnt.setStatus("current")
_AgnSpecific_Type = ObjectIdentifier
_AgnSpecific_Object = MibScalar
agnSpecific = _AgnSpecific_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 5),
    _AgnSpecific_Type()
)
agnSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnSpecific.setStatus("current")


class _AgnConfigMsg_Type(OctetString):
    """Custom type agnConfigMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AgnConfigMsg_Type.__name__ = "OctetString"
_AgnConfigMsg_Object = MibScalar
agnConfigMsg = _AgnConfigMsg_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 6),
    _AgnConfigMsg_Type()
)
agnConfigMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnConfigMsg.setStatus("current")
_MngTrapIpTable_Object = MibTable
mngTrapIpTable = _MngTrapIpTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7)
)
if mibBuilder.loadTexts:
    mngTrapIpTable.setStatus("current")
_MngEntry_Object = MibTableRow
mngEntry = _MngEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1)
)
mngEntry.setIndexNames(
    (0, "RAD-MIB", "mngID"),
)
if mibBuilder.loadTexts:
    mngEntry.setStatus("current")
_MngID_Type = Integer32
_MngID_Object = MibTableColumn
mngID = _MngID_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 1),
    _MngID_Type()
)
mngID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mngID.setStatus("current")
_MngIP_Type = IpAddress
_MngIP_Object = MibTableColumn
mngIP = _MngIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 2),
    _MngIP_Type()
)
mngIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngIP.setStatus("current")
_MngIPMask_Type = IpAddress
_MngIPMask_Object = MibTableColumn
mngIPMask = _MngIPMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 3),
    _MngIPMask_Type()
)
mngIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngIPMask.setStatus("deprecated")
_MngTrapMask_Type = Integer32
_MngTrapMask_Object = MibTableColumn
mngTrapMask = _MngTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 4),
    _MngTrapMask_Type()
)
mngTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngTrapMask.setStatus("current")


class _MngAlarmTrapMask_Type(OctetString):
    """Custom type mngAlarmTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_MngAlarmTrapMask_Type.__name__ = "OctetString"
_MngAlarmTrapMask_Object = MibTableColumn
mngAlarmTrapMask = _MngAlarmTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 5),
    _MngAlarmTrapMask_Type()
)
mngAlarmTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngAlarmTrapMask.setStatus("current")
_MngSnmpTrapUdpPort_Type = Unsigned32
_MngSnmpTrapUdpPort_Object = MibTableColumn
mngSnmpTrapUdpPort = _MngSnmpTrapUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 7, 1, 6),
    _MngSnmpTrapUdpPort_Type()
)
mngSnmpTrapUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mngSnmpTrapUdpPort.setStatus("current")


class _AgnIndication_Type(Integer32):
    """Custom type agnIndication based on Integer32"""
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
        *(("faulty", 1),
          ("warning", 2),
          ("normal", 3),
          ("minor", 4),
          ("major", 5),
          ("event", 6),
          ("critical", 7))
    )


_AgnIndication_Type.__name__ = "Integer32"
_AgnIndication_Object = MibScalar
agnIndication = _AgnIndication_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 8),
    _AgnIndication_Type()
)
agnIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnIndication.setStatus("current")


class _AgnMonitorModeCmd_Type(Integer32):
    """Custom type agnMonitorModeCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_AgnMonitorModeCmd_Type.__name__ = "Integer32"
_AgnMonitorModeCmd_Object = MibScalar
agnMonitorModeCmd = _AgnMonitorModeCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 9),
    _AgnMonitorModeCmd_Type()
)
agnMonitorModeCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnMonitorModeCmd.setStatus("current")


class _AgnLed_Type(OctetString):
    """Custom type agnLed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AgnLed_Type.__name__ = "OctetString"
_AgnLed_Object = MibScalar
agnLed = _AgnLed_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 10),
    _AgnLed_Type()
)
agnLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnLed.setStatus("current")
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("current")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1)
)
trapEntry.setIndexNames(
    (0, "RAD-MIB", "trapID"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("current")
_TrapID_Type = Integer32
_TrapID_Object = MibTableColumn
trapID = _TrapID_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1, 1),
    _TrapID_Type()
)
trapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapID.setStatus("current")
_TrapVal_Type = DisplayString
_TrapVal_Object = MibTableColumn
trapVal = _TrapVal_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1, 2),
    _TrapVal_Type()
)
trapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapVal.setStatus("current")
_TrapTimeSinceOccurrence_Type = TimeTicks
_TrapTimeSinceOccurrence_Object = MibTableColumn
trapTimeSinceOccurrence = _TrapTimeSinceOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 11, 1, 3),
    _TrapTimeSinceOccurrence_Type()
)
trapTimeSinceOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTimeSinceOccurrence.setStatus("current")
_FileTransfer_ObjectIdentity = ObjectIdentity
fileTransfer = _FileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12)
)
_FileServerIP_Type = IpAddress
_FileServerIP_Object = MibScalar
fileServerIP = _FileServerIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 1),
    _FileServerIP_Type()
)
fileServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileServerIP.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibScalar
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileName.setStatus("current")


class _FileTransCmd_Type(Integer32):
    """Custom type fileTransCmd based on Integer32"""
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


_FileTransCmd_Type.__name__ = "Integer32"
_FileTransCmd_Object = MibScalar
fileTransCmd = _FileTransCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 3),
    _FileTransCmd_Type()
)
fileTransCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransCmd.setStatus("current")
_TftpRetryTimeOut_Type = Integer32
_TftpRetryTimeOut_Object = MibScalar
tftpRetryTimeOut = _TftpRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 4),
    _TftpRetryTimeOut_Type()
)
tftpRetryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRetryTimeOut.setStatus("current")
_TftpTotalTimeOut_Type = Integer32
_TftpTotalTimeOut_Object = MibScalar
tftpTotalTimeOut = _TftpTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 5),
    _TftpTotalTimeOut_Type()
)
tftpTotalTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpTotalTimeOut.setStatus("current")


class _TftpStatus_Type(Integer32):
    """Custom type tftpStatus based on Integer32"""
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


_TftpStatus_Type.__name__ = "Integer32"
_TftpStatus_Object = MibScalar
tftpStatus = _TftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 6),
    _TftpStatus_Type()
)
tftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpStatus.setStatus("current")


class _TftpError_Type(OctetString):
    """Custom type tftpError based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_TftpError_Type.__name__ = "OctetString"
_TftpError_Object = MibScalar
tftpError = _TftpError_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 7),
    _TftpError_Type()
)
tftpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpError.setStatus("current")


class _FileTransferToSubSystems_Type(OctetString):
    """Custom type fileTransferToSubSystems based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_FileTransferToSubSystems_Type.__name__ = "OctetString"
_FileTransferToSubSystems_Object = MibScalar
fileTransferToSubSystems = _FileTransferToSubSystems_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 8),
    _FileTransferToSubSystems_Type()
)
fileTransferToSubSystems.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferToSubSystems.setStatus("current")
_FileNameWithinProduct_Type = DisplayString
_FileNameWithinProduct_Object = MibScalar
fileNameWithinProduct = _FileNameWithinProduct_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 9),
    _FileNameWithinProduct_Type()
)
fileNameWithinProduct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileNameWithinProduct.setStatus("current")
_IntSwdlTable_Object = MibTable
intSwdlTable = _IntSwdlTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10)
)
if mibBuilder.loadTexts:
    intSwdlTable.setStatus("current")
_IntSwdlEntry_Object = MibTableRow
intSwdlEntry = _IntSwdlEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1)
)
intSwdlEntry.setIndexNames(
    (0, "RAD-MIB", "intSwdlObjIdx"),
    (0, "RAD-MIB", "intSwdlFileIdx"),
)
if mibBuilder.loadTexts:
    intSwdlEntry.setStatus("current")
_IntSwdlObjIdx_Type = Integer32
_IntSwdlObjIdx_Object = MibTableColumn
intSwdlObjIdx = _IntSwdlObjIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 1),
    _IntSwdlObjIdx_Type()
)
intSwdlObjIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlObjIdx.setStatus("current")
_IntSwdlFileIdx_Type = Integer32
_IntSwdlFileIdx_Object = MibTableColumn
intSwdlFileIdx = _IntSwdlFileIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 2),
    _IntSwdlFileIdx_Type()
)
intSwdlFileIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlFileIdx.setStatus("current")
_IntSwdlFileName_Type = DisplayString
_IntSwdlFileName_Object = MibTableColumn
intSwdlFileName = _IntSwdlFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 3),
    _IntSwdlFileName_Type()
)
intSwdlFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlFileName.setStatus("current")
_IntSwdlFileSwVer_Type = DisplayString
_IntSwdlFileSwVer_Object = MibTableColumn
intSwdlFileSwVer = _IntSwdlFileSwVer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 4),
    _IntSwdlFileSwVer_Type()
)
intSwdlFileSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlFileSwVer.setStatus("current")
_IntSwdlSwDate_Type = DisplayString
_IntSwdlSwDate_Object = MibTableColumn
intSwdlSwDate = _IntSwdlSwDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 5),
    _IntSwdlSwDate_Type()
)
intSwdlSwDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlSwDate.setStatus("current")
_IntSwdlSize_Type = DisplayString
_IntSwdlSize_Object = MibTableColumn
intSwdlSize = _IntSwdlSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 6),
    _IntSwdlSize_Type()
)
intSwdlSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlSize.setStatus("current")


class _IntSwdlCmd_Type(Integer32):
    """Custom type intSwdlCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("off", 2),
          ("on", 3))
    )


_IntSwdlCmd_Type.__name__ = "Integer32"
_IntSwdlCmd_Object = MibTableColumn
intSwdlCmd = _IntSwdlCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 7),
    _IntSwdlCmd_Type()
)
intSwdlCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intSwdlCmd.setStatus("current")


class _IntSwdlToSubSystem_Type(OctetString):
    """Custom type intSwdlToSubSystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_IntSwdlToSubSystem_Type.__name__ = "OctetString"
_IntSwdlToSubSystem_Object = MibTableColumn
intSwdlToSubSystem = _IntSwdlToSubSystem_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 8),
    _IntSwdlToSubSystem_Type()
)
intSwdlToSubSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intSwdlToSubSystem.setStatus("current")


class _IntSwdlCardType_Type(Integer32):
    """Custom type intSwdlCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              220,
              221,
              222,
              223,
              270,
              271,
              272,
              273,
              280,
              290,
              300,
              301,
              302,
              303,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("gstm1", 220),
          ("goc3", 221),
          ("gstm1D", 222),
          ("goc3D", 223),
          ("serverE1", 270),
          ("serverT1", 271),
          ("serverE1Pw", 272),
          ("serverT1Pw", 273),
          ("gigabitEth", 280),
          ("channelizedT3Pw1", 290),
          ("cesT128", 300),
          ("cesE128", 301),
          ("cesT1Pw28", 302),
          ("cesE1Pw28", 303),
          ("vmxE1VeDe", 310),
          ("vmxE1VeDi", 311),
          ("vmxE1ViDe", 312),
          ("vmxE1ViDi", 313),
          ("vmxT1VeDe", 314),
          ("vmxT1VeDi", 315),
          ("vmxT1ViDe", 316),
          ("vmxT1ViDi", 317),
          ("vc12E1UeNe", 318),
          ("vc12E1UeNi", 319),
          ("vc12E1UiNe", 320),
          ("vc12E1UiNi", 321),
          ("vc12T1UeNe", 322),
          ("vc12T1UeNi", 323),
          ("vc12T1UiNe", 324),
          ("vc12T1UiNi", 325))
    )


_IntSwdlCardType_Type.__name__ = "Integer32"
_IntSwdlCardType_Object = MibTableColumn
intSwdlCardType = _IntSwdlCardType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 9),
    _IntSwdlCardType_Type()
)
intSwdlCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlCardType.setStatus("current")
_IntSwdlFlashIdx_Type = Integer32
_IntSwdlFlashIdx_Object = MibTableColumn
intSwdlFlashIdx = _IntSwdlFlashIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 10, 1, 10),
    _IntSwdlFlashIdx_Type()
)
intSwdlFlashIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSwdlFlashIdx.setStatus("current")
_SwdlStatusTable_Object = MibTable
swdlStatusTable = _SwdlStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11)
)
if mibBuilder.loadTexts:
    swdlStatusTable.setStatus("current")
_SwdlStatusEntry_Object = MibTableRow
swdlStatusEntry = _SwdlStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1)
)
swdlStatusEntry.setIndexNames(
    (0, "RAD-MIB", "swdlStatusTypeIdx"),
    (0, "RAD-MIB", "swdlStatusIdx"),
)
if mibBuilder.loadTexts:
    swdlStatusEntry.setStatus("current")
_SwdlStatusTypeIdx_Type = Integer32
_SwdlStatusTypeIdx_Object = MibTableColumn
swdlStatusTypeIdx = _SwdlStatusTypeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 1),
    _SwdlStatusTypeIdx_Type()
)
swdlStatusTypeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusTypeIdx.setStatus("current")
_SwdlStatusIdx_Type = Integer32
_SwdlStatusIdx_Object = MibTableColumn
swdlStatusIdx = _SwdlStatusIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 2),
    _SwdlStatusIdx_Type()
)
swdlStatusIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusIdx.setStatus("current")
_SwdlStatusFileName_Type = DisplayString
_SwdlStatusFileName_Object = MibTableColumn
swdlStatusFileName = _SwdlStatusFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 3),
    _SwdlStatusFileName_Type()
)
swdlStatusFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusFileName.setStatus("current")
_SwdlStatusSlot_Type = DisplayString
_SwdlStatusSlot_Object = MibTableColumn
swdlStatusSlot = _SwdlStatusSlot_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 4),
    _SwdlStatusSlot_Type()
)
swdlStatusSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusSlot.setStatus("current")
_SwdlStatusSubSystem_Type = DisplayString
_SwdlStatusSubSystem_Object = MibTableColumn
swdlStatusSubSystem = _SwdlStatusSubSystem_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 5),
    _SwdlStatusSubSystem_Type()
)
swdlStatusSubSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusSubSystem.setStatus("current")
_SwdlStatusStatus_Type = Integer32
_SwdlStatusStatus_Object = MibTableColumn
swdlStatusStatus = _SwdlStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 6),
    _SwdlStatusStatus_Type()
)
swdlStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusStatus.setStatus("current")
_SwdlStatusTime_Type = DisplayString
_SwdlStatusTime_Object = MibTableColumn
swdlStatusTime = _SwdlStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 11, 1, 7),
    _SwdlStatusTime_Type()
)
swdlStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swdlStatusTime.setStatus("current")
_ClearDwldStatusLog_Type = Integer32
_ClearDwldStatusLog_Object = MibScalar
clearDwldStatusLog = _ClearDwldStatusLog_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 12),
    _ClearDwldStatusLog_Type()
)
clearDwldStatusLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearDwldStatusLog.setStatus("current")
_AutoFileTransfer_ObjectIdentity = ObjectIdentity
autoFileTransfer = _AutoFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13)
)
_AutoFileTransferTable_Object = MibTable
autoFileTransferTable = _AutoFileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1)
)
if mibBuilder.loadTexts:
    autoFileTransferTable.setStatus("current")
_AutoFileTransferEntry_Object = MibTableRow
autoFileTransferEntry = _AutoFileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1, 1)
)
autoFileTransferEntry.setIndexNames(
    (0, "RAD-MIB", "autoFileTransferType"),
)
if mibBuilder.loadTexts:
    autoFileTransferEntry.setStatus("current")


class _AutoFileTransferType_Type(Integer32):
    """Custom type autoFileTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("alarmsBuffer", 1)
    )


_AutoFileTransferType_Type.__name__ = "Integer32"
_AutoFileTransferType_Object = MibTableColumn
autoFileTransferType = _AutoFileTransferType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1, 1, 1),
    _AutoFileTransferType_Type()
)
autoFileTransferType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoFileTransferType.setStatus("current")
_AutoFileTransferServerIp_Type = IpAddress
_AutoFileTransferServerIp_Object = MibTableColumn
autoFileTransferServerIp = _AutoFileTransferServerIp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1, 1, 2),
    _AutoFileTransferServerIp_Type()
)
autoFileTransferServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFileTransferServerIp.setStatus("current")
_AutoFileTransferFileName_Type = SnmpAdminString
_AutoFileTransferFileName_Object = MibTableColumn
autoFileTransferFileName = _AutoFileTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1, 1, 3),
    _AutoFileTransferFileName_Type()
)
autoFileTransferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFileTransferFileName.setStatus("current")


class _AutoFileTransferScheduling_Type(Integer32):
    """Custom type autoFileTransferScheduling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("now", 2),
          ("recurrence", 3))
    )


_AutoFileTransferScheduling_Type.__name__ = "Integer32"
_AutoFileTransferScheduling_Object = MibTableColumn
autoFileTransferScheduling = _AutoFileTransferScheduling_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1, 1, 4),
    _AutoFileTransferScheduling_Type()
)
autoFileTransferScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFileTransferScheduling.setStatus("current")
_AutoFileTransferTimeRecurrence_Type = Integer32
_AutoFileTransferTimeRecurrence_Object = MibTableColumn
autoFileTransferTimeRecurrence = _AutoFileTransferTimeRecurrence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1, 1, 5),
    _AutoFileTransferTimeRecurrence_Type()
)
autoFileTransferTimeRecurrence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFileTransferTimeRecurrence.setStatus("current")
_AutoFileTransferOccurrenceRecurrence_Type = Integer32
_AutoFileTransferOccurrenceRecurrence_Object = MibTableColumn
autoFileTransferOccurrenceRecurrence = _AutoFileTransferOccurrenceRecurrence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 13, 1, 1, 6),
    _AutoFileTransferOccurrenceRecurrence_Type()
)
autoFileTransferOccurrenceRecurrence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoFileTransferOccurrenceRecurrence.setStatus("current")
_FileTransferServerPort_Type = Unsigned32
_FileTransferServerPort_Object = MibScalar
fileTransferServerPort = _FileTransferServerPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 14),
    _FileTransferServerPort_Type()
)
fileTransferServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferServerPort.setStatus("current")


class _FileTransferProtocol_Type(Integer32):
    """Custom type fileTransferProtocol based on Integer32"""
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


_FileTransferProtocol_Type.__name__ = "Integer32"
_FileTransferProtocol_Object = MibScalar
fileTransferProtocol = _FileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 12, 15),
    _FileTransferProtocol_Type()
)
fileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferProtocol.setStatus("current")


class _SystemReset_Type(Integer32):
    """Custom type systemReset based on Integer32"""
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


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 13),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_SystemTiming_ObjectIdentity = ObjectIdentity
systemTiming = _SystemTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 14)
)
_SystemDate_Type = DisplayString
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 14, 1),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 14, 2),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")


class _SystemTimeElapsed_Type(Integer32):
    """Custom type systemTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_SystemTimeElapsed_Type.__name__ = "Integer32"
_SystemTimeElapsed_Object = MibScalar
systemTimeElapsed = _SystemTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 14, 3),
    _SystemTimeElapsed_Type()
)
systemTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTimeElapsed.setStatus("current")


class _SystemResetAllStatsCmd_Type(Integer32):
    """Custom type systemResetAllStatsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SystemResetAllStatsCmd_Type.__name__ = "Integer32"
_SystemResetAllStatsCmd_Object = MibScalar
systemResetAllStatsCmd = _SystemResetAllStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 16),
    _SystemResetAllStatsCmd_Type()
)
systemResetAllStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemResetAllStatsCmd.setStatus("current")


class _SystemClearTablesCmd_Type(Integer32):
    """Custom type systemClearTablesCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("tempCnfgTables", 3))
    )


_SystemClearTablesCmd_Type.__name__ = "Integer32"
_SystemClearTablesCmd_Object = MibScalar
systemClearTablesCmd = _SystemClearTablesCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 17),
    _SystemClearTablesCmd_Type()
)
systemClearTablesCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemClearTablesCmd.setStatus("current")
_SystemParameter_Type = Integer32
_SystemParameter_Object = MibScalar
systemParameter = _SystemParameter_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 18),
    _SystemParameter_Type()
)
systemParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemParameter.setStatus("current")


class _AgnGlobalAlarmMask_Type(OctetString):
    """Custom type agnGlobalAlarmMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )
    fixed_length = 100


_AgnGlobalAlarmMask_Type.__name__ = "OctetString"
_AgnGlobalAlarmMask_Object = MibScalar
agnGlobalAlarmMask = _AgnGlobalAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 19),
    _AgnGlobalAlarmMask_Type()
)
agnGlobalAlarmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnGlobalAlarmMask.setStatus("current")


class _AlarmSeverity_Type(Integer32):
    """Custom type alarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("event", 3),
          ("minor", 4),
          ("major", 5),
          ("warning", 6),
          ("critical", 7))
    )


_AlarmSeverity_Type.__name__ = "Integer32"
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 20),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")


class _AlarmState_Type(Integer32):
    """Custom type alarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AlarmState_Type.__name__ = "Integer32"
_AlarmState_Object = MibScalar
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 21),
    _AlarmState_Type()
)
alarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")


class _AgnTestStatus_Type(Integer32):
    """Custom type agnTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_AgnTestStatus_Type.__name__ = "Integer32"
_AgnTestStatus_Object = MibScalar
agnTestStatus = _AgnTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 22),
    _AgnTestStatus_Type()
)
agnTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnTestStatus.setStatus("current")


class _SystemSaveAndResetAllStatsCmd_Type(Integer32):
    """Custom type systemSaveAndResetAllStatsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_SystemSaveAndResetAllStatsCmd_Type.__name__ = "Integer32"
_SystemSaveAndResetAllStatsCmd_Object = MibScalar
systemSaveAndResetAllStatsCmd = _SystemSaveAndResetAllStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 23),
    _SystemSaveAndResetAllStatsCmd_Type()
)
systemSaveAndResetAllStatsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSaveAndResetAllStatsCmd.setStatus("current")
_SystemDefaultGateway_Type = IpAddress
_SystemDefaultGateway_Object = MibScalar
systemDefaultGateway = _SystemDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 24),
    _SystemDefaultGateway_Type()
)
systemDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDefaultGateway.setStatus("current")
_AgnSendTrapParameter_Type = Integer32
_AgnSendTrapParameter_Object = MibScalar
agnSendTrapParameter = _AgnSendTrapParameter_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 27),
    _AgnSendTrapParameter_Type()
)
agnSendTrapParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSendTrapParameter.setStatus("current")


class _AgnDeviceCapabilities_Type(OctetString):
    """Custom type agnDeviceCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AgnDeviceCapabilities_Type.__name__ = "OctetString"
_AgnDeviceCapabilities_Object = MibScalar
agnDeviceCapabilities = _AgnDeviceCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 42),
    _AgnDeviceCapabilities_Type()
)
agnDeviceCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agnDeviceCapabilities.setStatus("current")


class _AgnStoreCmd_Type(Integer32):
    """Custom type agnStoreCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("inFlash", 3),
          ("asDefConfigFile", 4))
    )


_AgnStoreCmd_Type.__name__ = "Integer32"
_AgnStoreCmd_Object = MibScalar
agnStoreCmd = _AgnStoreCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 44),
    _AgnStoreCmd_Type()
)
agnStoreCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnStoreCmd.setStatus("current")


class _AgnSwVersionSwapCmd_Type(Integer32):
    """Custom type agnSwVersionSwapCmd based on Integer32"""
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


_AgnSwVersionSwapCmd_Type.__name__ = "Integer32"
_AgnSwVersionSwapCmd_Object = MibScalar
agnSwVersionSwapCmd = _AgnSwVersionSwapCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 51),
    _AgnSwVersionSwapCmd_Type()
)
agnSwVersionSwapCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnSwVersionSwapCmd.setStatus("current")
_AgnTrapDelay_Type = Unsigned32
_AgnTrapDelay_Object = MibScalar
agnTrapDelay = _AgnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 60),
    _AgnTrapDelay_Type()
)
agnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnTrapDelay.setStatus("current")

# Managed Objects groups


# Notification objects

tftpStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 1)
)
tftpStatusChangeTrap.setObjects(
    ("RAD-MIB", "tftpStatus")
)
if mibBuilder.loadTexts:
    tftpStatusChangeTrap.setStatus(
        "current"
    )

agnStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 2)
)
agnStatusChangeTrap.setObjects(
    ("RAD-MIB", "agnIndication")
)
if mibBuilder.loadTexts:
    agnStatusChangeTrap.setStatus(
        "current"
    )

swdlStatusResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 4)
)
swdlStatusResult.setObjects(
    ("RAD-MIB", "swdlStatusFileName")
)
if mibBuilder.loadTexts:
    swdlStatusResult.setStatus(
        "current"
    )

intSwdlSlotFileMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 5)
)
intSwdlSlotFileMismatch.setObjects(
    ("RAD-MIB", "intSwdlFileName")
)
if mibBuilder.loadTexts:
    intSwdlSlotFileMismatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-MIB",
    **{"MacAddress": MacAddress,
       "rad": rad,
       "radGen": radGen,
       "systems": systems,
       "systemsEvents": systemsEvents,
       "tftpStatusChangeTrap": tftpStatusChangeTrap,
       "agnStatusChangeTrap": agnStatusChangeTrap,
       "swdlStatusResult": swdlStatusResult,
       "intSwdlSlotFileMismatch": intSwdlSlotFileMismatch,
       "agnt": agnt,
       "agnHwVersion": agnHwVersion,
       "agnTrapMask": agnTrapMask,
       "agnTrapValue": agnTrapValue,
       "agnChangeCnt": agnChangeCnt,
       "agnSpecific": agnSpecific,
       "agnConfigMsg": agnConfigMsg,
       "mngTrapIpTable": mngTrapIpTable,
       "mngEntry": mngEntry,
       "mngID": mngID,
       "mngIP": mngIP,
       "mngIPMask": mngIPMask,
       "mngTrapMask": mngTrapMask,
       "mngAlarmTrapMask": mngAlarmTrapMask,
       "mngSnmpTrapUdpPort": mngSnmpTrapUdpPort,
       "agnIndication": agnIndication,
       "agnMonitorModeCmd": agnMonitorModeCmd,
       "agnLed": agnLed,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapID": trapID,
       "trapVal": trapVal,
       "trapTimeSinceOccurrence": trapTimeSinceOccurrence,
       "fileTransfer": fileTransfer,
       "fileServerIP": fileServerIP,
       "fileName": fileName,
       "fileTransCmd": fileTransCmd,
       "tftpRetryTimeOut": tftpRetryTimeOut,
       "tftpTotalTimeOut": tftpTotalTimeOut,
       "tftpStatus": tftpStatus,
       "tftpError": tftpError,
       "fileTransferToSubSystems": fileTransferToSubSystems,
       "fileNameWithinProduct": fileNameWithinProduct,
       "intSwdlTable": intSwdlTable,
       "intSwdlEntry": intSwdlEntry,
       "intSwdlObjIdx": intSwdlObjIdx,
       "intSwdlFileIdx": intSwdlFileIdx,
       "intSwdlFileName": intSwdlFileName,
       "intSwdlFileSwVer": intSwdlFileSwVer,
       "intSwdlSwDate": intSwdlSwDate,
       "intSwdlSize": intSwdlSize,
       "intSwdlCmd": intSwdlCmd,
       "intSwdlToSubSystem": intSwdlToSubSystem,
       "intSwdlCardType": intSwdlCardType,
       "intSwdlFlashIdx": intSwdlFlashIdx,
       "swdlStatusTable": swdlStatusTable,
       "swdlStatusEntry": swdlStatusEntry,
       "swdlStatusTypeIdx": swdlStatusTypeIdx,
       "swdlStatusIdx": swdlStatusIdx,
       "swdlStatusFileName": swdlStatusFileName,
       "swdlStatusSlot": swdlStatusSlot,
       "swdlStatusSubSystem": swdlStatusSubSystem,
       "swdlStatusStatus": swdlStatusStatus,
       "swdlStatusTime": swdlStatusTime,
       "clearDwldStatusLog": clearDwldStatusLog,
       "autoFileTransfer": autoFileTransfer,
       "autoFileTransferTable": autoFileTransferTable,
       "autoFileTransferEntry": autoFileTransferEntry,
       "autoFileTransferType": autoFileTransferType,
       "autoFileTransferServerIp": autoFileTransferServerIp,
       "autoFileTransferFileName": autoFileTransferFileName,
       "autoFileTransferScheduling": autoFileTransferScheduling,
       "autoFileTransferTimeRecurrence": autoFileTransferTimeRecurrence,
       "autoFileTransferOccurrenceRecurrence": autoFileTransferOccurrenceRecurrence,
       "fileTransferServerPort": fileTransferServerPort,
       "fileTransferProtocol": fileTransferProtocol,
       "systemReset": systemReset,
       "systemTiming": systemTiming,
       "systemDate": systemDate,
       "systemTime": systemTime,
       "systemTimeElapsed": systemTimeElapsed,
       "systemResetAllStatsCmd": systemResetAllStatsCmd,
       "systemClearTablesCmd": systemClearTablesCmd,
       "systemParameter": systemParameter,
       "agnGlobalAlarmMask": agnGlobalAlarmMask,
       "alarmSeverity": alarmSeverity,
       "alarmState": alarmState,
       "agnTestStatus": agnTestStatus,
       "systemSaveAndResetAllStatsCmd": systemSaveAndResetAllStatsCmd,
       "systemDefaultGateway": systemDefaultGateway,
       "agnSendTrapParameter": agnSendTrapParameter,
       "agnDeviceCapabilities": agnDeviceCapabilities,
       "agnStoreCmd": agnStoreCmd,
       "agnSwVersionSwapCmd": agnSwVersionSwapCmd,
       "agnTrapDelay": agnTrapDelay}
)
