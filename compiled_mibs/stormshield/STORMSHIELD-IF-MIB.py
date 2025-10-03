# SNMP MIB module (STORMSHIELD-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-IF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:07 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsif = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4)
)
if mibBuilder.loadTexts:
    snsif.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsifTable_Object = MibTable
snsifTable = _SnsifTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snsifTable.setStatus("current")
_SnsifEntry_Object = MibTableRow
snsifEntry = _SnsifEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1)
)
snsifEntry.setIndexNames(
    (0, "STORMSHIELD-IF-MIB", "snsifIndex"),
)
if mibBuilder.loadTexts:
    snsifEntry.setStatus("current")


class _SnsifIndex_Type(Integer32):
    """Custom type snsifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsifIndex_Type.__name__ = "Integer32"
_SnsifIndex_Object = MibTableColumn
snsifIndex = _SnsifIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 1),
    _SnsifIndex_Type()
)
snsifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifIndex.setStatus("current")
_SnsifUserName_Type = SnmpAdminString
_SnsifUserName_Object = MibTableColumn
snsifUserName = _SnsifUserName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 2),
    _SnsifUserName_Type()
)
snsifUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifUserName.setStatus("current")
_SnsifName_Type = DisplayString
_SnsifName_Object = MibTableColumn
snsifName = _SnsifName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 3),
    _SnsifName_Type()
)
snsifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifName.setStatus("current")
_SnsifAddr_Type = DisplayString
_SnsifAddr_Object = MibTableColumn
snsifAddr = _SnsifAddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 4),
    _SnsifAddr_Type()
)
snsifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifAddr.setStatus("current")
_SnsifMask_Type = DisplayString
_SnsifMask_Object = MibTableColumn
snsifMask = _SnsifMask_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 5),
    _SnsifMask_Type()
)
snsifMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifMask.setStatus("current")
_SnsifType_Type = DisplayString
_SnsifType_Object = MibTableColumn
snsifType = _SnsifType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 6),
    _SnsifType_Type()
)
snsifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifType.setStatus("current")
_SnsifColor_Type = Integer32
_SnsifColor_Object = MibTableColumn
snsifColor = _SnsifColor_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 7),
    _SnsifColor_Type()
)
snsifColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifColor.setStatus("current")
_SnsifMacThroughput_Type = Integer32
_SnsifMacThroughput_Object = MibTableColumn
snsifMacThroughput = _SnsifMacThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 8),
    _SnsifMacThroughput_Type()
)
snsifMacThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifMacThroughput.setStatus("current")
_SnsifCurThroughput_Type = Integer32
_SnsifCurThroughput_Object = MibTableColumn
snsifCurThroughput = _SnsifCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 9),
    _SnsifCurThroughput_Type()
)
snsifCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifCurThroughput.setStatus("current")
_SnsifMaxThroughput_Type = Integer32
_SnsifMaxThroughput_Object = MibTableColumn
snsifMaxThroughput = _SnsifMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 10),
    _SnsifMaxThroughput_Type()
)
snsifMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifMaxThroughput.setStatus("current")
_SnsifPktAccepted_Type = Counter64
_SnsifPktAccepted_Object = MibTableColumn
snsifPktAccepted = _SnsifPktAccepted_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 11),
    _SnsifPktAccepted_Type()
)
snsifPktAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifPktAccepted.setStatus("current")
_SnsifPktBlocked_Type = Counter64
_SnsifPktBlocked_Object = MibTableColumn
snsifPktBlocked = _SnsifPktBlocked_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 12),
    _SnsifPktBlocked_Type()
)
snsifPktBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifPktBlocked.setStatus("current")
_SnsifPktFragmented_Type = Counter64
_SnsifPktFragmented_Object = MibTableColumn
snsifPktFragmented = _SnsifPktFragmented_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 13),
    _SnsifPktFragmented_Type()
)
snsifPktFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifPktFragmented.setStatus("current")
_SnsifPktTcp_Type = Counter64
_SnsifPktTcp_Object = MibTableColumn
snsifPktTcp = _SnsifPktTcp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 14),
    _SnsifPktTcp_Type()
)
snsifPktTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifPktTcp.setStatus("current")
_SnsifPktUdp_Type = Counter64
_SnsifPktUdp_Object = MibTableColumn
snsifPktUdp = _SnsifPktUdp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 15),
    _SnsifPktUdp_Type()
)
snsifPktUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifPktUdp.setStatus("current")
_SnsifPktIcmp_Type = Counter64
_SnsifPktIcmp_Object = MibTableColumn
snsifPktIcmp = _SnsifPktIcmp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 16),
    _SnsifPktIcmp_Type()
)
snsifPktIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifPktIcmp.setStatus("current")
_SnsifTotalBytes_Type = Counter64
_SnsifTotalBytes_Object = MibTableColumn
snsifTotalBytes = _SnsifTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 17),
    _SnsifTotalBytes_Type()
)
snsifTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifTotalBytes.setStatus("current")
_SnsifTcpBytes_Type = Counter64
_SnsifTcpBytes_Object = MibTableColumn
snsifTcpBytes = _SnsifTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 18),
    _SnsifTcpBytes_Type()
)
snsifTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifTcpBytes.setStatus("current")
_SnsifUdpBytes_Type = Counter64
_SnsifUdpBytes_Object = MibTableColumn
snsifUdpBytes = _SnsifUdpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 19),
    _SnsifUdpBytes_Type()
)
snsifUdpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifUdpBytes.setStatus("current")
_SnsifIcmpBytes_Type = Counter64
_SnsifIcmpBytes_Object = MibTableColumn
snsifIcmpBytes = _SnsifIcmpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 20),
    _SnsifIcmpBytes_Type()
)
snsifIcmpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifIcmpBytes.setStatus("current")
_SnsifTcpConn_Type = Counter64
_SnsifTcpConn_Object = MibTableColumn
snsifTcpConn = _SnsifTcpConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 21),
    _SnsifTcpConn_Type()
)
snsifTcpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifTcpConn.setStatus("current")
_SnsifUdpConn_Type = Counter64
_SnsifUdpConn_Object = MibTableColumn
snsifUdpConn = _SnsifUdpConn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 22),
    _SnsifUdpConn_Type()
)
snsifUdpConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifUdpConn.setStatus("current")
_SnsifTcpConnCount_Type = Integer32
_SnsifTcpConnCount_Object = MibTableColumn
snsifTcpConnCount = _SnsifTcpConnCount_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 23),
    _SnsifTcpConnCount_Type()
)
snsifTcpConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifTcpConnCount.setStatus("current")
_SnsifUdpConnCount_Type = Integer32
_SnsifUdpConnCount_Object = MibTableColumn
snsifUdpConnCount = _SnsifUdpConnCount_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 24),
    _SnsifUdpConnCount_Type()
)
snsifUdpConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifUdpConnCount.setStatus("current")
_SnsifInCurThroughput_Type = Integer32
_SnsifInCurThroughput_Object = MibTableColumn
snsifInCurThroughput = _SnsifInCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 25),
    _SnsifInCurThroughput_Type()
)
snsifInCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifInCurThroughput.setStatus("current")
_SnsifOutCurThroughput_Type = Integer32
_SnsifOutCurThroughput_Object = MibTableColumn
snsifOutCurThroughput = _SnsifOutCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 26),
    _SnsifOutCurThroughput_Type()
)
snsifOutCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifOutCurThroughput.setStatus("current")
_SnsifInMaxThroughput_Type = Integer32
_SnsifInMaxThroughput_Object = MibTableColumn
snsifInMaxThroughput = _SnsifInMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 27),
    _SnsifInMaxThroughput_Type()
)
snsifInMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifInMaxThroughput.setStatus("current")
_SnsifOutMaxThroughput_Type = Integer32
_SnsifOutMaxThroughput_Object = MibTableColumn
snsifOutMaxThroughput = _SnsifOutMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 28),
    _SnsifOutMaxThroughput_Type()
)
snsifOutMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifOutMaxThroughput.setStatus("current")
_SnsifInTotalBytes_Type = Counter64
_SnsifInTotalBytes_Object = MibTableColumn
snsifInTotalBytes = _SnsifInTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 29),
    _SnsifInTotalBytes_Type()
)
snsifInTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifInTotalBytes.setStatus("current")
_SnsifOutTotalBytes_Type = Counter64
_SnsifOutTotalBytes_Object = MibTableColumn
snsifOutTotalBytes = _SnsifOutTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 30),
    _SnsifOutTotalBytes_Type()
)
snsifOutTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifOutTotalBytes.setStatus("current")
_SnsifInTcpBytes_Type = Counter64
_SnsifInTcpBytes_Object = MibTableColumn
snsifInTcpBytes = _SnsifInTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 31),
    _SnsifInTcpBytes_Type()
)
snsifInTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifInTcpBytes.setStatus("current")
_SnsifOutTcpBytes_Type = Counter64
_SnsifOutTcpBytes_Object = MibTableColumn
snsifOutTcpBytes = _SnsifOutTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 32),
    _SnsifOutTcpBytes_Type()
)
snsifOutTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifOutTcpBytes.setStatus("current")
_SnsifInUdpBytes_Type = Counter64
_SnsifInUdpBytes_Object = MibTableColumn
snsifInUdpBytes = _SnsifInUdpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 33),
    _SnsifInUdpBytes_Type()
)
snsifInUdpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifInUdpBytes.setStatus("current")
_SnsifOutUdpBytes_Type = Counter64
_SnsifOutUdpBytes_Object = MibTableColumn
snsifOutUdpBytes = _SnsifOutUdpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 34),
    _SnsifOutUdpBytes_Type()
)
snsifOutUdpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifOutUdpBytes.setStatus("current")
_SnsifInIcmpBytes_Type = Counter64
_SnsifInIcmpBytes_Object = MibTableColumn
snsifInIcmpBytes = _SnsifInIcmpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 35),
    _SnsifInIcmpBytes_Type()
)
snsifInIcmpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifInIcmpBytes.setStatus("current")
_SnsifOutIcmpBytes_Type = Counter64
_SnsifOutIcmpBytes_Object = MibTableColumn
snsifOutIcmpBytes = _SnsifOutIcmpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 36),
    _SnsifOutIcmpBytes_Type()
)
snsifOutIcmpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifOutIcmpBytes.setStatus("current")
_SnsifProtected_Type = Integer32
_SnsifProtected_Object = MibTableColumn
snsifProtected = _SnsifProtected_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 37),
    _SnsifProtected_Type()
)
snsifProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifProtected.setStatus("current")
_SnsifDrvName_Type = DisplayString
_SnsifDrvName_Object = MibTableColumn
snsifDrvName = _SnsifDrvName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 4, 1, 1, 38),
    _SnsifDrvName_Type()
)
snsifDrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsifDrvName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-IF-MIB",
    **{"snsif": snsif,
       "snsifTable": snsifTable,
       "snsifEntry": snsifEntry,
       "snsifIndex": snsifIndex,
       "snsifUserName": snsifUserName,
       "snsifName": snsifName,
       "snsifAddr": snsifAddr,
       "snsifMask": snsifMask,
       "snsifType": snsifType,
       "snsifColor": snsifColor,
       "snsifMacThroughput": snsifMacThroughput,
       "snsifCurThroughput": snsifCurThroughput,
       "snsifMaxThroughput": snsifMaxThroughput,
       "snsifPktAccepted": snsifPktAccepted,
       "snsifPktBlocked": snsifPktBlocked,
       "snsifPktFragmented": snsifPktFragmented,
       "snsifPktTcp": snsifPktTcp,
       "snsifPktUdp": snsifPktUdp,
       "snsifPktIcmp": snsifPktIcmp,
       "snsifTotalBytes": snsifTotalBytes,
       "snsifTcpBytes": snsifTcpBytes,
       "snsifUdpBytes": snsifUdpBytes,
       "snsifIcmpBytes": snsifIcmpBytes,
       "snsifTcpConn": snsifTcpConn,
       "snsifUdpConn": snsifUdpConn,
       "snsifTcpConnCount": snsifTcpConnCount,
       "snsifUdpConnCount": snsifUdpConnCount,
       "snsifInCurThroughput": snsifInCurThroughput,
       "snsifOutCurThroughput": snsifOutCurThroughput,
       "snsifInMaxThroughput": snsifInMaxThroughput,
       "snsifOutMaxThroughput": snsifOutMaxThroughput,
       "snsifInTotalBytes": snsifInTotalBytes,
       "snsifOutTotalBytes": snsifOutTotalBytes,
       "snsifInTcpBytes": snsifInTcpBytes,
       "snsifOutTcpBytes": snsifOutTcpBytes,
       "snsifInUdpBytes": snsifInUdpBytes,
       "snsifOutUdpBytes": snsifOutUdpBytes,
       "snsifInIcmpBytes": snsifInIcmpBytes,
       "snsifOutIcmpBytes": snsifOutIcmpBytes,
       "snsifProtected": snsifProtected,
       "snsifDrvName": snsifDrvName}
)
