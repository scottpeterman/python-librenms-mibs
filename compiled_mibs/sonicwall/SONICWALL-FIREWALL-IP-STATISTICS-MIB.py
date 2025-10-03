# SNMP MIB module (SONICWALL-FIREWALL-IP-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sonicwall\SONICWALL-FIREWALL-IP-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:28:46 2025
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

(sonicwallFw,) = mibBuilder.importSymbols(
    "SONICWALL-SMI",
    "sonicwallFw")


# MODULE-IDENTITY

sonicwallFwStatsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3)
)
if mibBuilder.loadTexts:
    sonicwallFwStatsModule.setRevisions(
        ("2005-11-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonicwallFwStats_ObjectIdentity = ObjectIdentity
sonicwallFwStats = _SonicwallFwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1)
)
_SonicMaxConnCacheEntries_Type = Counter32
_SonicMaxConnCacheEntries_Object = MibScalar
sonicMaxConnCacheEntries = _SonicMaxConnCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 1),
    _SonicMaxConnCacheEntries_Type()
)
sonicMaxConnCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicMaxConnCacheEntries.setStatus("current")
_SonicCurrentConnCacheEntries_Type = Counter32
_SonicCurrentConnCacheEntries_Object = MibScalar
sonicCurrentConnCacheEntries = _SonicCurrentConnCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 2),
    _SonicCurrentConnCacheEntries_Type()
)
sonicCurrentConnCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentConnCacheEntries.setStatus("current")
_SonicCurrentCPUUtil_Type = Gauge32
_SonicCurrentCPUUtil_Object = MibScalar
sonicCurrentCPUUtil = _SonicCurrentCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 3),
    _SonicCurrentCPUUtil_Type()
)
sonicCurrentCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentCPUUtil.setStatus("current")
_SonicCurrentRAMUtil_Type = Gauge32
_SonicCurrentRAMUtil_Object = MibScalar
sonicCurrentRAMUtil = _SonicCurrentRAMUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 4),
    _SonicCurrentRAMUtil_Type()
)
sonicCurrentRAMUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentRAMUtil.setStatus("current")
_SonicwallFwVPNStats_ObjectIdentity = ObjectIdentity
sonicwallFwVPNStats = _SonicwallFwVPNStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2)
)
_SonicwallFwVpnIPSecStats_ObjectIdentity = ObjectIdentity
sonicwallFwVpnIPSecStats = _SonicwallFwVpnIPSecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1)
)
_SonicSAStatTable_Object = MibTable
sonicSAStatTable = _SonicSAStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sonicSAStatTable.setStatus("current")
_SonicSAStatEntry_Object = MibTableRow
sonicSAStatEntry = _SonicSAStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1)
)
sonicSAStatEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicIpsecSaIndex"),
)
if mibBuilder.loadTexts:
    sonicSAStatEntry.setStatus("current")
_SonicIpsecSaIndex_Type = Counter32
_SonicIpsecSaIndex_Object = MibTableColumn
sonicIpsecSaIndex = _SonicIpsecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 1),
    _SonicIpsecSaIndex_Type()
)
sonicIpsecSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIpsecSaIndex.setStatus("current")
_SonicSAStatPeerGateway_Type = IpAddress
_SonicSAStatPeerGateway_Object = MibTableColumn
sonicSAStatPeerGateway = _SonicSAStatPeerGateway_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 2),
    _SonicSAStatPeerGateway_Type()
)
sonicSAStatPeerGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatPeerGateway.setStatus("current")
_SonicSAStatSrcAddrBegin_Type = IpAddress
_SonicSAStatSrcAddrBegin_Object = MibTableColumn
sonicSAStatSrcAddrBegin = _SonicSAStatSrcAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 3),
    _SonicSAStatSrcAddrBegin_Type()
)
sonicSAStatSrcAddrBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatSrcAddrBegin.setStatus("current")
_SonicSAStatSrcAddrEnd_Type = IpAddress
_SonicSAStatSrcAddrEnd_Object = MibTableColumn
sonicSAStatSrcAddrEnd = _SonicSAStatSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 4),
    _SonicSAStatSrcAddrEnd_Type()
)
sonicSAStatSrcAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatSrcAddrEnd.setStatus("current")
_SonicSAStatDstAddrBegin_Type = IpAddress
_SonicSAStatDstAddrBegin_Object = MibTableColumn
sonicSAStatDstAddrBegin = _SonicSAStatDstAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 5),
    _SonicSAStatDstAddrBegin_Type()
)
sonicSAStatDstAddrBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDstAddrBegin.setStatus("current")
_SonicSAStatDstAddrEnd_Type = IpAddress
_SonicSAStatDstAddrEnd_Object = MibTableColumn
sonicSAStatDstAddrEnd = _SonicSAStatDstAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 6),
    _SonicSAStatDstAddrEnd_Type()
)
sonicSAStatDstAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDstAddrEnd.setStatus("current")
_SonicSAStatCreateTime_Type = DisplayString
_SonicSAStatCreateTime_Object = MibTableColumn
sonicSAStatCreateTime = _SonicSAStatCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 7),
    _SonicSAStatCreateTime_Type()
)
sonicSAStatCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatCreateTime.setStatus("current")
_SonicSAStatEncryptPktCount_Type = Counter32
_SonicSAStatEncryptPktCount_Object = MibTableColumn
sonicSAStatEncryptPktCount = _SonicSAStatEncryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 8),
    _SonicSAStatEncryptPktCount_Type()
)
sonicSAStatEncryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatEncryptPktCount.setStatus("current")
_SonicSAStatEncryptByteCount_Type = Counter32
_SonicSAStatEncryptByteCount_Object = MibTableColumn
sonicSAStatEncryptByteCount = _SonicSAStatEncryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 9),
    _SonicSAStatEncryptByteCount_Type()
)
sonicSAStatEncryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatEncryptByteCount.setStatus("current")
_SonicSAStatDecryptPktCount_Type = Counter32
_SonicSAStatDecryptPktCount_Object = MibTableColumn
sonicSAStatDecryptPktCount = _SonicSAStatDecryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 10),
    _SonicSAStatDecryptPktCount_Type()
)
sonicSAStatDecryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDecryptPktCount.setStatus("current")
_SonicSAStatDecryptByteCount_Type = Counter32
_SonicSAStatDecryptByteCount_Object = MibTableColumn
sonicSAStatDecryptByteCount = _SonicSAStatDecryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 11),
    _SonicSAStatDecryptByteCount_Type()
)
sonicSAStatDecryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDecryptByteCount.setStatus("current")
_SonicSAStatInFragPktCount_Type = Counter32
_SonicSAStatInFragPktCount_Object = MibTableColumn
sonicSAStatInFragPktCount = _SonicSAStatInFragPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 12),
    _SonicSAStatInFragPktCount_Type()
)
sonicSAStatInFragPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatInFragPktCount.setStatus("current")
_SonicSAStatOutFragPktCount_Type = Counter32
_SonicSAStatOutFragPktCount_Object = MibTableColumn
sonicSAStatOutFragPktCount = _SonicSAStatOutFragPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 13),
    _SonicSAStatOutFragPktCount_Type()
)
sonicSAStatOutFragPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatOutFragPktCount.setStatus("current")
_SonicSAStatUserName_Type = DisplayString
_SonicSAStatUserName_Object = MibTableColumn
sonicSAStatUserName = _SonicSAStatUserName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 14),
    _SonicSAStatUserName_Type()
)
sonicSAStatUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-FIREWALL-IP-STATISTICS-MIB",
    **{"sonicwallFwStatsModule": sonicwallFwStatsModule,
       "sonicwallFwStats": sonicwallFwStats,
       "sonicMaxConnCacheEntries": sonicMaxConnCacheEntries,
       "sonicCurrentConnCacheEntries": sonicCurrentConnCacheEntries,
       "sonicCurrentCPUUtil": sonicCurrentCPUUtil,
       "sonicCurrentRAMUtil": sonicCurrentRAMUtil,
       "sonicwallFwVPNStats": sonicwallFwVPNStats,
       "sonicwallFwVpnIPSecStats": sonicwallFwVpnIPSecStats,
       "sonicSAStatTable": sonicSAStatTable,
       "sonicSAStatEntry": sonicSAStatEntry,
       "sonicIpsecSaIndex": sonicIpsecSaIndex,
       "sonicSAStatPeerGateway": sonicSAStatPeerGateway,
       "sonicSAStatSrcAddrBegin": sonicSAStatSrcAddrBegin,
       "sonicSAStatSrcAddrEnd": sonicSAStatSrcAddrEnd,
       "sonicSAStatDstAddrBegin": sonicSAStatDstAddrBegin,
       "sonicSAStatDstAddrEnd": sonicSAStatDstAddrEnd,
       "sonicSAStatCreateTime": sonicSAStatCreateTime,
       "sonicSAStatEncryptPktCount": sonicSAStatEncryptPktCount,
       "sonicSAStatEncryptByteCount": sonicSAStatEncryptByteCount,
       "sonicSAStatDecryptPktCount": sonicSAStatDecryptPktCount,
       "sonicSAStatDecryptByteCount": sonicSAStatDecryptByteCount,
       "sonicSAStatInFragPktCount": sonicSAStatInFragPktCount,
       "sonicSAStatOutFragPktCount": sonicSAStatOutFragPktCount,
       "sonicSAStatUserName": sonicSAStatUserName}
)
