# SNMP MIB module (STORMSHIELD-VPNSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-VPNSA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:19 2025
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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsVPN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1)
)
if mibBuilder.loadTexts:
    snsVPN.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsVPNSATable_Object = MibTable
snsVPNSATable = _SnsVPNSATable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snsVPNSATable.setStatus("current")
_SnsVPNSAEntry_Object = MibTableRow
snsVPNSAEntry = _SnsVPNSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1)
)
snsVPNSAEntry.setIndexNames(
    (0, "STORMSHIELD-VPNSA-MIB", "snsVPNSAIndex"),
)
if mibBuilder.loadTexts:
    snsVPNSAEntry.setStatus("current")


class _SnsVPNSAIndex_Type(Integer32):
    """Custom type snsVPNSAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsVPNSAIndex_Type.__name__ = "Integer32"
_SnsVPNSAIndex_Object = MibTableColumn
snsVPNSAIndex = _SnsVPNSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 1),
    _SnsVPNSAIndex_Type()
)
snsVPNSAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAIndex.setStatus("current")
_SnsVPNIPSrc_Type = DisplayString
_SnsVPNIPSrc_Object = MibTableColumn
snsVPNIPSrc = _SnsVPNIPSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 2),
    _SnsVPNIPSrc_Type()
)
snsVPNIPSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIPSrc.setStatus("current")
_SnsVPNIPDst_Type = DisplayString
_SnsVPNIPDst_Object = MibTableColumn
snsVPNIPDst = _SnsVPNIPDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 3),
    _SnsVPNIPDst_Type()
)
snsVPNIPDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIPDst.setStatus("current")


class _SnsVPNType_Type(Integer32):
    """Custom type snsVPNType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unspec", 0),
          ("unknown", 1),
          ("ah", 2),
          ("esp", 3),
          ("rsvp", 4),
          ("ospfv2", 5),
          ("ripv2", 6),
          ("mip", 7),
          ("ipcomp", 8))
    )


_SnsVPNType_Type.__name__ = "Integer32"
_SnsVPNType_Object = MibTableColumn
snsVPNType = _SnsVPNType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 4),
    _SnsVPNType_Type()
)
snsVPNType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNType.setStatus("current")


class _SnsVPNMode_Type(Integer32):
    """Custom type snsVPNMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("transport", 1),
          ("tunnel", 2))
    )


_SnsVPNMode_Type.__name__ = "Integer32"
_SnsVPNMode_Object = MibTableColumn
snsVPNMode = _SnsVPNMode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 5),
    _SnsVPNMode_Type()
)
snsVPNMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNMode.setStatus("current")
_SnsVPNSpi_Type = Unsigned32
_SnsVPNSpi_Object = MibTableColumn
snsVPNSpi = _SnsVPNSpi_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 6),
    _SnsVPNSpi_Type()
)
snsVPNSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSpi.setStatus("current")
_SnsVPNPeerSpi_Type = Unsigned32
_SnsVPNPeerSpi_Object = MibTableColumn
snsVPNPeerSpi = _SnsVPNPeerSpi_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 7),
    _SnsVPNPeerSpi_Type()
)
snsVPNPeerSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNPeerSpi.setStatus("current")
_SnsVPNReqID_Type = Integer32
_SnsVPNReqID_Object = MibTableColumn
snsVPNReqID = _SnsVPNReqID_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 8),
    _SnsVPNReqID_Type()
)
snsVPNReqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNReqID.setStatus("current")
_SnsVPNEnc_Type = DisplayString
_SnsVPNEnc_Object = MibTableColumn
snsVPNEnc = _SnsVPNEnc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 9),
    _SnsVPNEnc_Type()
)
snsVPNEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNEnc.setStatus("current")


class _SnsVPNAuth_Type(Integer32):
    """Custom type snsVPNAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              5,
              6,
              7,
              249,
              250,
              251)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hmac-md5", 2),
          ("hmac-sha1", 3),
          ("hmac-sha256", 5),
          ("hmac-sha384", 6),
          ("hmac-sha512", 7),
          ("md5", 249),
          ("sha", 250),
          ("null", 251))
    )


_SnsVPNAuth_Type.__name__ = "Integer32"
_SnsVPNAuth_Object = MibTableColumn
snsVPNAuth = _SnsVPNAuth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 10),
    _SnsVPNAuth_Type()
)
snsVPNAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNAuth.setStatus("current")


class _SnsVPNState_Type(Integer32):
    """Custom type snsVPNState based on Integer32"""
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
        *(("larval", 0),
          ("mature", 1),
          ("dying", 2),
          ("dead", 3))
    )


_SnsVPNState_Type.__name__ = "Integer32"
_SnsVPNState_Object = MibTableColumn
snsVPNState = _SnsVPNState_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 11),
    _SnsVPNState_Type()
)
snsVPNState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNState.setStatus("current")
_SnsVPNLifetime_Type = Counter64
_SnsVPNLifetime_Object = MibTableColumn
snsVPNLifetime = _SnsVPNLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 12),
    _SnsVPNLifetime_Type()
)
snsVPNLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNLifetime.setStatus("current")
_SnsVPNBytes_Type = Counter64
_SnsVPNBytes_Object = MibTableColumn
snsVPNBytes = _SnsVPNBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 13),
    _SnsVPNBytes_Type()
)
snsVPNBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNBytes.setStatus("current")
_SnsVPNMaxLifetime_Type = Counter64
_SnsVPNMaxLifetime_Object = MibTableColumn
snsVPNMaxLifetime = _SnsVPNMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 14),
    _SnsVPNMaxLifetime_Type()
)
snsVPNMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNMaxLifetime.setStatus("current")
_SnsVPNMaxBytes_Type = Counter64
_SnsVPNMaxBytes_Object = MibTableColumn
snsVPNMaxBytes = _SnsVPNMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 15),
    _SnsVPNMaxBytes_Type()
)
snsVPNMaxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNMaxBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-VPNSA-MIB",
    **{"snsVPN": snsVPN,
       "snsVPNSATable": snsVPNSATable,
       "snsVPNSAEntry": snsVPNSAEntry,
       "snsVPNSAIndex": snsVPNSAIndex,
       "snsVPNIPSrc": snsVPNIPSrc,
       "snsVPNIPDst": snsVPNIPDst,
       "snsVPNType": snsVPNType,
       "snsVPNMode": snsVPNMode,
       "snsVPNSpi": snsVPNSpi,
       "snsVPNPeerSpi": snsVPNPeerSpi,
       "snsVPNReqID": snsVPNReqID,
       "snsVPNEnc": snsVPNEnc,
       "snsVPNAuth": snsVPNAuth,
       "snsVPNState": snsVPNState,
       "snsVPNLifetime": snsVPNLifetime,
       "snsVPNBytes": snsVPNBytes,
       "snsVPNMaxLifetime": snsVPNMaxLifetime,
       "snsVPNMaxBytes": snsVPNMaxBytes}
)
