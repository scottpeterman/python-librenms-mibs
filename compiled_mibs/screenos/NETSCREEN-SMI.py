# SNMP MIB module (NETSCREEN-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:10 2025
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

netscreen = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224)
)
if mibBuilder.loadTexts:
    netscreen.setRevisions(
        ("2004-08-31 00:00",
         "2004-05-03 00:00",
         "2004-03-03 00:00",
         "2001-09-28 00:00",
         "2000-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetscreenTrap_ObjectIdentity = ObjectIdentity
netscreenTrap = _NetscreenTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 0)
)
_NetscreenProducts_ObjectIdentity = ObjectIdentity
netscreenProducts = _NetscreenProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 1)
)
_NetscreenTrapInfo_ObjectIdentity = ObjectIdentity
netscreenTrapInfo = _NetscreenTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 2)
)
_NetscreenIDS_ObjectIdentity = ObjectIdentity
netscreenIDS = _NetscreenIDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 3)
)
_NetscreenVpn_ObjectIdentity = ObjectIdentity
netscreenVpn = _NetscreenVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4)
)
_NetscreenVpnMibModule_ObjectIdentity = ObjectIdentity
netscreenVpnMibModule = _NetscreenVpnMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0)
)
_NetscreenQos_ObjectIdentity = ObjectIdentity
netscreenQos = _NetscreenQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 5)
)
_NetscreenNsrp_ObjectIdentity = ObjectIdentity
netscreenNsrp = _NetscreenNsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6)
)
_NetscreenSetting_ObjectIdentity = ObjectIdentity
netscreenSetting = _NetscreenSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7)
)
_NetscreenSettingMibModule_ObjectIdentity = ObjectIdentity
netscreenSettingMibModule = _NetscreenSettingMibModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0)
)
_NetscreenZone_ObjectIdentity = ObjectIdentity
netscreenZone = _NetscreenZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 8)
)
_NetscreenInterface_ObjectIdentity = ObjectIdentity
netscreenInterface = _NetscreenInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 9)
)
_NetscreenPolicy_ObjectIdentity = ObjectIdentity
netscreenPolicy = _NetscreenPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 10)
)
_NetscreenNAT_ObjectIdentity = ObjectIdentity
netscreenNAT = _NetscreenNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 11)
)
_NetscreenAddr_ObjectIdentity = ObjectIdentity
netscreenAddr = _NetscreenAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 12)
)
_NetscreenService_ObjectIdentity = ObjectIdentity
netscreenService = _NetscreenService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 13)
)
_NetscreenSchedule_ObjectIdentity = ObjectIdentity
netscreenSchedule = _NetscreenSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 14)
)
_NetscreenVsys_ObjectIdentity = ObjectIdentity
netscreenVsys = _NetscreenVsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 15)
)
_NetscreenResource_ObjectIdentity = ObjectIdentity
netscreenResource = _NetscreenResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16)
)
_NetscreenIp_ObjectIdentity = ObjectIdentity
netscreenIp = _NetscreenIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 17)
)
_NetscreenVR_ObjectIdentity = ObjectIdentity
netscreenVR = _NetscreenVR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18)
)
_NetscreenChassis_ObjectIdentity = ObjectIdentity
netscreenChassis = _NetscreenChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 21)
)
_NetscreenUAC_ObjectIdentity = ObjectIdentity
netscreenUAC = _NetscreenUAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 22)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SMI",
    **{"netscreen": netscreen,
       "netscreenTrap": netscreenTrap,
       "netscreenProducts": netscreenProducts,
       "netscreenTrapInfo": netscreenTrapInfo,
       "netscreenIDS": netscreenIDS,
       "netscreenVpn": netscreenVpn,
       "netscreenVpnMibModule": netscreenVpnMibModule,
       "netscreenQos": netscreenQos,
       "netscreenNsrp": netscreenNsrp,
       "netscreenSetting": netscreenSetting,
       "netscreenSettingMibModule": netscreenSettingMibModule,
       "netscreenZone": netscreenZone,
       "netscreenInterface": netscreenInterface,
       "netscreenPolicy": netscreenPolicy,
       "netscreenNAT": netscreenNAT,
       "netscreenAddr": netscreenAddr,
       "netscreenService": netscreenService,
       "netscreenSchedule": netscreenSchedule,
       "netscreenVsys": netscreenVsys,
       "netscreenResource": netscreenResource,
       "netscreenIp": netscreenIp,
       "netscreenVR": netscreenVR,
       "netscreenChassis": netscreenChassis,
       "netscreenUAC": netscreenUAC}
)
