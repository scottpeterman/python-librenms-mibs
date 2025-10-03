# SNMP MIB module (DLINKSW-SYSTEM-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SYSTEM-FILE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:00 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwSystemFileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14)
)
if mibBuilder.loadTexts:
    dlinkSwSystemFileMIB.setRevisions(
        ("2013-08-19 00:00",
         "2013-04-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsfMIBNotifications_ObjectIdentity = ObjectIdentity
dsfMIBNotifications = _DsfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 0)
)
_DsfMIBObjects_ObjectIdentity = ObjectIdentity
dsfMIBObjects = _DsfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1)
)
_DsfBootInfoObjects_ObjectIdentity = ObjectIdentity
dsfBootInfoObjects = _DsfBootInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1)
)


class _DsfNextBootCfgUrl_Type(OctetString):
    """Custom type dsfNextBootCfgUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DsfNextBootCfgUrl_Type.__name__ = "OctetString"
_DsfNextBootCfgUrl_Object = MibScalar
dsfNextBootCfgUrl = _DsfNextBootCfgUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 1),
    _DsfNextBootCfgUrl_Type()
)
dsfNextBootCfgUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfNextBootCfgUrl.setStatus("current")


class _DsfNextBootImageUrl_Type(OctetString):
    """Custom type dsfNextBootImageUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DsfNextBootImageUrl_Type.__name__ = "OctetString"
_DsfNextBootImageUrl_Object = MibScalar
dsfNextBootImageUrl = _DsfNextBootImageUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 2),
    _DsfNextBootImageUrl_Type()
)
dsfNextBootImageUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfNextBootImageUrl.setStatus("current")
_DsfCheckingBootImageCheck_Type = TruthValue
_DsfCheckingBootImageCheck_Object = MibScalar
dsfCheckingBootImageCheck = _DsfCheckingBootImageCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 3),
    _DsfCheckingBootImageCheck_Type()
)
dsfCheckingBootImageCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfCheckingBootImageCheck.setStatus("current")
_DsfBootImageCheckResult_Type = DisplayString
_DsfBootImageCheckResult_Object = MibScalar
dsfBootImageCheckResult = _DsfBootImageCheckResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 4),
    _DsfBootImageCheckResult_Type()
)
dsfBootImageCheckResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsfBootImageCheckResult.setStatus("current")
_DsfBootImageTable_Object = MibTable
dsfBootImageTable = _DsfBootImageTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dsfBootImageTable.setStatus("current")
_DsfBootImageEntry_Object = MibTableRow
dsfBootImageEntry = _DsfBootImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 5, 1)
)
dsfBootImageEntry.setIndexNames(
    (0, "DLINKSW-SYSTEM-FILE-MIB", "dsfBootImageUnitId"),
    (0, "DLINKSW-SYSTEM-FILE-MIB", "dsfBootImageIndex"),
)
if mibBuilder.loadTexts:
    dsfBootImageEntry.setStatus("current")


class _DsfBootImageUnitId_Type(Unsigned32):
    """Custom type dsfBootImageUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsfBootImageUnitId_Type.__name__ = "Unsigned32"
_DsfBootImageUnitId_Object = MibTableColumn
dsfBootImageUnitId = _DsfBootImageUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 5, 1, 1),
    _DsfBootImageUnitId_Type()
)
dsfBootImageUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsfBootImageUnitId.setStatus("current")


class _DsfBootImageIndex_Type(Unsigned32):
    """Custom type dsfBootImageIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsfBootImageIndex_Type.__name__ = "Unsigned32"
_DsfBootImageIndex_Object = MibTableColumn
dsfBootImageIndex = _DsfBootImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 5, 1, 2),
    _DsfBootImageIndex_Type()
)
dsfBootImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsfBootImageIndex.setStatus("current")


class _DsfBootImageUrl_Type(OctetString):
    """Custom type dsfBootImageUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DsfBootImageUrl_Type.__name__ = "OctetString"
_DsfBootImageUrl_Object = MibTableColumn
dsfBootImageUrl = _DsfBootImageUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 5, 1, 3),
    _DsfBootImageUrl_Type()
)
dsfBootImageUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsfBootImageUrl.setStatus("current")
_DsfBootImageInWorking_Type = TruthValue
_DsfBootImageInWorking_Object = MibTableColumn
dsfBootImageInWorking = _DsfBootImageInWorking_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 5, 1, 4),
    _DsfBootImageInWorking_Type()
)
dsfBootImageInWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsfBootImageInWorking.setStatus("current")
_DsfBootCfgFileTable_Object = MibTable
dsfBootCfgFileTable = _DsfBootCfgFileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dsfBootCfgFileTable.setStatus("current")
_DsfBootCfgFileEntry_Object = MibTableRow
dsfBootCfgFileEntry = _DsfBootCfgFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 6, 1)
)
dsfBootCfgFileEntry.setIndexNames(
    (0, "DLINKSW-SYSTEM-FILE-MIB", "dsfBootCfgFileUnitId"),
)
if mibBuilder.loadTexts:
    dsfBootCfgFileEntry.setStatus("current")


class _DsfBootCfgFileUnitId_Type(Unsigned32):
    """Custom type dsfBootCfgFileUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DsfBootCfgFileUnitId_Type.__name__ = "Unsigned32"
_DsfBootCfgFileUnitId_Object = MibTableColumn
dsfBootCfgFileUnitId = _DsfBootCfgFileUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 6, 1, 1),
    _DsfBootCfgFileUnitId_Type()
)
dsfBootCfgFileUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsfBootCfgFileUnitId.setStatus("current")


class _DsfBootCfgFileUrl_Type(OctetString):
    """Custom type dsfBootCfgFileUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DsfBootCfgFileUrl_Type.__name__ = "OctetString"
_DsfBootCfgFileUrl_Object = MibTableColumn
dsfBootCfgFileUrl = _DsfBootCfgFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 1, 6, 1, 2),
    _DsfBootCfgFileUrl_Type()
)
dsfBootCfgFileUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsfBootCfgFileUrl.setStatus("current")
_DsfCopyTable_Object = MibTable
dsfCopyTable = _DsfCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2)
)
if mibBuilder.loadTexts:
    dsfCopyTable.setStatus("current")
_DsfCopyEntry_Object = MibTableRow
dsfCopyEntry = _DsfCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1)
)
dsfCopyEntry.setIndexNames(
    (0, "DLINKSW-SYSTEM-FILE-MIB", "dsfCopyIndex"),
)
if mibBuilder.loadTexts:
    dsfCopyEntry.setStatus("current")


class _DsfCopyIndex_Type(Unsigned32):
    """Custom type dsfCopyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DsfCopyIndex_Type.__name__ = "Unsigned32"
_DsfCopyIndex_Object = MibTableColumn
dsfCopyIndex = _DsfCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 1),
    _DsfCopyIndex_Type()
)
dsfCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsfCopyIndex.setStatus("current")


class _DsfCopyType_Type(Integer32):
    """Custom type dsfCopyType based on Integer32"""
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
        *(("localToLocal", 1),
          ("localToTftpRemote", 2),
          ("localToFtpRemote", 3),
          ("localToRcpRemote", 4),
          ("tftpRemoteToLocal", 5),
          ("ftpRemoteToLocal", 6),
          ("rcpRemoteToLocal", 7))
    )


_DsfCopyType_Type.__name__ = "Integer32"
_DsfCopyType_Object = MibTableColumn
dsfCopyType = _DsfCopyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 2),
    _DsfCopyType_Type()
)
dsfCopyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyType.setStatus("current")


class _DsfCopySrcUrl_Type(OctetString):
    """Custom type dsfCopySrcUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DsfCopySrcUrl_Type.__name__ = "OctetString"
_DsfCopySrcUrl_Object = MibTableColumn
dsfCopySrcUrl = _DsfCopySrcUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 3),
    _DsfCopySrcUrl_Type()
)
dsfCopySrcUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopySrcUrl.setStatus("current")


class _DsfCopyDstUrl_Type(OctetString):
    """Custom type dsfCopyDstUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DsfCopyDstUrl_Type.__name__ = "OctetString"
_DsfCopyDstUrl_Object = MibTableColumn
dsfCopyDstUrl = _DsfCopyDstUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 4),
    _DsfCopyDstUrl_Type()
)
dsfCopyDstUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyDstUrl.setStatus("current")


class _DsfCopyRemoteAddrType_Type(InetAddressType):
    """Custom type dsfCopyRemoteAddrType based on InetAddressType"""
    defaultValue = 1


_DsfCopyRemoteAddrType_Type.__name__ = "InetAddressType"
_DsfCopyRemoteAddrType_Object = MibTableColumn
dsfCopyRemoteAddrType = _DsfCopyRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 5),
    _DsfCopyRemoteAddrType_Type()
)
dsfCopyRemoteAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyRemoteAddrType.setStatus("current")
_DsfCopyRemoteAddr_Type = InetAddress
_DsfCopyRemoteAddr_Object = MibTableColumn
dsfCopyRemoteAddr = _DsfCopyRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 6),
    _DsfCopyRemoteAddr_Type()
)
dsfCopyRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyRemoteAddr.setStatus("current")
_DsfCopyUsrName_Type = DisplayString
_DsfCopyUsrName_Object = MibTableColumn
dsfCopyUsrName = _DsfCopyUsrName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 7),
    _DsfCopyUsrName_Type()
)
dsfCopyUsrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyUsrName.setStatus("current")
_DsfCopyUsrPwd_Type = DisplayString
_DsfCopyUsrPwd_Object = MibTableColumn
dsfCopyUsrPwd = _DsfCopyUsrPwd_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 8),
    _DsfCopyUsrPwd_Type()
)
dsfCopyUsrPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyUsrPwd.setStatus("current")
_DsfCopyRemoteTcpPort_Type = Unsigned32
_DsfCopyRemoteTcpPort_Object = MibTableColumn
dsfCopyRemoteTcpPort = _DsfCopyRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 9),
    _DsfCopyRemoteTcpPort_Type()
)
dsfCopyRemoteTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyRemoteTcpPort.setStatus("current")
_DsfCopyVrfName_Type = DisplayString
_DsfCopyVrfName_Object = MibTableColumn
dsfCopyVrfName = _DsfCopyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 10),
    _DsfCopyVrfName_Type()
)
dsfCopyVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyVrfName.setStatus("current")
_DsfCopyErrorStatus_Type = DisplayString
_DsfCopyErrorStatus_Object = MibTableColumn
dsfCopyErrorStatus = _DsfCopyErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 11),
    _DsfCopyErrorStatus_Type()
)
dsfCopyErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsfCopyErrorStatus.setStatus("current")
_DsfCopyRowStatus_Type = RowStatus
_DsfCopyRowStatus_Object = MibTableColumn
dsfCopyRowStatus = _DsfCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 2, 1, 12),
    _DsfCopyRowStatus_Type()
)
dsfCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCopyRowStatus.setStatus("current")
_DsfCfgReplaceTable_Object = MibTable
dsfCfgReplaceTable = _DsfCfgReplaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3)
)
if mibBuilder.loadTexts:
    dsfCfgReplaceTable.setStatus("current")
_DsfCfgReplaceEntry_Object = MibTableRow
dsfCfgReplaceEntry = _DsfCfgReplaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1)
)
dsfCfgReplaceEntry.setIndexNames(
    (0, "DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceIndex"),
)
if mibBuilder.loadTexts:
    dsfCfgReplaceEntry.setStatus("current")


class _DsfCfgReplaceIndex_Type(Unsigned32):
    """Custom type dsfCfgReplaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DsfCfgReplaceIndex_Type.__name__ = "Unsigned32"
_DsfCfgReplaceIndex_Object = MibTableColumn
dsfCfgReplaceIndex = _DsfCfgReplaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 1),
    _DsfCfgReplaceIndex_Type()
)
dsfCfgReplaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsfCfgReplaceIndex.setStatus("current")


class _DsfCfgReplaceSrcType_Type(Integer32):
    """Custom type dsfCfgReplaceSrcType based on Integer32"""
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
        *(("local", 1),
          ("tftpRemote", 2),
          ("ftpRemote", 3),
          ("rcpRemote", 4))
    )


_DsfCfgReplaceSrcType_Type.__name__ = "Integer32"
_DsfCfgReplaceSrcType_Object = MibTableColumn
dsfCfgReplaceSrcType = _DsfCfgReplaceSrcType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 2),
    _DsfCfgReplaceSrcType_Type()
)
dsfCfgReplaceSrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceSrcType.setStatus("current")


class _DsfCfgReplaceSrcUrl_Type(OctetString):
    """Custom type dsfCfgReplaceSrcUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 799),
    )


_DsfCfgReplaceSrcUrl_Type.__name__ = "OctetString"
_DsfCfgReplaceSrcUrl_Object = MibTableColumn
dsfCfgReplaceSrcUrl = _DsfCfgReplaceSrcUrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 3),
    _DsfCfgReplaceSrcUrl_Type()
)
dsfCfgReplaceSrcUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceSrcUrl.setStatus("current")


class _DsfCfgReplaceRemoteAddrType_Type(InetAddressType):
    """Custom type dsfCfgReplaceRemoteAddrType based on InetAddressType"""
    defaultValue = 1


_DsfCfgReplaceRemoteAddrType_Type.__name__ = "InetAddressType"
_DsfCfgReplaceRemoteAddrType_Object = MibTableColumn
dsfCfgReplaceRemoteAddrType = _DsfCfgReplaceRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 4),
    _DsfCfgReplaceRemoteAddrType_Type()
)
dsfCfgReplaceRemoteAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceRemoteAddrType.setStatus("current")
_DsfCfgReplaceRemoteAddr_Type = InetAddress
_DsfCfgReplaceRemoteAddr_Object = MibTableColumn
dsfCfgReplaceRemoteAddr = _DsfCfgReplaceRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 5),
    _DsfCfgReplaceRemoteAddr_Type()
)
dsfCfgReplaceRemoteAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceRemoteAddr.setStatus("current")
_DsfCfgReplaceUsrName_Type = DisplayString
_DsfCfgReplaceUsrName_Object = MibTableColumn
dsfCfgReplaceUsrName = _DsfCfgReplaceUsrName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 6),
    _DsfCfgReplaceUsrName_Type()
)
dsfCfgReplaceUsrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceUsrName.setStatus("current")
_DsfCfgReplaceUsrPwd_Type = DisplayString
_DsfCfgReplaceUsrPwd_Object = MibTableColumn
dsfCfgReplaceUsrPwd = _DsfCfgReplaceUsrPwd_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 7),
    _DsfCfgReplaceUsrPwd_Type()
)
dsfCfgReplaceUsrPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceUsrPwd.setStatus("current")
_DsfCfgReplaceRemoteTcpPort_Type = Unsigned32
_DsfCfgReplaceRemoteTcpPort_Object = MibTableColumn
dsfCfgReplaceRemoteTcpPort = _DsfCfgReplaceRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 8),
    _DsfCfgReplaceRemoteTcpPort_Type()
)
dsfCfgReplaceRemoteTcpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceRemoteTcpPort.setStatus("current")
_DsfCfgReplaceVrfName_Type = DisplayString
_DsfCfgReplaceVrfName_Object = MibTableColumn
dsfCfgReplaceVrfName = _DsfCfgReplaceVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 9),
    _DsfCfgReplaceVrfName_Type()
)
dsfCfgReplaceVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceVrfName.setStatus("current")
_DsfCfgReplaceErrorStatus_Type = DisplayString
_DsfCfgReplaceErrorStatus_Object = MibTableColumn
dsfCfgReplaceErrorStatus = _DsfCfgReplaceErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 10),
    _DsfCfgReplaceErrorStatus_Type()
)
dsfCfgReplaceErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsfCfgReplaceErrorStatus.setStatus("current")
_DsfCfgReplaceRowStatus_Type = RowStatus
_DsfCfgReplaceRowStatus_Object = MibTableColumn
dsfCfgReplaceRowStatus = _DsfCfgReplaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 3, 1, 11),
    _DsfCfgReplaceRowStatus_Type()
)
dsfCfgReplaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dsfCfgReplaceRowStatus.setStatus("current")
_DsfIpSrcIfObjects_ObjectIdentity = ObjectIdentity
dsfIpSrcIfObjects = _DsfIpSrcIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 4)
)
_DsfIpTftpSrcIf_Type = InterfaceIndexOrZero
_DsfIpTftpSrcIf_Object = MibScalar
dsfIpTftpSrcIf = _DsfIpTftpSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 4, 1),
    _DsfIpTftpSrcIf_Type()
)
dsfIpTftpSrcIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfIpTftpSrcIf.setStatus("current")
_DsfIpFtpSrcIf_Type = InterfaceIndexOrZero
_DsfIpFtpSrcIf_Object = MibScalar
dsfIpFtpSrcIf = _DsfIpFtpSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 4, 2),
    _DsfIpFtpSrcIf_Type()
)
dsfIpFtpSrcIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfIpFtpSrcIf.setStatus("current")
_DsfIpRcpSrcIf_Type = InterfaceIndexOrZero
_DsfIpRcpSrcIf_Object = MibScalar
dsfIpRcpSrcIf = _DsfIpRcpSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 4, 3),
    _DsfIpRcpSrcIf_Type()
)
dsfIpRcpSrcIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfIpRcpSrcIf.setStatus("current")


class _DsfClearRunCfg_Type(Integer32):
    """Custom type dsfClearRunCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DsfClearRunCfg_Type.__name__ = "Integer32"
_DsfClearRunCfg_Object = MibScalar
dsfClearRunCfg = _DsfClearRunCfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 5),
    _DsfClearRunCfg_Type()
)
dsfClearRunCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfClearRunCfg.setStatus("current")


class _DsfResetSystem_Type(Integer32):
    """Custom type dsfResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("noOp", 2))
    )


_DsfResetSystem_Type.__name__ = "Integer32"
_DsfResetSystem_Object = MibScalar
dsfResetSystem = _DsfResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 1, 6),
    _DsfResetSystem_Type()
)
dsfResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsfResetSystem.setStatus("current")
_DsfMIBConformance_ObjectIdentity = ObjectIdentity
dsfMIBConformance = _DsfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2)
)
_DsfCompliances_ObjectIdentity = ObjectIdentity
dsfCompliances = _DsfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 1)
)
_DsfGroups_ObjectIdentity = ObjectIdentity
dsfGroups = _DsfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 2)
)

# Managed Objects groups

dsfBootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 2, 1)
)
dsfBootInfoGroup.setObjects(
      *(("DLINKSW-SYSTEM-FILE-MIB", "dsfNextBootCfgUrl"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfNextBootImageUrl"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCheckingBootImageCheck"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfBootImageCheckResult"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfBootImageUrl"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfBootImageInWorking"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfBootCfgFileUrl"))
)
if mibBuilder.loadTexts:
    dsfBootInfoGroup.setStatus("current")

dsfCopyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 2, 2)
)
dsfCopyGroup.setObjects(
      *(("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyType"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopySrcUrl"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyDstUrl"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyRemoteAddrType"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyRemoteAddr"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyUsrName"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyUsrPwd"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyRemoteTcpPort"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyVrfName"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyErrorStatus"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyRowStatus"))
)
if mibBuilder.loadTexts:
    dsfCopyGroup.setStatus("current")

dsfCfgReplaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 2, 3)
)
dsfCfgReplaceGroup.setObjects(
      *(("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceSrcType"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceSrcUrl"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceRemoteAddrType"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceRemoteAddr"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceUsrName"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceUsrPwd"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceRemoteTcpPort"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceVrfName"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceErrorStatus"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceRowStatus"))
)
if mibBuilder.loadTexts:
    dsfCfgReplaceGroup.setStatus("current")

dsfIpSrcIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 2, 4)
)
dsfIpSrcIfGroup.setObjects(
      *(("DLINKSW-SYSTEM-FILE-MIB", "dsfIpTftpSrcIf"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfIpFtpSrcIf"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfIpRcpSrcIf"))
)
if mibBuilder.loadTexts:
    dsfIpSrcIfGroup.setStatus("current")

dsfClearCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 2, 5)
)
dsfClearCfgGroup.setObjects(
      *(("DLINKSW-SYSTEM-FILE-MIB", "dsfClearRunCfg"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfResetSystem"))
)
if mibBuilder.loadTexts:
    dsfClearCfgGroup.setStatus("current")


# Notification objects

dsfUploadImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 0, 1)
)
if mibBuilder.loadTexts:
    dsfUploadImage.setStatus(
        "current"
    )

dsfDownloadImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 0, 2)
)
if mibBuilder.loadTexts:
    dsfDownloadImage.setStatus(
        "current"
    )

dsfUploadCfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 0, 3)
)
if mibBuilder.loadTexts:
    dsfUploadCfg.setStatus(
        "current"
    )

dsfDownloadCfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 0, 4)
)
if mibBuilder.loadTexts:
    dsfDownloadCfg.setStatus(
        "current"
    )

dsfSaveCfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 0, 5)
)
if mibBuilder.loadTexts:
    dsfSaveCfg.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

dsfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 14, 2, 1, 1)
)
dsfCompliance.setObjects(
      *(("DLINKSW-SYSTEM-FILE-MIB", "dsfBootInfoGroup"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCopyGroup"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfCfgReplaceGroup"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfIpSrcIfGroup"),
        ("DLINKSW-SYSTEM-FILE-MIB", "dsfClearCfgGroup"))
)
if mibBuilder.loadTexts:
    dsfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SYSTEM-FILE-MIB",
    **{"dlinkSwSystemFileMIB": dlinkSwSystemFileMIB,
       "dsfMIBNotifications": dsfMIBNotifications,
       "dsfUploadImage": dsfUploadImage,
       "dsfDownloadImage": dsfDownloadImage,
       "dsfUploadCfg": dsfUploadCfg,
       "dsfDownloadCfg": dsfDownloadCfg,
       "dsfSaveCfg": dsfSaveCfg,
       "dsfMIBObjects": dsfMIBObjects,
       "dsfBootInfoObjects": dsfBootInfoObjects,
       "dsfNextBootCfgUrl": dsfNextBootCfgUrl,
       "dsfNextBootImageUrl": dsfNextBootImageUrl,
       "dsfCheckingBootImageCheck": dsfCheckingBootImageCheck,
       "dsfBootImageCheckResult": dsfBootImageCheckResult,
       "dsfBootImageTable": dsfBootImageTable,
       "dsfBootImageEntry": dsfBootImageEntry,
       "dsfBootImageUnitId": dsfBootImageUnitId,
       "dsfBootImageIndex": dsfBootImageIndex,
       "dsfBootImageUrl": dsfBootImageUrl,
       "dsfBootImageInWorking": dsfBootImageInWorking,
       "dsfBootCfgFileTable": dsfBootCfgFileTable,
       "dsfBootCfgFileEntry": dsfBootCfgFileEntry,
       "dsfBootCfgFileUnitId": dsfBootCfgFileUnitId,
       "dsfBootCfgFileUrl": dsfBootCfgFileUrl,
       "dsfCopyTable": dsfCopyTable,
       "dsfCopyEntry": dsfCopyEntry,
       "dsfCopyIndex": dsfCopyIndex,
       "dsfCopyType": dsfCopyType,
       "dsfCopySrcUrl": dsfCopySrcUrl,
       "dsfCopyDstUrl": dsfCopyDstUrl,
       "dsfCopyRemoteAddrType": dsfCopyRemoteAddrType,
       "dsfCopyRemoteAddr": dsfCopyRemoteAddr,
       "dsfCopyUsrName": dsfCopyUsrName,
       "dsfCopyUsrPwd": dsfCopyUsrPwd,
       "dsfCopyRemoteTcpPort": dsfCopyRemoteTcpPort,
       "dsfCopyVrfName": dsfCopyVrfName,
       "dsfCopyErrorStatus": dsfCopyErrorStatus,
       "dsfCopyRowStatus": dsfCopyRowStatus,
       "dsfCfgReplaceTable": dsfCfgReplaceTable,
       "dsfCfgReplaceEntry": dsfCfgReplaceEntry,
       "dsfCfgReplaceIndex": dsfCfgReplaceIndex,
       "dsfCfgReplaceSrcType": dsfCfgReplaceSrcType,
       "dsfCfgReplaceSrcUrl": dsfCfgReplaceSrcUrl,
       "dsfCfgReplaceRemoteAddrType": dsfCfgReplaceRemoteAddrType,
       "dsfCfgReplaceRemoteAddr": dsfCfgReplaceRemoteAddr,
       "dsfCfgReplaceUsrName": dsfCfgReplaceUsrName,
       "dsfCfgReplaceUsrPwd": dsfCfgReplaceUsrPwd,
       "dsfCfgReplaceRemoteTcpPort": dsfCfgReplaceRemoteTcpPort,
       "dsfCfgReplaceVrfName": dsfCfgReplaceVrfName,
       "dsfCfgReplaceErrorStatus": dsfCfgReplaceErrorStatus,
       "dsfCfgReplaceRowStatus": dsfCfgReplaceRowStatus,
       "dsfIpSrcIfObjects": dsfIpSrcIfObjects,
       "dsfIpTftpSrcIf": dsfIpTftpSrcIf,
       "dsfIpFtpSrcIf": dsfIpFtpSrcIf,
       "dsfIpRcpSrcIf": dsfIpRcpSrcIf,
       "dsfClearRunCfg": dsfClearRunCfg,
       "dsfResetSystem": dsfResetSystem,
       "dsfMIBConformance": dsfMIBConformance,
       "dsfCompliances": dsfCompliances,
       "dsfCompliance": dsfCompliance,
       "dsfGroups": dsfGroups,
       "dsfBootInfoGroup": dsfBootInfoGroup,
       "dsfCopyGroup": dsfCopyGroup,
       "dsfCfgReplaceGroup": dsfCfgReplaceGroup,
       "dsfIpSrcIfGroup": dsfIpSrcIfGroup,
       "dsfClearCfgGroup": dsfClearCfgGroup}
)
