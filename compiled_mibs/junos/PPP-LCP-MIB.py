# SNMP MIB module (PPP-LCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\PPP-LCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:20 2025
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pppLcp = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1)
)
if mibBuilder.loadTexts:
    pppLcp.setRevisions(
        ("2003-09-17 20:59",
         "1993-06-01 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23)
)
_PppLink_ObjectIdentity = ObjectIdentity
pppLink = _PppLink_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1)
)
_PppLinkStatusTable_Object = MibTable
pppLinkStatusTable = _PppLinkStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pppLinkStatusTable.setStatus("current")
_PppLinkStatusEntry_Object = MibTableRow
pppLinkStatusEntry = _PppLinkStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1)
)
pppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppLinkStatusEntry.setStatus("current")


class _PppLinkStatusPhysicalIndex_Type(Integer32):
    """Custom type pppLinkStatusPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppLinkStatusPhysicalIndex_Type.__name__ = "Integer32"
_PppLinkStatusPhysicalIndex_Object = MibTableColumn
pppLinkStatusPhysicalIndex = _PppLinkStatusPhysicalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 1),
    _PppLinkStatusPhysicalIndex_Type()
)
pppLinkStatusPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusPhysicalIndex.setStatus("current")
_PppLinkStatusBadAddresses_Type = Counter32
_PppLinkStatusBadAddresses_Object = MibTableColumn
pppLinkStatusBadAddresses = _PppLinkStatusBadAddresses_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 2),
    _PppLinkStatusBadAddresses_Type()
)
pppLinkStatusBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusBadAddresses.setStatus("current")
_PppLinkStatusBadControls_Type = Counter32
_PppLinkStatusBadControls_Object = MibTableColumn
pppLinkStatusBadControls = _PppLinkStatusBadControls_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 3),
    _PppLinkStatusBadControls_Type()
)
pppLinkStatusBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusBadControls.setStatus("current")
_PppLinkStatusPacketTooLongs_Type = Counter32
_PppLinkStatusPacketTooLongs_Object = MibTableColumn
pppLinkStatusPacketTooLongs = _PppLinkStatusPacketTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 4),
    _PppLinkStatusPacketTooLongs_Type()
)
pppLinkStatusPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusPacketTooLongs.setStatus("current")
_PppLinkStatusBadFCSs_Type = Counter32
_PppLinkStatusBadFCSs_Object = MibTableColumn
pppLinkStatusBadFCSs = _PppLinkStatusBadFCSs_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 5),
    _PppLinkStatusBadFCSs_Type()
)
pppLinkStatusBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusBadFCSs.setStatus("current")


class _PppLinkStatusLocalMRU_Type(Integer32):
    """Custom type pppLinkStatusLocalMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppLinkStatusLocalMRU_Type.__name__ = "Integer32"
_PppLinkStatusLocalMRU_Object = MibTableColumn
pppLinkStatusLocalMRU = _PppLinkStatusLocalMRU_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 6),
    _PppLinkStatusLocalMRU_Type()
)
pppLinkStatusLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalMRU.setStatus("current")


class _PppLinkStatusRemoteMRU_Type(Integer32):
    """Custom type pppLinkStatusRemoteMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppLinkStatusRemoteMRU_Type.__name__ = "Integer32"
_PppLinkStatusRemoteMRU_Object = MibTableColumn
pppLinkStatusRemoteMRU = _PppLinkStatusRemoteMRU_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 7),
    _PppLinkStatusRemoteMRU_Type()
)
pppLinkStatusRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusRemoteMRU.setStatus("current")


class _PppLinkStatusLocalToPeerACCMap_Type(OctetString):
    """Custom type pppLinkStatusLocalToPeerACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PppLinkStatusLocalToPeerACCMap_Type.__name__ = "OctetString"
_PppLinkStatusLocalToPeerACCMap_Object = MibTableColumn
pppLinkStatusLocalToPeerACCMap = _PppLinkStatusLocalToPeerACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 8),
    _PppLinkStatusLocalToPeerACCMap_Type()
)
pppLinkStatusLocalToPeerACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalToPeerACCMap.setStatus("current")


class _PppLinkStatusPeerToLocalACCMap_Type(OctetString):
    """Custom type pppLinkStatusPeerToLocalACCMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PppLinkStatusPeerToLocalACCMap_Type.__name__ = "OctetString"
_PppLinkStatusPeerToLocalACCMap_Object = MibTableColumn
pppLinkStatusPeerToLocalACCMap = _PppLinkStatusPeerToLocalACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 9),
    _PppLinkStatusPeerToLocalACCMap_Type()
)
pppLinkStatusPeerToLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusPeerToLocalACCMap.setStatus("current")


class _PppLinkStatusLocalToRemoteProtocolCompression_Type(Integer32):
    """Custom type pppLinkStatusLocalToRemoteProtocolCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PppLinkStatusLocalToRemoteProtocolCompression_Type.__name__ = "Integer32"
_PppLinkStatusLocalToRemoteProtocolCompression_Object = MibTableColumn
pppLinkStatusLocalToRemoteProtocolCompression = _PppLinkStatusLocalToRemoteProtocolCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 10),
    _PppLinkStatusLocalToRemoteProtocolCompression_Type()
)
pppLinkStatusLocalToRemoteProtocolCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalToRemoteProtocolCompression.setStatus("current")


class _PppLinkStatusRemoteToLocalProtocolCompression_Type(Integer32):
    """Custom type pppLinkStatusRemoteToLocalProtocolCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PppLinkStatusRemoteToLocalProtocolCompression_Type.__name__ = "Integer32"
_PppLinkStatusRemoteToLocalProtocolCompression_Object = MibTableColumn
pppLinkStatusRemoteToLocalProtocolCompression = _PppLinkStatusRemoteToLocalProtocolCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 11),
    _PppLinkStatusRemoteToLocalProtocolCompression_Type()
)
pppLinkStatusRemoteToLocalProtocolCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusRemoteToLocalProtocolCompression.setStatus("current")


class _PppLinkStatusLocalToRemoteACCompression_Type(Integer32):
    """Custom type pppLinkStatusLocalToRemoteACCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PppLinkStatusLocalToRemoteACCompression_Type.__name__ = "Integer32"
_PppLinkStatusLocalToRemoteACCompression_Object = MibTableColumn
pppLinkStatusLocalToRemoteACCompression = _PppLinkStatusLocalToRemoteACCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 12),
    _PppLinkStatusLocalToRemoteACCompression_Type()
)
pppLinkStatusLocalToRemoteACCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusLocalToRemoteACCompression.setStatus("current")


class _PppLinkStatusRemoteToLocalACCompression_Type(Integer32):
    """Custom type pppLinkStatusRemoteToLocalACCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PppLinkStatusRemoteToLocalACCompression_Type.__name__ = "Integer32"
_PppLinkStatusRemoteToLocalACCompression_Object = MibTableColumn
pppLinkStatusRemoteToLocalACCompression = _PppLinkStatusRemoteToLocalACCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 13),
    _PppLinkStatusRemoteToLocalACCompression_Type()
)
pppLinkStatusRemoteToLocalACCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusRemoteToLocalACCompression.setStatus("current")


class _PppLinkStatusTransmitFcsSize_Type(Integer32):
    """Custom type pppLinkStatusTransmitFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLinkStatusTransmitFcsSize_Type.__name__ = "Integer32"
_PppLinkStatusTransmitFcsSize_Object = MibTableColumn
pppLinkStatusTransmitFcsSize = _PppLinkStatusTransmitFcsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 14),
    _PppLinkStatusTransmitFcsSize_Type()
)
pppLinkStatusTransmitFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusTransmitFcsSize.setStatus("current")


class _PppLinkStatusReceiveFcsSize_Type(Integer32):
    """Custom type pppLinkStatusReceiveFcsSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLinkStatusReceiveFcsSize_Type.__name__ = "Integer32"
_PppLinkStatusReceiveFcsSize_Object = MibTableColumn
pppLinkStatusReceiveFcsSize = _PppLinkStatusReceiveFcsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 15),
    _PppLinkStatusReceiveFcsSize_Type()
)
pppLinkStatusReceiveFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkStatusReceiveFcsSize.setStatus("current")
_PppLinkConfigTable_Object = MibTable
pppLinkConfigTable = _PppLinkConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pppLinkConfigTable.setStatus("current")
_PppLinkConfigEntry_Object = MibTableRow
pppLinkConfigEntry = _PppLinkConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1)
)
pppLinkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppLinkConfigEntry.setStatus("current")


class _PppLinkConfigInitialMRU_Type(Integer32):
    """Custom type pppLinkConfigInitialMRU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppLinkConfigInitialMRU_Type.__name__ = "Integer32"
_PppLinkConfigInitialMRU_Object = MibTableColumn
pppLinkConfigInitialMRU = _PppLinkConfigInitialMRU_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 1),
    _PppLinkConfigInitialMRU_Type()
)
pppLinkConfigInitialMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkConfigInitialMRU.setStatus("current")


class _PppLinkConfigReceiveACCMap_Type(OctetString):
    """Custom type pppLinkConfigReceiveACCMap based on OctetString"""
    defaultHexValue = "ffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PppLinkConfigReceiveACCMap_Type.__name__ = "OctetString"
_PppLinkConfigReceiveACCMap_Object = MibTableColumn
pppLinkConfigReceiveACCMap = _PppLinkConfigReceiveACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 2),
    _PppLinkConfigReceiveACCMap_Type()
)
pppLinkConfigReceiveACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkConfigReceiveACCMap.setStatus("current")


class _PppLinkConfigTransmitACCMap_Type(OctetString):
    """Custom type pppLinkConfigTransmitACCMap based on OctetString"""
    defaultHexValue = "ffffffff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PppLinkConfigTransmitACCMap_Type.__name__ = "OctetString"
_PppLinkConfigTransmitACCMap_Object = MibTableColumn
pppLinkConfigTransmitACCMap = _PppLinkConfigTransmitACCMap_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 3),
    _PppLinkConfigTransmitACCMap_Type()
)
pppLinkConfigTransmitACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkConfigTransmitACCMap.setStatus("current")


class _PppLinkConfigMagicNumber_Type(Integer32):
    """Custom type pppLinkConfigMagicNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppLinkConfigMagicNumber_Type.__name__ = "Integer32"
_PppLinkConfigMagicNumber_Object = MibTableColumn
pppLinkConfigMagicNumber = _PppLinkConfigMagicNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 4),
    _PppLinkConfigMagicNumber_Type()
)
pppLinkConfigMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkConfigMagicNumber.setStatus("current")


class _PppLinkConfigFcsSize_Type(Integer32):
    """Custom type pppLinkConfigFcsSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PppLinkConfigFcsSize_Type.__name__ = "Integer32"
_PppLinkConfigFcsSize_Object = MibTableColumn
pppLinkConfigFcsSize = _PppLinkConfigFcsSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 5),
    _PppLinkConfigFcsSize_Type()
)
pppLinkConfigFcsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLinkConfigFcsSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PPP-LCP-MIB",
    **{"ppp": ppp,
       "pppLcp": pppLcp,
       "pppLink": pppLink,
       "pppLinkStatusTable": pppLinkStatusTable,
       "pppLinkStatusEntry": pppLinkStatusEntry,
       "pppLinkStatusPhysicalIndex": pppLinkStatusPhysicalIndex,
       "pppLinkStatusBadAddresses": pppLinkStatusBadAddresses,
       "pppLinkStatusBadControls": pppLinkStatusBadControls,
       "pppLinkStatusPacketTooLongs": pppLinkStatusPacketTooLongs,
       "pppLinkStatusBadFCSs": pppLinkStatusBadFCSs,
       "pppLinkStatusLocalMRU": pppLinkStatusLocalMRU,
       "pppLinkStatusRemoteMRU": pppLinkStatusRemoteMRU,
       "pppLinkStatusLocalToPeerACCMap": pppLinkStatusLocalToPeerACCMap,
       "pppLinkStatusPeerToLocalACCMap": pppLinkStatusPeerToLocalACCMap,
       "pppLinkStatusLocalToRemoteProtocolCompression": pppLinkStatusLocalToRemoteProtocolCompression,
       "pppLinkStatusRemoteToLocalProtocolCompression": pppLinkStatusRemoteToLocalProtocolCompression,
       "pppLinkStatusLocalToRemoteACCompression": pppLinkStatusLocalToRemoteACCompression,
       "pppLinkStatusRemoteToLocalACCompression": pppLinkStatusRemoteToLocalACCompression,
       "pppLinkStatusTransmitFcsSize": pppLinkStatusTransmitFcsSize,
       "pppLinkStatusReceiveFcsSize": pppLinkStatusReceiveFcsSize,
       "pppLinkConfigTable": pppLinkConfigTable,
       "pppLinkConfigEntry": pppLinkConfigEntry,
       "pppLinkConfigInitialMRU": pppLinkConfigInitialMRU,
       "pppLinkConfigReceiveACCMap": pppLinkConfigReceiveACCMap,
       "pppLinkConfigTransmitACCMap": pppLinkConfigTransmitACCMap,
       "pppLinkConfigMagicNumber": pppLinkConfigMagicNumber,
       "pppLinkConfigFcsSize": pppLinkConfigFcsSize}
)
