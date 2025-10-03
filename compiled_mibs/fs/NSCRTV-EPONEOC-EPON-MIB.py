# SNMP MIB module (NSCRTV-EPONEOC-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\NSCRTV-EPONEOC-EPON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:46:50 2025
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

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EponDeviceIndex(TextualConvention, Unsigned32):
    status = "current"


class EponCardIndex(TextualConvention, Unsigned32):
    status = "current"


class EponPortIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EponAlarmCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class EponAlarmInstance(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class EponSeverityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("info", 5),
          ("clear", 6))
    )



class AutoNegotiationTechAbility(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tenBaseTFullDuplex", 1),
          ("tenBaseTHalfDuplex", 2),
          ("hundredBaseTFullDuplex", 3),
          ("hundredBaseTHalfDuplex", 4),
          ("thousandBaseTFullDuplex", 5),
          ("thousandBaseTHalfDuplex", 6),
          ("thousandBaseXFullDuplex", 7),
          ("thousandBaseXHalfDuplex", 8),
          ("fdxPause", 9),
          ("fdxApause", 10),
          ("fdxSpause", 11),
          ("fdxBpause", 12))
    )


class TAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class EponStats15MinRecordType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )



class EponStats24HourRecordType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



class EponStatsThresholdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_NscrtvRoot_ObjectIdentity = ObjectIdentity
nscrtvRoot = _NscrtvRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409)
)
_NscrtvHFCemsTree_ObjectIdentity = ObjectIdentity
nscrtvHFCemsTree = _NscrtvHFCemsTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1)
)
_NscrtvEponEocTree_ObjectIdentity = ObjectIdentity
nscrtvEponEocTree = _NscrtvEponEocTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2)
)
_PropertyIdent_ObjectIdentity = ObjectIdentity
propertyIdent = _PropertyIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 1)
)
_AlarmsIdent_ObjectIdentity = ObjectIdentity
alarmsIdent = _AlarmsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2)
)
_EponAlarmTree_ObjectIdentity = ObjectIdentity
eponAlarmTree = _EponAlarmTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11)
)
_EponTrapObjectGroup_ObjectIdentity = ObjectIdentity
eponTrapObjectGroup = _EponTrapObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1)
)
_EponAlarmObjGroup_ObjectIdentity = ObjectIdentity
eponAlarmObjGroup = _EponAlarmObjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2)
)
_EponManagementObjGroup_ObjectIdentity = ObjectIdentity
eponManagementObjGroup = _EponManagementObjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3)
)
_EponTree_ObjectIdentity = ObjectIdentity
eponTree = _EponTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3)
)
_SystemObjects_ObjectIdentity = ObjectIdentity
systemObjects = _SystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1)
)
_SniObjects_ObjectIdentity = ObjectIdentity
sniObjects = _SniObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2)
)
_PonPortObjects_ObjectIdentity = ObjectIdentity
ponPortObjects = _PonPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3)
)
_OnuObjects_ObjectIdentity = ObjectIdentity
onuObjects = _OnuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4)
)
_UniObjects_ObjectIdentity = ObjectIdentity
uniObjects = _UniObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5)
)
_IgmpManagementObjects_ObjectIdentity = ObjectIdentity
igmpManagementObjects = _IgmpManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6)
)
_VlanManagementObjects_ObjectIdentity = ObjectIdentity
vlanManagementObjects = _VlanManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7)
)
_QosManagementObjects_ObjectIdentity = ObjectIdentity
qosManagementObjects = _QosManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8)
)
_StpManagementObjects_ObjectIdentity = ObjectIdentity
stpManagementObjects = _StpManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9)
)
_PerformanceStatisticObjects_ObjectIdentity = ObjectIdentity
performanceStatisticObjects = _PerformanceStatisticObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10)
)
_EponLinkedEoCManagementObjects_ObjectIdentity = ObjectIdentity
eponLinkedEoCManagementObjects = _EponLinkedEoCManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11)
)
_EoCTree_ObjectIdentity = ObjectIdentity
eoCTree = _EoCTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    **{"EponDeviceIndex": EponDeviceIndex,
       "EponCardIndex": EponCardIndex,
       "EponPortIndex": EponPortIndex,
       "EponAlarmCode": EponAlarmCode,
       "EponAlarmInstance": EponAlarmInstance,
       "EponSeverityType": EponSeverityType,
       "AutoNegotiationTechAbility": AutoNegotiationTechAbility,
       "TAddress": TAddress,
       "EponStats15MinRecordType": EponStats15MinRecordType,
       "EponStats24HourRecordType": EponStats24HourRecordType,
       "EponStatsThresholdType": EponStatsThresholdType,
       "nscrtvRoot": nscrtvRoot,
       "nscrtvHFCemsTree": nscrtvHFCemsTree,
       "nscrtvEponEocTree": nscrtvEponEocTree,
       "propertyIdent": propertyIdent,
       "alarmsIdent": alarmsIdent,
       "eponAlarmTree": eponAlarmTree,
       "eponTrapObjectGroup": eponTrapObjectGroup,
       "eponAlarmObjGroup": eponAlarmObjGroup,
       "eponManagementObjGroup": eponManagementObjGroup,
       "eponTree": eponTree,
       "systemObjects": systemObjects,
       "sniObjects": sniObjects,
       "ponPortObjects": ponPortObjects,
       "onuObjects": onuObjects,
       "uniObjects": uniObjects,
       "igmpManagementObjects": igmpManagementObjects,
       "vlanManagementObjects": vlanManagementObjects,
       "qosManagementObjects": qosManagementObjects,
       "stpManagementObjects": stpManagementObjects,
       "performanceStatisticObjects": performanceStatisticObjects,
       "eponLinkedEoCManagementObjects": eponLinkedEoCManagementObjects,
       "eoCTree": eoCTree}
)
