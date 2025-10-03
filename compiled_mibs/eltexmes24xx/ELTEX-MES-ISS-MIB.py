# SNMP MIB module (ELTEX-MES-ISS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltexmes24xx\ELTEX-MES-ISS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:47 2025
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

(elHardware,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "elHardware")

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

eltMesIss = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139)
)
if mibBuilder.loadTexts:
    eltMesIss.setRevisions(
        ("2024-09-11 00:00",
         "2023-04-10 00:00",
         "2022-05-04 00:00",
         "2021-12-06 00:00",
         "2021-10-07 00:00",
         "2021-04-21 00:00",
         "2021-03-09 00:00",
         "2018-11-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssAclMIB_ObjectIdentity = ObjectIdentity
eltMesIssAclMIB = _EltMesIssAclMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 1)
)
_EltMesIssPppoeMIB_ObjectIdentity = ObjectIdentity
eltMesIssPppoeMIB = _EltMesIssPppoeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 2)
)
_EltMesIssVlanMIB_ObjectIdentity = ObjectIdentity
eltMesIssVlanMIB = _EltMesIssVlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 3)
)
_EltMesIssInterfacesMIB_ObjectIdentity = ObjectIdentity
eltMesIssInterfacesMIB = _EltMesIssInterfacesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 4)
)
_EltMesIssQoSMIB_ObjectIdentity = ObjectIdentity
eltMesIssQoSMIB = _EltMesIssQoSMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5)
)
_EltMesIssCpuUtilMIB_ObjectIdentity = ObjectIdentity
eltMesIssCpuUtilMIB = _EltMesIssCpuUtilMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 6)
)
_EltMesIssAaaMIB_ObjectIdentity = ObjectIdentity
eltMesIssAaaMIB = _EltMesIssAaaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 7)
)
_EltMesIssSnoopMIB_ObjectIdentity = ObjectIdentity
eltMesIssSnoopMIB = _EltMesIssSnoopMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8)
)
_EltMesIssIpDbMIB_ObjectIdentity = ObjectIdentity
eltMesIssIpDbMIB = _EltMesIssIpDbMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9)
)
_EltMesIssLldpMIB_ObjectIdentity = ObjectIdentity
eltMesIssLldpMIB = _EltMesIssLldpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 10)
)
_EltMesIssPoeMIB_ObjectIdentity = ObjectIdentity
eltMesIssPoeMIB = _EltMesIssPoeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 11)
)
_EltMesIssEnvMIB_ObjectIdentity = ObjectIdentity
eltMesIssEnvMIB = _EltMesIssEnvMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 12)
)
_EltMesIssDcsMIB_ObjectIdentity = ObjectIdentity
eltMesIssDcsMIB = _EltMesIssDcsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 13)
)
_EltMesIssBridgeMIB_ObjectIdentity = ObjectIdentity
eltMesIssBridgeMIB = _EltMesIssBridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14)
)
_EltMesIssCopyMIB_ObjectIdentity = ObjectIdentity
eltMesIssCopyMIB = _EltMesIssCopyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15)
)
_EltMesIssSntpMIB_ObjectIdentity = ObjectIdentity
eltMesIssSntpMIB = _EltMesIssSntpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 16)
)
_EltMesIssSystemMIB_ObjectIdentity = ObjectIdentity
eltMesIssSystemMIB = _EltMesIssSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18)
)
_EltMesIssSnmp3MIB_ObjectIdentity = ObjectIdentity
eltMesIssSnmp3MIB = _EltMesIssSnmp3MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 19)
)
_EltMesIssCfaMIB_ObjectIdentity = ObjectIdentity
eltMesIssCfaMIB = _EltMesIssCfaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 20)
)
_EltMesIssL2ptMIB_ObjectIdentity = ObjectIdentity
eltMesIssL2ptMIB = _EltMesIssL2ptMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 21)
)
_EltMesIssSyslogMIB_ObjectIdentity = ObjectIdentity
eltMesIssSyslogMIB = _EltMesIssSyslogMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 22)
)
_EltMesIssLaMIB_ObjectIdentity = ObjectIdentity
eltMesIssLaMIB = _EltMesIssLaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23)
)
_EltMesIssIpMIB_ObjectIdentity = ObjectIdentity
eltMesIssIpMIB = _EltMesIssIpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24)
)
_EltMesIssL2Ip6SnpMIB_ObjectIdentity = ObjectIdentity
eltMesIssL2Ip6SnpMIB = _EltMesIssL2Ip6SnpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 25)
)
_EltMesIssArpMIB_ObjectIdentity = ObjectIdentity
eltMesIssArpMIB = _EltMesIssArpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 26)
)
_EltMesIssFwlMIB_ObjectIdentity = ObjectIdentity
eltMesIssFwlMIB = _EltMesIssFwlMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 27)
)
_EltMesIssDhcpRelayMIB_ObjectIdentity = ObjectIdentity
eltMesIssDhcpRelayMIB = _EltMesIssDhcpRelayMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 28)
)
_EltMesIssErpsMIB_ObjectIdentity = ObjectIdentity
eltMesIssErpsMIB = _EltMesIssErpsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 29)
)
_EltMesIssSshMIB_ObjectIdentity = ObjectIdentity
eltMesIssSshMIB = _EltMesIssSshMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 30)
)
_EltMesIssPnacMIB_ObjectIdentity = ObjectIdentity
eltMesIssPnacMIB = _EltMesIssPnacMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 31)
)
_EltMesIssDhcpSnoopMIB_ObjectIdentity = ObjectIdentity
eltMesIssDhcpSnoopMIB = _EltMesIssDhcpSnoopMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 32)
)
_EltMesIssDhcpSrvMIB_ObjectIdentity = ObjectIdentity
eltMesIssDhcpSrvMIB = _EltMesIssDhcpSrvMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 33)
)
_EltMesIssLbdMIB_ObjectIdentity = ObjectIdentity
eltMesIssLbdMIB = _EltMesIssLbdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 34)
)
_EltMesIssRadiusMIB_ObjectIdentity = ObjectIdentity
eltMesIssRadiusMIB = _EltMesIssRadiusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 35)
)
_EltMesIssUserMgmMIB_ObjectIdentity = ObjectIdentity
eltMesIssUserMgmMIB = _EltMesIssUserMgmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 36)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-MIB",
    **{"eltMesIss": eltMesIss,
       "eltMesIssAclMIB": eltMesIssAclMIB,
       "eltMesIssPppoeMIB": eltMesIssPppoeMIB,
       "eltMesIssVlanMIB": eltMesIssVlanMIB,
       "eltMesIssInterfacesMIB": eltMesIssInterfacesMIB,
       "eltMesIssQoSMIB": eltMesIssQoSMIB,
       "eltMesIssCpuUtilMIB": eltMesIssCpuUtilMIB,
       "eltMesIssAaaMIB": eltMesIssAaaMIB,
       "eltMesIssSnoopMIB": eltMesIssSnoopMIB,
       "eltMesIssIpDbMIB": eltMesIssIpDbMIB,
       "eltMesIssLldpMIB": eltMesIssLldpMIB,
       "eltMesIssPoeMIB": eltMesIssPoeMIB,
       "eltMesIssEnvMIB": eltMesIssEnvMIB,
       "eltMesIssDcsMIB": eltMesIssDcsMIB,
       "eltMesIssBridgeMIB": eltMesIssBridgeMIB,
       "eltMesIssCopyMIB": eltMesIssCopyMIB,
       "eltMesIssSntpMIB": eltMesIssSntpMIB,
       "eltMesIssSystemMIB": eltMesIssSystemMIB,
       "eltMesIssSnmp3MIB": eltMesIssSnmp3MIB,
       "eltMesIssCfaMIB": eltMesIssCfaMIB,
       "eltMesIssL2ptMIB": eltMesIssL2ptMIB,
       "eltMesIssSyslogMIB": eltMesIssSyslogMIB,
       "eltMesIssLaMIB": eltMesIssLaMIB,
       "eltMesIssIpMIB": eltMesIssIpMIB,
       "eltMesIssL2Ip6SnpMIB": eltMesIssL2Ip6SnpMIB,
       "eltMesIssArpMIB": eltMesIssArpMIB,
       "eltMesIssFwlMIB": eltMesIssFwlMIB,
       "eltMesIssDhcpRelayMIB": eltMesIssDhcpRelayMIB,
       "eltMesIssErpsMIB": eltMesIssErpsMIB,
       "eltMesIssSshMIB": eltMesIssSshMIB,
       "eltMesIssPnacMIB": eltMesIssPnacMIB,
       "eltMesIssDhcpSnoopMIB": eltMesIssDhcpSnoopMIB,
       "eltMesIssDhcpSrvMIB": eltMesIssDhcpSrvMIB,
       "eltMesIssLbdMIB": eltMesIssLbdMIB,
       "eltMesIssRadiusMIB": eltMesIssRadiusMIB,
       "eltMesIssUserMgmMIB": eltMesIssUserMgmMIB}
)
