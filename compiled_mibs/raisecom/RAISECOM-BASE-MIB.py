# SNMP MIB module (RAISECOM-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\raisecom\RAISECOM-BASE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:22:55 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Raisecom_ObjectIdentity = ObjectIdentity
raisecom = _Raisecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886)
)
_RaisecomAgent_ObjectIdentity = ObjectIdentity
raisecomAgent = _RaisecomAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1)
)
_Rc002_ObjectIdentity = ObjectIdentity
rc002 = _Rc002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2)
)
_Rc003_ObjectIdentity = ObjectIdentity
rc003 = _Rc003_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 3)
)
_Rc004_ObjectIdentity = ObjectIdentity
rc004 = _Rc004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 4)
)
_Rc701FE_ObjectIdentity = ObjectIdentity
rc701FE = _Rc701FE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 5)
)
_IscomSeries_ObjectIdentity = ObjectIdentity
iscomSeries = _IscomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6)
)
_IscomSwitch_ObjectIdentity = ObjectIdentity
iscomSwitch = _IscomSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1)
)
_OpcomSeries_ObjectIdentity = ObjectIdentity
opcomSeries = _OpcomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 7)
)
_RaisecomManager_ObjectIdentity = ObjectIdentity
raisecomManager = _RaisecomManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 8)
)
_IscomPM_ObjectIdentity = ObjectIdentity
iscomPM = _IscomPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 8, 1)
)
_PcAgent_ObjectIdentity = ObjectIdentity
pcAgent = _PcAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 9)
)
_PccomSeries_ObjectIdentity = ObjectIdentity
pccomSeries = _PccomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 10)
)
_OemSeries_ObjectIdentity = ObjectIdentity
oemSeries = _OemSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 11)
)
_RcSeries_ObjectIdentity = ObjectIdentity
rcSeries = _RcSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 12)
)
_RaisecomOptSysCommon_ObjectIdentity = ObjectIdentity
raisecomOptSysCommon = _RaisecomOptSysCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15)
)
_OptSysMgmt_ObjectIdentity = ObjectIdentity
optSysMgmt = _OptSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 1)
)
_OptSysModules_ObjectIdentity = ObjectIdentity
optSysModules = _OptSysModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 2)
)
_OptAgentCapability_ObjectIdentity = ObjectIdentity
optAgentCapability = _OptAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 3)
)
_OptUdSysMgmt_ObjectIdentity = ObjectIdentity
optUdSysMgmt = _OptUdSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 4)
)
_OptUdSysModules_ObjectIdentity = ObjectIdentity
optUdSysModules = _OptUdSysModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 15, 5)
)
_RosliteSeries_ObjectIdentity = ObjectIdentity
rosliteSeries = _RosliteSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 16)
)
_Draft_ObjectIdentity = ObjectIdentity
draft = _Draft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 17)
)
_PonSeries_ObjectIdentity = ObjectIdentity
ponSeries = _PonSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 18)
)
_TdmopSeries_ObjectIdentity = ObjectIdentity
tdmopSeries = _TdmopSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 19)
)
_DlcomSeries_ObjectIdentity = ObjectIdentity
dlcomSeries = _DlcomSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 20)
)
_RaisecomTerminalMgmt_ObjectIdentity = ObjectIdentity
raisecomTerminalMgmt = _RaisecomTerminalMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 21)
)
_MsgSeries_ObjectIdentity = ObjectIdentity
msgSeries = _MsgSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 22)
)
_ITNSeries_ObjectIdentity = ObjectIdentity
iTNSeries = _ITNSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 23)
)
_GazelleSwitchSeries_ObjectIdentity = ObjectIdentity
gazelleSwitchSeries = _GazelleSwitchSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 26)
)
_GazelleTransmitSeries_ObjectIdentity = ObjectIdentity
gazelleTransmitSeries = _GazelleTransmitSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 27)
)
_GazelleRouterSeries_ObjectIdentity = ObjectIdentity
gazelleRouterSeries = _GazelleRouterSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 28)
)
_ShenlanxuntongSeries_ObjectIdentity = ObjectIdentity
shenlanxuntongSeries = _ShenlanxuntongSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 29)
)
_SltSeries_ObjectIdentity = ObjectIdentity
sltSeries = _SltSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 29, 1)
)
_OTNSeries_ObjectIdentity = ObjectIdentity
OTNSeries = _OTNSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 30)
)
_RosMgmt_ObjectIdentity = ObjectIdentity
rosMgmt = _RosMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 60)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-BASE-MIB",
    **{"raisecom": raisecom,
       "raisecomAgent": raisecomAgent,
       "rc002": rc002,
       "rc003": rc003,
       "rc004": rc004,
       "rc701FE": rc701FE,
       "iscomSeries": iscomSeries,
       "iscomSwitch": iscomSwitch,
       "opcomSeries": opcomSeries,
       "raisecomManager": raisecomManager,
       "iscomPM": iscomPM,
       "pcAgent": pcAgent,
       "pccomSeries": pccomSeries,
       "oemSeries": oemSeries,
       "rcSeries": rcSeries,
       "raisecomOptSysCommon": raisecomOptSysCommon,
       "optSysMgmt": optSysMgmt,
       "optSysModules": optSysModules,
       "optAgentCapability": optAgentCapability,
       "optUdSysMgmt": optUdSysMgmt,
       "optUdSysModules": optUdSysModules,
       "rosliteSeries": rosliteSeries,
       "draft": draft,
       "ponSeries": ponSeries,
       "tdmopSeries": tdmopSeries,
       "dlcomSeries": dlcomSeries,
       "raisecomTerminalMgmt": raisecomTerminalMgmt,
       "msgSeries": msgSeries,
       "iTNSeries": iTNSeries,
       "gazelleSwitchSeries": gazelleSwitchSeries,
       "gazelleTransmitSeries": gazelleTransmitSeries,
       "gazelleRouterSeries": gazelleRouterSeries,
       "shenlanxuntongSeries": shenlanxuntongSeries,
       "sltSeries": sltSeries,
       "OTNSeries": OTNSeries,
       "rosMgmt": rosMgmt}
)
