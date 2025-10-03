# SNMP MIB module (LINKSYS-openflow-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-openflow-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:09:31 2025
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

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlOpenFlow_ObjectIdentity = ObjectIdentity
rlOpenFlow = _RlOpenFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319)
)
_RlOpenFlowSupported_Type = TruthValue
_RlOpenFlowSupported_Object = MibScalar
rlOpenFlowSupported = _RlOpenFlowSupported_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 1),
    _RlOpenFlowSupported_Type()
)
rlOpenFlowSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpenFlowSupported.setStatus("current")


class _RlOpenFlowTcpPort_Type(Integer32):
    """Custom type rlOpenFlowTcpPort based on Integer32"""
    defaultValue = 6633


_RlOpenFlowTcpPort_Type.__name__ = "Integer32"
_RlOpenFlowTcpPort_Object = MibScalar
rlOpenFlowTcpPort = _RlOpenFlowTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 2),
    _RlOpenFlowTcpPort_Type()
)
rlOpenFlowTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpenFlowTcpPort.setStatus("current")


class _RlOpenFlowServerIpAddr_Type(IpAddress):
    """Custom type rlOpenFlowServerIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_RlOpenFlowServerIpAddr_Type.__name__ = "IpAddress"
_RlOpenFlowServerIpAddr_Object = MibScalar
rlOpenFlowServerIpAddr = _RlOpenFlowServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 3),
    _RlOpenFlowServerIpAddr_Type()
)
rlOpenFlowServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpenFlowServerIpAddr.setStatus("current")


class _RlOpenFlowProtocolType_Type(Integer32):
    """Custom type rlOpenFlowProtocolType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 0),
          ("tls", 1))
    )


_RlOpenFlowProtocolType_Type.__name__ = "Integer32"
_RlOpenFlowProtocolType_Object = MibScalar
rlOpenFlowProtocolType = _RlOpenFlowProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 4),
    _RlOpenFlowProtocolType_Type()
)
rlOpenFlowProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpenFlowProtocolType.setStatus("current")


class _RlOpenFlowDefaultForwardAction_Type(Integer32):
    """Custom type rlOpenFlowDefaultForwardAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 0),
          ("drop", 1),
          ("toController", 2))
    )


_RlOpenFlowDefaultForwardAction_Type.__name__ = "Integer32"
_RlOpenFlowDefaultForwardAction_Object = MibScalar
rlOpenFlowDefaultForwardAction = _RlOpenFlowDefaultForwardAction_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 5),
    _RlOpenFlowDefaultForwardAction_Type()
)
rlOpenFlowDefaultForwardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpenFlowDefaultForwardAction.setStatus("current")
_RlOpenFlowEnable_Type = TruthValue
_RlOpenFlowEnable_Object = MibScalar
rlOpenFlowEnable = _RlOpenFlowEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 6),
    _RlOpenFlowEnable_Type()
)
rlOpenFlowEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlOpenFlowEnable.setStatus("current")


class _RlOpenFlowEnableAfterReset_Type(TruthValue):
    """Custom type rlOpenFlowEnableAfterReset based on TruthValue"""
    defaultValue = 2


_RlOpenFlowEnableAfterReset_Type.__name__ = "TruthValue"
_RlOpenFlowEnableAfterReset_Object = MibScalar
rlOpenFlowEnableAfterReset = _RlOpenFlowEnableAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 319, 7),
    _RlOpenFlowEnableAfterReset_Type()
)
rlOpenFlowEnableAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlOpenFlowEnableAfterReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-openflow-MIB",
    **{"rlOpenFlow": rlOpenFlow,
       "rlOpenFlowSupported": rlOpenFlowSupported,
       "rlOpenFlowTcpPort": rlOpenFlowTcpPort,
       "rlOpenFlowServerIpAddr": rlOpenFlowServerIpAddr,
       "rlOpenFlowProtocolType": rlOpenFlowProtocolType,
       "rlOpenFlowDefaultForwardAction": rlOpenFlowDefaultForwardAction,
       "rlOpenFlowEnable": rlOpenFlowEnable,
       "rlOpenFlowEnableAfterReset": rlOpenFlowEnableAfterReset}
)
