# SNMP MIB module (HH3C-BGP-EVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-BGP-EVPN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:47 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cBgpEvpn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172)
)
if mibBuilder.loadTexts:
    hh3cBgpEvpn.setRevisions(
        ("2018-07-07 14:30",
         "2017-11-29 14:31",
         "2017-11-04 14:31")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cBgpEvpnObjects_ObjectIdentity = ObjectIdentity
hh3cBgpEvpnObjects = _Hh3cBgpEvpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1)
)
_Hh3cBgpEvpnConf_ObjectIdentity = ObjectIdentity
hh3cBgpEvpnConf = _Hh3cBgpEvpnConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1)
)
_Hh3cBgpEvpnNbrAddrTable_Object = MibTable
hh3cBgpEvpnNbrAddrTable = _Hh3cBgpEvpnNbrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cBgpEvpnNbrAddrTable.setStatus("current")
_Hh3cBgpEvpnNbrAddrEntry_Object = MibTableRow
hh3cBgpEvpnNbrAddrEntry = _Hh3cBgpEvpnNbrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 1, 1)
)
hh3cBgpEvpnNbrAddrEntry.setIndexNames(
    (0, "HH3C-BGP-EVPN-MIB", "hh3cBgpEvpnNbrAddr"),
)
if mibBuilder.loadTexts:
    hh3cBgpEvpnNbrAddrEntry.setStatus("current")
_Hh3cBgpEvpnNbrAddr_Type = IpAddress
_Hh3cBgpEvpnNbrAddr_Object = MibTableColumn
hh3cBgpEvpnNbrAddr = _Hh3cBgpEvpnNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 1, 1, 1),
    _Hh3cBgpEvpnNbrAddr_Type()
)
hh3cBgpEvpnNbrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpEvpnNbrAddr.setStatus("current")
_Hh3cBgpEvpnNbrAsNumber_Type = Unsigned32
_Hh3cBgpEvpnNbrAsNumber_Object = MibTableColumn
hh3cBgpEvpnNbrAsNumber = _Hh3cBgpEvpnNbrAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 1, 1, 2),
    _Hh3cBgpEvpnNbrAsNumber_Type()
)
hh3cBgpEvpnNbrAsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnNbrAsNumber.setStatus("current")
_Hh3cBgpEvpnNbrPrefixTable_Object = MibTable
hh3cBgpEvpnNbrPrefixTable = _Hh3cBgpEvpnNbrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cBgpEvpnNbrPrefixTable.setStatus("current")
_Hh3cBgpEvpnNbrPrefixEntry_Object = MibTableRow
hh3cBgpEvpnNbrPrefixEntry = _Hh3cBgpEvpnNbrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1)
)
hh3cBgpEvpnNbrPrefixEntry.setIndexNames(
    (0, "HH3C-BGP-EVPN-MIB", "hh3cBgpEvpnPAtrRD"),
    (0, "HH3C-BGP-EVPN-MIB", "hh3cBgpEvpnPAtrAddrPrefix"),
    (0, "HH3C-BGP-EVPN-MIB", "hh3cBgpEvpnPAtrAddrPrefixLen"),
    (0, "HH3C-BGP-EVPN-MIB", "hh3cBgpEvpnPAtrPeer"),
)
if mibBuilder.loadTexts:
    hh3cBgpEvpnNbrPrefixEntry.setStatus("current")


class _Hh3cBgpEvpnPAtrRD_Type(OctetString):
    """Custom type hh3cBgpEvpnPAtrRD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 21),
    )


_Hh3cBgpEvpnPAtrRD_Type.__name__ = "OctetString"
_Hh3cBgpEvpnPAtrRD_Object = MibTableColumn
hh3cBgpEvpnPAtrRD = _Hh3cBgpEvpnPAtrRD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 1),
    _Hh3cBgpEvpnPAtrRD_Type()
)
hh3cBgpEvpnPAtrRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrRD.setStatus("current")


class _Hh3cBgpEvpnPAtrAddrPrefix_Type(OctetString):
    """Custom type hh3cBgpEvpnPAtrAddrPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 86),
    )


_Hh3cBgpEvpnPAtrAddrPrefix_Type.__name__ = "OctetString"
_Hh3cBgpEvpnPAtrAddrPrefix_Object = MibTableColumn
hh3cBgpEvpnPAtrAddrPrefix = _Hh3cBgpEvpnPAtrAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 2),
    _Hh3cBgpEvpnPAtrAddrPrefix_Type()
)
hh3cBgpEvpnPAtrAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrAddrPrefix.setStatus("current")


class _Hh3cBgpEvpnPAtrAddrPrefixLen_Type(Integer32):
    """Custom type hh3cBgpEvpnPAtrAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Hh3cBgpEvpnPAtrAddrPrefixLen_Type.__name__ = "Integer32"
_Hh3cBgpEvpnPAtrAddrPrefixLen_Object = MibTableColumn
hh3cBgpEvpnPAtrAddrPrefixLen = _Hh3cBgpEvpnPAtrAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 3),
    _Hh3cBgpEvpnPAtrAddrPrefixLen_Type()
)
hh3cBgpEvpnPAtrAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrAddrPrefixLen.setStatus("current")
_Hh3cBgpEvpnPAtrPeer_Type = IpAddress
_Hh3cBgpEvpnPAtrPeer_Object = MibTableColumn
hh3cBgpEvpnPAtrPeer = _Hh3cBgpEvpnPAtrPeer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 4),
    _Hh3cBgpEvpnPAtrPeer_Type()
)
hh3cBgpEvpnPAtrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrPeer.setStatus("current")
_Hh3cBgpEvpnPAtrRouteType_Type = Unsigned32
_Hh3cBgpEvpnPAtrRouteType_Object = MibTableColumn
hh3cBgpEvpnPAtrRouteType = _Hh3cBgpEvpnPAtrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 5),
    _Hh3cBgpEvpnPAtrRouteType_Type()
)
hh3cBgpEvpnPAtrRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrRouteType.setStatus("current")


class _Hh3cBgpEvpnPAtrOrigin_Type(Integer32):
    """Custom type hh3cBgpEvpnPAtrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_Hh3cBgpEvpnPAtrOrigin_Type.__name__ = "Integer32"
_Hh3cBgpEvpnPAtrOrigin_Object = MibTableColumn
hh3cBgpEvpnPAtrOrigin = _Hh3cBgpEvpnPAtrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 6),
    _Hh3cBgpEvpnPAtrOrigin_Type()
)
hh3cBgpEvpnPAtrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrOrigin.setStatus("current")


class _Hh3cBgpEvpnPAtrASPathSegment_Type(OctetString):
    """Custom type hh3cBgpEvpnPAtrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_Hh3cBgpEvpnPAtrASPathSegment_Type.__name__ = "OctetString"
_Hh3cBgpEvpnPAtrASPathSegment_Object = MibTableColumn
hh3cBgpEvpnPAtrASPathSegment = _Hh3cBgpEvpnPAtrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 7),
    _Hh3cBgpEvpnPAtrASPathSegment_Type()
)
hh3cBgpEvpnPAtrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrASPathSegment.setStatus("current")
_Hh3cBgpEvpnPAtrNextHop_Type = IpAddress
_Hh3cBgpEvpnPAtrNextHop_Object = MibTableColumn
hh3cBgpEvpnPAtrNextHop = _Hh3cBgpEvpnPAtrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 8),
    _Hh3cBgpEvpnPAtrNextHop_Type()
)
hh3cBgpEvpnPAtrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrNextHop.setStatus("current")


class _Hh3cBgpEvpnPAtrMultiExitDisc_Type(Integer32):
    """Custom type hh3cBgpEvpnPAtrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Hh3cBgpEvpnPAtrMultiExitDisc_Type.__name__ = "Integer32"
_Hh3cBgpEvpnPAtrMultiExitDisc_Object = MibTableColumn
hh3cBgpEvpnPAtrMultiExitDisc = _Hh3cBgpEvpnPAtrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 9),
    _Hh3cBgpEvpnPAtrMultiExitDisc_Type()
)
hh3cBgpEvpnPAtrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrMultiExitDisc.setStatus("current")


class _Hh3cBgpEvpnPAtrLocalPref_Type(Integer32):
    """Custom type hh3cBgpEvpnPAtrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Hh3cBgpEvpnPAtrLocalPref_Type.__name__ = "Integer32"
_Hh3cBgpEvpnPAtrLocalPref_Object = MibTableColumn
hh3cBgpEvpnPAtrLocalPref = _Hh3cBgpEvpnPAtrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 10),
    _Hh3cBgpEvpnPAtrLocalPref_Type()
)
hh3cBgpEvpnPAtrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrLocalPref.setStatus("current")


class _Hh3cBgpEvpnPAtrIGMPFlags_Type(Integer32):
    """Custom type hh3cBgpEvpnPAtrIGMPFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_Hh3cBgpEvpnPAtrIGMPFlags_Type.__name__ = "Integer32"
_Hh3cBgpEvpnPAtrIGMPFlags_Object = MibTableColumn
hh3cBgpEvpnPAtrIGMPFlags = _Hh3cBgpEvpnPAtrIGMPFlags_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 11),
    _Hh3cBgpEvpnPAtrIGMPFlags_Type()
)
hh3cBgpEvpnPAtrIGMPFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrIGMPFlags.setStatus("current")
_Hh3cBgpEvpnPAtrMaxRespTime_Type = Unsigned32
_Hh3cBgpEvpnPAtrMaxRespTime_Object = MibTableColumn
hh3cBgpEvpnPAtrMaxRespTime = _Hh3cBgpEvpnPAtrMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 12),
    _Hh3cBgpEvpnPAtrMaxRespTime_Type()
)
hh3cBgpEvpnPAtrMaxRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrMaxRespTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrMaxRespTime.setUnits("ms")


class _Hh3cBgpEvpnPAtrPMSITunnel_Type(OctetString):
    """Custom type hh3cBgpEvpnPAtrPMSITunnel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 21),
    )


_Hh3cBgpEvpnPAtrPMSITunnel_Type.__name__ = "OctetString"
_Hh3cBgpEvpnPAtrPMSITunnel_Object = MibTableColumn
hh3cBgpEvpnPAtrPMSITunnel = _Hh3cBgpEvpnPAtrPMSITunnel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 13),
    _Hh3cBgpEvpnPAtrPMSITunnel_Type()
)
hh3cBgpEvpnPAtrPMSITunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrPMSITunnel.setStatus("current")
_Hh3cBgpEvpnPAtrL2VNI_Type = Unsigned32
_Hh3cBgpEvpnPAtrL2VNI_Object = MibTableColumn
hh3cBgpEvpnPAtrL2VNI = _Hh3cBgpEvpnPAtrL2VNI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 14),
    _Hh3cBgpEvpnPAtrL2VNI_Type()
)
hh3cBgpEvpnPAtrL2VNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrL2VNI.setStatus("current")
_Hh3cBgpEvpnPAtrL3VNI_Type = Unsigned32
_Hh3cBgpEvpnPAtrL3VNI_Object = MibTableColumn
hh3cBgpEvpnPAtrL3VNI = _Hh3cBgpEvpnPAtrL3VNI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 15),
    _Hh3cBgpEvpnPAtrL3VNI_Type()
)
hh3cBgpEvpnPAtrL3VNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrL3VNI.setStatus("current")
_Hh3cBgpEvpnPAtrBest_Type = TruthValue
_Hh3cBgpEvpnPAtrBest_Object = MibTableColumn
hh3cBgpEvpnPAtrBest = _Hh3cBgpEvpnPAtrBest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 16),
    _Hh3cBgpEvpnPAtrBest_Type()
)
hh3cBgpEvpnPAtrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrBest.setStatus("current")


class _Hh3cBgpEvpnPAtrUnknown_Type(OctetString):
    """Custom type hh3cBgpEvpnPAtrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cBgpEvpnPAtrUnknown_Type.__name__ = "OctetString"
_Hh3cBgpEvpnPAtrUnknown_Object = MibTableColumn
hh3cBgpEvpnPAtrUnknown = _Hh3cBgpEvpnPAtrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 172, 1, 1, 2, 1, 17),
    _Hh3cBgpEvpnPAtrUnknown_Type()
)
hh3cBgpEvpnPAtrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBgpEvpnPAtrUnknown.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-BGP-EVPN-MIB",
    **{"hh3cBgpEvpn": hh3cBgpEvpn,
       "hh3cBgpEvpnObjects": hh3cBgpEvpnObjects,
       "hh3cBgpEvpnConf": hh3cBgpEvpnConf,
       "hh3cBgpEvpnNbrAddrTable": hh3cBgpEvpnNbrAddrTable,
       "hh3cBgpEvpnNbrAddrEntry": hh3cBgpEvpnNbrAddrEntry,
       "hh3cBgpEvpnNbrAddr": hh3cBgpEvpnNbrAddr,
       "hh3cBgpEvpnNbrAsNumber": hh3cBgpEvpnNbrAsNumber,
       "hh3cBgpEvpnNbrPrefixTable": hh3cBgpEvpnNbrPrefixTable,
       "hh3cBgpEvpnNbrPrefixEntry": hh3cBgpEvpnNbrPrefixEntry,
       "hh3cBgpEvpnPAtrRD": hh3cBgpEvpnPAtrRD,
       "hh3cBgpEvpnPAtrAddrPrefix": hh3cBgpEvpnPAtrAddrPrefix,
       "hh3cBgpEvpnPAtrAddrPrefixLen": hh3cBgpEvpnPAtrAddrPrefixLen,
       "hh3cBgpEvpnPAtrPeer": hh3cBgpEvpnPAtrPeer,
       "hh3cBgpEvpnPAtrRouteType": hh3cBgpEvpnPAtrRouteType,
       "hh3cBgpEvpnPAtrOrigin": hh3cBgpEvpnPAtrOrigin,
       "hh3cBgpEvpnPAtrASPathSegment": hh3cBgpEvpnPAtrASPathSegment,
       "hh3cBgpEvpnPAtrNextHop": hh3cBgpEvpnPAtrNextHop,
       "hh3cBgpEvpnPAtrMultiExitDisc": hh3cBgpEvpnPAtrMultiExitDisc,
       "hh3cBgpEvpnPAtrLocalPref": hh3cBgpEvpnPAtrLocalPref,
       "hh3cBgpEvpnPAtrIGMPFlags": hh3cBgpEvpnPAtrIGMPFlags,
       "hh3cBgpEvpnPAtrMaxRespTime": hh3cBgpEvpnPAtrMaxRespTime,
       "hh3cBgpEvpnPAtrPMSITunnel": hh3cBgpEvpnPAtrPMSITunnel,
       "hh3cBgpEvpnPAtrL2VNI": hh3cBgpEvpnPAtrL2VNI,
       "hh3cBgpEvpnPAtrL3VNI": hh3cBgpEvpnPAtrL3VNI,
       "hh3cBgpEvpnPAtrBest": hh3cBgpEvpnPAtrBest,
       "hh3cBgpEvpnPAtrUnknown": hh3cBgpEvpnPAtrUnknown}
)
