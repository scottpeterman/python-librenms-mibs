# SNMP MIB module (JUNIPER-IPSEC-FLOW-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-IPSEC-FLOW-MON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:42 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(jnxIpSecMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxIpSecMibRoot")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

jnxIpSecFlowMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1)
)
if mibBuilder.loadTexts:
    jnxIpSecFlowMonMIB.setRevisions(
        ("2020-04-29 00:00",
         "2020-04-28 00:00",
         "2020-04-19 00:00",
         "2019-09-10 00:00",
         "2019-08-22 00:00",
         "2016-06-22 00:00",
         "2007-05-16 00:00",
         "2016-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxIkePeerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("idIpv4Addr", 1),
          ("idFqdn", 2),
          ("idDn", 3),
          ("idUfqdn", 4),
          ("idIpv6Addr", 5))
    )



class JnxIkeNegoMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("aggressive", 2),
          ("ikev2", 3))
    )



class JnxIkeHashAlgo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2),
          ("sha256", 3),
          ("sha384", 4),
          ("sha512", 5))
    )



class JnxIkeAuthMethod(TextualConvention, Integer32):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("preSharedKey", 1),
          ("dssSignature", 2),
          ("rsaSignature", 3),
          ("rsaEncryption", 4),
          ("revRsaEncryption", 5),
          ("xauthPreSharedKey", 6),
          ("xauthDssSignature", 7),
          ("xauthRsaSignature", 8),
          ("xauthRsaEncryption", 9),
          ("xauthRevRsaEncryption", 10),
          ("ecdsa256Signature", 11),
          ("ecdsa384Signature", 12),
          ("ecdsa521Signature", 13))
    )



class JnxIkePeerRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 2))
    )



class JnxIkeTunStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class JnxDiffHellmanGrp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              15,
              16,
              19,
              20,
              21,
              24)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("modp768", 1),
          ("modp1024", 2),
          ("modp1536", 5),
          ("modp2048", 14),
          ("modp3072", 15),
          ("modp4096", 16),
          ("ecmodp256", 19),
          ("ecmodp384", 20),
          ("ecmodp521", 21),
          ("modp2048s256", 24))
    )



class JnxKeyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("keyIke", 1),
          ("keyManual", 2))
    )



class JnxEncapMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tunnel", 1),
          ("transport", 2))
    )



class JnxEncryptAlgo(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("espDes", 1),
          ("esp3des", 2),
          ("espNull", 3),
          ("espAes128", 4),
          ("espAes192", 5),
          ("espAes256", 6),
          ("espAesGcm128", 7),
          ("espAesGcm192", 8),
          ("espAesGcm256", 9))
    )



class JnxAuthAlgo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("hmacMd5", 1),
          ("hmacSha", 2),
          ("hmacSha256", 3),
          ("hmacSha384", 4),
          ("hmacSha512", 5))
    )



class JnxRemotePeerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("static", 1),
          ("dynamic", 2))
    )



class JnxPeerStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



class JnxSpiType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )



class JnxSAType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("manual", 1),
          ("dynamic", 2))
    )



class JnxEsnMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1),
          ("disable", 2))
    )



class JnxIkeTunType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("halink", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JnxIpSecFlowMonNotifications_ObjectIdentity = ObjectIdentity
jnxIpSecFlowMonNotifications = _JnxIpSecFlowMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0)
)
_JnxIkeNotificationType_ObjectIdentity = ObjectIdentity
jnxIkeNotificationType = _JnxIkeNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 0)
)
_JnxIkeNotificationObj_ObjectIdentity = ObjectIdentity
jnxIkeNotificationObj = _JnxIkeNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1)
)
_JnxIkeTrapPeerRemoteGwAddrType_Type = InetAddressType
_JnxIkeTrapPeerRemoteGwAddrType_Object = MibScalar
jnxIkeTrapPeerRemoteGwAddrType = _JnxIkeTrapPeerRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 1),
    _JnxIkeTrapPeerRemoteGwAddrType_Type()
)
jnxIkeTrapPeerRemoteGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerRemoteGwAddrType.setStatus("current")
_JnxIkeTrapPeerRemoteGwAddr_Type = InetAddress
_JnxIkeTrapPeerRemoteGwAddr_Object = MibScalar
jnxIkeTrapPeerRemoteGwAddr = _JnxIkeTrapPeerRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 2),
    _JnxIkeTrapPeerRemoteGwAddr_Type()
)
jnxIkeTrapPeerRemoteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerRemoteGwAddr.setStatus("current")
_JnxIkeTrapPeerRemotePort_Type = InetPortNumber
_JnxIkeTrapPeerRemotePort_Object = MibScalar
jnxIkeTrapPeerRemotePort = _JnxIkeTrapPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 3),
    _JnxIkeTrapPeerRemotePort_Type()
)
jnxIkeTrapPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerRemotePort.setStatus("current")
_JnxIkeTrapPeerLocalGwAddrType_Type = InetAddressType
_JnxIkeTrapPeerLocalGwAddrType_Object = MibScalar
jnxIkeTrapPeerLocalGwAddrType = _JnxIkeTrapPeerLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 4),
    _JnxIkeTrapPeerLocalGwAddrType_Type()
)
jnxIkeTrapPeerLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerLocalGwAddrType.setStatus("current")
_JnxIkeTrapPeerLocalGwAddr_Type = InetAddress
_JnxIkeTrapPeerLocalGwAddr_Object = MibScalar
jnxIkeTrapPeerLocalGwAddr = _JnxIkeTrapPeerLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 5),
    _JnxIkeTrapPeerLocalGwAddr_Type()
)
jnxIkeTrapPeerLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerLocalGwAddr.setStatus("current")
_JnxIkeTrapPeerLocalPort_Type = InetPortNumber
_JnxIkeTrapPeerLocalPort_Object = MibScalar
jnxIkeTrapPeerLocalPort = _JnxIkeTrapPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 6),
    _JnxIkeTrapPeerLocalPort_Type()
)
jnxIkeTrapPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerLocalPort.setStatus("current")
_JnxIkeTrapPeerRoutingInstance_Type = DisplayString
_JnxIkeTrapPeerRoutingInstance_Object = MibScalar
jnxIkeTrapPeerRoutingInstance = _JnxIkeTrapPeerRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 7),
    _JnxIkeTrapPeerRoutingInstance_Type()
)
jnxIkeTrapPeerRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerRoutingInstance.setStatus("current")
_JnxIkeTrapPeerLocalIdType_Type = JnxIkePeerType
_JnxIkeTrapPeerLocalIdType_Object = MibScalar
jnxIkeTrapPeerLocalIdType = _JnxIkeTrapPeerLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 8),
    _JnxIkeTrapPeerLocalIdType_Type()
)
jnxIkeTrapPeerLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerLocalIdType.setStatus("current")
_JnxIkeTrapPeerLocalIdValue_Type = DisplayString
_JnxIkeTrapPeerLocalIdValue_Object = MibScalar
jnxIkeTrapPeerLocalIdValue = _JnxIkeTrapPeerLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 9),
    _JnxIkeTrapPeerLocalIdValue_Type()
)
jnxIkeTrapPeerLocalIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerLocalIdValue.setStatus("current")
_JnxIkeTrapPeerRemoteIdType_Type = JnxIkePeerType
_JnxIkeTrapPeerRemoteIdType_Object = MibScalar
jnxIkeTrapPeerRemoteIdType = _JnxIkeTrapPeerRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 10),
    _JnxIkeTrapPeerRemoteIdType_Type()
)
jnxIkeTrapPeerRemoteIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerRemoteIdType.setStatus("current")
_JnxIkeTrapPeerRemoteIdValue_Type = DisplayString
_JnxIkeTrapPeerRemoteIdValue_Object = MibScalar
jnxIkeTrapPeerRemoteIdValue = _JnxIkeTrapPeerRemoteIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 11),
    _JnxIkeTrapPeerRemoteIdValue_Type()
)
jnxIkeTrapPeerRemoteIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerRemoteIdValue.setStatus("current")
_JnxIkeTrapPeerAAAUserName_Type = DisplayString
_JnxIkeTrapPeerAAAUserName_Object = MibScalar
jnxIkeTrapPeerAAAUserName = _JnxIkeTrapPeerAAAUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 12),
    _JnxIkeTrapPeerAAAUserName_Type()
)
jnxIkeTrapPeerAAAUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerAAAUserName.setStatus("current")
_JnxIkeTrapPeerGwName_Type = DisplayString
_JnxIkeTrapPeerGwName_Object = MibScalar
jnxIkeTrapPeerGwName = _JnxIkeTrapPeerGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 13),
    _JnxIkeTrapPeerGwName_Type()
)
jnxIkeTrapPeerGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapPeerGwName.setStatus("current")
_JnxIkeTrapIpSecTunVpnName_Type = DisplayString
_JnxIkeTrapIpSecTunVpnName_Object = MibScalar
jnxIkeTrapIpSecTunVpnName = _JnxIkeTrapIpSecTunVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 14),
    _JnxIkeTrapIpSecTunVpnName_Type()
)
jnxIkeTrapIpSecTunVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapIpSecTunVpnName.setStatus("current")
_JnxIkeTrapIpSecTunTsName_Type = DisplayString
_JnxIkeTrapIpSecTunTsName_Object = MibScalar
jnxIkeTrapIpSecTunTsName = _JnxIkeTrapIpSecTunTsName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 15),
    _JnxIkeTrapIpSecTunTsName_Type()
)
jnxIkeTrapIpSecTunTsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapIpSecTunTsName.setStatus("current")
_JnxIkeTrapIpSecTunLocalTS_Type = DisplayString
_JnxIkeTrapIpSecTunLocalTS_Object = MibScalar
jnxIkeTrapIpSecTunLocalTS = _JnxIkeTrapIpSecTunLocalTS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 16),
    _JnxIkeTrapIpSecTunLocalTS_Type()
)
jnxIkeTrapIpSecTunLocalTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapIpSecTunLocalTS.setStatus("current")
_JnxIkeTrapIpSecTunRemoteTS_Type = DisplayString
_JnxIkeTrapIpSecTunRemoteTS_Object = MibScalar
jnxIkeTrapIpSecTunRemoteTS = _JnxIkeTrapIpSecTunRemoteTS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 1, 17),
    _JnxIkeTrapIpSecTunRemoteTS_Type()
)
jnxIkeTrapIpSecTunRemoteTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTrapIpSecTunRemoteTS.setStatus("current")
_JnxIpSecFlowMonPhaseOne_ObjectIdentity = ObjectIdentity
jnxIpSecFlowMonPhaseOne = _JnxIpSecFlowMonPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1)
)
_JnxIkeNumOfTunnels_Type = Integer32
_JnxIkeNumOfTunnels_Object = MibScalar
jnxIkeNumOfTunnels = _JnxIkeNumOfTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 1),
    _JnxIkeNumOfTunnels_Type()
)
jnxIkeNumOfTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeNumOfTunnels.setStatus("current")
_JnxIkeTunnelMonTable_Object = MibTable
jnxIkeTunnelMonTable = _JnxIkeTunnelMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxIkeTunnelMonTable.setStatus("current")
_JnxIkeTunnelMonEntry_Object = MibTableRow
jnxIkeTunnelMonEntry = _JnxIkeTunnelMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1)
)
jnxIkeTunnelMonEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonRemoteGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonRemoteGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonIndex"),
)
if mibBuilder.loadTexts:
    jnxIkeTunnelMonEntry.setStatus("current")
_JnxIkeTunMonRemoteGwAddrType_Type = InetAddressType
_JnxIkeTunMonRemoteGwAddrType_Object = MibTableColumn
jnxIkeTunMonRemoteGwAddrType = _JnxIkeTunMonRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 1),
    _JnxIkeTunMonRemoteGwAddrType_Type()
)
jnxIkeTunMonRemoteGwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteGwAddrType.setStatus("current")
_JnxIkeTunMonRemoteGwAddr_Type = InetAddress
_JnxIkeTunMonRemoteGwAddr_Object = MibTableColumn
jnxIkeTunMonRemoteGwAddr = _JnxIkeTunMonRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 2),
    _JnxIkeTunMonRemoteGwAddr_Type()
)
jnxIkeTunMonRemoteGwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteGwAddr.setStatus("current")


class _JnxIkeTunMonIndex_Type(Integer32):
    """Custom type jnxIkeTunMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkeTunMonIndex_Type.__name__ = "Integer32"
_JnxIkeTunMonIndex_Object = MibTableColumn
jnxIkeTunMonIndex = _JnxIkeTunMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 3),
    _JnxIkeTunMonIndex_Type()
)
jnxIkeTunMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkeTunMonIndex.setStatus("current")
_JnxIkeTunMonLocalGwAddr_Type = InetAddress
_JnxIkeTunMonLocalGwAddr_Object = MibTableColumn
jnxIkeTunMonLocalGwAddr = _JnxIkeTunMonLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 4),
    _JnxIkeTunMonLocalGwAddr_Type()
)
jnxIkeTunMonLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalGwAddr.setStatus("current")
_JnxIkeTunMonLocalGwAddrType_Type = InetAddressType
_JnxIkeTunMonLocalGwAddrType_Object = MibTableColumn
jnxIkeTunMonLocalGwAddrType = _JnxIkeTunMonLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 5),
    _JnxIkeTunMonLocalGwAddrType_Type()
)
jnxIkeTunMonLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalGwAddrType.setStatus("current")
_JnxIkeTunMonState_Type = JnxIkeTunStateType
_JnxIkeTunMonState_Object = MibTableColumn
jnxIkeTunMonState = _JnxIkeTunMonState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 6),
    _JnxIkeTunMonState_Type()
)
jnxIkeTunMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonState.setStatus("current")
_JnxIkeTunMonInitiatorCookie_Type = DisplayString
_JnxIkeTunMonInitiatorCookie_Object = MibTableColumn
jnxIkeTunMonInitiatorCookie = _JnxIkeTunMonInitiatorCookie_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 7),
    _JnxIkeTunMonInitiatorCookie_Type()
)
jnxIkeTunMonInitiatorCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorCookie.setStatus("current")
_JnxIkeTunMonResponderCookie_Type = DisplayString
_JnxIkeTunMonResponderCookie_Object = MibTableColumn
jnxIkeTunMonResponderCookie = _JnxIkeTunMonResponderCookie_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 8),
    _JnxIkeTunMonResponderCookie_Type()
)
jnxIkeTunMonResponderCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderCookie.setStatus("current")
_JnxIkeTunMonLocalRole_Type = JnxIkePeerRole
_JnxIkeTunMonLocalRole_Object = MibTableColumn
jnxIkeTunMonLocalRole = _JnxIkeTunMonLocalRole_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 9),
    _JnxIkeTunMonLocalRole_Type()
)
jnxIkeTunMonLocalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalRole.setStatus("current")
_JnxIkeTunMonLocalIdType_Type = JnxIkePeerType
_JnxIkeTunMonLocalIdType_Object = MibTableColumn
jnxIkeTunMonLocalIdType = _JnxIkeTunMonLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 10),
    _JnxIkeTunMonLocalIdType_Type()
)
jnxIkeTunMonLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalIdType.setStatus("current")
_JnxIkeTunMonLocalIdValue_Type = DisplayString
_JnxIkeTunMonLocalIdValue_Object = MibTableColumn
jnxIkeTunMonLocalIdValue = _JnxIkeTunMonLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 11),
    _JnxIkeTunMonLocalIdValue_Type()
)
jnxIkeTunMonLocalIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalIdValue.setStatus("current")
_JnxIkeTunMonLocalCertName_Type = DisplayString
_JnxIkeTunMonLocalCertName_Object = MibTableColumn
jnxIkeTunMonLocalCertName = _JnxIkeTunMonLocalCertName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 12),
    _JnxIkeTunMonLocalCertName_Type()
)
jnxIkeTunMonLocalCertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLocalCertName.setStatus("current")
_JnxIkeTunMonRemoteIdType_Type = JnxIkePeerType
_JnxIkeTunMonRemoteIdType_Object = MibTableColumn
jnxIkeTunMonRemoteIdType = _JnxIkeTunMonRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 13),
    _JnxIkeTunMonRemoteIdType_Type()
)
jnxIkeTunMonRemoteIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteIdType.setStatus("current")
_JnxIkeTunMonRemoteIdValue_Type = DisplayString
_JnxIkeTunMonRemoteIdValue_Object = MibTableColumn
jnxIkeTunMonRemoteIdValue = _JnxIkeTunMonRemoteIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 14),
    _JnxIkeTunMonRemoteIdValue_Type()
)
jnxIkeTunMonRemoteIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonRemoteIdValue.setStatus("current")
_JnxIkeTunMonNegoMode_Type = JnxIkeNegoMode
_JnxIkeTunMonNegoMode_Object = MibTableColumn
jnxIkeTunMonNegoMode = _JnxIkeTunMonNegoMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 15),
    _JnxIkeTunMonNegoMode_Type()
)
jnxIkeTunMonNegoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonNegoMode.setStatus("current")
_JnxIkeTunMonDiffHellmanGrp_Type = JnxDiffHellmanGrp
_JnxIkeTunMonDiffHellmanGrp_Object = MibTableColumn
jnxIkeTunMonDiffHellmanGrp = _JnxIkeTunMonDiffHellmanGrp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 16),
    _JnxIkeTunMonDiffHellmanGrp_Type()
)
jnxIkeTunMonDiffHellmanGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonDiffHellmanGrp.setStatus("current")
_JnxIkeTunMonEncryptAlgo_Type = JnxEncryptAlgo
_JnxIkeTunMonEncryptAlgo_Object = MibTableColumn
jnxIkeTunMonEncryptAlgo = _JnxIkeTunMonEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 17),
    _JnxIkeTunMonEncryptAlgo_Type()
)
jnxIkeTunMonEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonEncryptAlgo.setStatus("current")
_JnxIkeTunMonHashAlgo_Type = JnxIkeHashAlgo
_JnxIkeTunMonHashAlgo_Object = MibTableColumn
jnxIkeTunMonHashAlgo = _JnxIkeTunMonHashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 18),
    _JnxIkeTunMonHashAlgo_Type()
)
jnxIkeTunMonHashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonHashAlgo.setStatus("current")
_JnxIkeTunMonAuthMethod_Type = JnxIkeAuthMethod
_JnxIkeTunMonAuthMethod_Object = MibTableColumn
jnxIkeTunMonAuthMethod = _JnxIkeTunMonAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 19),
    _JnxIkeTunMonAuthMethod_Type()
)
jnxIkeTunMonAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonAuthMethod.setStatus("current")


class _JnxIkeTunMonLifeTime_Type(Integer32):
    """Custom type jnxIkeTunMonLifeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkeTunMonLifeTime_Type.__name__ = "Integer32"
_JnxIkeTunMonLifeTime_Object = MibTableColumn
jnxIkeTunMonLifeTime = _JnxIkeTunMonLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 20),
    _JnxIkeTunMonLifeTime_Type()
)
jnxIkeTunMonLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonLifeTime.setUnits("seconds")
_JnxIkeTunMonActiveTime_Type = TimeInterval
_JnxIkeTunMonActiveTime_Object = MibTableColumn
jnxIkeTunMonActiveTime = _JnxIkeTunMonActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 21),
    _JnxIkeTunMonActiveTime_Type()
)
jnxIkeTunMonActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonActiveTime.setStatus("current")
_JnxIkeTunMonInOctets_Type = Counter64
_JnxIkeTunMonInOctets_Object = MibTableColumn
jnxIkeTunMonInOctets = _JnxIkeTunMonInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 22),
    _JnxIkeTunMonInOctets_Type()
)
jnxIkeTunMonInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInOctets.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInOctets.setUnits("Octets")
_JnxIkeTunMonInPkts_Type = Counter32
_JnxIkeTunMonInPkts_Object = MibTableColumn
jnxIkeTunMonInPkts = _JnxIkeTunMonInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 23),
    _JnxIkeTunMonInPkts_Type()
)
jnxIkeTunMonInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInPkts.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInPkts.setUnits("Packets")
_JnxIkeTunMonOutOctets_Type = Counter64
_JnxIkeTunMonOutOctets_Object = MibTableColumn
jnxIkeTunMonOutOctets = _JnxIkeTunMonOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 24),
    _JnxIkeTunMonOutOctets_Type()
)
jnxIkeTunMonOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutOctets.setUnits("Octets")
_JnxIkeTunMonOutPkts_Type = Counter32
_JnxIkeTunMonOutPkts_Object = MibTableColumn
jnxIkeTunMonOutPkts = _JnxIkeTunMonOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 25),
    _JnxIkeTunMonOutPkts_Type()
)
jnxIkeTunMonOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonOutPkts.setUnits("Packets")
_JnxIkeTunMonXAuthUserId_Type = DisplayString
_JnxIkeTunMonXAuthUserId_Object = MibTableColumn
jnxIkeTunMonXAuthUserId = _JnxIkeTunMonXAuthUserId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 26),
    _JnxIkeTunMonXAuthUserId_Type()
)
jnxIkeTunMonXAuthUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonXAuthUserId.setStatus("current")
_JnxIkeTunMonDPDDownCount_Type = Counter32
_JnxIkeTunMonDPDDownCount_Object = MibTableColumn
jnxIkeTunMonDPDDownCount = _JnxIkeTunMonDPDDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 27),
    _JnxIkeTunMonDPDDownCount_Type()
)
jnxIkeTunMonDPDDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonDPDDownCount.setStatus("obsolete")
if mibBuilder.loadTexts:
    jnxIkeTunMonDPDDownCount.setUnits("Packets")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 28),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 29),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 30),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 31),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 32),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 33),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 34),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 35),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail.setUnits("Messages")
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail_Object = MibTableColumn
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail = _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 36),
    _JnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail.setUnits("Messages")
_JnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn_Type = Counter64
_JnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn_Object = MibTableColumn
jnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn = _JnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 37),
    _JnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn_Type()
)
jnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn.setUnits("Messages")
_JnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut_Type = Counter64
_JnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut_Object = MibTableColumn
jnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut = _JnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 38),
    _JnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut_Type()
)
jnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut.setUnits("Messages")
_JnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut_Type = Counter64
_JnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut_Object = MibTableColumn
jnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut = _JnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 39),
    _JnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut_Type()
)
jnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut.setUnits("Messages")
_JnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut_Type = Counter64
_JnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut_Object = MibTableColumn
jnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut = _JnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 40),
    _JnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut_Type()
)
jnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut.setUnits("Messages")
_JnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut_Type = Counter64
_JnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut_Object = MibTableColumn
jnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut = _JnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 41),
    _JnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut_Type()
)
jnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut.setUnits("Messages")
_JnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail_Object = MibTableColumn
jnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail = _JnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 42),
    _JnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail.setUnits("Messages")
_JnxIkeTunMonGwName_Type = DisplayString
_JnxIkeTunMonGwName_Object = MibTableColumn
jnxIkeTunMonGwName = _JnxIkeTunMonGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 43),
    _JnxIkeTunMonGwName_Type()
)
jnxIkeTunMonGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonGwName.setStatus("current")
_JnxIkeTunMonTunType_Type = JnxIkeTunType
_JnxIkeTunMonTunType_Object = MibTableColumn
jnxIkeTunMonTunType = _JnxIkeTunMonTunType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 44),
    _JnxIkeTunMonTunType_Type()
)
jnxIkeTunMonTunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeTunMonTunType.setStatus("current")
_JnxIkeGlobalStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalStats = _JnxIkeGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3)
)
_JnxIkeGlobalInitiatorIkev2SaInitStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalInitiatorIkev2SaInitStats = _JnxIkeGlobalInitiatorIkev2SaInitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1)
)
_JnxIkeGlobalInitiatorIkev2SaInitRequestOut_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitRequestOut_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitRequestOut = _JnxIkeGlobalInitiatorIkev2SaInitRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 1),
    _JnxIkeGlobalInitiatorIkev2SaInitRequestOut_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitRequestOut.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitResponseIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitResponseIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitResponseIn = _JnxIkeGlobalInitiatorIkev2SaInitResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 2),
    _JnxIkeGlobalInitiatorIkev2SaInitResponseIn_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitResponseIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi = _JnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 3),
    _JnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn = _JnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 4),
    _JnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn = _JnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 5),
    _JnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail = _JnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 6),
    _JnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail = _JnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 7),
    _JnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail = _JnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 8),
    _JnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn = _JnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 9),
    _JnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut = _JnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 10),
    _JnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut.setStatus("current")
_JnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail = _JnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 1, 11),
    _JnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail_Type()
)
jnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalResponderIkev2SaInitStats = _JnxIkeGlobalResponderIkev2SaInitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2)
)
_JnxIkeGlobalResponderIkev2SaInitRequestIn_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitRequestIn_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitRequestIn = _JnxIkeGlobalResponderIkev2SaInitRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 1),
    _JnxIkeGlobalResponderIkev2SaInitRequestIn_Type()
)
jnxIkeGlobalResponderIkev2SaInitRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitRequestIn.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitResponseOut_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitResponseOut_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitResponseOut = _JnxIkeGlobalResponderIkev2SaInitResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 2),
    _JnxIkeGlobalResponderIkev2SaInitResponseOut_Type()
)
jnxIkeGlobalResponderIkev2SaInitResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitResponseOut.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut = _JnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 3),
    _JnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut_Type()
)
jnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut = _JnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 4),
    _JnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut_Type()
)
jnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf = _JnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 5),
    _JnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf_Type()
)
jnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail = _JnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 6),
    _JnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail_Type()
)
jnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitResGetCAsFail_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitResGetCAsFail_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitResGetCAsFail = _JnxIkeGlobalResponderIkev2SaInitResGetCAsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 7),
    _JnxIkeGlobalResponderIkev2SaInitResGetCAsFail_Type()
)
jnxIkeGlobalResponderIkev2SaInitResGetCAsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitResGetCAsFail.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitResGetVidFail_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitResGetVidFail_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitResGetVidFail = _JnxIkeGlobalResponderIkev2SaInitResGetVidFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 8),
    _JnxIkeGlobalResponderIkev2SaInitResGetVidFail_Type()
)
jnxIkeGlobalResponderIkev2SaInitResGetVidFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitResGetVidFail.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail = _JnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 9),
    _JnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail_Type()
)
jnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitCookieRequestOut_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitCookieRequestOut_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitCookieRequestOut = _JnxIkeGlobalResponderIkev2SaInitCookieRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 10),
    _JnxIkeGlobalResponderIkev2SaInitCookieRequestOut_Type()
)
jnxIkeGlobalResponderIkev2SaInitCookieRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitCookieRequestOut.setStatus("current")
_JnxIkeGlobalResponderIkev2SaInitCookieResponseIn_Type = Counter64
_JnxIkeGlobalResponderIkev2SaInitCookieResponseIn_Object = MibScalar
jnxIkeGlobalResponderIkev2SaInitCookieResponseIn = _JnxIkeGlobalResponderIkev2SaInitCookieResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 2, 11),
    _JnxIkeGlobalResponderIkev2SaInitCookieResponseIn_Type()
)
jnxIkeGlobalResponderIkev2SaInitCookieResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2SaInitCookieResponseIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2AuthStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalInitiatorIkev2AuthStats = _JnxIkeGlobalInitiatorIkev2AuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 3)
)
_JnxIkeGlobalInitiatorIkev2AuthRequestOut_Type = Counter64
_JnxIkeGlobalInitiatorIkev2AuthRequestOut_Object = MibScalar
jnxIkeGlobalInitiatorIkev2AuthRequestOut = _JnxIkeGlobalInitiatorIkev2AuthRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 3, 1),
    _JnxIkeGlobalInitiatorIkev2AuthRequestOut_Type()
)
jnxIkeGlobalInitiatorIkev2AuthRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2AuthRequestOut.setStatus("current")
_JnxIkeGlobalInitiatorIkev2AuthResponseIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2AuthResponseIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2AuthResponseIn = _JnxIkeGlobalInitiatorIkev2AuthResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 3, 2),
    _JnxIkeGlobalInitiatorIkev2AuthResponseIn_Type()
)
jnxIkeGlobalInitiatorIkev2AuthResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2AuthResponseIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn = _JnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 3, 3),
    _JnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn_Type()
)
jnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn = _JnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 3, 4),
    _JnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn_Type()
)
jnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn = _JnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 3, 5),
    _JnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn_Type()
)
jnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn.setStatus("current")
_JnxIkeGlobalResponderIkev2AuthStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalResponderIkev2AuthStats = _JnxIkeGlobalResponderIkev2AuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 4)
)
_JnxIkeGlobalResponderIkev2AuthRequestIn_Type = Counter64
_JnxIkeGlobalResponderIkev2AuthRequestIn_Object = MibScalar
jnxIkeGlobalResponderIkev2AuthRequestIn = _JnxIkeGlobalResponderIkev2AuthRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 4, 1),
    _JnxIkeGlobalResponderIkev2AuthRequestIn_Type()
)
jnxIkeGlobalResponderIkev2AuthRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2AuthRequestIn.setStatus("current")
_JnxIkeGlobalResponderIkev2AuthResponseOut_Type = Counter64
_JnxIkeGlobalResponderIkev2AuthResponseOut_Object = MibScalar
jnxIkeGlobalResponderIkev2AuthResponseOut = _JnxIkeGlobalResponderIkev2AuthResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 4, 2),
    _JnxIkeGlobalResponderIkev2AuthResponseOut_Type()
)
jnxIkeGlobalResponderIkev2AuthResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2AuthResponseOut.setStatus("current")
_JnxIkeGlobalResponderIkev2AuthNoProposalChosenOut_Type = Counter64
_JnxIkeGlobalResponderIkev2AuthNoProposalChosenOut_Object = MibScalar
jnxIkeGlobalResponderIkev2AuthNoProposalChosenOut = _JnxIkeGlobalResponderIkev2AuthNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 4, 3),
    _JnxIkeGlobalResponderIkev2AuthNoProposalChosenOut_Type()
)
jnxIkeGlobalResponderIkev2AuthNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2AuthNoProposalChosenOut.setStatus("current")
_JnxIkeGlobalResponderIkev2AuthTsUnacceptableOut_Type = Counter64
_JnxIkeGlobalResponderIkev2AuthTsUnacceptableOut_Object = MibScalar
jnxIkeGlobalResponderIkev2AuthTsUnacceptableOut = _JnxIkeGlobalResponderIkev2AuthTsUnacceptableOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 4, 4),
    _JnxIkeGlobalResponderIkev2AuthTsUnacceptableOut_Type()
)
jnxIkeGlobalResponderIkev2AuthTsUnacceptableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2AuthTsUnacceptableOut.setStatus("current")
_JnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut_Type = Counter64
_JnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut_Object = MibScalar
jnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut = _JnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 4, 5),
    _JnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut_Type()
)
jnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalInitiatorIkev2IkeSaRekeyStats = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5)
)
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 1),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 2),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 3),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 4),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 5),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 6),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 7),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail = _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 5, 8),
    _JnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Type()
)
jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail.setStatus("current")
_JnxIkeGlobalResponderIkev2IkeSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalResponderIkev2IkeSaRekeyStats = _JnxIkeGlobalResponderIkev2IkeSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 6)
)
_JnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn_Type = Counter64
_JnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn_Object = MibScalar
jnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn = _JnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 6, 1),
    _JnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn_Type()
)
jnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn.setStatus("current")
_JnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut_Type = Counter64
_JnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut_Object = MibScalar
jnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut = _JnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 6, 2),
    _JnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut_Type()
)
jnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut.setStatus("current")
_JnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Type = Counter64
_JnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Object = MibScalar
jnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut = _JnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 6, 3),
    _JnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Type()
)
jnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut.setStatus("current")
_JnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Type = Counter64
_JnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Object = MibScalar
jnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut = _JnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 6, 4),
    _JnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Type()
)
jnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut.setStatus("current")
_JnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail = _JnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 6, 5),
    _JnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyStats = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7)
)
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 1),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 2),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 3),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 4),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 5),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 6),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 7),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 8),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail.setStatus("current")
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Type = Counter64
_JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Object = MibScalar
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail = _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 7, 9),
    _JnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Type()
)
jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail.setStatus("current")
_JnxIkeGlobalResponderIkev2IpsecSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalResponderIkev2IpsecSaRekeyStats = _JnxIkeGlobalResponderIkev2IpsecSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 8)
)
_JnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn_Type = Counter64
_JnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn_Object = MibScalar
jnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn = _JnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 8, 1),
    _JnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn_Type()
)
jnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn.setStatus("current")
_JnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut_Type = Counter64
_JnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut_Object = MibScalar
jnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut = _JnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 8, 2),
    _JnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut_Type()
)
jnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut.setStatus("current")
_JnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Type = Counter64
_JnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Object = MibScalar
jnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut = _JnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 8, 3),
    _JnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Type()
)
jnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut.setStatus("current")
_JnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Type = Counter64
_JnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Object = MibScalar
jnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut = _JnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 8, 4),
    _JnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Type()
)
jnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut.setStatus("current")
_JnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Type = Counter64
_JnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Object = MibScalar
jnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut = _JnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 8, 5),
    _JnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Type()
)
jnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut.setStatus("current")
_JnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail = _JnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 8, 6),
    _JnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeGlobalIkev2MsgFailStats_ObjectIdentity = ObjectIdentity
jnxIkeGlobalIkev2MsgFailStats = _JnxIkeGlobalIkev2MsgFailStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9)
)
_JnxIkeGlobalIkev2TotalDiscarded_Type = Counter64
_JnxIkeGlobalIkev2TotalDiscarded_Object = MibScalar
jnxIkeGlobalIkev2TotalDiscarded = _JnxIkeGlobalIkev2TotalDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9, 1),
    _JnxIkeGlobalIkev2TotalDiscarded_Type()
)
jnxIkeGlobalIkev2TotalDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalIkev2TotalDiscarded.setStatus("current")
_JnxIkeGlobalIkev2TotalIdError_Type = Counter64
_JnxIkeGlobalIkev2TotalIdError_Object = MibScalar
jnxIkeGlobalIkev2TotalIdError = _JnxIkeGlobalIkev2TotalIdError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9, 2),
    _JnxIkeGlobalIkev2TotalIdError_Type()
)
jnxIkeGlobalIkev2TotalIdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalIkev2TotalIdError.setStatus("current")
_JnxIkeGlobalIkev2TotalIntegrityFail_Type = Counter64
_JnxIkeGlobalIkev2TotalIntegrityFail_Object = MibScalar
jnxIkeGlobalIkev2TotalIntegrityFail = _JnxIkeGlobalIkev2TotalIntegrityFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9, 3),
    _JnxIkeGlobalIkev2TotalIntegrityFail_Type()
)
jnxIkeGlobalIkev2TotalIntegrityFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalIkev2TotalIntegrityFail.setStatus("current")
_JnxIkeGlobalIkev2TotalInvalidSPI_Type = Counter64
_JnxIkeGlobalIkev2TotalInvalidSPI_Object = MibScalar
jnxIkeGlobalIkev2TotalInvalidSPI = _JnxIkeGlobalIkev2TotalInvalidSPI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9, 4),
    _JnxIkeGlobalIkev2TotalInvalidSPI_Type()
)
jnxIkeGlobalIkev2TotalInvalidSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalIkev2TotalInvalidSPI.setStatus("current")
_JnxIkeGlobalIkev2TotalInvalidExchgType_Type = Counter64
_JnxIkeGlobalIkev2TotalInvalidExchgType_Object = MibScalar
jnxIkeGlobalIkev2TotalInvalidExchgType = _JnxIkeGlobalIkev2TotalInvalidExchgType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9, 5),
    _JnxIkeGlobalIkev2TotalInvalidExchgType_Type()
)
jnxIkeGlobalIkev2TotalInvalidExchgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalIkev2TotalInvalidExchgType.setStatus("current")
_JnxIkeGlobalIkev2TotalInvalidLength_Type = Counter64
_JnxIkeGlobalIkev2TotalInvalidLength_Object = MibScalar
jnxIkeGlobalIkev2TotalInvalidLength = _JnxIkeGlobalIkev2TotalInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9, 6),
    _JnxIkeGlobalIkev2TotalInvalidLength_Type()
)
jnxIkeGlobalIkev2TotalInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalIkev2TotalInvalidLength.setStatus("current")
_JnxIkeGlobalIkev2TotalDisorder_Type = Counter64
_JnxIkeGlobalIkev2TotalDisorder_Object = MibScalar
jnxIkeGlobalIkev2TotalDisorder = _JnxIkeGlobalIkev2TotalDisorder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 3, 9, 7),
    _JnxIkeGlobalIkev2TotalDisorder_Type()
)
jnxIkeGlobalIkev2TotalDisorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeGlobalIkev2TotalDisorder.setStatus("current")
_JnxIkePeerAddrTable_Object = MibTable
jnxIkePeerAddrTable = _JnxIkePeerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxIkePeerAddrTable.setStatus("current")
_JnxIkePeerAddrEntry_Object = MibTableRow
jnxIkePeerAddrEntry = _JnxIkePeerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1)
)
jnxIkePeerAddrEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrState"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrRemoteGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrRemoteGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrRemotePort"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrLocalGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrLocalGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrLocalPort"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerAddrRoutingInstance"),
)
if mibBuilder.loadTexts:
    jnxIkePeerAddrEntry.setStatus("current")
_JnxIkePeerAddrState_Type = JnxPeerStateType
_JnxIkePeerAddrState_Object = MibTableColumn
jnxIkePeerAddrState = _JnxIkePeerAddrState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 1),
    _JnxIkePeerAddrState_Type()
)
jnxIkePeerAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrState.setStatus("current")
_JnxIkePeerAddrRemoteGwAddrType_Type = InetAddressType
_JnxIkePeerAddrRemoteGwAddrType_Object = MibTableColumn
jnxIkePeerAddrRemoteGwAddrType = _JnxIkePeerAddrRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 2),
    _JnxIkePeerAddrRemoteGwAddrType_Type()
)
jnxIkePeerAddrRemoteGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrRemoteGwAddrType.setStatus("current")
_JnxIkePeerAddrRemoteGwAddr_Type = InetAddress
_JnxIkePeerAddrRemoteGwAddr_Object = MibTableColumn
jnxIkePeerAddrRemoteGwAddr = _JnxIkePeerAddrRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 3),
    _JnxIkePeerAddrRemoteGwAddr_Type()
)
jnxIkePeerAddrRemoteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrRemoteGwAddr.setStatus("current")
_JnxIkePeerAddrRemotePort_Type = InetPortNumber
_JnxIkePeerAddrRemotePort_Object = MibTableColumn
jnxIkePeerAddrRemotePort = _JnxIkePeerAddrRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 4),
    _JnxIkePeerAddrRemotePort_Type()
)
jnxIkePeerAddrRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrRemotePort.setStatus("current")
_JnxIkePeerAddrLocalGwAddrType_Type = InetAddressType
_JnxIkePeerAddrLocalGwAddrType_Object = MibTableColumn
jnxIkePeerAddrLocalGwAddrType = _JnxIkePeerAddrLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 5),
    _JnxIkePeerAddrLocalGwAddrType_Type()
)
jnxIkePeerAddrLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrLocalGwAddrType.setStatus("current")
_JnxIkePeerAddrLocalGwAddr_Type = InetAddress
_JnxIkePeerAddrLocalGwAddr_Object = MibTableColumn
jnxIkePeerAddrLocalGwAddr = _JnxIkePeerAddrLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 6),
    _JnxIkePeerAddrLocalGwAddr_Type()
)
jnxIkePeerAddrLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrLocalGwAddr.setStatus("current")
_JnxIkePeerAddrLocalPort_Type = InetPortNumber
_JnxIkePeerAddrLocalPort_Object = MibTableColumn
jnxIkePeerAddrLocalPort = _JnxIkePeerAddrLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 7),
    _JnxIkePeerAddrLocalPort_Type()
)
jnxIkePeerAddrLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrLocalPort.setStatus("current")
_JnxIkePeerAddrRoutingInstance_Type = DisplayString
_JnxIkePeerAddrRoutingInstance_Object = MibTableColumn
jnxIkePeerAddrRoutingInstance = _JnxIkePeerAddrRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 8),
    _JnxIkePeerAddrRoutingInstance_Type()
)
jnxIkePeerAddrRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrRoutingInstance.setStatus("current")


class _JnxIkePeerAddrIndex_Type(Integer32):
    """Custom type jnxIkePeerAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkePeerAddrIndex_Type.__name__ = "Integer32"
_JnxIkePeerAddrIndex_Object = MibTableColumn
jnxIkePeerAddrIndex = _JnxIkePeerAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 4, 1, 9),
    _JnxIkePeerAddrIndex_Type()
)
jnxIkePeerAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerAddrIndex.setStatus("current")
_JnxIkePeerIdTable_Object = MibTable
jnxIkePeerIdTable = _JnxIkePeerIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxIkePeerIdTable.setStatus("current")
_JnxIkePeerIdEntry_Object = MibTableRow
jnxIkePeerIdEntry = _JnxIkePeerIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1)
)
jnxIkePeerIdEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerIdState"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerIdRemoteIdType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerIdRemoteIdValue"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerIdLocalIdType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerIdLocalIdValue"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerIdAAAUserName"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerInternalIndex"),
)
if mibBuilder.loadTexts:
    jnxIkePeerIdEntry.setStatus("current")
_JnxIkePeerIdState_Type = JnxPeerStateType
_JnxIkePeerIdState_Object = MibTableColumn
jnxIkePeerIdState = _JnxIkePeerIdState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 1),
    _JnxIkePeerIdState_Type()
)
jnxIkePeerIdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerIdState.setStatus("current")
_JnxIkePeerIdRemoteIdType_Type = JnxIkePeerType
_JnxIkePeerIdRemoteIdType_Object = MibTableColumn
jnxIkePeerIdRemoteIdType = _JnxIkePeerIdRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 2),
    _JnxIkePeerIdRemoteIdType_Type()
)
jnxIkePeerIdRemoteIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerIdRemoteIdType.setStatus("current")
_JnxIkePeerIdRemoteIdValue_Type = DisplayString
_JnxIkePeerIdRemoteIdValue_Object = MibTableColumn
jnxIkePeerIdRemoteIdValue = _JnxIkePeerIdRemoteIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 3),
    _JnxIkePeerIdRemoteIdValue_Type()
)
jnxIkePeerIdRemoteIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerIdRemoteIdValue.setStatus("current")
_JnxIkePeerIdLocalIdType_Type = JnxIkePeerType
_JnxIkePeerIdLocalIdType_Object = MibTableColumn
jnxIkePeerIdLocalIdType = _JnxIkePeerIdLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 4),
    _JnxIkePeerIdLocalIdType_Type()
)
jnxIkePeerIdLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerIdLocalIdType.setStatus("current")
_JnxIkePeerIdLocalIdValue_Type = DisplayString
_JnxIkePeerIdLocalIdValue_Object = MibTableColumn
jnxIkePeerIdLocalIdValue = _JnxIkePeerIdLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 5),
    _JnxIkePeerIdLocalIdValue_Type()
)
jnxIkePeerIdLocalIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerIdLocalIdValue.setStatus("current")
_JnxIkePeerIdAAAUserName_Type = DisplayString
_JnxIkePeerIdAAAUserName_Object = MibTableColumn
jnxIkePeerIdAAAUserName = _JnxIkePeerIdAAAUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 6),
    _JnxIkePeerIdAAAUserName_Type()
)
jnxIkePeerIdAAAUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerIdAAAUserName.setStatus("current")


class _JnxIkePeerInternalIndex_Type(Integer32):
    """Custom type jnxIkePeerInternalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkePeerInternalIndex_Type.__name__ = "Integer32"
_JnxIkePeerInternalIndex_Object = MibTableColumn
jnxIkePeerInternalIndex = _JnxIkePeerInternalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 7),
    _JnxIkePeerInternalIndex_Type()
)
jnxIkePeerInternalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIkePeerInternalIndex.setStatus("current")


class _JnxIkePeerIdIndex_Type(Integer32):
    """Custom type jnxIkePeerIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkePeerIdIndex_Type.__name__ = "Integer32"
_JnxIkePeerIdIndex_Object = MibTableColumn
jnxIkePeerIdIndex = _JnxIkePeerIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 5, 1, 8),
    _JnxIkePeerIdIndex_Type()
)
jnxIkePeerIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerIdIndex.setStatus("current")
_JnxIkePeerStatsTable_Object = MibTable
jnxIkePeerStatsTable = _JnxIkePeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxIkePeerStatsTable.setStatus("current")
_JnxIkePeerStatsEntry_Object = MibTableRow
jnxIkePeerStatsEntry = _JnxIkePeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1)
)
jnxIkePeerStatsEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerStatsState"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkePeerStatsIndex"),
)
if mibBuilder.loadTexts:
    jnxIkePeerStatsEntry.setStatus("current")
_JnxIkePeerStatsState_Type = JnxPeerStateType
_JnxIkePeerStatsState_Object = MibTableColumn
jnxIkePeerStatsState = _JnxIkePeerStatsState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 1),
    _JnxIkePeerStatsState_Type()
)
jnxIkePeerStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsState.setStatus("current")


class _JnxIkePeerStatsIndex_Type(Integer32):
    """Custom type jnxIkePeerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIkePeerStatsIndex_Type.__name__ = "Integer32"
_JnxIkePeerStatsIndex_Object = MibTableColumn
jnxIkePeerStatsIndex = _JnxIkePeerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 2),
    _JnxIkePeerStatsIndex_Type()
)
jnxIkePeerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIndex.setStatus("current")
_JnxIkePeerStatsRemoteGwAddrType_Type = InetAddressType
_JnxIkePeerStatsRemoteGwAddrType_Object = MibTableColumn
jnxIkePeerStatsRemoteGwAddrType = _JnxIkePeerStatsRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 3),
    _JnxIkePeerStatsRemoteGwAddrType_Type()
)
jnxIkePeerStatsRemoteGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsRemoteGwAddrType.setStatus("current")
_JnxIkePeerStatsRemoteGwAddr_Type = InetAddress
_JnxIkePeerStatsRemoteGwAddr_Object = MibTableColumn
jnxIkePeerStatsRemoteGwAddr = _JnxIkePeerStatsRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 4),
    _JnxIkePeerStatsRemoteGwAddr_Type()
)
jnxIkePeerStatsRemoteGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsRemoteGwAddr.setStatus("current")
_JnxIkePeerStatsRemotePort_Type = InetPortNumber
_JnxIkePeerStatsRemotePort_Object = MibTableColumn
jnxIkePeerStatsRemotePort = _JnxIkePeerStatsRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 5),
    _JnxIkePeerStatsRemotePort_Type()
)
jnxIkePeerStatsRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsRemotePort.setStatus("current")
_JnxIkePeerStatsLocalGwAddrType_Type = InetAddressType
_JnxIkePeerStatsLocalGwAddrType_Object = MibTableColumn
jnxIkePeerStatsLocalGwAddrType = _JnxIkePeerStatsLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 6),
    _JnxIkePeerStatsLocalGwAddrType_Type()
)
jnxIkePeerStatsLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsLocalGwAddrType.setStatus("current")
_JnxIkePeerStatsLocalGwAddr_Type = InetAddress
_JnxIkePeerStatsLocalGwAddr_Object = MibTableColumn
jnxIkePeerStatsLocalGwAddr = _JnxIkePeerStatsLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 7),
    _JnxIkePeerStatsLocalGwAddr_Type()
)
jnxIkePeerStatsLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsLocalGwAddr.setStatus("current")
_JnxIkePeerStatsLocalPort_Type = InetPortNumber
_JnxIkePeerStatsLocalPort_Object = MibTableColumn
jnxIkePeerStatsLocalPort = _JnxIkePeerStatsLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 8),
    _JnxIkePeerStatsLocalPort_Type()
)
jnxIkePeerStatsLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsLocalPort.setStatus("current")
_JnxIkePeerStatsRoutingInstance_Type = DisplayString
_JnxIkePeerStatsRoutingInstance_Object = MibTableColumn
jnxIkePeerStatsRoutingInstance = _JnxIkePeerStatsRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 9),
    _JnxIkePeerStatsRoutingInstance_Type()
)
jnxIkePeerStatsRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsRoutingInstance.setStatus("current")
_JnxIkePeerStatsRemoteIdType_Type = JnxIkePeerType
_JnxIkePeerStatsRemoteIdType_Object = MibTableColumn
jnxIkePeerStatsRemoteIdType = _JnxIkePeerStatsRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 10),
    _JnxIkePeerStatsRemoteIdType_Type()
)
jnxIkePeerStatsRemoteIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsRemoteIdType.setStatus("current")
_JnxIkePeerStatsRemoteIdValue_Type = DisplayString
_JnxIkePeerStatsRemoteIdValue_Object = MibTableColumn
jnxIkePeerStatsRemoteIdValue = _JnxIkePeerStatsRemoteIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 11),
    _JnxIkePeerStatsRemoteIdValue_Type()
)
jnxIkePeerStatsRemoteIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsRemoteIdValue.setStatus("current")
_JnxIkePeerStatsLocalIdType_Type = JnxIkePeerType
_JnxIkePeerStatsLocalIdType_Object = MibTableColumn
jnxIkePeerStatsLocalIdType = _JnxIkePeerStatsLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 12),
    _JnxIkePeerStatsLocalIdType_Type()
)
jnxIkePeerStatsLocalIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsLocalIdType.setStatus("current")
_JnxIkePeerStatsLocalIdValue_Type = DisplayString
_JnxIkePeerStatsLocalIdValue_Object = MibTableColumn
jnxIkePeerStatsLocalIdValue = _JnxIkePeerStatsLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 13),
    _JnxIkePeerStatsLocalIdValue_Type()
)
jnxIkePeerStatsLocalIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsLocalIdValue.setStatus("current")
_JnxIkePeerStatsAAAUserName_Type = DisplayString
_JnxIkePeerStatsAAAUserName_Object = MibTableColumn
jnxIkePeerStatsAAAUserName = _JnxIkePeerStatsAAAUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 14),
    _JnxIkePeerStatsAAAUserName_Type()
)
jnxIkePeerStatsAAAUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsAAAUserName.setStatus("current")
_JnxIkePeerStatsGwName_Type = DisplayString
_JnxIkePeerStatsGwName_Object = MibTableColumn
jnxIkePeerStatsGwName = _JnxIkePeerStatsGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 15),
    _JnxIkePeerStatsGwName_Type()
)
jnxIkePeerStatsGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsGwName.setStatus("current")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 16),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 17),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 18),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 19),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 20),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 21),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 22),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 23),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 24),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 25),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail = _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 26),
    _JnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn = _JnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 27),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut = _JnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 28),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut = _JnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 29),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut = _JnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 30),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf = _JnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 31),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail = _JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 32),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail = _JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 33),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail = _JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 34),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail = _JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 35),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut = _JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 36),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn = _JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 37),
    _JnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut = _JnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 38),
    _JnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn = _JnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 39),
    _JnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn = _JnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 40),
    _JnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn = _JnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 41),
    _JnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn = _JnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 42),
    _JnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn = _JnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 43),
    _JnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut = _JnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 44),
    _JnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut = _JnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 45),
    _JnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut = _JnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 46),
    _JnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut = _JnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 47),
    _JnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 48),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 49),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 50),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 51),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 52),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 53),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 54),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 55),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn = _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 56),
    _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut = _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 57),
    _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut = _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 58),
    _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut = _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 59),
    _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail = _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 60),
    _JnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 61),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 62),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 63),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 64),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 65),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 66),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 67),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 68),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail_Type = Counter64
_JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail = _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 69),
    _JnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail_Type()
)
jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn = _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 70),
    _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut = _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 71),
    _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut = _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 72),
    _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut = _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 73),
    _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut = _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 74),
    _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut.setUnits("Messages")
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail_Type = Counter64
_JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail_Object = MibTableColumn
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail = _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 75),
    _JnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail_Type()
)
jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail.setUnits("Messages")
_JnxIkePeerStatsTunType_Type = JnxIkeTunType
_JnxIkePeerStatsTunType_Object = MibTableColumn
jnxIkePeerStatsTunType = _JnxIkePeerStatsTunType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 6, 1, 76),
    _JnxIkePeerStatsTunType_Type()
)
jnxIkePeerStatsTunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkePeerStatsTunType.setStatus("current")
_JnxPeerIkeSaCorrTable_Object = MibTable
jnxPeerIkeSaCorrTable = _JnxPeerIkeSaCorrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxPeerIkeSaCorrTable.setStatus("current")
_JnxPeerIkeSaCorrEntry_Object = MibTableRow
jnxPeerIkeSaCorrEntry = _JnxPeerIkeSaCorrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 7, 1)
)
jnxPeerIkeSaCorrEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxPeerIkeSaCorrPeerIndex"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxPeerIkeSaCorrIntIndex"),
)
if mibBuilder.loadTexts:
    jnxPeerIkeSaCorrEntry.setStatus("current")


class _JnxPeerIkeSaCorrPeerIndex_Type(Integer32):
    """Custom type jnxPeerIkeSaCorrPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxPeerIkeSaCorrPeerIndex_Type.__name__ = "Integer32"
_JnxPeerIkeSaCorrPeerIndex_Object = MibTableColumn
jnxPeerIkeSaCorrPeerIndex = _JnxPeerIkeSaCorrPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 7, 1, 1),
    _JnxPeerIkeSaCorrPeerIndex_Type()
)
jnxPeerIkeSaCorrPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPeerIkeSaCorrPeerIndex.setStatus("current")


class _JnxPeerIkeSaCorrIntIndex_Type(Integer32):
    """Custom type jnxPeerIkeSaCorrIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxPeerIkeSaCorrIntIndex_Type.__name__ = "Integer32"
_JnxPeerIkeSaCorrIntIndex_Object = MibTableColumn
jnxPeerIkeSaCorrIntIndex = _JnxPeerIkeSaCorrIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 7, 1, 2),
    _JnxPeerIkeSaCorrIntIndex_Type()
)
jnxPeerIkeSaCorrIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPeerIkeSaCorrIntIndex.setStatus("current")


class _JnxPeerIkeSaCorrIkeTunMonIndex_Type(Integer32):
    """Custom type jnxPeerIkeSaCorrIkeTunMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxPeerIkeSaCorrIkeTunMonIndex_Type.__name__ = "Integer32"
_JnxPeerIkeSaCorrIkeTunMonIndex_Object = MibTableColumn
jnxPeerIkeSaCorrIkeTunMonIndex = _JnxPeerIkeSaCorrIkeTunMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 7, 1, 3),
    _JnxPeerIkeSaCorrIkeTunMonIndex_Type()
)
jnxPeerIkeSaCorrIkeTunMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerIkeSaCorrIkeTunMonIndex.setStatus("current")
_JnxPeerIPSecTunnelCorrTable_Object = MibTable
jnxPeerIPSecTunnelCorrTable = _JnxPeerIPSecTunnelCorrTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 8)
)
if mibBuilder.loadTexts:
    jnxPeerIPSecTunnelCorrTable.setStatus("current")
_JnxPeerIPSecTunnelCorrEntry_Object = MibTableRow
jnxPeerIPSecTunnelCorrEntry = _JnxPeerIPSecTunnelCorrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 8, 1)
)
jnxPeerIPSecTunnelCorrEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxPeerIPSecTunnelCorrPeerIndex"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxPeerIPSecTunnelCorrIntIndex"),
)
if mibBuilder.loadTexts:
    jnxPeerIPSecTunnelCorrEntry.setStatus("current")


class _JnxPeerIPSecTunnelCorrPeerIndex_Type(Integer32):
    """Custom type jnxPeerIPSecTunnelCorrPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxPeerIPSecTunnelCorrPeerIndex_Type.__name__ = "Integer32"
_JnxPeerIPSecTunnelCorrPeerIndex_Object = MibTableColumn
jnxPeerIPSecTunnelCorrPeerIndex = _JnxPeerIPSecTunnelCorrPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 8, 1, 1),
    _JnxPeerIPSecTunnelCorrPeerIndex_Type()
)
jnxPeerIPSecTunnelCorrPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPeerIPSecTunnelCorrPeerIndex.setStatus("current")


class _JnxPeerIPSecTunnelCorrIntIndex_Type(Integer32):
    """Custom type jnxPeerIPSecTunnelCorrIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxPeerIPSecTunnelCorrIntIndex_Type.__name__ = "Integer32"
_JnxPeerIPSecTunnelCorrIntIndex_Object = MibTableColumn
jnxPeerIPSecTunnelCorrIntIndex = _JnxPeerIPSecTunnelCorrIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 8, 1, 2),
    _JnxPeerIPSecTunnelCorrIntIndex_Type()
)
jnxPeerIPSecTunnelCorrIntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPeerIPSecTunnelCorrIntIndex.setStatus("current")


class _JnxPeerIPSecTunnelCorrIPSecTunMonIndex_Type(Integer32):
    """Custom type jnxPeerIPSecTunnelCorrIPSecTunMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxPeerIPSecTunnelCorrIPSecTunMonIndex_Type.__name__ = "Integer32"
_JnxPeerIPSecTunnelCorrIPSecTunMonIndex_Object = MibTableColumn
jnxPeerIPSecTunnelCorrIPSecTunMonIndex = _JnxPeerIPSecTunnelCorrIPSecTunMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 8, 1, 3),
    _JnxPeerIPSecTunnelCorrIPSecTunMonIndex_Type()
)
jnxPeerIPSecTunnelCorrIPSecTunMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPeerIPSecTunnelCorrIPSecTunMonIndex.setStatus("current")
_JnxIkeHaLinkGlobalStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalStats = _JnxIkeHaLinkGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9)
)
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalInitiatorIkev2SaInitStats = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1)
)
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 1),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 2),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 3),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 4),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 5),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 6),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 7),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 8),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 9),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut = _JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 1, 10),
    _JnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalResponderIkev2SaInitStats = _JnxIkeHaLinkGlobalResponderIkev2SaInitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2)
)
_JnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn = _JnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 1),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut = _JnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 2),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut = _JnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 3),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut = _JnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 4),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf = _JnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 5),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail = _JnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 6),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail = _JnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 7),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail = _JnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 8),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail = _JnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 9),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut = _JnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 10),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn = _JnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 2, 11),
    _JnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn_Type()
)
jnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2AuthStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalInitiatorIkev2AuthStats = _JnxIkeHaLinkGlobalInitiatorIkev2AuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 3)
)
_JnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut = _JnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 3, 1),
    _JnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn = _JnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 3, 2),
    _JnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn = _JnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 3, 3),
    _JnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn = _JnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 3, 4),
    _JnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn = _JnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 3, 5),
    _JnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2AuthStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalResponderIkev2AuthStats = _JnxIkeHaLinkGlobalResponderIkev2AuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 4)
)
_JnxIkeHaLinkGlobalResponderIkev2AuthRequestIn_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2AuthRequestIn_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2AuthRequestIn = _JnxIkeHaLinkGlobalResponderIkev2AuthRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 4, 1),
    _JnxIkeHaLinkGlobalResponderIkev2AuthRequestIn_Type()
)
jnxIkeHaLinkGlobalResponderIkev2AuthRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2AuthRequestIn.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2AuthResponseOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2AuthResponseOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2AuthResponseOut = _JnxIkeHaLinkGlobalResponderIkev2AuthResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 4, 2),
    _JnxIkeHaLinkGlobalResponderIkev2AuthResponseOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2AuthResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2AuthResponseOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut = _JnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 4, 3),
    _JnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut = _JnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 4, 4),
    _JnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut = _JnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 4, 5),
    _JnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyStats = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5)
)
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 1),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 2),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 3),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 4),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 5),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 6),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 7),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail = _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 5, 8),
    _JnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyStats = _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 6)
)
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn = _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 6, 1),
    _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut = _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 6, 2),
    _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut = _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 6, 3),
    _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut = _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 6, 4),
    _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail = _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 6, 5),
    _JnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyStats = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7)
)
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 1),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 2),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 3),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 4),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 5),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 6),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 7),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 8),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail.setStatus("current")
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Type = Counter64
_JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Object = MibScalar
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail = _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 7, 9),
    _JnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail_Type()
)
jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyStats = _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 8)
)
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn = _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 8, 1),
    _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut = _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 8, 2),
    _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut = _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 8, 3),
    _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut = _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 8, 4),
    _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut = _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 8, 5),
    _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut.setStatus("current")
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Type = Counter64
_JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Object = MibScalar
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail = _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 8, 6),
    _JnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail_Type()
)
jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail.setStatus("current")
_JnxIkeHaLinkGlobalIkev2MsgFailStats_ObjectIdentity = ObjectIdentity
jnxIkeHaLinkGlobalIkev2MsgFailStats = _JnxIkeHaLinkGlobalIkev2MsgFailStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9)
)
_JnxIkeHaLinkGlobalIkev2TotalDiscarded_Type = Counter64
_JnxIkeHaLinkGlobalIkev2TotalDiscarded_Object = MibScalar
jnxIkeHaLinkGlobalIkev2TotalDiscarded = _JnxIkeHaLinkGlobalIkev2TotalDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9, 1),
    _JnxIkeHaLinkGlobalIkev2TotalDiscarded_Type()
)
jnxIkeHaLinkGlobalIkev2TotalDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalIkev2TotalDiscarded.setStatus("current")
_JnxIkeHaLinkGlobalIkev2TotalIdError_Type = Counter64
_JnxIkeHaLinkGlobalIkev2TotalIdError_Object = MibScalar
jnxIkeHaLinkGlobalIkev2TotalIdError = _JnxIkeHaLinkGlobalIkev2TotalIdError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9, 2),
    _JnxIkeHaLinkGlobalIkev2TotalIdError_Type()
)
jnxIkeHaLinkGlobalIkev2TotalIdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalIkev2TotalIdError.setStatus("current")
_JnxIkeHaLinkGlobalIkev2TotalIntegrityFail_Type = Counter64
_JnxIkeHaLinkGlobalIkev2TotalIntegrityFail_Object = MibScalar
jnxIkeHaLinkGlobalIkev2TotalIntegrityFail = _JnxIkeHaLinkGlobalIkev2TotalIntegrityFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9, 3),
    _JnxIkeHaLinkGlobalIkev2TotalIntegrityFail_Type()
)
jnxIkeHaLinkGlobalIkev2TotalIntegrityFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalIkev2TotalIntegrityFail.setStatus("current")
_JnxIkeHaLinkGlobalIkev2TotalInvalidSPI_Type = Counter64
_JnxIkeHaLinkGlobalIkev2TotalInvalidSPI_Object = MibScalar
jnxIkeHaLinkGlobalIkev2TotalInvalidSPI = _JnxIkeHaLinkGlobalIkev2TotalInvalidSPI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9, 4),
    _JnxIkeHaLinkGlobalIkev2TotalInvalidSPI_Type()
)
jnxIkeHaLinkGlobalIkev2TotalInvalidSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalIkev2TotalInvalidSPI.setStatus("current")
_JnxIkeHaLinkGlobalIkev2TotalInvalidExchgType_Type = Counter64
_JnxIkeHaLinkGlobalIkev2TotalInvalidExchgType_Object = MibScalar
jnxIkeHaLinkGlobalIkev2TotalInvalidExchgType = _JnxIkeHaLinkGlobalIkev2TotalInvalidExchgType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9, 5),
    _JnxIkeHaLinkGlobalIkev2TotalInvalidExchgType_Type()
)
jnxIkeHaLinkGlobalIkev2TotalInvalidExchgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalIkev2TotalInvalidExchgType.setStatus("current")
_JnxIkeHaLinkGlobalIkev2TotalInvalidLength_Type = Counter64
_JnxIkeHaLinkGlobalIkev2TotalInvalidLength_Object = MibScalar
jnxIkeHaLinkGlobalIkev2TotalInvalidLength = _JnxIkeHaLinkGlobalIkev2TotalInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9, 6),
    _JnxIkeHaLinkGlobalIkev2TotalInvalidLength_Type()
)
jnxIkeHaLinkGlobalIkev2TotalInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalIkev2TotalInvalidLength.setStatus("current")
_JnxIkeHaLinkGlobalIkev2TotalDisorder_Type = Counter64
_JnxIkeHaLinkGlobalIkev2TotalDisorder_Object = MibScalar
jnxIkeHaLinkGlobalIkev2TotalDisorder = _JnxIkeHaLinkGlobalIkev2TotalDisorder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 9, 9, 7),
    _JnxIkeHaLinkGlobalIkev2TotalDisorder_Type()
)
jnxIkeHaLinkGlobalIkev2TotalDisorder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIkeHaLinkGlobalIkev2TotalDisorder.setStatus("current")
_JnxIpSecFlowMonPhaseTwo_ObjectIdentity = ObjectIdentity
jnxIpSecFlowMonPhaseTwo = _JnxIpSecFlowMonPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2)
)
_JnxIpSecNumOfTunnels_Type = Integer32
_JnxIpSecNumOfTunnels_Object = MibScalar
jnxIpSecNumOfTunnels = _JnxIpSecNumOfTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 1),
    _JnxIpSecNumOfTunnels_Type()
)
jnxIpSecNumOfTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecNumOfTunnels.setStatus("current")
_JnxIpSecTunnelMonTable_Object = MibTable
jnxIpSecTunnelMonTable = _JnxIpSecTunnelMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxIpSecTunnelMonTable.setStatus("current")
_JnxIpSecTunnelMonEntry_Object = MibTableRow
jnxIpSecTunnelMonEntry = _JnxIpSecTunnelMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1)
)
jnxIpSecTunnelMonEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonIndex"),
)
if mibBuilder.loadTexts:
    jnxIpSecTunnelMonEntry.setStatus("current")
_JnxIpSecTunMonRemoteGwAddrType_Type = InetAddressType
_JnxIpSecTunMonRemoteGwAddrType_Object = MibTableColumn
jnxIpSecTunMonRemoteGwAddrType = _JnxIpSecTunMonRemoteGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 1),
    _JnxIpSecTunMonRemoteGwAddrType_Type()
)
jnxIpSecTunMonRemoteGwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemoteGwAddrType.setStatus("current")
_JnxIpSecTunMonRemoteGwAddr_Type = InetAddress
_JnxIpSecTunMonRemoteGwAddr_Object = MibTableColumn
jnxIpSecTunMonRemoteGwAddr = _JnxIpSecTunMonRemoteGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 2),
    _JnxIpSecTunMonRemoteGwAddr_Type()
)
jnxIpSecTunMonRemoteGwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemoteGwAddr.setStatus("current")


class _JnxIpSecTunMonIndex_Type(Integer32):
    """Custom type jnxIpSecTunMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxIpSecTunMonIndex_Type.__name__ = "Integer32"
_JnxIpSecTunMonIndex_Object = MibTableColumn
jnxIpSecTunMonIndex = _JnxIpSecTunMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 3),
    _JnxIpSecTunMonIndex_Type()
)
jnxIpSecTunMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecTunMonIndex.setStatus("current")
_JnxIpSecTunMonLocalGwAddrType_Type = InetAddressType
_JnxIpSecTunMonLocalGwAddrType_Object = MibTableColumn
jnxIpSecTunMonLocalGwAddrType = _JnxIpSecTunMonLocalGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 4),
    _JnxIpSecTunMonLocalGwAddrType_Type()
)
jnxIpSecTunMonLocalGwAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonLocalGwAddrType.setStatus("current")
_JnxIpSecTunMonLocalGwAddr_Type = InetAddress
_JnxIpSecTunMonLocalGwAddr_Object = MibTableColumn
jnxIpSecTunMonLocalGwAddr = _JnxIpSecTunMonLocalGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 5),
    _JnxIpSecTunMonLocalGwAddr_Type()
)
jnxIpSecTunMonLocalGwAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonLocalGwAddr.setStatus("current")
_JnxIpSecTunMonLocalProxyId_Type = DisplayString
_JnxIpSecTunMonLocalProxyId_Object = MibTableColumn
jnxIpSecTunMonLocalProxyId = _JnxIpSecTunMonLocalProxyId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 6),
    _JnxIpSecTunMonLocalProxyId_Type()
)
jnxIpSecTunMonLocalProxyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonLocalProxyId.setStatus("current")
_JnxIpSecTunMonRemoteProxyId_Type = DisplayString
_JnxIpSecTunMonRemoteProxyId_Object = MibTableColumn
jnxIpSecTunMonRemoteProxyId = _JnxIpSecTunMonRemoteProxyId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 7),
    _JnxIpSecTunMonRemoteProxyId_Type()
)
jnxIpSecTunMonRemoteProxyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemoteProxyId.setStatus("current")
_JnxIpSecTunMonKeyType_Type = JnxKeyType
_JnxIpSecTunMonKeyType_Object = MibTableColumn
jnxIpSecTunMonKeyType = _JnxIpSecTunMonKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 8),
    _JnxIpSecTunMonKeyType_Type()
)
jnxIpSecTunMonKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonKeyType.setStatus("current")
_JnxIpSecTunMonRemotePeerType_Type = JnxRemotePeerType
_JnxIpSecTunMonRemotePeerType_Object = MibTableColumn
jnxIpSecTunMonRemotePeerType = _JnxIpSecTunMonRemotePeerType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 9),
    _JnxIpSecTunMonRemotePeerType_Type()
)
jnxIpSecTunMonRemotePeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonRemotePeerType.setStatus("current")
_JnxIpSecTunMonOutEncryptedBytes_Type = Counter64
_JnxIpSecTunMonOutEncryptedBytes_Object = MibTableColumn
jnxIpSecTunMonOutEncryptedBytes = _JnxIpSecTunMonOutEncryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 10),
    _JnxIpSecTunMonOutEncryptedBytes_Type()
)
jnxIpSecTunMonOutEncryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonOutEncryptedBytes.setStatus("current")
_JnxIpSecTunMonOutEncryptedPkts_Type = Counter64
_JnxIpSecTunMonOutEncryptedPkts_Object = MibTableColumn
jnxIpSecTunMonOutEncryptedPkts = _JnxIpSecTunMonOutEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 11),
    _JnxIpSecTunMonOutEncryptedPkts_Type()
)
jnxIpSecTunMonOutEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonOutEncryptedPkts.setStatus("current")
_JnxIpSecTunMonInDecryptedBytes_Type = Counter64
_JnxIpSecTunMonInDecryptedBytes_Object = MibTableColumn
jnxIpSecTunMonInDecryptedBytes = _JnxIpSecTunMonInDecryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 12),
    _JnxIpSecTunMonInDecryptedBytes_Type()
)
jnxIpSecTunMonInDecryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonInDecryptedBytes.setStatus("current")
_JnxIpSecTunMonInDecryptedPkts_Type = Counter64
_JnxIpSecTunMonInDecryptedPkts_Object = MibTableColumn
jnxIpSecTunMonInDecryptedPkts = _JnxIpSecTunMonInDecryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 13),
    _JnxIpSecTunMonInDecryptedPkts_Type()
)
jnxIpSecTunMonInDecryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonInDecryptedPkts.setStatus("current")
_JnxIpSecTunMonAHInBytes_Type = Counter64
_JnxIpSecTunMonAHInBytes_Object = MibTableColumn
jnxIpSecTunMonAHInBytes = _JnxIpSecTunMonAHInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 14),
    _JnxIpSecTunMonAHInBytes_Type()
)
jnxIpSecTunMonAHInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHInBytes.setStatus("current")
_JnxIpSecTunMonAHInPkts_Type = Counter64
_JnxIpSecTunMonAHInPkts_Object = MibTableColumn
jnxIpSecTunMonAHInPkts = _JnxIpSecTunMonAHInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 15),
    _JnxIpSecTunMonAHInPkts_Type()
)
jnxIpSecTunMonAHInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHInPkts.setStatus("current")
_JnxIpSecTunMonAHOutBytes_Type = Counter64
_JnxIpSecTunMonAHOutBytes_Object = MibTableColumn
jnxIpSecTunMonAHOutBytes = _JnxIpSecTunMonAHOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 16),
    _JnxIpSecTunMonAHOutBytes_Type()
)
jnxIpSecTunMonAHOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHOutBytes.setStatus("current")
_JnxIpSecTunMonAHOutPkts_Type = Counter64
_JnxIpSecTunMonAHOutPkts_Object = MibTableColumn
jnxIpSecTunMonAHOutPkts = _JnxIpSecTunMonAHOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 17),
    _JnxIpSecTunMonAHOutPkts_Type()
)
jnxIpSecTunMonAHOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAHOutPkts.setStatus("current")
_JnxIpSecTunMonReplayDropPkts_Type = Counter64
_JnxIpSecTunMonReplayDropPkts_Object = MibTableColumn
jnxIpSecTunMonReplayDropPkts = _JnxIpSecTunMonReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 18),
    _JnxIpSecTunMonReplayDropPkts_Type()
)
jnxIpSecTunMonReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonReplayDropPkts.setStatus("current")
_JnxIpSecTunMonAhAuthFails_Type = Counter64
_JnxIpSecTunMonAhAuthFails_Object = MibTableColumn
jnxIpSecTunMonAhAuthFails = _JnxIpSecTunMonAhAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 19),
    _JnxIpSecTunMonAhAuthFails_Type()
)
jnxIpSecTunMonAhAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonAhAuthFails.setStatus("current")
_JnxIpSecTunMonEspAuthFails_Type = Counter64
_JnxIpSecTunMonEspAuthFails_Object = MibTableColumn
jnxIpSecTunMonEspAuthFails = _JnxIpSecTunMonEspAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 20),
    _JnxIpSecTunMonEspAuthFails_Type()
)
jnxIpSecTunMonEspAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonEspAuthFails.setStatus("current")
_JnxIpSecTunMonDecryptFails_Type = Counter64
_JnxIpSecTunMonDecryptFails_Object = MibTableColumn
jnxIpSecTunMonDecryptFails = _JnxIpSecTunMonDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 21),
    _JnxIpSecTunMonDecryptFails_Type()
)
jnxIpSecTunMonDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonDecryptFails.setStatus("current")
_JnxIpSecTunMonBadHeaders_Type = Counter64
_JnxIpSecTunMonBadHeaders_Object = MibTableColumn
jnxIpSecTunMonBadHeaders = _JnxIpSecTunMonBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 22),
    _JnxIpSecTunMonBadHeaders_Type()
)
jnxIpSecTunMonBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonBadHeaders.setStatus("current")
_JnxIpSecTunMonBadTrailers_Type = Counter64
_JnxIpSecTunMonBadTrailers_Object = MibTableColumn
jnxIpSecTunMonBadTrailers = _JnxIpSecTunMonBadTrailers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 23),
    _JnxIpSecTunMonBadTrailers_Type()
)
jnxIpSecTunMonBadTrailers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonBadTrailers.setStatus("current")
_JnxIpSecTunMonDroppedPkts_Type = Counter64
_JnxIpSecTunMonDroppedPkts_Object = MibTableColumn
jnxIpSecTunMonDroppedPkts = _JnxIpSecTunMonDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 26),
    _JnxIpSecTunMonDroppedPkts_Type()
)
jnxIpSecTunMonDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonDroppedPkts.setStatus("obsolete")
_JnxIpSecTunMonVpnName_Type = DisplayString
_JnxIpSecTunMonVpnName_Object = MibTableColumn
jnxIpSecTunMonVpnName = _JnxIpSecTunMonVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 27),
    _JnxIpSecTunMonVpnName_Type()
)
jnxIpSecTunMonVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonVpnName.setStatus("current")
_JnxIpSecTunMonTsName_Type = DisplayString
_JnxIpSecTunMonTsName_Object = MibTableColumn
jnxIpSecTunMonTsName = _JnxIpSecTunMonTsName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 28),
    _JnxIpSecTunMonTsName_Type()
)
jnxIpSecTunMonTsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonTsName.setStatus("current")


class _JnxIpSecTunMonMultiSa_Type(Integer32):
    """Custom type jnxIpSecTunMonMultiSa based on Integer32"""
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


_JnxIpSecTunMonMultiSa_Type.__name__ = "Integer32"
_JnxIpSecTunMonMultiSa_Object = MibTableColumn
jnxIpSecTunMonMultiSa = _JnxIpSecTunMonMultiSa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 29),
    _JnxIpSecTunMonMultiSa_Type()
)
jnxIpSecTunMonMultiSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonMultiSa.setStatus("current")
_JnxIpSecTunMonInvalidSpi_Type = Counter64
_JnxIpSecTunMonInvalidSpi_Object = MibTableColumn
jnxIpSecTunMonInvalidSpi = _JnxIpSecTunMonInvalidSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 30),
    _JnxIpSecTunMonInvalidSpi_Type()
)
jnxIpSecTunMonInvalidSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonInvalidSpi.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecTunMonInvalidSpi.setUnits("Packets")
_JnxIpSecTunMonTsCheckFail_Type = Counter64
_JnxIpSecTunMonTsCheckFail_Object = MibTableColumn
jnxIpSecTunMonTsCheckFail = _JnxIpSecTunMonTsCheckFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 31),
    _JnxIpSecTunMonTsCheckFail_Type()
)
jnxIpSecTunMonTsCheckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonTsCheckFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecTunMonTsCheckFail.setUnits("Packets")
_JnxIpSecTunMonDiscarded_Type = Counter64
_JnxIpSecTunMonDiscarded_Object = MibTableColumn
jnxIpSecTunMonDiscarded = _JnxIpSecTunMonDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 32),
    _JnxIpSecTunMonDiscarded_Type()
)
jnxIpSecTunMonDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecTunMonDiscarded.setUnits("Packets")
_JnxIpSecTunMonTunType_Type = JnxIkeTunType
_JnxIpSecTunMonTunType_Object = MibTableColumn
jnxIpSecTunMonTunType = _JnxIpSecTunMonTunType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 33),
    _JnxIpSecTunMonTunType_Type()
)
jnxIpSecTunMonTunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecTunMonTunType.setStatus("current")
_JnxIpSecSaMonTable_Object = MibTable
jnxIpSecSaMonTable = _JnxIpSecSaMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxIpSecSaMonTable.setStatus("current")
_JnxIpSecSaMonEntry_Object = MibTableRow
jnxIpSecSaMonEntry = _JnxIpSecSaMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1)
)
jnxIpSecSaMonEntry.setIndexNames(
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddrType"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddr"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonIndex"),
    (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecSaMonIndex"),
)
if mibBuilder.loadTexts:
    jnxIpSecSaMonEntry.setStatus("current")


class _JnxIpSecSaMonIndex_Type(Integer32):
    """Custom type jnxIpSecSaMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxIpSecSaMonIndex_Type.__name__ = "Integer32"
_JnxIpSecSaMonIndex_Object = MibTableColumn
jnxIpSecSaMonIndex = _JnxIpSecSaMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 1),
    _JnxIpSecSaMonIndex_Type()
)
jnxIpSecSaMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIpSecSaMonIndex.setStatus("current")


class _JnxIpSecSaMonProtocol_Type(Integer32):
    """Custom type jnxIpSecSaMonProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2))
    )


_JnxIpSecSaMonProtocol_Type.__name__ = "Integer32"
_JnxIpSecSaMonProtocol_Object = MibTableColumn
jnxIpSecSaMonProtocol = _JnxIpSecSaMonProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 2),
    _JnxIpSecSaMonProtocol_Type()
)
jnxIpSecSaMonProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonProtocol.setStatus("current")
_JnxIpSecSaMonInSpi_Type = JnxSpiType
_JnxIpSecSaMonInSpi_Object = MibTableColumn
jnxIpSecSaMonInSpi = _JnxIpSecSaMonInSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 3),
    _JnxIpSecSaMonInSpi_Type()
)
jnxIpSecSaMonInSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonInSpi.setStatus("current")
_JnxIpSecSaMonOutSpi_Type = JnxSpiType
_JnxIpSecSaMonOutSpi_Object = MibTableColumn
jnxIpSecSaMonOutSpi = _JnxIpSecSaMonOutSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 4),
    _JnxIpSecSaMonOutSpi_Type()
)
jnxIpSecSaMonOutSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonOutSpi.setStatus("current")
_JnxIpSecSaMonType_Type = JnxSAType
_JnxIpSecSaMonType_Object = MibTableColumn
jnxIpSecSaMonType = _JnxIpSecSaMonType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 5),
    _JnxIpSecSaMonType_Type()
)
jnxIpSecSaMonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonType.setStatus("current")
_JnxIpSecSaMonEncapMode_Type = JnxEncapMode
_JnxIpSecSaMonEncapMode_Object = MibTableColumn
jnxIpSecSaMonEncapMode = _JnxIpSecSaMonEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 6),
    _JnxIpSecSaMonEncapMode_Type()
)
jnxIpSecSaMonEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonEncapMode.setStatus("current")
_JnxIpSecSaMonLifeSize_Type = Integer32
_JnxIpSecSaMonLifeSize_Object = MibTableColumn
jnxIpSecSaMonLifeSize = _JnxIpSecSaMonLifeSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 7),
    _JnxIpSecSaMonLifeSize_Type()
)
jnxIpSecSaMonLifeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeSize.setStatus("current")
_JnxIpSecSaMonLifeTime_Type = Integer32
_JnxIpSecSaMonLifeTime_Object = MibTableColumn
jnxIpSecSaMonLifeTime = _JnxIpSecSaMonLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 8),
    _JnxIpSecSaMonLifeTime_Type()
)
jnxIpSecSaMonLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeTime.setStatus("current")
_JnxIpSecSaMonActiveTime_Type = TimeInterval
_JnxIpSecSaMonActiveTime_Object = MibTableColumn
jnxIpSecSaMonActiveTime = _JnxIpSecSaMonActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 9),
    _JnxIpSecSaMonActiveTime_Type()
)
jnxIpSecSaMonActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonActiveTime.setStatus("current")
_JnxIpSecSaMonLifeSizeThreshold_Type = Integer32
_JnxIpSecSaMonLifeSizeThreshold_Object = MibTableColumn
jnxIpSecSaMonLifeSizeThreshold = _JnxIpSecSaMonLifeSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 10),
    _JnxIpSecSaMonLifeSizeThreshold_Type()
)
jnxIpSecSaMonLifeSizeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeSizeThreshold.setStatus("current")
_JnxIpSecSaMonLifeTimeThreshold_Type = Integer32
_JnxIpSecSaMonLifeTimeThreshold_Object = MibTableColumn
jnxIpSecSaMonLifeTimeThreshold = _JnxIpSecSaMonLifeTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 11),
    _JnxIpSecSaMonLifeTimeThreshold_Type()
)
jnxIpSecSaMonLifeTimeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonLifeTimeThreshold.setStatus("current")
_JnxIpSecSaMonEncryptAlgo_Type = JnxEncryptAlgo
_JnxIpSecSaMonEncryptAlgo_Object = MibTableColumn
jnxIpSecSaMonEncryptAlgo = _JnxIpSecSaMonEncryptAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 12),
    _JnxIpSecSaMonEncryptAlgo_Type()
)
jnxIpSecSaMonEncryptAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonEncryptAlgo.setStatus("current")
_JnxIpSecSaMonAuthAlgo_Type = JnxAuthAlgo
_JnxIpSecSaMonAuthAlgo_Object = MibTableColumn
jnxIpSecSaMonAuthAlgo = _JnxIpSecSaMonAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 13),
    _JnxIpSecSaMonAuthAlgo_Type()
)
jnxIpSecSaMonAuthAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonAuthAlgo.setStatus("current")


class _JnxIpSecSaMonState_Type(Integer32):
    """Custom type jnxIpSecSaMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("expiring", 2))
    )


_JnxIpSecSaMonState_Type.__name__ = "Integer32"
_JnxIpSecSaMonState_Object = MibTableColumn
jnxIpSecSaMonState = _JnxIpSecSaMonState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 14),
    _JnxIpSecSaMonState_Type()
)
jnxIpSecSaMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonState.setStatus("current")
_JnxIpSecSaMonFcName_Type = DisplayString
_JnxIpSecSaMonFcName_Object = MibTableColumn
jnxIpSecSaMonFcName = _JnxIpSecSaMonFcName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 15),
    _JnxIpSecSaMonFcName_Type()
)
jnxIpSecSaMonFcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonFcName.setStatus("current")
_JnxIpSecSaMonEsnMode_Type = JnxEsnMode
_JnxIpSecSaMonEsnMode_Object = MibTableColumn
jnxIpSecSaMonEsnMode = _JnxIpSecSaMonEsnMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 16),
    _JnxIpSecSaMonEsnMode_Type()
)
jnxIpSecSaMonEsnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecSaMonEsnMode.setStatus("current")
_JnxIpSecGlobalStats_ObjectIdentity = ObjectIdentity
jnxIpSecGlobalStats = _JnxIpSecGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4)
)
_JnxIpSecGlobalOutEncryptedBytes_Type = Counter64
_JnxIpSecGlobalOutEncryptedBytes_Object = MibScalar
jnxIpSecGlobalOutEncryptedBytes = _JnxIpSecGlobalOutEncryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 1),
    _JnxIpSecGlobalOutEncryptedBytes_Type()
)
jnxIpSecGlobalOutEncryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalOutEncryptedBytes.setStatus("current")
_JnxIpSecGlobalOutEncryptedPkts_Type = Counter64
_JnxIpSecGlobalOutEncryptedPkts_Object = MibScalar
jnxIpSecGlobalOutEncryptedPkts = _JnxIpSecGlobalOutEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 2),
    _JnxIpSecGlobalOutEncryptedPkts_Type()
)
jnxIpSecGlobalOutEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalOutEncryptedPkts.setStatus("current")
_JnxIpSecGlobalInDecryptedBytes_Type = Counter64
_JnxIpSecGlobalInDecryptedBytes_Object = MibScalar
jnxIpSecGlobalInDecryptedBytes = _JnxIpSecGlobalInDecryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 3),
    _JnxIpSecGlobalInDecryptedBytes_Type()
)
jnxIpSecGlobalInDecryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalInDecryptedBytes.setStatus("current")
_JnxIpSecGlobalInDecryptedPkts_Type = Counter64
_JnxIpSecGlobalInDecryptedPkts_Object = MibScalar
jnxIpSecGlobalInDecryptedPkts = _JnxIpSecGlobalInDecryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 4),
    _JnxIpSecGlobalInDecryptedPkts_Type()
)
jnxIpSecGlobalInDecryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalInDecryptedPkts.setStatus("current")
_JnxIpSecGlobalAHInBytes_Type = Counter64
_JnxIpSecGlobalAHInBytes_Object = MibScalar
jnxIpSecGlobalAHInBytes = _JnxIpSecGlobalAHInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 5),
    _JnxIpSecGlobalAHInBytes_Type()
)
jnxIpSecGlobalAHInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalAHInBytes.setStatus("current")
_JnxIpSecGlobalAHInPkts_Type = Counter64
_JnxIpSecGlobalAHInPkts_Object = MibScalar
jnxIpSecGlobalAHInPkts = _JnxIpSecGlobalAHInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 6),
    _JnxIpSecGlobalAHInPkts_Type()
)
jnxIpSecGlobalAHInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalAHInPkts.setStatus("current")
_JnxIpSecGlobalAHOutBytes_Type = Counter64
_JnxIpSecGlobalAHOutBytes_Object = MibScalar
jnxIpSecGlobalAHOutBytes = _JnxIpSecGlobalAHOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 7),
    _JnxIpSecGlobalAHOutBytes_Type()
)
jnxIpSecGlobalAHOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalAHOutBytes.setStatus("current")
_JnxIpSecGlobalAHOutPkts_Type = Counter64
_JnxIpSecGlobalAHOutPkts_Object = MibScalar
jnxIpSecGlobalAHOutPkts = _JnxIpSecGlobalAHOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 8),
    _JnxIpSecGlobalAHOutPkts_Type()
)
jnxIpSecGlobalAHOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalAHOutPkts.setStatus("current")
_JnxIpSecGlobalReplayDropPkts_Type = Counter64
_JnxIpSecGlobalReplayDropPkts_Object = MibScalar
jnxIpSecGlobalReplayDropPkts = _JnxIpSecGlobalReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 9),
    _JnxIpSecGlobalReplayDropPkts_Type()
)
jnxIpSecGlobalReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalReplayDropPkts.setStatus("current")
_JnxIpSecGlobalAhAuthFails_Type = Counter64
_JnxIpSecGlobalAhAuthFails_Object = MibScalar
jnxIpSecGlobalAhAuthFails = _JnxIpSecGlobalAhAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 10),
    _JnxIpSecGlobalAhAuthFails_Type()
)
jnxIpSecGlobalAhAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalAhAuthFails.setStatus("current")
_JnxIpSecGlobalEspAuthFails_Type = Counter64
_JnxIpSecGlobalEspAuthFails_Object = MibScalar
jnxIpSecGlobalEspAuthFails = _JnxIpSecGlobalEspAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 11),
    _JnxIpSecGlobalEspAuthFails_Type()
)
jnxIpSecGlobalEspAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalEspAuthFails.setStatus("current")
_JnxIpSecGlobalDecryptFails_Type = Counter64
_JnxIpSecGlobalDecryptFails_Object = MibScalar
jnxIpSecGlobalDecryptFails = _JnxIpSecGlobalDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 12),
    _JnxIpSecGlobalDecryptFails_Type()
)
jnxIpSecGlobalDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalDecryptFails.setStatus("current")
_JnxIpSecGlobalBadHeaders_Type = Counter64
_JnxIpSecGlobalBadHeaders_Object = MibScalar
jnxIpSecGlobalBadHeaders = _JnxIpSecGlobalBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 13),
    _JnxIpSecGlobalBadHeaders_Type()
)
jnxIpSecGlobalBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalBadHeaders.setStatus("current")
_JnxIpSecGlobalBadTrailers_Type = Counter64
_JnxIpSecGlobalBadTrailers_Object = MibScalar
jnxIpSecGlobalBadTrailers = _JnxIpSecGlobalBadTrailers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 14),
    _JnxIpSecGlobalBadTrailers_Type()
)
jnxIpSecGlobalBadTrailers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalBadTrailers.setStatus("current")
_JnxIpSecGlobalInvalidSpi_Type = Counter64
_JnxIpSecGlobalInvalidSpi_Object = MibScalar
jnxIpSecGlobalInvalidSpi = _JnxIpSecGlobalInvalidSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 15),
    _JnxIpSecGlobalInvalidSpi_Type()
)
jnxIpSecGlobalInvalidSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalInvalidSpi.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecGlobalInvalidSpi.setUnits("Packets")
_JnxIpSecGlobalTsCheckFail_Type = Counter64
_JnxIpSecGlobalTsCheckFail_Object = MibScalar
jnxIpSecGlobalTsCheckFail = _JnxIpSecGlobalTsCheckFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 16),
    _JnxIpSecGlobalTsCheckFail_Type()
)
jnxIpSecGlobalTsCheckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalTsCheckFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecGlobalTsCheckFail.setUnits("Packets")
_JnxIpSecGlobalDiscarded_Type = Counter64
_JnxIpSecGlobalDiscarded_Object = MibScalar
jnxIpSecGlobalDiscarded = _JnxIpSecGlobalDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 4, 17),
    _JnxIpSecGlobalDiscarded_Type()
)
jnxIpSecGlobalDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecGlobalDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecGlobalDiscarded.setUnits("Packets")
_JnxIpSecHaLinkGlobalStats_ObjectIdentity = ObjectIdentity
jnxIpSecHaLinkGlobalStats = _JnxIpSecHaLinkGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5)
)
_JnxIpSecHaLinkGlobalOutEncryptedBytes_Type = Counter64
_JnxIpSecHaLinkGlobalOutEncryptedBytes_Object = MibScalar
jnxIpSecHaLinkGlobalOutEncryptedBytes = _JnxIpSecHaLinkGlobalOutEncryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 1),
    _JnxIpSecHaLinkGlobalOutEncryptedBytes_Type()
)
jnxIpSecHaLinkGlobalOutEncryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalOutEncryptedBytes.setStatus("current")
_JnxIpSecHaLinkGlobalOutEncryptedPkts_Type = Counter64
_JnxIpSecHaLinkGlobalOutEncryptedPkts_Object = MibScalar
jnxIpSecHaLinkGlobalOutEncryptedPkts = _JnxIpSecHaLinkGlobalOutEncryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 2),
    _JnxIpSecHaLinkGlobalOutEncryptedPkts_Type()
)
jnxIpSecHaLinkGlobalOutEncryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalOutEncryptedPkts.setStatus("current")
_JnxIpSecHaLinkGlobalInDecryptedBytes_Type = Counter64
_JnxIpSecHaLinkGlobalInDecryptedBytes_Object = MibScalar
jnxIpSecHaLinkGlobalInDecryptedBytes = _JnxIpSecHaLinkGlobalInDecryptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 3),
    _JnxIpSecHaLinkGlobalInDecryptedBytes_Type()
)
jnxIpSecHaLinkGlobalInDecryptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalInDecryptedBytes.setStatus("current")
_JnxIpSecHaLinkGlobalInDecryptedPkts_Type = Counter64
_JnxIpSecHaLinkGlobalInDecryptedPkts_Object = MibScalar
jnxIpSecHaLinkGlobalInDecryptedPkts = _JnxIpSecHaLinkGlobalInDecryptedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 4),
    _JnxIpSecHaLinkGlobalInDecryptedPkts_Type()
)
jnxIpSecHaLinkGlobalInDecryptedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalInDecryptedPkts.setStatus("current")
_JnxIpSecHaLinkGlobalAHInBytes_Type = Counter64
_JnxIpSecHaLinkGlobalAHInBytes_Object = MibScalar
jnxIpSecHaLinkGlobalAHInBytes = _JnxIpSecHaLinkGlobalAHInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 5),
    _JnxIpSecHaLinkGlobalAHInBytes_Type()
)
jnxIpSecHaLinkGlobalAHInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalAHInBytes.setStatus("current")
_JnxIpSecHaLinkGlobalAHInPkts_Type = Counter64
_JnxIpSecHaLinkGlobalAHInPkts_Object = MibScalar
jnxIpSecHaLinkGlobalAHInPkts = _JnxIpSecHaLinkGlobalAHInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 6),
    _JnxIpSecHaLinkGlobalAHInPkts_Type()
)
jnxIpSecHaLinkGlobalAHInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalAHInPkts.setStatus("current")
_JnxIpSecHaLinkGlobalAHOutBytes_Type = Counter64
_JnxIpSecHaLinkGlobalAHOutBytes_Object = MibScalar
jnxIpSecHaLinkGlobalAHOutBytes = _JnxIpSecHaLinkGlobalAHOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 7),
    _JnxIpSecHaLinkGlobalAHOutBytes_Type()
)
jnxIpSecHaLinkGlobalAHOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalAHOutBytes.setStatus("current")
_JnxIpSecHaLinkGlobalAHOutPkts_Type = Counter64
_JnxIpSecHaLinkGlobalAHOutPkts_Object = MibScalar
jnxIpSecHaLinkGlobalAHOutPkts = _JnxIpSecHaLinkGlobalAHOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 8),
    _JnxIpSecHaLinkGlobalAHOutPkts_Type()
)
jnxIpSecHaLinkGlobalAHOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalAHOutPkts.setStatus("current")
_JnxIpSecHaLinkGlobalReplayDropPkts_Type = Counter64
_JnxIpSecHaLinkGlobalReplayDropPkts_Object = MibScalar
jnxIpSecHaLinkGlobalReplayDropPkts = _JnxIpSecHaLinkGlobalReplayDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 9),
    _JnxIpSecHaLinkGlobalReplayDropPkts_Type()
)
jnxIpSecHaLinkGlobalReplayDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalReplayDropPkts.setStatus("current")
_JnxIpSecHaLinkGlobalAhAuthFails_Type = Counter64
_JnxIpSecHaLinkGlobalAhAuthFails_Object = MibScalar
jnxIpSecHaLinkGlobalAhAuthFails = _JnxIpSecHaLinkGlobalAhAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 10),
    _JnxIpSecHaLinkGlobalAhAuthFails_Type()
)
jnxIpSecHaLinkGlobalAhAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalAhAuthFails.setStatus("current")
_JnxIpSecHaLinkGlobalEspAuthFails_Type = Counter64
_JnxIpSecHaLinkGlobalEspAuthFails_Object = MibScalar
jnxIpSecHaLinkGlobalEspAuthFails = _JnxIpSecHaLinkGlobalEspAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 11),
    _JnxIpSecHaLinkGlobalEspAuthFails_Type()
)
jnxIpSecHaLinkGlobalEspAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalEspAuthFails.setStatus("current")
_JnxIpSecHaLinkGlobalDecryptFails_Type = Counter64
_JnxIpSecHaLinkGlobalDecryptFails_Object = MibScalar
jnxIpSecHaLinkGlobalDecryptFails = _JnxIpSecHaLinkGlobalDecryptFails_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 12),
    _JnxIpSecHaLinkGlobalDecryptFails_Type()
)
jnxIpSecHaLinkGlobalDecryptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalDecryptFails.setStatus("current")
_JnxIpSecHaLinkGlobalBadHeaders_Type = Counter64
_JnxIpSecHaLinkGlobalBadHeaders_Object = MibScalar
jnxIpSecHaLinkGlobalBadHeaders = _JnxIpSecHaLinkGlobalBadHeaders_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 13),
    _JnxIpSecHaLinkGlobalBadHeaders_Type()
)
jnxIpSecHaLinkGlobalBadHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalBadHeaders.setStatus("current")
_JnxIpSecHaLinkGlobalBadTrailers_Type = Counter64
_JnxIpSecHaLinkGlobalBadTrailers_Object = MibScalar
jnxIpSecHaLinkGlobalBadTrailers = _JnxIpSecHaLinkGlobalBadTrailers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 14),
    _JnxIpSecHaLinkGlobalBadTrailers_Type()
)
jnxIpSecHaLinkGlobalBadTrailers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalBadTrailers.setStatus("current")
_JnxIpSecHaLinkGlobalInvalidSpi_Type = Counter64
_JnxIpSecHaLinkGlobalInvalidSpi_Object = MibScalar
jnxIpSecHaLinkGlobalInvalidSpi = _JnxIpSecHaLinkGlobalInvalidSpi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 15),
    _JnxIpSecHaLinkGlobalInvalidSpi_Type()
)
jnxIpSecHaLinkGlobalInvalidSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalInvalidSpi.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalInvalidSpi.setUnits("Packets")
_JnxIpSecHaLinkGlobalTsCheckFail_Type = Counter64
_JnxIpSecHaLinkGlobalTsCheckFail_Object = MibScalar
jnxIpSecHaLinkGlobalTsCheckFail = _JnxIpSecHaLinkGlobalTsCheckFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 16),
    _JnxIpSecHaLinkGlobalTsCheckFail_Type()
)
jnxIpSecHaLinkGlobalTsCheckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalTsCheckFail.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalTsCheckFail.setUnits("Packets")
_JnxIpSecHaLinkGlobalDiscarded_Type = Counter64
_JnxIpSecHaLinkGlobalDiscarded_Object = MibScalar
jnxIpSecHaLinkGlobalDiscarded = _JnxIpSecHaLinkGlobalDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 5, 17),
    _JnxIpSecHaLinkGlobalDiscarded_Type()
)
jnxIpSecHaLinkGlobalDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    jnxIpSecHaLinkGlobalDiscarded.setUnits("Packets")

# Managed Objects groups


# Notification objects

jnxIkePeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 0, 1)
)
jnxIkePeerDown.setObjects(
      *(("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteGwAddrType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteGwAddr"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemotePort"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalGwAddrType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalGwAddr"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalPort"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRoutingInstance"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalIdType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalIdValue"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteIdType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteIdValue"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerAAAUserName"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerGwName"))
)
if mibBuilder.loadTexts:
    jnxIkePeerDown.setStatus(
        "current"
    )

jnxIkePeerIPSecTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0, 0, 2)
)
jnxIkePeerIPSecTunnelDown.setObjects(
      *(("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteGwAddrType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteGwAddr"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemotePort"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalGwAddrType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalGwAddr"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalPort"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRoutingInstance"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalIdType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerLocalIdValue"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteIdType"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerRemoteIdValue"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerAAAUserName"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapPeerGwName"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapIpSecTunVpnName"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapIpSecTunTsName"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapIpSecTunLocalTS"),
        ("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTrapIpSecTunRemoteTS"))
)
if mibBuilder.loadTexts:
    jnxIkePeerIPSecTunnelDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IPSEC-FLOW-MON-MIB",
    **{"JnxIkePeerType": JnxIkePeerType,
       "JnxIkeNegoMode": JnxIkeNegoMode,
       "JnxIkeHashAlgo": JnxIkeHashAlgo,
       "JnxIkeAuthMethod": JnxIkeAuthMethod,
       "JnxIkePeerRole": JnxIkePeerRole,
       "JnxIkeTunStateType": JnxIkeTunStateType,
       "JnxDiffHellmanGrp": JnxDiffHellmanGrp,
       "JnxKeyType": JnxKeyType,
       "JnxEncapMode": JnxEncapMode,
       "JnxEncryptAlgo": JnxEncryptAlgo,
       "JnxAuthAlgo": JnxAuthAlgo,
       "JnxRemotePeerType": JnxRemotePeerType,
       "JnxPeerStateType": JnxPeerStateType,
       "JnxSpiType": JnxSpiType,
       "JnxSAType": JnxSAType,
       "JnxEsnMode": JnxEsnMode,
       "JnxIkeTunType": JnxIkeTunType,
       "jnxIpSecFlowMonMIB": jnxIpSecFlowMonMIB,
       "jnxIpSecFlowMonNotifications": jnxIpSecFlowMonNotifications,
       "jnxIkeNotificationType": jnxIkeNotificationType,
       "jnxIkePeerDown": jnxIkePeerDown,
       "jnxIkePeerIPSecTunnelDown": jnxIkePeerIPSecTunnelDown,
       "jnxIkeNotificationObj": jnxIkeNotificationObj,
       "jnxIkeTrapPeerRemoteGwAddrType": jnxIkeTrapPeerRemoteGwAddrType,
       "jnxIkeTrapPeerRemoteGwAddr": jnxIkeTrapPeerRemoteGwAddr,
       "jnxIkeTrapPeerRemotePort": jnxIkeTrapPeerRemotePort,
       "jnxIkeTrapPeerLocalGwAddrType": jnxIkeTrapPeerLocalGwAddrType,
       "jnxIkeTrapPeerLocalGwAddr": jnxIkeTrapPeerLocalGwAddr,
       "jnxIkeTrapPeerLocalPort": jnxIkeTrapPeerLocalPort,
       "jnxIkeTrapPeerRoutingInstance": jnxIkeTrapPeerRoutingInstance,
       "jnxIkeTrapPeerLocalIdType": jnxIkeTrapPeerLocalIdType,
       "jnxIkeTrapPeerLocalIdValue": jnxIkeTrapPeerLocalIdValue,
       "jnxIkeTrapPeerRemoteIdType": jnxIkeTrapPeerRemoteIdType,
       "jnxIkeTrapPeerRemoteIdValue": jnxIkeTrapPeerRemoteIdValue,
       "jnxIkeTrapPeerAAAUserName": jnxIkeTrapPeerAAAUserName,
       "jnxIkeTrapPeerGwName": jnxIkeTrapPeerGwName,
       "jnxIkeTrapIpSecTunVpnName": jnxIkeTrapIpSecTunVpnName,
       "jnxIkeTrapIpSecTunTsName": jnxIkeTrapIpSecTunTsName,
       "jnxIkeTrapIpSecTunLocalTS": jnxIkeTrapIpSecTunLocalTS,
       "jnxIkeTrapIpSecTunRemoteTS": jnxIkeTrapIpSecTunRemoteTS,
       "jnxIpSecFlowMonPhaseOne": jnxIpSecFlowMonPhaseOne,
       "jnxIkeNumOfTunnels": jnxIkeNumOfTunnels,
       "jnxIkeTunnelMonTable": jnxIkeTunnelMonTable,
       "jnxIkeTunnelMonEntry": jnxIkeTunnelMonEntry,
       "jnxIkeTunMonRemoteGwAddrType": jnxIkeTunMonRemoteGwAddrType,
       "jnxIkeTunMonRemoteGwAddr": jnxIkeTunMonRemoteGwAddr,
       "jnxIkeTunMonIndex": jnxIkeTunMonIndex,
       "jnxIkeTunMonLocalGwAddr": jnxIkeTunMonLocalGwAddr,
       "jnxIkeTunMonLocalGwAddrType": jnxIkeTunMonLocalGwAddrType,
       "jnxIkeTunMonState": jnxIkeTunMonState,
       "jnxIkeTunMonInitiatorCookie": jnxIkeTunMonInitiatorCookie,
       "jnxIkeTunMonResponderCookie": jnxIkeTunMonResponderCookie,
       "jnxIkeTunMonLocalRole": jnxIkeTunMonLocalRole,
       "jnxIkeTunMonLocalIdType": jnxIkeTunMonLocalIdType,
       "jnxIkeTunMonLocalIdValue": jnxIkeTunMonLocalIdValue,
       "jnxIkeTunMonLocalCertName": jnxIkeTunMonLocalCertName,
       "jnxIkeTunMonRemoteIdType": jnxIkeTunMonRemoteIdType,
       "jnxIkeTunMonRemoteIdValue": jnxIkeTunMonRemoteIdValue,
       "jnxIkeTunMonNegoMode": jnxIkeTunMonNegoMode,
       "jnxIkeTunMonDiffHellmanGrp": jnxIkeTunMonDiffHellmanGrp,
       "jnxIkeTunMonEncryptAlgo": jnxIkeTunMonEncryptAlgo,
       "jnxIkeTunMonHashAlgo": jnxIkeTunMonHashAlgo,
       "jnxIkeTunMonAuthMethod": jnxIkeTunMonAuthMethod,
       "jnxIkeTunMonLifeTime": jnxIkeTunMonLifeTime,
       "jnxIkeTunMonActiveTime": jnxIkeTunMonActiveTime,
       "jnxIkeTunMonInOctets": jnxIkeTunMonInOctets,
       "jnxIkeTunMonInPkts": jnxIkeTunMonInPkts,
       "jnxIkeTunMonOutOctets": jnxIkeTunMonOutOctets,
       "jnxIkeTunMonOutPkts": jnxIkeTunMonOutPkts,
       "jnxIkeTunMonXAuthUserId": jnxIkeTunMonXAuthUserId,
       "jnxIkeTunMonDPDDownCount": jnxIkeTunMonDPDDownCount,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyRequestOut,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResponseIn,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyNoProposalChosenIn,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyInvalidKeIn,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyTsUnacceptableIn,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifySaFail,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyDhGroupFail,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResVerifyTsFail,
       "jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail": jnxIkeTunMonInitiatorIkev2IPSecSaRekeyResDhComputeKeyFail,
       "jnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn": jnxIkeTunMonResponderIkev2IPSecSaRekeyRequestIn,
       "jnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut": jnxIkeTunMonResponderIkev2IPSecSaRekeyResponseOut,
       "jnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut": jnxIkeTunMonResponderIkev2IPSecSaRekeyNoProposalChosenOut,
       "jnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut": jnxIkeTunMonResponderIkev2IPSecSaRekeyInvalidKeOut,
       "jnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut": jnxIkeTunMonResponderIkev2IPSecSaRekeyTsUnacceptableOut,
       "jnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail": jnxIkeTunMonResponderIkev2IPSecSaRekeyResDhComputeKeyFail,
       "jnxIkeTunMonGwName": jnxIkeTunMonGwName,
       "jnxIkeTunMonTunType": jnxIkeTunMonTunType,
       "jnxIkeGlobalStats": jnxIkeGlobalStats,
       "jnxIkeGlobalInitiatorIkev2SaInitStats": jnxIkeGlobalInitiatorIkev2SaInitStats,
       "jnxIkeGlobalInitiatorIkev2SaInitRequestOut": jnxIkeGlobalInitiatorIkev2SaInitRequestOut,
       "jnxIkeGlobalInitiatorIkev2SaInitResponseIn": jnxIkeGlobalInitiatorIkev2SaInitResponseIn,
       "jnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi": jnxIkeGlobalInitiatorIkev2SaInitResInvalidIkeSpi,
       "jnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn": jnxIkeGlobalInitiatorIkev2SaInitInvalidKePayloadIn,
       "jnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn": jnxIkeGlobalInitiatorIkev2SaInitNoProposalChosenIn,
       "jnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail": jnxIkeGlobalInitiatorIkev2SaInitResVerifySaFail,
       "jnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail": jnxIkeGlobalInitiatorIkev2SaInitResIkeSaFillFail,
       "jnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail": jnxIkeGlobalInitiatorIkev2SaInitResVerifyDhGroupFail,
       "jnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn": jnxIkeGlobalInitiatorIkev2SaInitCookieRequestIn,
       "jnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut": jnxIkeGlobalInitiatorIkev2SaInitCookieResponseOut,
       "jnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail": jnxIkeGlobalInitiatorIkev2SaInitResDhComputeKeyFail,
       "jnxIkeGlobalResponderIkev2SaInitStats": jnxIkeGlobalResponderIkev2SaInitStats,
       "jnxIkeGlobalResponderIkev2SaInitRequestIn": jnxIkeGlobalResponderIkev2SaInitRequestIn,
       "jnxIkeGlobalResponderIkev2SaInitResponseOut": jnxIkeGlobalResponderIkev2SaInitResponseOut,
       "jnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut": jnxIkeGlobalResponderIkev2SaInitNoProposalChosenOut,
       "jnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut": jnxIkeGlobalResponderIkev2SaInitInvalidKePayloadOut,
       "jnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf": jnxIkeGlobalResponderIkev2SaInitResInvalidDhGroupConf,
       "jnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail": jnxIkeGlobalResponderIkev2SaInitResDhGenKeyFail,
       "jnxIkeGlobalResponderIkev2SaInitResGetCAsFail": jnxIkeGlobalResponderIkev2SaInitResGetCAsFail,
       "jnxIkeGlobalResponderIkev2SaInitResGetVidFail": jnxIkeGlobalResponderIkev2SaInitResGetVidFail,
       "jnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail": jnxIkeGlobalResponderIkev2SaInitResDhComputeKeyFail,
       "jnxIkeGlobalResponderIkev2SaInitCookieRequestOut": jnxIkeGlobalResponderIkev2SaInitCookieRequestOut,
       "jnxIkeGlobalResponderIkev2SaInitCookieResponseIn": jnxIkeGlobalResponderIkev2SaInitCookieResponseIn,
       "jnxIkeGlobalInitiatorIkev2AuthStats": jnxIkeGlobalInitiatorIkev2AuthStats,
       "jnxIkeGlobalInitiatorIkev2AuthRequestOut": jnxIkeGlobalInitiatorIkev2AuthRequestOut,
       "jnxIkeGlobalInitiatorIkev2AuthResponseIn": jnxIkeGlobalInitiatorIkev2AuthResponseIn,
       "jnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn": jnxIkeGlobalInitiatorIkev2AuthNoProposalChosenIn,
       "jnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn": jnxIkeGlobalInitiatorIkev2AuthTsUnacceptableIn,
       "jnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn": jnxIkeGlobalInitiatorIkev2AuthAuthenticationFailedIn,
       "jnxIkeGlobalResponderIkev2AuthStats": jnxIkeGlobalResponderIkev2AuthStats,
       "jnxIkeGlobalResponderIkev2AuthRequestIn": jnxIkeGlobalResponderIkev2AuthRequestIn,
       "jnxIkeGlobalResponderIkev2AuthResponseOut": jnxIkeGlobalResponderIkev2AuthResponseOut,
       "jnxIkeGlobalResponderIkev2AuthNoProposalChosenOut": jnxIkeGlobalResponderIkev2AuthNoProposalChosenOut,
       "jnxIkeGlobalResponderIkev2AuthTsUnacceptableOut": jnxIkeGlobalResponderIkev2AuthTsUnacceptableOut,
       "jnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut": jnxIkeGlobalResponderIkev2AuthAuthenticationFailedOut,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyStats": jnxIkeGlobalInitiatorIkev2IkeSaRekeyStats,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut": jnxIkeGlobalInitiatorIkev2IkeSaRekeyRequestOut,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn": jnxIkeGlobalInitiatorIkev2IkeSaRekeyResponseIn,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn": jnxIkeGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn": jnxIkeGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail": jnxIkeGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail": jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail": jnxIkeGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail,
       "jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail": jnxIkeGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail,
       "jnxIkeGlobalResponderIkev2IkeSaRekeyStats": jnxIkeGlobalResponderIkev2IkeSaRekeyStats,
       "jnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn": jnxIkeGlobalResponderIkev2IkeSaRekeyRequestIn,
       "jnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut": jnxIkeGlobalResponderIkev2IkeSaRekeyResponseOut,
       "jnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut": jnxIkeGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut,
       "jnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut": jnxIkeGlobalResponderIkev2IkeSaRekeyInvalidKeOut,
       "jnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail": jnxIkeGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyStats": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyStats,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyRequestOut,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResponseIn,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail,
       "jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail": jnxIkeGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail,
       "jnxIkeGlobalResponderIkev2IpsecSaRekeyStats": jnxIkeGlobalResponderIkev2IpsecSaRekeyStats,
       "jnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn": jnxIkeGlobalResponderIkev2IpsecSaRekeyRequestIn,
       "jnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut": jnxIkeGlobalResponderIkev2IpsecSaRekeyResponseOut,
       "jnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut": jnxIkeGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut,
       "jnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut": jnxIkeGlobalResponderIkev2IpsecSaRekeyInvalidKeOut,
       "jnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut": jnxIkeGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut,
       "jnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail": jnxIkeGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail,
       "jnxIkeGlobalIkev2MsgFailStats": jnxIkeGlobalIkev2MsgFailStats,
       "jnxIkeGlobalIkev2TotalDiscarded": jnxIkeGlobalIkev2TotalDiscarded,
       "jnxIkeGlobalIkev2TotalIdError": jnxIkeGlobalIkev2TotalIdError,
       "jnxIkeGlobalIkev2TotalIntegrityFail": jnxIkeGlobalIkev2TotalIntegrityFail,
       "jnxIkeGlobalIkev2TotalInvalidSPI": jnxIkeGlobalIkev2TotalInvalidSPI,
       "jnxIkeGlobalIkev2TotalInvalidExchgType": jnxIkeGlobalIkev2TotalInvalidExchgType,
       "jnxIkeGlobalIkev2TotalInvalidLength": jnxIkeGlobalIkev2TotalInvalidLength,
       "jnxIkeGlobalIkev2TotalDisorder": jnxIkeGlobalIkev2TotalDisorder,
       "jnxIkePeerAddrTable": jnxIkePeerAddrTable,
       "jnxIkePeerAddrEntry": jnxIkePeerAddrEntry,
       "jnxIkePeerAddrState": jnxIkePeerAddrState,
       "jnxIkePeerAddrRemoteGwAddrType": jnxIkePeerAddrRemoteGwAddrType,
       "jnxIkePeerAddrRemoteGwAddr": jnxIkePeerAddrRemoteGwAddr,
       "jnxIkePeerAddrRemotePort": jnxIkePeerAddrRemotePort,
       "jnxIkePeerAddrLocalGwAddrType": jnxIkePeerAddrLocalGwAddrType,
       "jnxIkePeerAddrLocalGwAddr": jnxIkePeerAddrLocalGwAddr,
       "jnxIkePeerAddrLocalPort": jnxIkePeerAddrLocalPort,
       "jnxIkePeerAddrRoutingInstance": jnxIkePeerAddrRoutingInstance,
       "jnxIkePeerAddrIndex": jnxIkePeerAddrIndex,
       "jnxIkePeerIdTable": jnxIkePeerIdTable,
       "jnxIkePeerIdEntry": jnxIkePeerIdEntry,
       "jnxIkePeerIdState": jnxIkePeerIdState,
       "jnxIkePeerIdRemoteIdType": jnxIkePeerIdRemoteIdType,
       "jnxIkePeerIdRemoteIdValue": jnxIkePeerIdRemoteIdValue,
       "jnxIkePeerIdLocalIdType": jnxIkePeerIdLocalIdType,
       "jnxIkePeerIdLocalIdValue": jnxIkePeerIdLocalIdValue,
       "jnxIkePeerIdAAAUserName": jnxIkePeerIdAAAUserName,
       "jnxIkePeerInternalIndex": jnxIkePeerInternalIndex,
       "jnxIkePeerIdIndex": jnxIkePeerIdIndex,
       "jnxIkePeerStatsTable": jnxIkePeerStatsTable,
       "jnxIkePeerStatsEntry": jnxIkePeerStatsEntry,
       "jnxIkePeerStatsState": jnxIkePeerStatsState,
       "jnxIkePeerStatsIndex": jnxIkePeerStatsIndex,
       "jnxIkePeerStatsRemoteGwAddrType": jnxIkePeerStatsRemoteGwAddrType,
       "jnxIkePeerStatsRemoteGwAddr": jnxIkePeerStatsRemoteGwAddr,
       "jnxIkePeerStatsRemotePort": jnxIkePeerStatsRemotePort,
       "jnxIkePeerStatsLocalGwAddrType": jnxIkePeerStatsLocalGwAddrType,
       "jnxIkePeerStatsLocalGwAddr": jnxIkePeerStatsLocalGwAddr,
       "jnxIkePeerStatsLocalPort": jnxIkePeerStatsLocalPort,
       "jnxIkePeerStatsRoutingInstance": jnxIkePeerStatsRoutingInstance,
       "jnxIkePeerStatsRemoteIdType": jnxIkePeerStatsRemoteIdType,
       "jnxIkePeerStatsRemoteIdValue": jnxIkePeerStatsRemoteIdValue,
       "jnxIkePeerStatsLocalIdType": jnxIkePeerStatsLocalIdType,
       "jnxIkePeerStatsLocalIdValue": jnxIkePeerStatsLocalIdValue,
       "jnxIkePeerStatsAAAUserName": jnxIkePeerStatsAAAUserName,
       "jnxIkePeerStatsGwName": jnxIkePeerStatsGwName,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitRequestOut,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResponseIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResInvalidIkeSpi,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitInvalidKePayloadIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitNoProposalChosenIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifySaFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResIkeSaFillFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResVerifyDhGroupFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieRequestIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitCookieResponseOut,
       "jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail": jnxIkePeerStatsIkeSaInitiatorIkev2SaInitResDhComputeKeyFail,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn": jnxIkePeerStatsIkeSaResponderIkev2SaInitRequestIn,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut": jnxIkePeerStatsIkeSaResponderIkev2SaInitResponseOut,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut": jnxIkePeerStatsIkeSaResponderIkev2SaInitNoProposalChosenOut,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut": jnxIkePeerStatsIkeSaResponderIkev2SaInitInvalidKePayloadOut,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf": jnxIkePeerStatsIkeSaResponderIkev2SaInitResInvalidDhGroupConf,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail": jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhGenKeyFail,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail": jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetCAsFail,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail": jnxIkePeerStatsIkeSaResponderIkev2SaInitResGetVidFail,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail": jnxIkePeerStatsIkeSaResponderIkev2SaInitResDhComputeKeyFail,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut": jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieRequestOut,
       "jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn": jnxIkePeerStatsIkeSaResponderIkev2SaInitCookieResponseIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut": jnxIkePeerStatsIkeSaInitiatorIkev2AuthRequestOut,
       "jnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn": jnxIkePeerStatsIkeSaInitiatorIkev2AuthResponseIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn": jnxIkePeerStatsIkeSaInitiatorIkev2AuthNoProposalChosenIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn": jnxIkePeerStatsIkeSaInitiatorIkev2AuthTsUnacceptableIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn": jnxIkePeerStatsIkeSaInitiatorIkev2AuthAuthenticationFailedIn,
       "jnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn": jnxIkePeerStatsIkeSaResponderIkev2AuthRequestIn,
       "jnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut": jnxIkePeerStatsIkeSaResponderIkev2AuthResponseOut,
       "jnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut": jnxIkePeerStatsIkeSaResponderIkev2AuthAuthenticationFailedOut,
       "jnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut": jnxIkePeerStatsIkeSaResponderIkev2AuthNoProposalChosenOut,
       "jnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut": jnxIkePeerStatsIkeSaResponderIkev2AuthTsUnacceptableOut,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyRequestOut,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResponseIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyNoProposalChosenIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyInvalidKeIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifySaFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResFillIkeSaFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail": jnxIkePeerStatsIkeSaInitiatorIkev2IkeSaRekeyResDhComputeKeyFail,
       "jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn": jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyRequestIn,
       "jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut": jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResponseOut,
       "jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut": jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyNoProposalChosenOut,
       "jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut": jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyInvalidKeOut,
       "jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail": jnxIkePeerStatsIkeSaResponderIkev2IkeSaRekeyResDhComputeKeyFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyRequestOut,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResponseIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyNoProposalChosenIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyInvalidKeIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyTsUnacceptableIn,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifySaFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyDhGrpFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResVerifyTsFail,
       "jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail": jnxIkePeerStatsIkeSaInitiatorIkev2IPSecSaRekeyResDhCompKeyFail,
       "jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn": jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyRequestIn,
       "jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut": jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResponseOut,
       "jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut": jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyNoPropChosenOut,
       "jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut": jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyInvalidKeOut,
       "jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut": jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyTsUnacceptableOut,
       "jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail": jnxIkePeerStatsIkeSaResponderIkev2IPSecSaRekeyResDhCompKeyFail,
       "jnxIkePeerStatsTunType": jnxIkePeerStatsTunType,
       "jnxPeerIkeSaCorrTable": jnxPeerIkeSaCorrTable,
       "jnxPeerIkeSaCorrEntry": jnxPeerIkeSaCorrEntry,
       "jnxPeerIkeSaCorrPeerIndex": jnxPeerIkeSaCorrPeerIndex,
       "jnxPeerIkeSaCorrIntIndex": jnxPeerIkeSaCorrIntIndex,
       "jnxPeerIkeSaCorrIkeTunMonIndex": jnxPeerIkeSaCorrIkeTunMonIndex,
       "jnxPeerIPSecTunnelCorrTable": jnxPeerIPSecTunnelCorrTable,
       "jnxPeerIPSecTunnelCorrEntry": jnxPeerIPSecTunnelCorrEntry,
       "jnxPeerIPSecTunnelCorrPeerIndex": jnxPeerIPSecTunnelCorrPeerIndex,
       "jnxPeerIPSecTunnelCorrIntIndex": jnxPeerIPSecTunnelCorrIntIndex,
       "jnxPeerIPSecTunnelCorrIPSecTunMonIndex": jnxPeerIPSecTunnelCorrIPSecTunMonIndex,
       "jnxIkeHaLinkGlobalStats": jnxIkeHaLinkGlobalStats,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitStats": jnxIkeHaLinkGlobalInitiatorIkev2SaInitStats,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut": jnxIkeHaLinkGlobalInitiatorIkev2SaInitRequestOut,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn": jnxIkeHaLinkGlobalInitiatorIkev2SaInitResponseIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi": jnxIkeHaLinkGlobalInitiatorIkev2SaInitResInvalidIkeSpi,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn": jnxIkeHaLinkGlobalInitiatorIkev2SaInitInvalidKePayloadIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn": jnxIkeHaLinkGlobalInitiatorIkev2SaInitNoProposalChosenIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail": jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifySaFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail": jnxIkeHaLinkGlobalInitiatorIkev2SaInitResIkeSaFillFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail": jnxIkeHaLinkGlobalInitiatorIkev2SaInitResVerifyDhGroupFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn": jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieRequestIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut": jnxIkeHaLinkGlobalInitiatorIkev2SaInitCookieResponseOut,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitStats": jnxIkeHaLinkGlobalResponderIkev2SaInitStats,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn": jnxIkeHaLinkGlobalResponderIkev2SaInitRequestIn,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut": jnxIkeHaLinkGlobalResponderIkev2SaInitResponseOut,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut": jnxIkeHaLinkGlobalResponderIkev2SaInitNoProposalChosenOut,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut": jnxIkeHaLinkGlobalResponderIkev2SaInitInvalidKePayloadOut,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf": jnxIkeHaLinkGlobalResponderIkev2SaInitResInvalidDhGroupConf,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail": jnxIkeHaLinkGlobalResponderIkev2SaInitResDhGenKeyFail,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail": jnxIkeHaLinkGlobalResponderIkev2SaInitResGetCAsFail,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail": jnxIkeHaLinkGlobalResponderIkev2SaInitResGetVidFail,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail": jnxIkeHaLinkGlobalResponderIkev2SaInitResDhComputeKeyFail,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut": jnxIkeHaLinkGlobalResponderIkev2SaInitCookieRequestOut,
       "jnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn": jnxIkeHaLinkGlobalResponderIkev2SaInitCookieResponseIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2AuthStats": jnxIkeHaLinkGlobalInitiatorIkev2AuthStats,
       "jnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut": jnxIkeHaLinkGlobalInitiatorIkev2AuthRequestOut,
       "jnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn": jnxIkeHaLinkGlobalInitiatorIkev2AuthResponseIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn": jnxIkeHaLinkGlobalInitiatorIkev2AuthNoProposalChosenIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn": jnxIkeHaLinkGlobalInitiatorIkev2AuthTsUnacceptableIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn": jnxIkeHaLinkGlobalInitiatorIkev2AuthAuthenticationFailedIn,
       "jnxIkeHaLinkGlobalResponderIkev2AuthStats": jnxIkeHaLinkGlobalResponderIkev2AuthStats,
       "jnxIkeHaLinkGlobalResponderIkev2AuthRequestIn": jnxIkeHaLinkGlobalResponderIkev2AuthRequestIn,
       "jnxIkeHaLinkGlobalResponderIkev2AuthResponseOut": jnxIkeHaLinkGlobalResponderIkev2AuthResponseOut,
       "jnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut": jnxIkeHaLinkGlobalResponderIkev2AuthNoProposalChosenOut,
       "jnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut": jnxIkeHaLinkGlobalResponderIkev2AuthTsUnacceptableOut,
       "jnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut": jnxIkeHaLinkGlobalResponderIkev2AuthAuthenticationFailedOut,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyStats": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyStats,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyRequestOut,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResponseIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyNoProposalChosenIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyInvalidKeIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResDhComputeKeyFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifySaFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResFillIkeSaFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail": jnxIkeHaLinkGlobalInitiatorIkev2IkeSaRekeyResVerifyDhGroupFail,
       "jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyStats": jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyStats,
       "jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn": jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyRequestIn,
       "jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut": jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResponseOut,
       "jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut": jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyNoProposalChosenOut,
       "jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut": jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyInvalidKeOut,
       "jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail": jnxIkeHaLinkGlobalResponderIkev2IkeSaRekeyResDhComputeKeyFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyStats": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyStats,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyRequestOut,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResponseIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyNoProposalChosenIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyInvalidKeIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyTsUnacceptableIn,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifySaFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResDhComputeKeyFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyDhGroupFail,
       "jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail": jnxIkeHaLinkGlobalInitiatorIkev2IpsecSaRekeyResVerifyTsFail,
       "jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyStats": jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyStats,
       "jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn": jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyRequestIn,
       "jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut": jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResponseOut,
       "jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut": jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyNoProposalChosenOut,
       "jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut": jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyInvalidKeOut,
       "jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut": jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyTsUnacceptableOut,
       "jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail": jnxIkeHaLinkGlobalResponderIkev2IpsecSaRekeyResDhComputeKeyFail,
       "jnxIkeHaLinkGlobalIkev2MsgFailStats": jnxIkeHaLinkGlobalIkev2MsgFailStats,
       "jnxIkeHaLinkGlobalIkev2TotalDiscarded": jnxIkeHaLinkGlobalIkev2TotalDiscarded,
       "jnxIkeHaLinkGlobalIkev2TotalIdError": jnxIkeHaLinkGlobalIkev2TotalIdError,
       "jnxIkeHaLinkGlobalIkev2TotalIntegrityFail": jnxIkeHaLinkGlobalIkev2TotalIntegrityFail,
       "jnxIkeHaLinkGlobalIkev2TotalInvalidSPI": jnxIkeHaLinkGlobalIkev2TotalInvalidSPI,
       "jnxIkeHaLinkGlobalIkev2TotalInvalidExchgType": jnxIkeHaLinkGlobalIkev2TotalInvalidExchgType,
       "jnxIkeHaLinkGlobalIkev2TotalInvalidLength": jnxIkeHaLinkGlobalIkev2TotalInvalidLength,
       "jnxIkeHaLinkGlobalIkev2TotalDisorder": jnxIkeHaLinkGlobalIkev2TotalDisorder,
       "jnxIpSecFlowMonPhaseTwo": jnxIpSecFlowMonPhaseTwo,
       "jnxIpSecNumOfTunnels": jnxIpSecNumOfTunnels,
       "jnxIpSecTunnelMonTable": jnxIpSecTunnelMonTable,
       "jnxIpSecTunnelMonEntry": jnxIpSecTunnelMonEntry,
       "jnxIpSecTunMonRemoteGwAddrType": jnxIpSecTunMonRemoteGwAddrType,
       "jnxIpSecTunMonRemoteGwAddr": jnxIpSecTunMonRemoteGwAddr,
       "jnxIpSecTunMonIndex": jnxIpSecTunMonIndex,
       "jnxIpSecTunMonLocalGwAddrType": jnxIpSecTunMonLocalGwAddrType,
       "jnxIpSecTunMonLocalGwAddr": jnxIpSecTunMonLocalGwAddr,
       "jnxIpSecTunMonLocalProxyId": jnxIpSecTunMonLocalProxyId,
       "jnxIpSecTunMonRemoteProxyId": jnxIpSecTunMonRemoteProxyId,
       "jnxIpSecTunMonKeyType": jnxIpSecTunMonKeyType,
       "jnxIpSecTunMonRemotePeerType": jnxIpSecTunMonRemotePeerType,
       "jnxIpSecTunMonOutEncryptedBytes": jnxIpSecTunMonOutEncryptedBytes,
       "jnxIpSecTunMonOutEncryptedPkts": jnxIpSecTunMonOutEncryptedPkts,
       "jnxIpSecTunMonInDecryptedBytes": jnxIpSecTunMonInDecryptedBytes,
       "jnxIpSecTunMonInDecryptedPkts": jnxIpSecTunMonInDecryptedPkts,
       "jnxIpSecTunMonAHInBytes": jnxIpSecTunMonAHInBytes,
       "jnxIpSecTunMonAHInPkts": jnxIpSecTunMonAHInPkts,
       "jnxIpSecTunMonAHOutBytes": jnxIpSecTunMonAHOutBytes,
       "jnxIpSecTunMonAHOutPkts": jnxIpSecTunMonAHOutPkts,
       "jnxIpSecTunMonReplayDropPkts": jnxIpSecTunMonReplayDropPkts,
       "jnxIpSecTunMonAhAuthFails": jnxIpSecTunMonAhAuthFails,
       "jnxIpSecTunMonEspAuthFails": jnxIpSecTunMonEspAuthFails,
       "jnxIpSecTunMonDecryptFails": jnxIpSecTunMonDecryptFails,
       "jnxIpSecTunMonBadHeaders": jnxIpSecTunMonBadHeaders,
       "jnxIpSecTunMonBadTrailers": jnxIpSecTunMonBadTrailers,
       "jnxIpSecTunMonDroppedPkts": jnxIpSecTunMonDroppedPkts,
       "jnxIpSecTunMonVpnName": jnxIpSecTunMonVpnName,
       "jnxIpSecTunMonTsName": jnxIpSecTunMonTsName,
       "jnxIpSecTunMonMultiSa": jnxIpSecTunMonMultiSa,
       "jnxIpSecTunMonInvalidSpi": jnxIpSecTunMonInvalidSpi,
       "jnxIpSecTunMonTsCheckFail": jnxIpSecTunMonTsCheckFail,
       "jnxIpSecTunMonDiscarded": jnxIpSecTunMonDiscarded,
       "jnxIpSecTunMonTunType": jnxIpSecTunMonTunType,
       "jnxIpSecSaMonTable": jnxIpSecSaMonTable,
       "jnxIpSecSaMonEntry": jnxIpSecSaMonEntry,
       "jnxIpSecSaMonIndex": jnxIpSecSaMonIndex,
       "jnxIpSecSaMonProtocol": jnxIpSecSaMonProtocol,
       "jnxIpSecSaMonInSpi": jnxIpSecSaMonInSpi,
       "jnxIpSecSaMonOutSpi": jnxIpSecSaMonOutSpi,
       "jnxIpSecSaMonType": jnxIpSecSaMonType,
       "jnxIpSecSaMonEncapMode": jnxIpSecSaMonEncapMode,
       "jnxIpSecSaMonLifeSize": jnxIpSecSaMonLifeSize,
       "jnxIpSecSaMonLifeTime": jnxIpSecSaMonLifeTime,
       "jnxIpSecSaMonActiveTime": jnxIpSecSaMonActiveTime,
       "jnxIpSecSaMonLifeSizeThreshold": jnxIpSecSaMonLifeSizeThreshold,
       "jnxIpSecSaMonLifeTimeThreshold": jnxIpSecSaMonLifeTimeThreshold,
       "jnxIpSecSaMonEncryptAlgo": jnxIpSecSaMonEncryptAlgo,
       "jnxIpSecSaMonAuthAlgo": jnxIpSecSaMonAuthAlgo,
       "jnxIpSecSaMonState": jnxIpSecSaMonState,
       "jnxIpSecSaMonFcName": jnxIpSecSaMonFcName,
       "jnxIpSecSaMonEsnMode": jnxIpSecSaMonEsnMode,
       "jnxIpSecGlobalStats": jnxIpSecGlobalStats,
       "jnxIpSecGlobalOutEncryptedBytes": jnxIpSecGlobalOutEncryptedBytes,
       "jnxIpSecGlobalOutEncryptedPkts": jnxIpSecGlobalOutEncryptedPkts,
       "jnxIpSecGlobalInDecryptedBytes": jnxIpSecGlobalInDecryptedBytes,
       "jnxIpSecGlobalInDecryptedPkts": jnxIpSecGlobalInDecryptedPkts,
       "jnxIpSecGlobalAHInBytes": jnxIpSecGlobalAHInBytes,
       "jnxIpSecGlobalAHInPkts": jnxIpSecGlobalAHInPkts,
       "jnxIpSecGlobalAHOutBytes": jnxIpSecGlobalAHOutBytes,
       "jnxIpSecGlobalAHOutPkts": jnxIpSecGlobalAHOutPkts,
       "jnxIpSecGlobalReplayDropPkts": jnxIpSecGlobalReplayDropPkts,
       "jnxIpSecGlobalAhAuthFails": jnxIpSecGlobalAhAuthFails,
       "jnxIpSecGlobalEspAuthFails": jnxIpSecGlobalEspAuthFails,
       "jnxIpSecGlobalDecryptFails": jnxIpSecGlobalDecryptFails,
       "jnxIpSecGlobalBadHeaders": jnxIpSecGlobalBadHeaders,
       "jnxIpSecGlobalBadTrailers": jnxIpSecGlobalBadTrailers,
       "jnxIpSecGlobalInvalidSpi": jnxIpSecGlobalInvalidSpi,
       "jnxIpSecGlobalTsCheckFail": jnxIpSecGlobalTsCheckFail,
       "jnxIpSecGlobalDiscarded": jnxIpSecGlobalDiscarded,
       "jnxIpSecHaLinkGlobalStats": jnxIpSecHaLinkGlobalStats,
       "jnxIpSecHaLinkGlobalOutEncryptedBytes": jnxIpSecHaLinkGlobalOutEncryptedBytes,
       "jnxIpSecHaLinkGlobalOutEncryptedPkts": jnxIpSecHaLinkGlobalOutEncryptedPkts,
       "jnxIpSecHaLinkGlobalInDecryptedBytes": jnxIpSecHaLinkGlobalInDecryptedBytes,
       "jnxIpSecHaLinkGlobalInDecryptedPkts": jnxIpSecHaLinkGlobalInDecryptedPkts,
       "jnxIpSecHaLinkGlobalAHInBytes": jnxIpSecHaLinkGlobalAHInBytes,
       "jnxIpSecHaLinkGlobalAHInPkts": jnxIpSecHaLinkGlobalAHInPkts,
       "jnxIpSecHaLinkGlobalAHOutBytes": jnxIpSecHaLinkGlobalAHOutBytes,
       "jnxIpSecHaLinkGlobalAHOutPkts": jnxIpSecHaLinkGlobalAHOutPkts,
       "jnxIpSecHaLinkGlobalReplayDropPkts": jnxIpSecHaLinkGlobalReplayDropPkts,
       "jnxIpSecHaLinkGlobalAhAuthFails": jnxIpSecHaLinkGlobalAhAuthFails,
       "jnxIpSecHaLinkGlobalEspAuthFails": jnxIpSecHaLinkGlobalEspAuthFails,
       "jnxIpSecHaLinkGlobalDecryptFails": jnxIpSecHaLinkGlobalDecryptFails,
       "jnxIpSecHaLinkGlobalBadHeaders": jnxIpSecHaLinkGlobalBadHeaders,
       "jnxIpSecHaLinkGlobalBadTrailers": jnxIpSecHaLinkGlobalBadTrailers,
       "jnxIpSecHaLinkGlobalInvalidSpi": jnxIpSecHaLinkGlobalInvalidSpi,
       "jnxIpSecHaLinkGlobalTsCheckFail": jnxIpSecHaLinkGlobalTsCheckFail,
       "jnxIpSecHaLinkGlobalDiscarded": jnxIpSecHaLinkGlobalDiscarded}
)
