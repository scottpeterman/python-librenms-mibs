# SNMP MIB module (JUNIPER-JS-IPSEC-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-JS-IPSEC-VPN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:29 2025
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

(jnxIpSecTunnelMonEntry,) = mibBuilder.importSymbols(
    "JUNIPER-IPSEC-FLOW-MON-MIB",
    "jnxIpSecTunnelMonEntry")

(jnxJsIPSecVpn,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsIPSecVpn")

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


# MODULE-IDENTITY

jnxJsIpSecVpnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1)
)
if mibBuilder.loadTexts:
    jnxJsIpSecVpnMib.setRevisions(
        ("2007-04-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxJsIpSecVpnType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("policyBased", 1),
          ("routeBased", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JnxJsIpSecVpnNotifications_ObjectIdentity = ObjectIdentity
jnxJsIpSecVpnNotifications = _JnxJsIpSecVpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 0)
)
_JnxJsIpSecVpnPhaseOne_ObjectIdentity = ObjectIdentity
jnxJsIpSecVpnPhaseOne = _JnxJsIpSecVpnPhaseOne_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 1)
)
_JnxJsIpSecVpnPhaseTwo_ObjectIdentity = ObjectIdentity
jnxJsIpSecVpnPhaseTwo = _JnxJsIpSecVpnPhaseTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2)
)
_JnxJsIpSecTunnelTable_Object = MibTable
jnxJsIpSecTunnelTable = _JnxJsIpSecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxJsIpSecTunnelTable.setStatus("current")
_JnxJsIpSecTunnelEntry_Object = MibTableRow
jnxJsIpSecTunnelEntry = _JnxJsIpSecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxJsIpSecTunnelEntry.setStatus("current")


class _JnxJsIpSecTunPolicyName_Type(DisplayString):
    """Custom type jnxJsIpSecTunPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JnxJsIpSecTunPolicyName_Type.__name__ = "DisplayString"
_JnxJsIpSecTunPolicyName_Object = MibTableColumn
jnxJsIpSecTunPolicyName = _JnxJsIpSecTunPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 1),
    _JnxJsIpSecTunPolicyName_Type()
)
jnxJsIpSecTunPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIpSecTunPolicyName.setStatus("current")
_JnxJsIpSecVpnTunType_Type = JnxJsIpSecVpnType
_JnxJsIpSecVpnTunType_Object = MibTableColumn
jnxJsIpSecVpnTunType = _JnxJsIpSecVpnTunType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 2),
    _JnxJsIpSecVpnTunType_Type()
)
jnxJsIpSecVpnTunType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIpSecVpnTunType.setStatus("current")


class _JnxJsIpSecTunCfgMonState_Type(Integer32):
    """Custom type jnxJsIpSecTunCfgMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_JnxJsIpSecTunCfgMonState_Type.__name__ = "Integer32"
_JnxJsIpSecTunCfgMonState_Object = MibTableColumn
jnxJsIpSecTunCfgMonState = _JnxJsIpSecTunCfgMonState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 3),
    _JnxJsIpSecTunCfgMonState_Type()
)
jnxJsIpSecTunCfgMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIpSecTunCfgMonState.setStatus("current")


class _JnxJsIpSecTunState_Type(Integer32):
    """Custom type jnxJsIpSecTunState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("vpnMonitoringDisabled", 3))
    )


_JnxJsIpSecTunState_Type.__name__ = "Integer32"
_JnxJsIpSecTunState_Object = MibTableColumn
jnxJsIpSecTunState = _JnxJsIpSecTunState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 4),
    _JnxJsIpSecTunState_Type()
)
jnxJsIpSecTunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIpSecTunState.setStatus("current")
jnxIpSecTunnelMonEntry.registerAugmentions(
    ("JUNIPER-JS-IPSEC-VPN-MIB",
     "jnxJsIpSecTunnelEntry")
)
jnxJsIpSecTunnelEntry.setIndexNames(*jnxIpSecTunnelMonEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-IPSEC-VPN-MIB",
    **{"JnxJsIpSecVpnType": JnxJsIpSecVpnType,
       "jnxJsIpSecVpnMib": jnxJsIpSecVpnMib,
       "jnxJsIpSecVpnNotifications": jnxJsIpSecVpnNotifications,
       "jnxJsIpSecVpnPhaseOne": jnxJsIpSecVpnPhaseOne,
       "jnxJsIpSecVpnPhaseTwo": jnxJsIpSecVpnPhaseTwo,
       "jnxJsIpSecTunnelTable": jnxJsIpSecTunnelTable,
       "jnxJsIpSecTunnelEntry": jnxJsIpSecTunnelEntry,
       "jnxJsIpSecTunPolicyName": jnxJsIpSecTunPolicyName,
       "jnxJsIpSecVpnTunType": jnxJsIpSecVpnTunType,
       "jnxJsIpSecTunCfgMonState": jnxJsIpSecTunCfgMonState,
       "jnxJsIpSecTunState": jnxJsIpSecTunState}
)
