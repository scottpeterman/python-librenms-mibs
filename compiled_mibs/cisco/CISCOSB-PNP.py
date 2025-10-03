# SNMP MIB module (CISCOSB-PNP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-PNP
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:13 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlPNP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234)
)
if mibBuilder.loadTexts:
    rlPNP.setRevisions(
        ("2011-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlOwnerType(TextualConvention, Integer32):
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
        *(("rlOwnerNone", 0),
          ("rlOwnerDefault", 1),
          ("rlOwnerStatic", 2),
          ("rlOwnerDHCP", 3),
          ("rlOwnerProtocol", 4),
          ("rlOwnerDelete", 5))
    )



# MIB Managed Objects in the order of their OIDs

_RlPNPParamsTable_Object = MibTable
rlPNPParamsTable = _RlPNPParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1)
)
if mibBuilder.loadTexts:
    rlPNPParamsTable.setStatus("current")
_RlPNPParamsEntry_Object = MibTableRow
rlPNPParamsEntry = _RlPNPParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1)
)
rlPNPParamsEntry.setIndexNames(
    (0, "CISCOSB-PNP", "rlPNPParamsAvailability"),
)
if mibBuilder.loadTexts:
    rlPNPParamsEntry.setStatus("current")


class _RlPNPParamsAvailability_Type(Integer32):
    """Custom type rlPNPParamsAvailability based on Integer32"""
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
          ("next", 1),
          ("current", 2))
    )


_RlPNPParamsAvailability_Type.__name__ = "Integer32"
_RlPNPParamsAvailability_Object = MibTableColumn
rlPNPParamsAvailability = _RlPNPParamsAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 1),
    _RlPNPParamsAvailability_Type()
)
rlPNPParamsAvailability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPNPParamsAvailability.setStatus("current")
_RlPNPServerAddrType_Type = InetAddressType
_RlPNPServerAddrType_Object = MibTableColumn
rlPNPServerAddrType = _RlPNPServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 2),
    _RlPNPServerAddrType_Type()
)
rlPNPServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPServerAddrType.setStatus("current")


class _RlPNPServerAddr_Type(InetAddress):
    """Custom type rlPNPServerAddr based on InetAddress"""
    defaultHexValue = "706e70736572766572"


_RlPNPServerAddr_Type.__name__ = "InetAddress"
_RlPNPServerAddr_Object = MibTableColumn
rlPNPServerAddr = _RlPNPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 3),
    _RlPNPServerAddr_Type()
)
rlPNPServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPServerAddr.setStatus("current")


class _RlPNPServerAddrOwner_Type(RlOwnerType):
    """Custom type rlPNPServerAddrOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPServerAddrOwner_Type.__name__ = "RlOwnerType"
_RlPNPServerAddrOwner_Object = MibTableColumn
rlPNPServerAddrOwner = _RlPNPServerAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 4),
    _RlPNPServerAddrOwner_Type()
)
rlPNPServerAddrOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPServerAddrOwner.setStatus("current")


class _RlPNPProtocol_Type(Integer32):
    """Custom type rlPNPProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("http", 0),
          ("https", 1))
    )


_RlPNPProtocol_Type.__name__ = "Integer32"
_RlPNPProtocol_Object = MibTableColumn
rlPNPProtocol = _RlPNPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 5),
    _RlPNPProtocol_Type()
)
rlPNPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPProtocol.setStatus("current")


class _RlPNPProtocolOwner_Type(RlOwnerType):
    """Custom type rlPNPProtocolOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPProtocolOwner_Type.__name__ = "RlOwnerType"
_RlPNPProtocolOwner_Object = MibTableColumn
rlPNPProtocolOwner = _RlPNPProtocolOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 6),
    _RlPNPProtocolOwner_Type()
)
rlPNPProtocolOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPProtocolOwner.setStatus("current")


class _RlPNPHTTPPort_Type(Unsigned32):
    """Custom type rlPNPHTTPPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlPNPHTTPPort_Type.__name__ = "Unsigned32"
_RlPNPHTTPPort_Object = MibTableColumn
rlPNPHTTPPort = _RlPNPHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 7),
    _RlPNPHTTPPort_Type()
)
rlPNPHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPHTTPPort.setStatus("current")


class _RlPNPHTTPPortOwner_Type(RlOwnerType):
    """Custom type rlPNPHTTPPortOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPHTTPPortOwner_Type.__name__ = "RlOwnerType"
_RlPNPHTTPPortOwner_Object = MibTableColumn
rlPNPHTTPPortOwner = _RlPNPHTTPPortOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 8),
    _RlPNPHTTPPortOwner_Type()
)
rlPNPHTTPPortOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPHTTPPortOwner.setStatus("current")


class _RlPNPHTTPSPort_Type(Unsigned32):
    """Custom type rlPNPHTTPSPort based on Unsigned32"""
    defaultValue = 443

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlPNPHTTPSPort_Type.__name__ = "Unsigned32"
_RlPNPHTTPSPort_Object = MibTableColumn
rlPNPHTTPSPort = _RlPNPHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 9),
    _RlPNPHTTPSPort_Type()
)
rlPNPHTTPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPHTTPSPort.setStatus("current")


class _RlPNPHTTPSPortOwner_Type(RlOwnerType):
    """Custom type rlPNPHTTPSPortOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPHTTPSPortOwner_Type.__name__ = "RlOwnerType"
_RlPNPHTTPSPortOwner_Object = MibTableColumn
rlPNPHTTPSPortOwner = _RlPNPHTTPSPortOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 10),
    _RlPNPHTTPSPortOwner_Type()
)
rlPNPHTTPSPortOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPHTTPSPortOwner.setStatus("current")


class _RlPNPUserName_Type(DisplayString):
    """Custom type rlPNPUserName based on DisplayString"""
    defaultValue = OctetString("")


_RlPNPUserName_Type.__name__ = "DisplayString"
_RlPNPUserName_Object = MibTableColumn
rlPNPUserName = _RlPNPUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 11),
    _RlPNPUserName_Type()
)
rlPNPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPUserName.setStatus("current")


class _RlPNPUserNameOwner_Type(RlOwnerType):
    """Custom type rlPNPUserNameOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPUserNameOwner_Type.__name__ = "RlOwnerType"
_RlPNPUserNameOwner_Object = MibTableColumn
rlPNPUserNameOwner = _RlPNPUserNameOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 12),
    _RlPNPUserNameOwner_Type()
)
rlPNPUserNameOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPUserNameOwner.setStatus("current")


class _RlPNPPassword_Type(SnmpAdminString):
    """Custom type rlPNPPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlPNPPassword_Type.__name__ = "SnmpAdminString"
_RlPNPPassword_Object = MibTableColumn
rlPNPPassword = _RlPNPPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 13),
    _RlPNPPassword_Type()
)
rlPNPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPPassword.setStatus("current")


class _RlPNPPasswordOwner_Type(RlOwnerType):
    """Custom type rlPNPPasswordOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPPasswordOwner_Type.__name__ = "RlOwnerType"
_RlPNPPasswordOwner_Object = MibTableColumn
rlPNPPasswordOwner = _RlPNPPasswordOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 14),
    _RlPNPPasswordOwner_Type()
)
rlPNPPasswordOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPPasswordOwner.setStatus("current")


class _RlPNPDiscoveryTimeout_Type(Unsigned32):
    """Custom type rlPNPDiscoveryTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000),
    )


_RlPNPDiscoveryTimeout_Type.__name__ = "Unsigned32"
_RlPNPDiscoveryTimeout_Object = MibTableColumn
rlPNPDiscoveryTimeout = _RlPNPDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 15),
    _RlPNPDiscoveryTimeout_Type()
)
rlPNPDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPDiscoveryTimeout.setStatus("current")


class _RlPNPDiscoveryTimeoutOwner_Type(RlOwnerType):
    """Custom type rlPNPDiscoveryTimeoutOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPDiscoveryTimeoutOwner_Type.__name__ = "RlOwnerType"
_RlPNPDiscoveryTimeoutOwner_Object = MibTableColumn
rlPNPDiscoveryTimeoutOwner = _RlPNPDiscoveryTimeoutOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 16),
    _RlPNPDiscoveryTimeoutOwner_Type()
)
rlPNPDiscoveryTimeoutOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPDiscoveryTimeoutOwner.setStatus("current")


class _RlPNPDiscoveryExpoFactor_Type(Unsigned32):
    """Custom type rlPNPDiscoveryExpoFactor based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_RlPNPDiscoveryExpoFactor_Type.__name__ = "Unsigned32"
_RlPNPDiscoveryExpoFactor_Object = MibTableColumn
rlPNPDiscoveryExpoFactor = _RlPNPDiscoveryExpoFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 17),
    _RlPNPDiscoveryExpoFactor_Type()
)
rlPNPDiscoveryExpoFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPDiscoveryExpoFactor.setStatus("current")


class _RlPNPDiscoveryExpoFactorOwner_Type(RlOwnerType):
    """Custom type rlPNPDiscoveryExpoFactorOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPDiscoveryExpoFactorOwner_Type.__name__ = "RlOwnerType"
_RlPNPDiscoveryExpoFactorOwner_Object = MibTableColumn
rlPNPDiscoveryExpoFactorOwner = _RlPNPDiscoveryExpoFactorOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 18),
    _RlPNPDiscoveryExpoFactorOwner_Type()
)
rlPNPDiscoveryExpoFactorOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPDiscoveryExpoFactorOwner.setStatus("current")


class _RlPNPDiscoveryTimeoutMax_Type(Unsigned32):
    """Custom type rlPNPDiscoveryTimeoutMax based on Unsigned32"""
    defaultValue = 540

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000),
    )


_RlPNPDiscoveryTimeoutMax_Type.__name__ = "Unsigned32"
_RlPNPDiscoveryTimeoutMax_Object = MibTableColumn
rlPNPDiscoveryTimeoutMax = _RlPNPDiscoveryTimeoutMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 19),
    _RlPNPDiscoveryTimeoutMax_Type()
)
rlPNPDiscoveryTimeoutMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPDiscoveryTimeoutMax.setStatus("current")


class _RlPNPDiscoveryTimeoutMaxOwner_Type(RlOwnerType):
    """Custom type rlPNPDiscoveryTimeoutMaxOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPDiscoveryTimeoutMaxOwner_Type.__name__ = "RlOwnerType"
_RlPNPDiscoveryTimeoutMaxOwner_Object = MibTableColumn
rlPNPDiscoveryTimeoutMaxOwner = _RlPNPDiscoveryTimeoutMaxOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 20),
    _RlPNPDiscoveryTimeoutMaxOwner_Type()
)
rlPNPDiscoveryTimeoutMaxOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPDiscoveryTimeoutMaxOwner.setStatus("current")


class _RlPNPReconnectTimeout_Type(Unsigned32):
    """Custom type rlPNPReconnectTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000),
    )


_RlPNPReconnectTimeout_Type.__name__ = "Unsigned32"
_RlPNPReconnectTimeout_Object = MibTableColumn
rlPNPReconnectTimeout = _RlPNPReconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 21),
    _RlPNPReconnectTimeout_Type()
)
rlPNPReconnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPReconnectTimeout.setStatus("current")


class _RlPNPReconnectTimeoutOwner_Type(RlOwnerType):
    """Custom type rlPNPReconnectTimeoutOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPReconnectTimeoutOwner_Type.__name__ = "RlOwnerType"
_RlPNPReconnectTimeoutOwner_Object = MibTableColumn
rlPNPReconnectTimeoutOwner = _RlPNPReconnectTimeoutOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 22),
    _RlPNPReconnectTimeoutOwner_Type()
)
rlPNPReconnectTimeoutOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPReconnectTimeoutOwner.setStatus("current")
_RlPNPSrcAddrTyp_Type = InetAddressType
_RlPNPSrcAddrTyp_Object = MibTableColumn
rlPNPSrcAddrTyp = _RlPNPSrcAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 23),
    _RlPNPSrcAddrTyp_Type()
)
rlPNPSrcAddrTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPSrcAddrTyp.setStatus("current")


class _RlPNPSrcAddr_Type(InetAddress):
    """Custom type rlPNPSrcAddr based on InetAddress"""
    defaultHexValue = "00000000"


_RlPNPSrcAddr_Type.__name__ = "InetAddress"
_RlPNPSrcAddr_Object = MibTableColumn
rlPNPSrcAddr = _RlPNPSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 24),
    _RlPNPSrcAddr_Type()
)
rlPNPSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPSrcAddr.setStatus("current")


class _RlPNPSrcAddrOwner_Type(RlOwnerType):
    """Custom type rlPNPSrcAddrOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPSrcAddrOwner_Type.__name__ = "RlOwnerType"
_RlPNPSrcAddrOwner_Object = MibTableColumn
rlPNPSrcAddrOwner = _RlPNPSrcAddrOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 25),
    _RlPNPSrcAddrOwner_Type()
)
rlPNPSrcAddrOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPSrcAddrOwner.setStatus("current")


class _RlPNPWatchdogTimeout_Type(Unsigned32):
    """Custom type rlPNPWatchdogTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_RlPNPWatchdogTimeout_Type.__name__ = "Unsigned32"
_RlPNPWatchdogTimeout_Object = MibTableColumn
rlPNPWatchdogTimeout = _RlPNPWatchdogTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 26),
    _RlPNPWatchdogTimeout_Type()
)
rlPNPWatchdogTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPWatchdogTimeout.setStatus("current")


class _RlPNPWatchdogTimeoutOwner_Type(RlOwnerType):
    """Custom type rlPNPWatchdogTimeoutOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPWatchdogTimeoutOwner_Type.__name__ = "RlOwnerType"
_RlPNPWatchdogTimeoutOwner_Object = MibTableColumn
rlPNPWatchdogTimeoutOwner = _RlPNPWatchdogTimeoutOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 27),
    _RlPNPWatchdogTimeoutOwner_Type()
)
rlPNPWatchdogTimeoutOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPWatchdogTimeoutOwner.setStatus("current")


class _RlPNPAdminState_Type(Integer32):
    """Custom type rlPNPAdminState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_RlPNPAdminState_Type.__name__ = "Integer32"
_RlPNPAdminState_Object = MibTableColumn
rlPNPAdminState = _RlPNPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 28),
    _RlPNPAdminState_Type()
)
rlPNPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPAdminState.setStatus("current")


class _RlPNPAdminStateOwner_Type(RlOwnerType):
    """Custom type rlPNPAdminStateOwner based on RlOwnerType"""
    defaultValue = 1


_RlPNPAdminStateOwner_Type.__name__ = "RlOwnerType"
_RlPNPAdminStateOwner_Object = MibTableColumn
rlPNPAdminStateOwner = _RlPNPAdminStateOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 29),
    _RlPNPAdminStateOwner_Type()
)
rlPNPAdminStateOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPAdminStateOwner.setStatus("current")
_RlPNPRowStatus_Type = RowStatus
_RlPNPRowStatus_Object = MibTableColumn
rlPNPRowStatus = _RlPNPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 1, 1, 30),
    _RlPNPRowStatus_Type()
)
rlPNPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlPNPRowStatus.setStatus("current")


class _RlPNPResume_Type(Integer32):
    """Custom type rlPNPResume based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_RlPNPResume_Type.__name__ = "Integer32"
_RlPNPResume_Object = MibScalar
rlPNPResume = _RlPNPResume_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 2),
    _RlPNPResume_Type()
)
rlPNPResume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPNPResume.setStatus("current")


class _RlPNPNreadyReason_Type(Integer32):
    """Custom type rlPNPNreadyReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serverIP", 0),
          ("certificate", 1),
          ("tod", 2))
    )


_RlPNPNreadyReason_Type.__name__ = "Integer32"
_RlPNPNreadyReason_Object = MibScalar
rlPNPNreadyReason = _RlPNPNreadyReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 3),
    _RlPNPNreadyReason_Type()
)
rlPNPNreadyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPNPNreadyReason.setStatus("current")


class _RlPNPState_Type(Integer32):
    """Custom type rlPNPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bootup", 0),
          ("discovery", 1),
          ("discoveryWait", 2),
          ("session", 3),
          ("sessionWait", 4),
          ("disabled", 5),
          ("notReady", 6))
    )


_RlPNPState_Type.__name__ = "Integer32"
_RlPNPState_Object = MibScalar
rlPNPState = _RlPNPState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 4),
    _RlPNPState_Type()
)
rlPNPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPNPState.setStatus("current")
_RlPNPTimerRemainder_Type = Integer32
_RlPNPTimerRemainder_Object = MibScalar
rlPNPTimerRemainder = _RlPNPTimerRemainder_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 234, 5),
    _RlPNPTimerRemainder_Type()
)
rlPNPTimerRemainder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPNPTimerRemainder.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-PNP",
    **{"RlOwnerType": RlOwnerType,
       "rlPNP": rlPNP,
       "rlPNPParamsTable": rlPNPParamsTable,
       "rlPNPParamsEntry": rlPNPParamsEntry,
       "rlPNPParamsAvailability": rlPNPParamsAvailability,
       "rlPNPServerAddrType": rlPNPServerAddrType,
       "rlPNPServerAddr": rlPNPServerAddr,
       "rlPNPServerAddrOwner": rlPNPServerAddrOwner,
       "rlPNPProtocol": rlPNPProtocol,
       "rlPNPProtocolOwner": rlPNPProtocolOwner,
       "rlPNPHTTPPort": rlPNPHTTPPort,
       "rlPNPHTTPPortOwner": rlPNPHTTPPortOwner,
       "rlPNPHTTPSPort": rlPNPHTTPSPort,
       "rlPNPHTTPSPortOwner": rlPNPHTTPSPortOwner,
       "rlPNPUserName": rlPNPUserName,
       "rlPNPUserNameOwner": rlPNPUserNameOwner,
       "rlPNPPassword": rlPNPPassword,
       "rlPNPPasswordOwner": rlPNPPasswordOwner,
       "rlPNPDiscoveryTimeout": rlPNPDiscoveryTimeout,
       "rlPNPDiscoveryTimeoutOwner": rlPNPDiscoveryTimeoutOwner,
       "rlPNPDiscoveryExpoFactor": rlPNPDiscoveryExpoFactor,
       "rlPNPDiscoveryExpoFactorOwner": rlPNPDiscoveryExpoFactorOwner,
       "rlPNPDiscoveryTimeoutMax": rlPNPDiscoveryTimeoutMax,
       "rlPNPDiscoveryTimeoutMaxOwner": rlPNPDiscoveryTimeoutMaxOwner,
       "rlPNPReconnectTimeout": rlPNPReconnectTimeout,
       "rlPNPReconnectTimeoutOwner": rlPNPReconnectTimeoutOwner,
       "rlPNPSrcAddrTyp": rlPNPSrcAddrTyp,
       "rlPNPSrcAddr": rlPNPSrcAddr,
       "rlPNPSrcAddrOwner": rlPNPSrcAddrOwner,
       "rlPNPWatchdogTimeout": rlPNPWatchdogTimeout,
       "rlPNPWatchdogTimeoutOwner": rlPNPWatchdogTimeoutOwner,
       "rlPNPAdminState": rlPNPAdminState,
       "rlPNPAdminStateOwner": rlPNPAdminStateOwner,
       "rlPNPRowStatus": rlPNPRowStatus,
       "rlPNPResume": rlPNPResume,
       "rlPNPNreadyReason": rlPNPNreadyReason,
       "rlPNPState": rlPNPState,
       "rlPNPTimerRemainder": rlPNPTimerRemainder}
)
