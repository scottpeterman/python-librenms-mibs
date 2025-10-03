# SNMP MIB module (EIP-DNSBLAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\efficientip\EIP-DNSBLAST-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:10 2025
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

eip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2440)
)
if mibBuilder.loadTexts:
    eip.setRevisions(
        ("2015-11-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1)
)
_EipDNSGUARDIAN_ObjectIdentity = ObjectIdentity
eipDNSGUARDIAN = _EipDNSGUARDIAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11)
)
_EipDNSGUARDIANStat_ObjectIdentity = ObjectIdentity
eipDNSGUARDIANStat = _EipDNSGUARDIANStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2)
)
_EipDNSGUARDIANViewStatTable_Object = MibTable
eipDNSGUARDIANViewStatTable = _EipDNSGUARDIANViewStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3)
)
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatTable.setStatus("current")
_EipDNSGUARDIANViewStatEntry_Object = MibTableRow
eipDNSGUARDIANViewStatEntry = _EipDNSGUARDIANViewStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1)
)
eipDNSGUARDIANViewStatEntry.setIndexNames(
    (0, "EIP-DNSBLAST-MIB", "eipDNSGUARDIANViewStatViewID"),
)
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatEntry.setStatus("current")


class _EipDNSGUARDIANViewStatViewID_Type(Integer32):
    """Custom type eipDNSGUARDIANViewStatViewID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EipDNSGUARDIANViewStatViewID_Type.__name__ = "Integer32"
_EipDNSGUARDIANViewStatViewID_Object = MibTableColumn
eipDNSGUARDIANViewStatViewID = _EipDNSGUARDIANViewStatViewID_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 1),
    _EipDNSGUARDIANViewStatViewID_Type()
)
eipDNSGUARDIANViewStatViewID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatViewID.setStatus("current")
_EipDNSGUARDIANViewStatViewName_Type = DisplayString
_EipDNSGUARDIANViewStatViewName_Object = MibTableColumn
eipDNSGUARDIANViewStatViewName = _EipDNSGUARDIANViewStatViewName_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 2),
    _EipDNSGUARDIANViewStatViewName_Type()
)
eipDNSGUARDIANViewStatViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatViewName.setStatus("current")
_EipDNSGUARDIANViewStatCacheHit_Type = Counter64
_EipDNSGUARDIANViewStatCacheHit_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheHit = _EipDNSGUARDIANViewStatCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 3),
    _EipDNSGUARDIANViewStatCacheHit_Type()
)
eipDNSGUARDIANViewStatCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheHit.setStatus("current")
_EipDNSGUARDIANViewStatCacheMiss_Type = Counter64
_EipDNSGUARDIANViewStatCacheMiss_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMiss = _EipDNSGUARDIANViewStatCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 4),
    _EipDNSGUARDIANViewStatCacheMiss_Type()
)
eipDNSGUARDIANViewStatCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMiss.setStatus("current")
_EipDNSGUARDIANViewStatCacheSize_Type = Gauge32
_EipDNSGUARDIANViewStatCacheSize_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheSize = _EipDNSGUARDIANViewStatCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 5),
    _EipDNSGUARDIANViewStatCacheSize_Type()
)
eipDNSGUARDIANViewStatCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheSize.setStatus("current")
_EipDNSGUARDIANViewStatSendDNSPacket_Type = Counter64
_EipDNSGUARDIANViewStatSendDNSPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatSendDNSPacket = _EipDNSGUARDIANViewStatSendDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 6),
    _EipDNSGUARDIANViewStatSendDNSPacket_Type()
)
eipDNSGUARDIANViewStatSendDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatSendDNSPacket.setStatus("current")
_EipDNSGUARDIANViewStatSendDNSByte_Type = Counter64
_EipDNSGUARDIANViewStatSendDNSByte_Object = MibTableColumn
eipDNSGUARDIANViewStatSendDNSByte = _EipDNSGUARDIANViewStatSendDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 7),
    _EipDNSGUARDIANViewStatSendDNSByte_Type()
)
eipDNSGUARDIANViewStatSendDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatSendDNSByte.setStatus("current")
_EipDNSGUARDIANViewStatRecvDNSPacket_Type = Counter64
_EipDNSGUARDIANViewStatRecvDNSPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvDNSPacket = _EipDNSGUARDIANViewStatRecvDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 8),
    _EipDNSGUARDIANViewStatRecvDNSPacket_Type()
)
eipDNSGUARDIANViewStatRecvDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvDNSPacket.setStatus("current")
_EipDNSGUARDIANViewStatRecvDNSByte_Type = Counter64
_EipDNSGUARDIANViewStatRecvDNSByte_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvDNSByte = _EipDNSGUARDIANViewStatRecvDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 9),
    _EipDNSGUARDIANViewStatRecvDNSByte_Type()
)
eipDNSGUARDIANViewStatRecvDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvDNSByte.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissExist_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissExist_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissExist = _EipDNSGUARDIANViewStatCacheMissExist_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 10),
    _EipDNSGUARDIANViewStatCacheMissExist_Type()
)
eipDNSGUARDIANViewStatCacheMissExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissExist.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissNotExist_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissNotExist_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissNotExist = _EipDNSGUARDIANViewStatCacheMissNotExist_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 11),
    _EipDNSGUARDIANViewStatCacheMissNotExist_Type()
)
eipDNSGUARDIANViewStatCacheMissNotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissNotExist.setStatus("current")
_EipDNSGUARDIANViewStatSendRescueDNSPacket_Type = Counter64
_EipDNSGUARDIANViewStatSendRescueDNSPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatSendRescueDNSPacket = _EipDNSGUARDIANViewStatSendRescueDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 12),
    _EipDNSGUARDIANViewStatSendRescueDNSPacket_Type()
)
eipDNSGUARDIANViewStatSendRescueDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatSendRescueDNSPacket.setStatus("current")
_EipDNSGUARDIANViewStatSendRescueDNSByte_Type = Counter64
_EipDNSGUARDIANViewStatSendRescueDNSByte_Object = MibTableColumn
eipDNSGUARDIANViewStatSendRescueDNSByte = _EipDNSGUARDIANViewStatSendRescueDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 13),
    _EipDNSGUARDIANViewStatSendRescueDNSByte_Type()
)
eipDNSGUARDIANViewStatSendRescueDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatSendRescueDNSByte.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidDNSPacket_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidDNSPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidDNSPacket = _EipDNSGUARDIANViewStatRecvInvalidDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 14),
    _EipDNSGUARDIANViewStatRecvInvalidDNSPacket_Type()
)
eipDNSGUARDIANViewStatRecvInvalidDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidDNSPacket.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidDNSByte_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidDNSByte_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidDNSByte = _EipDNSGUARDIANViewStatRecvInvalidDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 15),
    _EipDNSGUARDIANViewStatRecvInvalidDNSByte_Type()
)
eipDNSGUARDIANViewStatRecvInvalidDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidDNSByte.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidClass_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidClass_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidClass = _EipDNSGUARDIANViewStatRecvInvalidClass_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 16),
    _EipDNSGUARDIANViewStatRecvInvalidClass_Type()
)
eipDNSGUARDIANViewStatRecvInvalidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidClass.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidOverflow_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidOverflow_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidOverflow = _EipDNSGUARDIANViewStatRecvInvalidOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 17),
    _EipDNSGUARDIANViewStatRecvInvalidOverflow_Type()
)
eipDNSGUARDIANViewStatRecvInvalidOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidOverflow.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidEtherSource_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidEtherSource_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidEtherSource = _EipDNSGUARDIANViewStatRecvInvalidEtherSource_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 18),
    _EipDNSGUARDIANViewStatRecvInvalidEtherSource_Type()
)
eipDNSGUARDIANViewStatRecvInvalidEtherSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidEtherSource.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidUDPSource_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidUDPSource_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidUDPSource = _EipDNSGUARDIANViewStatRecvInvalidUDPSource_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 19),
    _EipDNSGUARDIANViewStatRecvInvalidUDPSource_Type()
)
eipDNSGUARDIANViewStatRecvInvalidUDPSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidUDPSource.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst = _EipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 20),
    _EipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst_Type()
)
eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidQDCount_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidQDCount_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidQDCount = _EipDNSGUARDIANViewStatRecvInvalidQDCount_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 21),
    _EipDNSGUARDIANViewStatRecvInvalidQDCount_Type()
)
eipDNSGUARDIANViewStatRecvInvalidQDCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidQDCount.setStatus("current")
_EipDNSGUARDIANViewStatRecvInvalidOPCode_Type = Counter64
_EipDNSGUARDIANViewStatRecvInvalidOPCode_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvInvalidOPCode = _EipDNSGUARDIANViewStatRecvInvalidOPCode_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 22),
    _EipDNSGUARDIANViewStatRecvInvalidOPCode_Type()
)
eipDNSGUARDIANViewStatRecvInvalidOPCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvInvalidOPCode.setStatus("current")
_EipDNSGUARDIANViewStatRecvSharedPacket_Type = Counter64
_EipDNSGUARDIANViewStatRecvSharedPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvSharedPacket = _EipDNSGUARDIANViewStatRecvSharedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 30),
    _EipDNSGUARDIANViewStatRecvSharedPacket_Type()
)
eipDNSGUARDIANViewStatRecvSharedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvSharedPacket.setStatus("current")
_EipDNSGUARDIANViewStatRecvSharedByte_Type = Counter64
_EipDNSGUARDIANViewStatRecvSharedByte_Object = MibTableColumn
eipDNSGUARDIANViewStatRecvSharedByte = _EipDNSGUARDIANViewStatRecvSharedByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 31),
    _EipDNSGUARDIANViewStatRecvSharedByte_Type()
)
eipDNSGUARDIANViewStatRecvSharedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRecvSharedByte.setStatus("current")
_EipDNSGUARDIANViewStatSendSharedPacket_Type = Counter64
_EipDNSGUARDIANViewStatSendSharedPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatSendSharedPacket = _EipDNSGUARDIANViewStatSendSharedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 32),
    _EipDNSGUARDIANViewStatSendSharedPacket_Type()
)
eipDNSGUARDIANViewStatSendSharedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatSendSharedPacket.setStatus("current")
_EipDNSGUARDIANViewStatSendSharedByte_Type = Counter64
_EipDNSGUARDIANViewStatSendSharedByte_Object = MibTableColumn
eipDNSGUARDIANViewStatSendSharedByte = _EipDNSGUARDIANViewStatSendSharedByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 33),
    _EipDNSGUARDIANViewStatSendSharedByte_Type()
)
eipDNSGUARDIANViewStatSendSharedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatSendSharedByte.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissQuarantine_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissQuarantine_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissQuarantine = _EipDNSGUARDIANViewStatCacheMissQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 34),
    _EipDNSGUARDIANViewStatCacheMissQuarantine_Type()
)
eipDNSGUARDIANViewStatCacheMissQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissQuarantine.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissExistQuarantine_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissExistQuarantine_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissExistQuarantine = _EipDNSGUARDIANViewStatCacheMissExistQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 35),
    _EipDNSGUARDIANViewStatCacheMissExistQuarantine_Type()
)
eipDNSGUARDIANViewStatCacheMissExistQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissExistQuarantine.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissNotExistQuarantine_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissNotExistQuarantine_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissNotExistQuarantine = _EipDNSGUARDIANViewStatCacheMissNotExistQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 36),
    _EipDNSGUARDIANViewStatCacheMissNotExistQuarantine_Type()
)
eipDNSGUARDIANViewStatCacheMissNotExistQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissNotExistQuarantine.setStatus("current")
_EipDNSGUARDIANViewStatCacheHitQuarantine_Type = Counter64
_EipDNSGUARDIANViewStatCacheHitQuarantine_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheHitQuarantine = _EipDNSGUARDIANViewStatCacheHitQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 37),
    _EipDNSGUARDIANViewStatCacheHitQuarantine_Type()
)
eipDNSGUARDIANViewStatCacheHitQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheHitQuarantine.setStatus("current")
_EipDNSGUARDIANViewStatQuarantineSendDNSPacket_Type = Counter64
_EipDNSGUARDIANViewStatQuarantineSendDNSPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatQuarantineSendDNSPacket = _EipDNSGUARDIANViewStatQuarantineSendDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 38),
    _EipDNSGUARDIANViewStatQuarantineSendDNSPacket_Type()
)
eipDNSGUARDIANViewStatQuarantineSendDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatQuarantineSendDNSPacket.setStatus("current")
_EipDNSGUARDIANViewStatQuarantineSendDNSByte_Type = Counter64
_EipDNSGUARDIANViewStatQuarantineSendDNSByte_Object = MibTableColumn
eipDNSGUARDIANViewStatQuarantineSendDNSByte = _EipDNSGUARDIANViewStatQuarantineSendDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 39),
    _EipDNSGUARDIANViewStatQuarantineSendDNSByte_Type()
)
eipDNSGUARDIANViewStatQuarantineSendDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatQuarantineSendDNSByte.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissRescue_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissRescue_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissRescue = _EipDNSGUARDIANViewStatCacheMissRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 40),
    _EipDNSGUARDIANViewStatCacheMissRescue_Type()
)
eipDNSGUARDIANViewStatCacheMissRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissRescue.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissExistRescue_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissExistRescue_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissExistRescue = _EipDNSGUARDIANViewStatCacheMissExistRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 41),
    _EipDNSGUARDIANViewStatCacheMissExistRescue_Type()
)
eipDNSGUARDIANViewStatCacheMissExistRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissExistRescue.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissNotExistRescue_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissNotExistRescue_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissNotExistRescue = _EipDNSGUARDIANViewStatCacheMissNotExistRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 42),
    _EipDNSGUARDIANViewStatCacheMissNotExistRescue_Type()
)
eipDNSGUARDIANViewStatCacheMissNotExistRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissNotExistRescue.setStatus("current")
_EipDNSGUARDIANViewStatCacheHitRescue_Type = Counter64
_EipDNSGUARDIANViewStatCacheHitRescue_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheHitRescue = _EipDNSGUARDIANViewStatCacheHitRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 43),
    _EipDNSGUARDIANViewStatCacheHitRescue_Type()
)
eipDNSGUARDIANViewStatCacheHitRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheHitRescue.setStatus("current")
_EipDNSGUARDIANViewStatBlockedQuery_Type = Counter64
_EipDNSGUARDIANViewStatBlockedQuery_Object = MibTableColumn
eipDNSGUARDIANViewStatBlockedQuery = _EipDNSGUARDIANViewStatBlockedQuery_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 44),
    _EipDNSGUARDIANViewStatBlockedQuery_Type()
)
eipDNSGUARDIANViewStatBlockedQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatBlockedQuery.setStatus("current")
_EipDNSGUARDIANViewStatRatelimitedQuery_Type = Counter64
_EipDNSGUARDIANViewStatRatelimitedQuery_Object = MibTableColumn
eipDNSGUARDIANViewStatRatelimitedQuery = _EipDNSGUARDIANViewStatRatelimitedQuery_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 47),
    _EipDNSGUARDIANViewStatRatelimitedQuery_Type()
)
eipDNSGUARDIANViewStatRatelimitedQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRatelimitedQuery.setStatus("current")
_EipDNSGUARDIANViewStatRTT10_Type = Counter64
_EipDNSGUARDIANViewStatRTT10_Object = MibTableColumn
eipDNSGUARDIANViewStatRTT10 = _EipDNSGUARDIANViewStatRTT10_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 48),
    _EipDNSGUARDIANViewStatRTT10_Type()
)
eipDNSGUARDIANViewStatRTT10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRTT10.setStatus("current")
_EipDNSGUARDIANViewStatRTT100_Type = Counter64
_EipDNSGUARDIANViewStatRTT100_Object = MibTableColumn
eipDNSGUARDIANViewStatRTT100 = _EipDNSGUARDIANViewStatRTT100_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 49),
    _EipDNSGUARDIANViewStatRTT100_Type()
)
eipDNSGUARDIANViewStatRTT100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRTT100.setStatus("current")
_EipDNSGUARDIANViewStatRTT500_Type = Counter64
_EipDNSGUARDIANViewStatRTT500_Object = MibTableColumn
eipDNSGUARDIANViewStatRTT500 = _EipDNSGUARDIANViewStatRTT500_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 50),
    _EipDNSGUARDIANViewStatRTT500_Type()
)
eipDNSGUARDIANViewStatRTT500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRTT500.setStatus("current")
_EipDNSGUARDIANViewStatRTT800_Type = Counter64
_EipDNSGUARDIANViewStatRTT800_Object = MibTableColumn
eipDNSGUARDIANViewStatRTT800 = _EipDNSGUARDIANViewStatRTT800_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 51),
    _EipDNSGUARDIANViewStatRTT800_Type()
)
eipDNSGUARDIANViewStatRTT800.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRTT800.setStatus("current")
_EipDNSGUARDIANViewStatRTT1600_Type = Counter64
_EipDNSGUARDIANViewStatRTT1600_Object = MibTableColumn
eipDNSGUARDIANViewStatRTT1600 = _EipDNSGUARDIANViewStatRTT1600_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 52),
    _EipDNSGUARDIANViewStatRTT1600_Type()
)
eipDNSGUARDIANViewStatRTT1600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRTT1600.setStatus("current")
_EipDNSGUARDIANViewStatRTTMax_Type = Counter64
_EipDNSGUARDIANViewStatRTTMax_Object = MibTableColumn
eipDNSGUARDIANViewStatRTTMax = _EipDNSGUARDIANViewStatRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 53),
    _EipDNSGUARDIANViewStatRTTMax_Type()
)
eipDNSGUARDIANViewStatRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatRTTMax.setStatus("current")
_EipDNSGUARDIANViewStatCacheMissQuarantineRedirect_Type = Counter64
_EipDNSGUARDIANViewStatCacheMissQuarantineRedirect_Object = MibTableColumn
eipDNSGUARDIANViewStatCacheMissQuarantineRedirect = _EipDNSGUARDIANViewStatCacheMissQuarantineRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 54),
    _EipDNSGUARDIANViewStatCacheMissQuarantineRedirect_Type()
)
eipDNSGUARDIANViewStatCacheMissQuarantineRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatCacheMissQuarantineRedirect.setStatus("current")
_EipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket_Type = Counter64
_EipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket_Object = MibTableColumn
eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket = _EipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 55),
    _EipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket_Type()
)
eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket.setStatus("current")
_EipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte_Type = Counter64
_EipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte_Object = MibTableColumn
eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte = _EipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 3, 1, 56),
    _EipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte_Type()
)
eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte.setStatus("current")
_EipDNSGUARDIANGlobalStat_ObjectIdentity = ObjectIdentity
eipDNSGUARDIANGlobalStat = _EipDNSGUARDIANGlobalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4)
)
_EipDNSGUARDIANStatCacheHit_Type = Counter64
_EipDNSGUARDIANStatCacheHit_Object = MibScalar
eipDNSGUARDIANStatCacheHit = _EipDNSGUARDIANStatCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 3),
    _EipDNSGUARDIANStatCacheHit_Type()
)
eipDNSGUARDIANStatCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheHit.setStatus("current")
_EipDNSGUARDIANStatCacheMiss_Type = Counter64
_EipDNSGUARDIANStatCacheMiss_Object = MibScalar
eipDNSGUARDIANStatCacheMiss = _EipDNSGUARDIANStatCacheMiss_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 4),
    _EipDNSGUARDIANStatCacheMiss_Type()
)
eipDNSGUARDIANStatCacheMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMiss.setStatus("current")
_EipDNSGUARDIANStatCacheSize_Type = Gauge32
_EipDNSGUARDIANStatCacheSize_Object = MibScalar
eipDNSGUARDIANStatCacheSize = _EipDNSGUARDIANStatCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 5),
    _EipDNSGUARDIANStatCacheSize_Type()
)
eipDNSGUARDIANStatCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheSize.setStatus("current")
_EipDNSGUARDIANStatSendDNSPacket_Type = Counter64
_EipDNSGUARDIANStatSendDNSPacket_Object = MibScalar
eipDNSGUARDIANStatSendDNSPacket = _EipDNSGUARDIANStatSendDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 6),
    _EipDNSGUARDIANStatSendDNSPacket_Type()
)
eipDNSGUARDIANStatSendDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatSendDNSPacket.setStatus("current")
_EipDNSGUARDIANStatSendDNSByte_Type = Counter64
_EipDNSGUARDIANStatSendDNSByte_Object = MibScalar
eipDNSGUARDIANStatSendDNSByte = _EipDNSGUARDIANStatSendDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 7),
    _EipDNSGUARDIANStatSendDNSByte_Type()
)
eipDNSGUARDIANStatSendDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatSendDNSByte.setStatus("current")
_EipDNSGUARDIANStatRecvDNSPacket_Type = Counter64
_EipDNSGUARDIANStatRecvDNSPacket_Object = MibScalar
eipDNSGUARDIANStatRecvDNSPacket = _EipDNSGUARDIANStatRecvDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 8),
    _EipDNSGUARDIANStatRecvDNSPacket_Type()
)
eipDNSGUARDIANStatRecvDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvDNSPacket.setStatus("current")
_EipDNSGUARDIANStatRecvDNSByte_Type = Counter64
_EipDNSGUARDIANStatRecvDNSByte_Object = MibScalar
eipDNSGUARDIANStatRecvDNSByte = _EipDNSGUARDIANStatRecvDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 9),
    _EipDNSGUARDIANStatRecvDNSByte_Type()
)
eipDNSGUARDIANStatRecvDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvDNSByte.setStatus("current")
_EipDNSGUARDIANStatCacheMissExist_Type = Counter64
_EipDNSGUARDIANStatCacheMissExist_Object = MibScalar
eipDNSGUARDIANStatCacheMissExist = _EipDNSGUARDIANStatCacheMissExist_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 10),
    _EipDNSGUARDIANStatCacheMissExist_Type()
)
eipDNSGUARDIANStatCacheMissExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissExist.setStatus("current")
_EipDNSGUARDIANStatCacheMissNotExist_Type = Counter64
_EipDNSGUARDIANStatCacheMissNotExist_Object = MibScalar
eipDNSGUARDIANStatCacheMissNotExist = _EipDNSGUARDIANStatCacheMissNotExist_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 11),
    _EipDNSGUARDIANStatCacheMissNotExist_Type()
)
eipDNSGUARDIANStatCacheMissNotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissNotExist.setStatus("current")
_EipDNSGUARDIANStatSendRescueDNSPacket_Type = Counter64
_EipDNSGUARDIANStatSendRescueDNSPacket_Object = MibScalar
eipDNSGUARDIANStatSendRescueDNSPacket = _EipDNSGUARDIANStatSendRescueDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 12),
    _EipDNSGUARDIANStatSendRescueDNSPacket_Type()
)
eipDNSGUARDIANStatSendRescueDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatSendRescueDNSPacket.setStatus("current")
_EipDNSGUARDIANStatSendRescueDNSByte_Type = Counter64
_EipDNSGUARDIANStatSendRescueDNSByte_Object = MibScalar
eipDNSGUARDIANStatSendRescueDNSByte = _EipDNSGUARDIANStatSendRescueDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 13),
    _EipDNSGUARDIANStatSendRescueDNSByte_Type()
)
eipDNSGUARDIANStatSendRescueDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatSendRescueDNSByte.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidDNSPacket_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidDNSPacket_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidDNSPacket = _EipDNSGUARDIANStatRecvInvalidDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 14),
    _EipDNSGUARDIANStatRecvInvalidDNSPacket_Type()
)
eipDNSGUARDIANStatRecvInvalidDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidDNSPacket.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidDNSByte_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidDNSByte_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidDNSByte = _EipDNSGUARDIANStatRecvInvalidDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 15),
    _EipDNSGUARDIANStatRecvInvalidDNSByte_Type()
)
eipDNSGUARDIANStatRecvInvalidDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidDNSByte.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidClass_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidClass_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidClass = _EipDNSGUARDIANStatRecvInvalidClass_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 16),
    _EipDNSGUARDIANStatRecvInvalidClass_Type()
)
eipDNSGUARDIANStatRecvInvalidClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidClass.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidOverflow_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidOverflow_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidOverflow = _EipDNSGUARDIANStatRecvInvalidOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 17),
    _EipDNSGUARDIANStatRecvInvalidOverflow_Type()
)
eipDNSGUARDIANStatRecvInvalidOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidOverflow.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidEtherSource_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidEtherSource_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidEtherSource = _EipDNSGUARDIANStatRecvInvalidEtherSource_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 18),
    _EipDNSGUARDIANStatRecvInvalidEtherSource_Type()
)
eipDNSGUARDIANStatRecvInvalidEtherSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidEtherSource.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidUDPSource_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidUDPSource_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidUDPSource = _EipDNSGUARDIANStatRecvInvalidUDPSource_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 19),
    _EipDNSGUARDIANStatRecvInvalidUDPSource_Type()
)
eipDNSGUARDIANStatRecvInvalidUDPSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidUDPSource.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidIPSrcEqDst_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidIPSrcEqDst_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidIPSrcEqDst = _EipDNSGUARDIANStatRecvInvalidIPSrcEqDst_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 20),
    _EipDNSGUARDIANStatRecvInvalidIPSrcEqDst_Type()
)
eipDNSGUARDIANStatRecvInvalidIPSrcEqDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidIPSrcEqDst.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidQDCount_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidQDCount_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidQDCount = _EipDNSGUARDIANStatRecvInvalidQDCount_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 21),
    _EipDNSGUARDIANStatRecvInvalidQDCount_Type()
)
eipDNSGUARDIANStatRecvInvalidQDCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidQDCount.setStatus("current")
_EipDNSGUARDIANStatRecvInvalidOPCode_Type = Counter64
_EipDNSGUARDIANStatRecvInvalidOPCode_Object = MibScalar
eipDNSGUARDIANStatRecvInvalidOPCode = _EipDNSGUARDIANStatRecvInvalidOPCode_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 22),
    _EipDNSGUARDIANStatRecvInvalidOPCode_Type()
)
eipDNSGUARDIANStatRecvInvalidOPCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvInvalidOPCode.setStatus("current")
_EipDNSGUARDIANStatRecvSharedPacket_Type = Counter64
_EipDNSGUARDIANStatRecvSharedPacket_Object = MibScalar
eipDNSGUARDIANStatRecvSharedPacket = _EipDNSGUARDIANStatRecvSharedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 30),
    _EipDNSGUARDIANStatRecvSharedPacket_Type()
)
eipDNSGUARDIANStatRecvSharedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvSharedPacket.setStatus("current")
_EipDNSGUARDIANStatRecvSharedByte_Type = Counter64
_EipDNSGUARDIANStatRecvSharedByte_Object = MibScalar
eipDNSGUARDIANStatRecvSharedByte = _EipDNSGUARDIANStatRecvSharedByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 31),
    _EipDNSGUARDIANStatRecvSharedByte_Type()
)
eipDNSGUARDIANStatRecvSharedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRecvSharedByte.setStatus("current")
_EipDNSGUARDIANStatSendSharedPacket_Type = Counter64
_EipDNSGUARDIANStatSendSharedPacket_Object = MibScalar
eipDNSGUARDIANStatSendSharedPacket = _EipDNSGUARDIANStatSendSharedPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 32),
    _EipDNSGUARDIANStatSendSharedPacket_Type()
)
eipDNSGUARDIANStatSendSharedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatSendSharedPacket.setStatus("current")
_EipDNSGUARDIANStatSendSharedByte_Type = Counter64
_EipDNSGUARDIANStatSendSharedByte_Object = MibScalar
eipDNSGUARDIANStatSendSharedByte = _EipDNSGUARDIANStatSendSharedByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 33),
    _EipDNSGUARDIANStatSendSharedByte_Type()
)
eipDNSGUARDIANStatSendSharedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatSendSharedByte.setStatus("current")
_EipDNSGUARDIANStatCacheMissQuarantine_Type = Counter64
_EipDNSGUARDIANStatCacheMissQuarantine_Object = MibScalar
eipDNSGUARDIANStatCacheMissQuarantine = _EipDNSGUARDIANStatCacheMissQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 34),
    _EipDNSGUARDIANStatCacheMissQuarantine_Type()
)
eipDNSGUARDIANStatCacheMissQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissQuarantine.setStatus("current")
_EipDNSGUARDIANStatCacheMissExistQuarantine_Type = Counter64
_EipDNSGUARDIANStatCacheMissExistQuarantine_Object = MibScalar
eipDNSGUARDIANStatCacheMissExistQuarantine = _EipDNSGUARDIANStatCacheMissExistQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 35),
    _EipDNSGUARDIANStatCacheMissExistQuarantine_Type()
)
eipDNSGUARDIANStatCacheMissExistQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissExistQuarantine.setStatus("current")
_EipDNSGUARDIANStatCacheMissNotExistQuarantine_Type = Counter64
_EipDNSGUARDIANStatCacheMissNotExistQuarantine_Object = MibScalar
eipDNSGUARDIANStatCacheMissNotExistQuarantine = _EipDNSGUARDIANStatCacheMissNotExistQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 36),
    _EipDNSGUARDIANStatCacheMissNotExistQuarantine_Type()
)
eipDNSGUARDIANStatCacheMissNotExistQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissNotExistQuarantine.setStatus("current")
_EipDNSGUARDIANStatCacheHitQuarantine_Type = Counter64
_EipDNSGUARDIANStatCacheHitQuarantine_Object = MibScalar
eipDNSGUARDIANStatCacheHitQuarantine = _EipDNSGUARDIANStatCacheHitQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 37),
    _EipDNSGUARDIANStatCacheHitQuarantine_Type()
)
eipDNSGUARDIANStatCacheHitQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheHitQuarantine.setStatus("current")
_EipDNSGUARDIANStatQuarantineSendDNSPacket_Type = Counter64
_EipDNSGUARDIANStatQuarantineSendDNSPacket_Object = MibScalar
eipDNSGUARDIANStatQuarantineSendDNSPacket = _EipDNSGUARDIANStatQuarantineSendDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 38),
    _EipDNSGUARDIANStatQuarantineSendDNSPacket_Type()
)
eipDNSGUARDIANStatQuarantineSendDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatQuarantineSendDNSPacket.setStatus("current")
_EipDNSGUARDIANStatQuarantineSendDNSByte_Type = Counter64
_EipDNSGUARDIANStatQuarantineSendDNSByte_Object = MibScalar
eipDNSGUARDIANStatQuarantineSendDNSByte = _EipDNSGUARDIANStatQuarantineSendDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 39),
    _EipDNSGUARDIANStatQuarantineSendDNSByte_Type()
)
eipDNSGUARDIANStatQuarantineSendDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatQuarantineSendDNSByte.setStatus("current")
_EipDNSGUARDIANStatCacheMissRescue_Type = Counter64
_EipDNSGUARDIANStatCacheMissRescue_Object = MibScalar
eipDNSGUARDIANStatCacheMissRescue = _EipDNSGUARDIANStatCacheMissRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 40),
    _EipDNSGUARDIANStatCacheMissRescue_Type()
)
eipDNSGUARDIANStatCacheMissRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissRescue.setStatus("current")
_EipDNSGUARDIANStatCacheMissExistRescue_Type = Counter64
_EipDNSGUARDIANStatCacheMissExistRescue_Object = MibScalar
eipDNSGUARDIANStatCacheMissExistRescue = _EipDNSGUARDIANStatCacheMissExistRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 41),
    _EipDNSGUARDIANStatCacheMissExistRescue_Type()
)
eipDNSGUARDIANStatCacheMissExistRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissExistRescue.setStatus("current")
_EipDNSGUARDIANStatCacheMissNotExistRescue_Type = Counter64
_EipDNSGUARDIANStatCacheMissNotExistRescue_Object = MibScalar
eipDNSGUARDIANStatCacheMissNotExistRescue = _EipDNSGUARDIANStatCacheMissNotExistRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 42),
    _EipDNSGUARDIANStatCacheMissNotExistRescue_Type()
)
eipDNSGUARDIANStatCacheMissNotExistRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissNotExistRescue.setStatus("current")
_EipDNSGUARDIANStatCacheHitRescue_Type = Counter64
_EipDNSGUARDIANStatCacheHitRescue_Object = MibScalar
eipDNSGUARDIANStatCacheHitRescue = _EipDNSGUARDIANStatCacheHitRescue_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 43),
    _EipDNSGUARDIANStatCacheHitRescue_Type()
)
eipDNSGUARDIANStatCacheHitRescue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheHitRescue.setStatus("current")
_EipDNSGUARDIANStatBlockedQuery_Type = Counter64
_EipDNSGUARDIANStatBlockedQuery_Object = MibScalar
eipDNSGUARDIANStatBlockedQuery = _EipDNSGUARDIANStatBlockedQuery_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 44),
    _EipDNSGUARDIANStatBlockedQuery_Type()
)
eipDNSGUARDIANStatBlockedQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatBlockedQuery.setStatus("current")
_EipDNSGUARDIANStatClientsSize_Type = Gauge32
_EipDNSGUARDIANStatClientsSize_Object = MibScalar
eipDNSGUARDIANStatClientsSize = _EipDNSGUARDIANStatClientsSize_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 45),
    _EipDNSGUARDIANStatClientsSize_Type()
)
eipDNSGUARDIANStatClientsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatClientsSize.setStatus("current")
_EipDNSGUARDIANStatClientsUpdated_Type = Counter64
_EipDNSGUARDIANStatClientsUpdated_Object = MibScalar
eipDNSGUARDIANStatClientsUpdated = _EipDNSGUARDIANStatClientsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 46),
    _EipDNSGUARDIANStatClientsUpdated_Type()
)
eipDNSGUARDIANStatClientsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatClientsUpdated.setStatus("current")
_EipDNSGUARDIANStatRatelimitedQuery_Type = Counter64
_EipDNSGUARDIANStatRatelimitedQuery_Object = MibScalar
eipDNSGUARDIANStatRatelimitedQuery = _EipDNSGUARDIANStatRatelimitedQuery_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 47),
    _EipDNSGUARDIANStatRatelimitedQuery_Type()
)
eipDNSGUARDIANStatRatelimitedQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRatelimitedQuery.setStatus("current")
_EipDNSGUARDIANStatRTT10_Type = Counter64
_EipDNSGUARDIANStatRTT10_Object = MibScalar
eipDNSGUARDIANStatRTT10 = _EipDNSGUARDIANStatRTT10_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 48),
    _EipDNSGUARDIANStatRTT10_Type()
)
eipDNSGUARDIANStatRTT10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRTT10.setStatus("current")
_EipDNSGUARDIANStatRTT100_Type = Counter64
_EipDNSGUARDIANStatRTT100_Object = MibScalar
eipDNSGUARDIANStatRTT100 = _EipDNSGUARDIANStatRTT100_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 49),
    _EipDNSGUARDIANStatRTT100_Type()
)
eipDNSGUARDIANStatRTT100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRTT100.setStatus("current")
_EipDNSGUARDIANStatRTT500_Type = Counter64
_EipDNSGUARDIANStatRTT500_Object = MibScalar
eipDNSGUARDIANStatRTT500 = _EipDNSGUARDIANStatRTT500_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 50),
    _EipDNSGUARDIANStatRTT500_Type()
)
eipDNSGUARDIANStatRTT500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRTT500.setStatus("current")
_EipDNSGUARDIANStatRTT800_Type = Counter64
_EipDNSGUARDIANStatRTT800_Object = MibScalar
eipDNSGUARDIANStatRTT800 = _EipDNSGUARDIANStatRTT800_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 51),
    _EipDNSGUARDIANStatRTT800_Type()
)
eipDNSGUARDIANStatRTT800.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRTT800.setStatus("current")
_EipDNSGUARDIANStatRTT1600_Type = Counter64
_EipDNSGUARDIANStatRTT1600_Object = MibScalar
eipDNSGUARDIANStatRTT1600 = _EipDNSGUARDIANStatRTT1600_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 52),
    _EipDNSGUARDIANStatRTT1600_Type()
)
eipDNSGUARDIANStatRTT1600.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRTT1600.setStatus("current")
_EipDNSGUARDIANStatRTTMax_Type = Counter64
_EipDNSGUARDIANStatRTTMax_Object = MibScalar
eipDNSGUARDIANStatRTTMax = _EipDNSGUARDIANStatRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 53),
    _EipDNSGUARDIANStatRTTMax_Type()
)
eipDNSGUARDIANStatRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatRTTMax.setStatus("current")
_EipDNSGUARDIANStatCacheMissQuarantineRedirect_Type = Counter64
_EipDNSGUARDIANStatCacheMissQuarantineRedirect_Object = MibScalar
eipDNSGUARDIANStatCacheMissQuarantineRedirect = _EipDNSGUARDIANStatCacheMissQuarantineRedirect_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 54),
    _EipDNSGUARDIANStatCacheMissQuarantineRedirect_Type()
)
eipDNSGUARDIANStatCacheMissQuarantineRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatCacheMissQuarantineRedirect.setStatus("current")
_EipDNSGUARDIANStatQuarantineRedirectSendDNSPacket_Type = Counter64
_EipDNSGUARDIANStatQuarantineRedirectSendDNSPacket_Object = MibScalar
eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket = _EipDNSGUARDIANStatQuarantineRedirectSendDNSPacket_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 55),
    _EipDNSGUARDIANStatQuarantineRedirectSendDNSPacket_Type()
)
eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket.setStatus("current")
_EipDNSGUARDIANStatQuarantineRedirectSendDNSByte_Type = Counter64
_EipDNSGUARDIANStatQuarantineRedirectSendDNSByte_Object = MibScalar
eipDNSGUARDIANStatQuarantineRedirectSendDNSByte = _EipDNSGUARDIANStatQuarantineRedirectSendDNSByte_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 56),
    _EipDNSGUARDIANStatQuarantineRedirectSendDNSByte_Type()
)
eipDNSGUARDIANStatQuarantineRedirectSendDNSByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatQuarantineRedirectSendDNSByte.setStatus("current")
_EipDNSGUARDIANStatReplyNOERROR_Type = Counter64
_EipDNSGUARDIANStatReplyNOERROR_Object = MibScalar
eipDNSGUARDIANStatReplyNOERROR = _EipDNSGUARDIANStatReplyNOERROR_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 101),
    _EipDNSGUARDIANStatReplyNOERROR_Type()
)
eipDNSGUARDIANStatReplyNOERROR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyNOERROR.setStatus("current")
_EipDNSGUARDIANStatReplyFORMERR_Type = Counter64
_EipDNSGUARDIANStatReplyFORMERR_Object = MibScalar
eipDNSGUARDIANStatReplyFORMERR = _EipDNSGUARDIANStatReplyFORMERR_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 102),
    _EipDNSGUARDIANStatReplyFORMERR_Type()
)
eipDNSGUARDIANStatReplyFORMERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyFORMERR.setStatus("current")
_EipDNSGUARDIANStatReplySERVFAIL_Type = Counter64
_EipDNSGUARDIANStatReplySERVFAIL_Object = MibScalar
eipDNSGUARDIANStatReplySERVFAIL = _EipDNSGUARDIANStatReplySERVFAIL_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 103),
    _EipDNSGUARDIANStatReplySERVFAIL_Type()
)
eipDNSGUARDIANStatReplySERVFAIL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplySERVFAIL.setStatus("current")
_EipDNSGUARDIANStatReplyNXDOMAIN_Type = Counter64
_EipDNSGUARDIANStatReplyNXDOMAIN_Object = MibScalar
eipDNSGUARDIANStatReplyNXDOMAIN = _EipDNSGUARDIANStatReplyNXDOMAIN_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 104),
    _EipDNSGUARDIANStatReplyNXDOMAIN_Type()
)
eipDNSGUARDIANStatReplyNXDOMAIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyNXDOMAIN.setStatus("current")
_EipDNSGUARDIANStatReplyNOTIMP_Type = Counter64
_EipDNSGUARDIANStatReplyNOTIMP_Object = MibScalar
eipDNSGUARDIANStatReplyNOTIMP = _EipDNSGUARDIANStatReplyNOTIMP_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 105),
    _EipDNSGUARDIANStatReplyNOTIMP_Type()
)
eipDNSGUARDIANStatReplyNOTIMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyNOTIMP.setStatus("current")
_EipDNSGUARDIANStatReplyREFUSED_Type = Counter64
_EipDNSGUARDIANStatReplyREFUSED_Object = MibScalar
eipDNSGUARDIANStatReplyREFUSED = _EipDNSGUARDIANStatReplyREFUSED_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 106),
    _EipDNSGUARDIANStatReplyREFUSED_Type()
)
eipDNSGUARDIANStatReplyREFUSED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyREFUSED.setStatus("current")
_EipDNSGUARDIANStatReplyYXDOMAIN_Type = Counter64
_EipDNSGUARDIANStatReplyYXDOMAIN_Object = MibScalar
eipDNSGUARDIANStatReplyYXDOMAIN = _EipDNSGUARDIANStatReplyYXDOMAIN_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 107),
    _EipDNSGUARDIANStatReplyYXDOMAIN_Type()
)
eipDNSGUARDIANStatReplyYXDOMAIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyYXDOMAIN.setStatus("current")
_EipDNSGUARDIANStatReplyYXRRSET_Type = Counter64
_EipDNSGUARDIANStatReplyYXRRSET_Object = MibScalar
eipDNSGUARDIANStatReplyYXRRSET = _EipDNSGUARDIANStatReplyYXRRSET_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 108),
    _EipDNSGUARDIANStatReplyYXRRSET_Type()
)
eipDNSGUARDIANStatReplyYXRRSET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyYXRRSET.setStatus("current")
_EipDNSGUARDIANStatReplyNXRRSET_Type = Counter64
_EipDNSGUARDIANStatReplyNXRRSET_Object = MibScalar
eipDNSGUARDIANStatReplyNXRRSET = _EipDNSGUARDIANStatReplyNXRRSET_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 109),
    _EipDNSGUARDIANStatReplyNXRRSET_Type()
)
eipDNSGUARDIANStatReplyNXRRSET.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyNXRRSET.setStatus("current")
_EipDNSGUARDIANStatReplyNOTAUTH_Type = Counter64
_EipDNSGUARDIANStatReplyNOTAUTH_Object = MibScalar
eipDNSGUARDIANStatReplyNOTAUTH = _EipDNSGUARDIANStatReplyNOTAUTH_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 120),
    _EipDNSGUARDIANStatReplyNOTAUTH_Type()
)
eipDNSGUARDIANStatReplyNOTAUTH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyNOTAUTH.setStatus("current")
_EipDNSGUARDIANStatReplyNOTZONE_Type = Counter64
_EipDNSGUARDIANStatReplyNOTZONE_Object = MibScalar
eipDNSGUARDIANStatReplyNOTZONE = _EipDNSGUARDIANStatReplyNOTZONE_Object(
    (1, 3, 6, 1, 4, 1, 2440, 1, 11, 2, 4, 121),
    _EipDNSGUARDIANStatReplyNOTZONE_Type()
)
eipDNSGUARDIANStatReplyNOTZONE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eipDNSGUARDIANStatReplyNOTZONE.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EIP-DNSBLAST-MIB",
    **{"eip": eip,
       "products": products,
       "eipDNSGUARDIAN": eipDNSGUARDIAN,
       "eipDNSGUARDIANStat": eipDNSGUARDIANStat,
       "eipDNSGUARDIANViewStatTable": eipDNSGUARDIANViewStatTable,
       "eipDNSGUARDIANViewStatEntry": eipDNSGUARDIANViewStatEntry,
       "eipDNSGUARDIANViewStatViewID": eipDNSGUARDIANViewStatViewID,
       "eipDNSGUARDIANViewStatViewName": eipDNSGUARDIANViewStatViewName,
       "eipDNSGUARDIANViewStatCacheHit": eipDNSGUARDIANViewStatCacheHit,
       "eipDNSGUARDIANViewStatCacheMiss": eipDNSGUARDIANViewStatCacheMiss,
       "eipDNSGUARDIANViewStatCacheSize": eipDNSGUARDIANViewStatCacheSize,
       "eipDNSGUARDIANViewStatSendDNSPacket": eipDNSGUARDIANViewStatSendDNSPacket,
       "eipDNSGUARDIANViewStatSendDNSByte": eipDNSGUARDIANViewStatSendDNSByte,
       "eipDNSGUARDIANViewStatRecvDNSPacket": eipDNSGUARDIANViewStatRecvDNSPacket,
       "eipDNSGUARDIANViewStatRecvDNSByte": eipDNSGUARDIANViewStatRecvDNSByte,
       "eipDNSGUARDIANViewStatCacheMissExist": eipDNSGUARDIANViewStatCacheMissExist,
       "eipDNSGUARDIANViewStatCacheMissNotExist": eipDNSGUARDIANViewStatCacheMissNotExist,
       "eipDNSGUARDIANViewStatSendRescueDNSPacket": eipDNSGUARDIANViewStatSendRescueDNSPacket,
       "eipDNSGUARDIANViewStatSendRescueDNSByte": eipDNSGUARDIANViewStatSendRescueDNSByte,
       "eipDNSGUARDIANViewStatRecvInvalidDNSPacket": eipDNSGUARDIANViewStatRecvInvalidDNSPacket,
       "eipDNSGUARDIANViewStatRecvInvalidDNSByte": eipDNSGUARDIANViewStatRecvInvalidDNSByte,
       "eipDNSGUARDIANViewStatRecvInvalidClass": eipDNSGUARDIANViewStatRecvInvalidClass,
       "eipDNSGUARDIANViewStatRecvInvalidOverflow": eipDNSGUARDIANViewStatRecvInvalidOverflow,
       "eipDNSGUARDIANViewStatRecvInvalidEtherSource": eipDNSGUARDIANViewStatRecvInvalidEtherSource,
       "eipDNSGUARDIANViewStatRecvInvalidUDPSource": eipDNSGUARDIANViewStatRecvInvalidUDPSource,
       "eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst": eipDNSGUARDIANViewStatRecvInvalidIPSrcEqDst,
       "eipDNSGUARDIANViewStatRecvInvalidQDCount": eipDNSGUARDIANViewStatRecvInvalidQDCount,
       "eipDNSGUARDIANViewStatRecvInvalidOPCode": eipDNSGUARDIANViewStatRecvInvalidOPCode,
       "eipDNSGUARDIANViewStatRecvSharedPacket": eipDNSGUARDIANViewStatRecvSharedPacket,
       "eipDNSGUARDIANViewStatRecvSharedByte": eipDNSGUARDIANViewStatRecvSharedByte,
       "eipDNSGUARDIANViewStatSendSharedPacket": eipDNSGUARDIANViewStatSendSharedPacket,
       "eipDNSGUARDIANViewStatSendSharedByte": eipDNSGUARDIANViewStatSendSharedByte,
       "eipDNSGUARDIANViewStatCacheMissQuarantine": eipDNSGUARDIANViewStatCacheMissQuarantine,
       "eipDNSGUARDIANViewStatCacheMissExistQuarantine": eipDNSGUARDIANViewStatCacheMissExistQuarantine,
       "eipDNSGUARDIANViewStatCacheMissNotExistQuarantine": eipDNSGUARDIANViewStatCacheMissNotExistQuarantine,
       "eipDNSGUARDIANViewStatCacheHitQuarantine": eipDNSGUARDIANViewStatCacheHitQuarantine,
       "eipDNSGUARDIANViewStatQuarantineSendDNSPacket": eipDNSGUARDIANViewStatQuarantineSendDNSPacket,
       "eipDNSGUARDIANViewStatQuarantineSendDNSByte": eipDNSGUARDIANViewStatQuarantineSendDNSByte,
       "eipDNSGUARDIANViewStatCacheMissRescue": eipDNSGUARDIANViewStatCacheMissRescue,
       "eipDNSGUARDIANViewStatCacheMissExistRescue": eipDNSGUARDIANViewStatCacheMissExistRescue,
       "eipDNSGUARDIANViewStatCacheMissNotExistRescue": eipDNSGUARDIANViewStatCacheMissNotExistRescue,
       "eipDNSGUARDIANViewStatCacheHitRescue": eipDNSGUARDIANViewStatCacheHitRescue,
       "eipDNSGUARDIANViewStatBlockedQuery": eipDNSGUARDIANViewStatBlockedQuery,
       "eipDNSGUARDIANViewStatRatelimitedQuery": eipDNSGUARDIANViewStatRatelimitedQuery,
       "eipDNSGUARDIANViewStatRTT10": eipDNSGUARDIANViewStatRTT10,
       "eipDNSGUARDIANViewStatRTT100": eipDNSGUARDIANViewStatRTT100,
       "eipDNSGUARDIANViewStatRTT500": eipDNSGUARDIANViewStatRTT500,
       "eipDNSGUARDIANViewStatRTT800": eipDNSGUARDIANViewStatRTT800,
       "eipDNSGUARDIANViewStatRTT1600": eipDNSGUARDIANViewStatRTT1600,
       "eipDNSGUARDIANViewStatRTTMax": eipDNSGUARDIANViewStatRTTMax,
       "eipDNSGUARDIANViewStatCacheMissQuarantineRedirect": eipDNSGUARDIANViewStatCacheMissQuarantineRedirect,
       "eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket": eipDNSGUARDIANViewStatQuarantineRedirectSendDNSPacket,
       "eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte": eipDNSGUARDIANViewStatQuarantineRedirectSendDNSByte,
       "eipDNSGUARDIANGlobalStat": eipDNSGUARDIANGlobalStat,
       "eipDNSGUARDIANStatCacheHit": eipDNSGUARDIANStatCacheHit,
       "eipDNSGUARDIANStatCacheMiss": eipDNSGUARDIANStatCacheMiss,
       "eipDNSGUARDIANStatCacheSize": eipDNSGUARDIANStatCacheSize,
       "eipDNSGUARDIANStatSendDNSPacket": eipDNSGUARDIANStatSendDNSPacket,
       "eipDNSGUARDIANStatSendDNSByte": eipDNSGUARDIANStatSendDNSByte,
       "eipDNSGUARDIANStatRecvDNSPacket": eipDNSGUARDIANStatRecvDNSPacket,
       "eipDNSGUARDIANStatRecvDNSByte": eipDNSGUARDIANStatRecvDNSByte,
       "eipDNSGUARDIANStatCacheMissExist": eipDNSGUARDIANStatCacheMissExist,
       "eipDNSGUARDIANStatCacheMissNotExist": eipDNSGUARDIANStatCacheMissNotExist,
       "eipDNSGUARDIANStatSendRescueDNSPacket": eipDNSGUARDIANStatSendRescueDNSPacket,
       "eipDNSGUARDIANStatSendRescueDNSByte": eipDNSGUARDIANStatSendRescueDNSByte,
       "eipDNSGUARDIANStatRecvInvalidDNSPacket": eipDNSGUARDIANStatRecvInvalidDNSPacket,
       "eipDNSGUARDIANStatRecvInvalidDNSByte": eipDNSGUARDIANStatRecvInvalidDNSByte,
       "eipDNSGUARDIANStatRecvInvalidClass": eipDNSGUARDIANStatRecvInvalidClass,
       "eipDNSGUARDIANStatRecvInvalidOverflow": eipDNSGUARDIANStatRecvInvalidOverflow,
       "eipDNSGUARDIANStatRecvInvalidEtherSource": eipDNSGUARDIANStatRecvInvalidEtherSource,
       "eipDNSGUARDIANStatRecvInvalidUDPSource": eipDNSGUARDIANStatRecvInvalidUDPSource,
       "eipDNSGUARDIANStatRecvInvalidIPSrcEqDst": eipDNSGUARDIANStatRecvInvalidIPSrcEqDst,
       "eipDNSGUARDIANStatRecvInvalidQDCount": eipDNSGUARDIANStatRecvInvalidQDCount,
       "eipDNSGUARDIANStatRecvInvalidOPCode": eipDNSGUARDIANStatRecvInvalidOPCode,
       "eipDNSGUARDIANStatRecvSharedPacket": eipDNSGUARDIANStatRecvSharedPacket,
       "eipDNSGUARDIANStatRecvSharedByte": eipDNSGUARDIANStatRecvSharedByte,
       "eipDNSGUARDIANStatSendSharedPacket": eipDNSGUARDIANStatSendSharedPacket,
       "eipDNSGUARDIANStatSendSharedByte": eipDNSGUARDIANStatSendSharedByte,
       "eipDNSGUARDIANStatCacheMissQuarantine": eipDNSGUARDIANStatCacheMissQuarantine,
       "eipDNSGUARDIANStatCacheMissExistQuarantine": eipDNSGUARDIANStatCacheMissExistQuarantine,
       "eipDNSGUARDIANStatCacheMissNotExistQuarantine": eipDNSGUARDIANStatCacheMissNotExistQuarantine,
       "eipDNSGUARDIANStatCacheHitQuarantine": eipDNSGUARDIANStatCacheHitQuarantine,
       "eipDNSGUARDIANStatQuarantineSendDNSPacket": eipDNSGUARDIANStatQuarantineSendDNSPacket,
       "eipDNSGUARDIANStatQuarantineSendDNSByte": eipDNSGUARDIANStatQuarantineSendDNSByte,
       "eipDNSGUARDIANStatCacheMissRescue": eipDNSGUARDIANStatCacheMissRescue,
       "eipDNSGUARDIANStatCacheMissExistRescue": eipDNSGUARDIANStatCacheMissExistRescue,
       "eipDNSGUARDIANStatCacheMissNotExistRescue": eipDNSGUARDIANStatCacheMissNotExistRescue,
       "eipDNSGUARDIANStatCacheHitRescue": eipDNSGUARDIANStatCacheHitRescue,
       "eipDNSGUARDIANStatBlockedQuery": eipDNSGUARDIANStatBlockedQuery,
       "eipDNSGUARDIANStatClientsSize": eipDNSGUARDIANStatClientsSize,
       "eipDNSGUARDIANStatClientsUpdated": eipDNSGUARDIANStatClientsUpdated,
       "eipDNSGUARDIANStatRatelimitedQuery": eipDNSGUARDIANStatRatelimitedQuery,
       "eipDNSGUARDIANStatRTT10": eipDNSGUARDIANStatRTT10,
       "eipDNSGUARDIANStatRTT100": eipDNSGUARDIANStatRTT100,
       "eipDNSGUARDIANStatRTT500": eipDNSGUARDIANStatRTT500,
       "eipDNSGUARDIANStatRTT800": eipDNSGUARDIANStatRTT800,
       "eipDNSGUARDIANStatRTT1600": eipDNSGUARDIANStatRTT1600,
       "eipDNSGUARDIANStatRTTMax": eipDNSGUARDIANStatRTTMax,
       "eipDNSGUARDIANStatCacheMissQuarantineRedirect": eipDNSGUARDIANStatCacheMissQuarantineRedirect,
       "eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket": eipDNSGUARDIANStatQuarantineRedirectSendDNSPacket,
       "eipDNSGUARDIANStatQuarantineRedirectSendDNSByte": eipDNSGUARDIANStatQuarantineRedirectSendDNSByte,
       "eipDNSGUARDIANStatReplyNOERROR": eipDNSGUARDIANStatReplyNOERROR,
       "eipDNSGUARDIANStatReplyFORMERR": eipDNSGUARDIANStatReplyFORMERR,
       "eipDNSGUARDIANStatReplySERVFAIL": eipDNSGUARDIANStatReplySERVFAIL,
       "eipDNSGUARDIANStatReplyNXDOMAIN": eipDNSGUARDIANStatReplyNXDOMAIN,
       "eipDNSGUARDIANStatReplyNOTIMP": eipDNSGUARDIANStatReplyNOTIMP,
       "eipDNSGUARDIANStatReplyREFUSED": eipDNSGUARDIANStatReplyREFUSED,
       "eipDNSGUARDIANStatReplyYXDOMAIN": eipDNSGUARDIANStatReplyYXDOMAIN,
       "eipDNSGUARDIANStatReplyYXRRSET": eipDNSGUARDIANStatReplyYXRRSET,
       "eipDNSGUARDIANStatReplyNXRRSET": eipDNSGUARDIANStatReplyNXRRSET,
       "eipDNSGUARDIANStatReplyNOTAUTH": eipDNSGUARDIANStatReplyNOTAUTH,
       "eipDNSGUARDIANStatReplyNOTZONE": eipDNSGUARDIANStatReplyNOTZONE}
)
