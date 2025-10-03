# SNMP MIB module (CORERO-CMS-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\corero\CORERO-CMS-STATISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:33 2025
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

(coreroCMSMIBCompliances,
 coreroCMSMIBGroups,
 coreroCMSMIBObjects) = mibBuilder.importSymbols(
    "CORERO-CMS-MIB",
    "coreroCMSMIBCompliances",
    "coreroCMSMIBGroups",
    "coreroCMSMIBObjects")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

statistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5)
)
if mibBuilder.loadTexts:
    statistics.setRevisions(
        ("2017-10-12 00:00",
         "2018-02-02 00:00",
         "2018-03-28 00:00",
         "2018-05-28 00:00",
         "2018-06-29 00:00",
         "2019-04-29 00:00",
         "2019-06-24 00:00",
         "2019-12-11 00:00",
         "2020-02-26 00:00",
         "2020-06-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class GroupType(TextualConvention, Integer32):
    status = "current"
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
        *(("all", 0),
          ("cluster", 1),
          ("device", 2),
          ("segment", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AdvancedStatisticsTable_Object = MibTable
advancedStatisticsTable = _AdvancedStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    advancedStatisticsTable.setStatus("current")
_AdvancedStatisticsEntry_Object = MibTableRow
advancedStatisticsEntry = _AdvancedStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1)
)
advancedStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "advancedStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "advancedStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    advancedStatisticsEntry.setStatus("current")
_AdvancedStatisticsGroup_Type = GroupType
_AdvancedStatisticsGroup_Object = MibTableColumn
advancedStatisticsGroup = _AdvancedStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 1),
    _AdvancedStatisticsGroup_Type()
)
advancedStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    advancedStatisticsGroup.setStatus("current")


class _AdvancedStatisticsGroupIndex_Type(Integer32):
    """Custom type advancedStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdvancedStatisticsGroupIndex_Type.__name__ = "Integer32"
_AdvancedStatisticsGroupIndex_Object = MibTableColumn
advancedStatisticsGroupIndex = _AdvancedStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 2),
    _AdvancedStatisticsGroupIndex_Type()
)
advancedStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    advancedStatisticsGroupIndex.setStatus("current")
_AdvancedStatisticsStartTrustedAddresses_Type = Counter64
_AdvancedStatisticsStartTrustedAddresses_Object = MibTableColumn
advancedStatisticsStartTrustedAddresses = _AdvancedStatisticsStartTrustedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 3),
    _AdvancedStatisticsStartTrustedAddresses_Type()
)
advancedStatisticsStartTrustedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsStartTrustedAddresses.setStatus("current")
_AdvancedStatisticsStartUnclassifiedAddresses_Type = Counter64
_AdvancedStatisticsStartUnclassifiedAddresses_Object = MibTableColumn
advancedStatisticsStartUnclassifiedAddresses = _AdvancedStatisticsStartUnclassifiedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 4),
    _AdvancedStatisticsStartUnclassifiedAddresses_Type()
)
advancedStatisticsStartUnclassifiedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsStartUnclassifiedAddresses.setStatus("current")
_AdvancedStatisticsFinishTrustedAddresses_Type = Counter64
_AdvancedStatisticsFinishTrustedAddresses_Object = MibTableColumn
advancedStatisticsFinishTrustedAddresses = _AdvancedStatisticsFinishTrustedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 5),
    _AdvancedStatisticsFinishTrustedAddresses_Type()
)
advancedStatisticsFinishTrustedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFinishTrustedAddresses.setStatus("current")
_AdvancedStatisticsFinishUnclassifiedAddresses_Type = Counter64
_AdvancedStatisticsFinishUnclassifiedAddresses_Object = MibTableColumn
advancedStatisticsFinishUnclassifiedAddresses = _AdvancedStatisticsFinishUnclassifiedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 6),
    _AdvancedStatisticsFinishUnclassifiedAddresses_Type()
)
advancedStatisticsFinishUnclassifiedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFinishUnclassifiedAddresses.setStatus("current")
_AdvancedStatisticsTotalAddressAdds_Type = Counter64
_AdvancedStatisticsTotalAddressAdds_Object = MibTableColumn
advancedStatisticsTotalAddressAdds = _AdvancedStatisticsTotalAddressAdds_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 7),
    _AdvancedStatisticsTotalAddressAdds_Type()
)
advancedStatisticsTotalAddressAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsTotalAddressAdds.setStatus("current")
_AdvancedStatisticsInputOverloadPackets_Type = Counter64
_AdvancedStatisticsInputOverloadPackets_Object = MibTableColumn
advancedStatisticsInputOverloadPackets = _AdvancedStatisticsInputOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 8),
    _AdvancedStatisticsInputOverloadPackets_Type()
)
advancedStatisticsInputOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsInputOverloadPackets.setStatus("current")
_AdvancedStatisticsInputOverloadPacketRate_Type = Counter32
_AdvancedStatisticsInputOverloadPacketRate_Object = MibTableColumn
advancedStatisticsInputOverloadPacketRate = _AdvancedStatisticsInputOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 9),
    _AdvancedStatisticsInputOverloadPacketRate_Type()
)
advancedStatisticsInputOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsInputOverloadPacketRate.setStatus("current")
_AdvancedStatisticsSetupOverloadPackets_Type = Counter64
_AdvancedStatisticsSetupOverloadPackets_Object = MibTableColumn
advancedStatisticsSetupOverloadPackets = _AdvancedStatisticsSetupOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 10),
    _AdvancedStatisticsSetupOverloadPackets_Type()
)
advancedStatisticsSetupOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsSetupOverloadPackets.setStatus("current")
_AdvancedStatisticsSetupOverloadPacketRate_Type = Counter32
_AdvancedStatisticsSetupOverloadPacketRate_Object = MibTableColumn
advancedStatisticsSetupOverloadPacketRate = _AdvancedStatisticsSetupOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 11),
    _AdvancedStatisticsSetupOverloadPacketRate_Type()
)
advancedStatisticsSetupOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsSetupOverloadPacketRate.setStatus("current")
_AdvancedStatisticsContextOverloadPackets_Type = Counter64
_AdvancedStatisticsContextOverloadPackets_Object = MibTableColumn
advancedStatisticsContextOverloadPackets = _AdvancedStatisticsContextOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 12),
    _AdvancedStatisticsContextOverloadPackets_Type()
)
advancedStatisticsContextOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsContextOverloadPackets.setStatus("current")
_AdvancedStatisticsContextOverloadPacketRate_Type = Counter32
_AdvancedStatisticsContextOverloadPacketRate_Object = MibTableColumn
advancedStatisticsContextOverloadPacketRate = _AdvancedStatisticsContextOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 13),
    _AdvancedStatisticsContextOverloadPacketRate_Type()
)
advancedStatisticsContextOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsContextOverloadPacketRate.setStatus("current")
_AdvancedStatisticsEgressDropPackets_Type = Counter64
_AdvancedStatisticsEgressDropPackets_Object = MibTableColumn
advancedStatisticsEgressDropPackets = _AdvancedStatisticsEgressDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 14),
    _AdvancedStatisticsEgressDropPackets_Type()
)
advancedStatisticsEgressDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsEgressDropPackets.setStatus("current")
_AdvancedStatisticsEgressDropPacketRate_Type = Counter32
_AdvancedStatisticsEgressDropPacketRate_Object = MibTableColumn
advancedStatisticsEgressDropPacketRate = _AdvancedStatisticsEgressDropPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 15),
    _AdvancedStatisticsEgressDropPacketRate_Type()
)
advancedStatisticsEgressDropPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsEgressDropPacketRate.setStatus("current")
_AdvancedStatisticsIngressDropPackets_Type = Counter64
_AdvancedStatisticsIngressDropPackets_Object = MibTableColumn
advancedStatisticsIngressDropPackets = _AdvancedStatisticsIngressDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 16),
    _AdvancedStatisticsIngressDropPackets_Type()
)
advancedStatisticsIngressDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIngressDropPackets.setStatus("current")
_AdvancedStatisticsIngressDropPacketRate_Type = Counter32
_AdvancedStatisticsIngressDropPacketRate_Object = MibTableColumn
advancedStatisticsIngressDropPacketRate = _AdvancedStatisticsIngressDropPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 17),
    _AdvancedStatisticsIngressDropPacketRate_Type()
)
advancedStatisticsIngressDropPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIngressDropPacketRate.setStatus("current")
_AdvancedStatisticsEgressOverloadPackets_Type = Counter64
_AdvancedStatisticsEgressOverloadPackets_Object = MibTableColumn
advancedStatisticsEgressOverloadPackets = _AdvancedStatisticsEgressOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 18),
    _AdvancedStatisticsEgressOverloadPackets_Type()
)
advancedStatisticsEgressOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsEgressOverloadPackets.setStatus("current")
_AdvancedStatisticsEgressOverloadPacketRate_Type = Counter32
_AdvancedStatisticsEgressOverloadPacketRate_Object = MibTableColumn
advancedStatisticsEgressOverloadPacketRate = _AdvancedStatisticsEgressOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 19),
    _AdvancedStatisticsEgressOverloadPacketRate_Type()
)
advancedStatisticsEgressOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsEgressOverloadPacketRate.setStatus("current")
_AdvancedStatisticsFlowOverloadPackets_Type = Counter64
_AdvancedStatisticsFlowOverloadPackets_Object = MibTableColumn
advancedStatisticsFlowOverloadPackets = _AdvancedStatisticsFlowOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 20),
    _AdvancedStatisticsFlowOverloadPackets_Type()
)
advancedStatisticsFlowOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFlowOverloadPackets.setStatus("current")
_AdvancedStatisticsFlowOverloadPacketRate_Type = Counter32
_AdvancedStatisticsFlowOverloadPacketRate_Object = MibTableColumn
advancedStatisticsFlowOverloadPacketRate = _AdvancedStatisticsFlowOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 21),
    _AdvancedStatisticsFlowOverloadPacketRate_Type()
)
advancedStatisticsFlowOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFlowOverloadPacketRate.setStatus("current")
_AdvancedStatisticsSmartRuleOverloadPackets_Type = Counter64
_AdvancedStatisticsSmartRuleOverloadPackets_Object = MibTableColumn
advancedStatisticsSmartRuleOverloadPackets = _AdvancedStatisticsSmartRuleOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 22),
    _AdvancedStatisticsSmartRuleOverloadPackets_Type()
)
advancedStatisticsSmartRuleOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsSmartRuleOverloadPackets.setStatus("current")
_AdvancedStatisticsSmartRuleOverloadPacketRate_Type = Counter32
_AdvancedStatisticsSmartRuleOverloadPacketRate_Object = MibTableColumn
advancedStatisticsSmartRuleOverloadPacketRate = _AdvancedStatisticsSmartRuleOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 23),
    _AdvancedStatisticsSmartRuleOverloadPacketRate_Type()
)
advancedStatisticsSmartRuleOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsSmartRuleOverloadPacketRate.setStatus("current")
_AdvancedStatisticsSourceSmartRuleOverloadPackets_Type = Counter64
_AdvancedStatisticsSourceSmartRuleOverloadPackets_Object = MibTableColumn
advancedStatisticsSourceSmartRuleOverloadPackets = _AdvancedStatisticsSourceSmartRuleOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 24),
    _AdvancedStatisticsSourceSmartRuleOverloadPackets_Type()
)
advancedStatisticsSourceSmartRuleOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsSourceSmartRuleOverloadPackets.setStatus("current")
_AdvancedStatisticsSourceSmartRuleOverloadPacketRate_Type = Counter32
_AdvancedStatisticsSourceSmartRuleOverloadPacketRate_Object = MibTableColumn
advancedStatisticsSourceSmartRuleOverloadPacketRate = _AdvancedStatisticsSourceSmartRuleOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 25),
    _AdvancedStatisticsSourceSmartRuleOverloadPacketRate_Type()
)
advancedStatisticsSourceSmartRuleOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsSourceSmartRuleOverloadPacketRate.setStatus("current")
_AdvancedStatisticsFragmentOverloadPackets_Type = Counter64
_AdvancedStatisticsFragmentOverloadPackets_Object = MibTableColumn
advancedStatisticsFragmentOverloadPackets = _AdvancedStatisticsFragmentOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 26),
    _AdvancedStatisticsFragmentOverloadPackets_Type()
)
advancedStatisticsFragmentOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFragmentOverloadPackets.setStatus("current")
_AdvancedStatisticsFragmentOverloadPacketRate_Type = Counter32
_AdvancedStatisticsFragmentOverloadPacketRate_Object = MibTableColumn
advancedStatisticsFragmentOverloadPacketRate = _AdvancedStatisticsFragmentOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 27),
    _AdvancedStatisticsFragmentOverloadPacketRate_Type()
)
advancedStatisticsFragmentOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFragmentOverloadPacketRate.setStatus("current")
_AdvancedStatisticsIpOverloadPackets_Type = Counter64
_AdvancedStatisticsIpOverloadPackets_Object = MibTableColumn
advancedStatisticsIpOverloadPackets = _AdvancedStatisticsIpOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 28),
    _AdvancedStatisticsIpOverloadPackets_Type()
)
advancedStatisticsIpOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIpOverloadPackets.setStatus("current")
_AdvancedStatisticsIpOverloadPacketRate_Type = Counter32
_AdvancedStatisticsIpOverloadPacketRate_Object = MibTableColumn
advancedStatisticsIpOverloadPacketRate = _AdvancedStatisticsIpOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 29),
    _AdvancedStatisticsIpOverloadPacketRate_Type()
)
advancedStatisticsIpOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIpOverloadPacketRate.setStatus("current")
_AdvancedStatisticsFlexRuleOverloadPackets_Type = Counter64
_AdvancedStatisticsFlexRuleOverloadPackets_Object = MibTableColumn
advancedStatisticsFlexRuleOverloadPackets = _AdvancedStatisticsFlexRuleOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 30),
    _AdvancedStatisticsFlexRuleOverloadPackets_Type()
)
advancedStatisticsFlexRuleOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFlexRuleOverloadPackets.setStatus("current")
_AdvancedStatisticsFlexRuleOverloadPacketRate_Type = Counter32
_AdvancedStatisticsFlexRuleOverloadPacketRate_Object = MibTableColumn
advancedStatisticsFlexRuleOverloadPacketRate = _AdvancedStatisticsFlexRuleOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 31),
    _AdvancedStatisticsFlexRuleOverloadPacketRate_Type()
)
advancedStatisticsFlexRuleOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsFlexRuleOverloadPacketRate.setStatus("current")
_AdvancedStatisticsIngressOverloadPackets_Type = Counter64
_AdvancedStatisticsIngressOverloadPackets_Object = MibTableColumn
advancedStatisticsIngressOverloadPackets = _AdvancedStatisticsIngressOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 32),
    _AdvancedStatisticsIngressOverloadPackets_Type()
)
advancedStatisticsIngressOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIngressOverloadPackets.setStatus("current")
_AdvancedStatisticsIngressOverloadPacketRate_Type = Counter32
_AdvancedStatisticsIngressOverloadPacketRate_Object = MibTableColumn
advancedStatisticsIngressOverloadPacketRate = _AdvancedStatisticsIngressOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 33),
    _AdvancedStatisticsIngressOverloadPacketRate_Type()
)
advancedStatisticsIngressOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIngressOverloadPacketRate.setStatus("current")
_AdvancedStatisticsIngressOverloadBytes_Type = Counter64
_AdvancedStatisticsIngressOverloadBytes_Object = MibTableColumn
advancedStatisticsIngressOverloadBytes = _AdvancedStatisticsIngressOverloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 34),
    _AdvancedStatisticsIngressOverloadBytes_Type()
)
advancedStatisticsIngressOverloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIngressOverloadBytes.setStatus("current")
_AdvancedStatisticsIngressOverloadBitRate_Type = Counter32
_AdvancedStatisticsIngressOverloadBitRate_Object = MibTableColumn
advancedStatisticsIngressOverloadBitRate = _AdvancedStatisticsIngressOverloadBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 35),
    _AdvancedStatisticsIngressOverloadBitRate_Type()
)
advancedStatisticsIngressOverloadBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsIngressOverloadBitRate.setStatus("current")
_AdvancedStatisticsStartTrackingFlow_Type = Counter64
_AdvancedStatisticsStartTrackingFlow_Object = MibTableColumn
advancedStatisticsStartTrackingFlow = _AdvancedStatisticsStartTrackingFlow_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 36),
    _AdvancedStatisticsStartTrackingFlow_Type()
)
advancedStatisticsStartTrackingFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsStartTrackingFlow.setStatus("current")
_AdvancedStatisticsStopTrackingFlow_Type = Counter64
_AdvancedStatisticsStopTrackingFlow_Object = MibTableColumn
advancedStatisticsStopTrackingFlow = _AdvancedStatisticsStopTrackingFlow_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 37),
    _AdvancedStatisticsStopTrackingFlow_Type()
)
advancedStatisticsStopTrackingFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsStopTrackingFlow.setStatus("current")
_AdvancedStatisticsDDoSScorecardOverloadPackets_Type = Counter64
_AdvancedStatisticsDDoSScorecardOverloadPackets_Object = MibTableColumn
advancedStatisticsDDoSScorecardOverloadPackets = _AdvancedStatisticsDDoSScorecardOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 38),
    _AdvancedStatisticsDDoSScorecardOverloadPackets_Type()
)
advancedStatisticsDDoSScorecardOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsDDoSScorecardOverloadPackets.setStatus("current")
_AdvancedStatisticsDDoSScorecardOverloadPacketRate_Type = Counter32
_AdvancedStatisticsDDoSScorecardOverloadPacketRate_Object = MibTableColumn
advancedStatisticsDDoSScorecardOverloadPacketRate = _AdvancedStatisticsDDoSScorecardOverloadPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 1, 1, 39),
    _AdvancedStatisticsDDoSScorecardOverloadPacketRate_Type()
)
advancedStatisticsDDoSScorecardOverloadPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedStatisticsDDoSScorecardOverloadPacketRate.setStatus("current")
_BlockRateStatisticsTable_Object = MibTable
blockRateStatisticsTable = _BlockRateStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2)
)
if mibBuilder.loadTexts:
    blockRateStatisticsTable.setStatus("current")
_BlockRateStatisticsEntry_Object = MibTableRow
blockRateStatisticsEntry = _BlockRateStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1)
)
blockRateStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    blockRateStatisticsEntry.setStatus("current")
_BlockRateStatisticsGroup_Type = GroupType
_BlockRateStatisticsGroup_Object = MibTableColumn
blockRateStatisticsGroup = _BlockRateStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 1),
    _BlockRateStatisticsGroup_Type()
)
blockRateStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockRateStatisticsGroup.setStatus("current")


class _BlockRateStatisticsGroupIndex_Type(Integer32):
    """Custom type blockRateStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BlockRateStatisticsGroupIndex_Type.__name__ = "Integer32"
_BlockRateStatisticsGroupIndex_Object = MibTableColumn
blockRateStatisticsGroupIndex = _BlockRateStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 2),
    _BlockRateStatisticsGroupIndex_Type()
)
blockRateStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockRateStatisticsGroupIndex.setStatus("current")
_BlockRateStatisticsAllRulesBlockPackets_Type = Counter64
_BlockRateStatisticsAllRulesBlockPackets_Object = MibTableColumn
blockRateStatisticsAllRulesBlockPackets = _BlockRateStatisticsAllRulesBlockPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 3),
    _BlockRateStatisticsAllRulesBlockPackets_Type()
)
blockRateStatisticsAllRulesBlockPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockRateStatisticsAllRulesBlockPackets.setStatus("current")
_BlockRateStatisticsAllRulesBlockPacketRate_Type = Counter32
_BlockRateStatisticsAllRulesBlockPacketRate_Object = MibTableColumn
blockRateStatisticsAllRulesBlockPacketRate = _BlockRateStatisticsAllRulesBlockPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 4),
    _BlockRateStatisticsAllRulesBlockPacketRate_Type()
)
blockRateStatisticsAllRulesBlockPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockRateStatisticsAllRulesBlockPacketRate.setStatus("current")
_BlockRateStatisticsAllRulesBlockBytes_Type = Counter64
_BlockRateStatisticsAllRulesBlockBytes_Object = MibTableColumn
blockRateStatisticsAllRulesBlockBytes = _BlockRateStatisticsAllRulesBlockBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 5),
    _BlockRateStatisticsAllRulesBlockBytes_Type()
)
blockRateStatisticsAllRulesBlockBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockRateStatisticsAllRulesBlockBytes.setStatus("current")
_BlockRateStatisticsAllRulesBlockBitRate_Type = Counter32
_BlockRateStatisticsAllRulesBlockBitRate_Object = MibTableColumn
blockRateStatisticsAllRulesBlockBitRate = _BlockRateStatisticsAllRulesBlockBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 6),
    _BlockRateStatisticsAllRulesBlockBitRate_Type()
)
blockRateStatisticsAllRulesBlockBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockRateStatisticsAllRulesBlockBitRate.setStatus("current")
_BlockRateStatisticsAllRulesBlockFrameBytes_Type = Counter64
_BlockRateStatisticsAllRulesBlockFrameBytes_Object = MibTableColumn
blockRateStatisticsAllRulesBlockFrameBytes = _BlockRateStatisticsAllRulesBlockFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 7),
    _BlockRateStatisticsAllRulesBlockFrameBytes_Type()
)
blockRateStatisticsAllRulesBlockFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockRateStatisticsAllRulesBlockFrameBytes.setStatus("current")
_BlockRateStatisticsAllRulesBlockFrameBitRate_Type = Counter32
_BlockRateStatisticsAllRulesBlockFrameBitRate_Object = MibTableColumn
blockRateStatisticsAllRulesBlockFrameBitRate = _BlockRateStatisticsAllRulesBlockFrameBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 2, 1, 8),
    _BlockRateStatisticsAllRulesBlockFrameBitRate_Type()
)
blockRateStatisticsAllRulesBlockFrameBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockRateStatisticsAllRulesBlockFrameBitRate.setStatus("current")
_InterfaceStatisticsTable_Object = MibTable
interfaceStatisticsTable = _InterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3)
)
if mibBuilder.loadTexts:
    interfaceStatisticsTable.setStatus("current")
_InterfaceStatisticsEntry_Object = MibTableRow
interfaceStatisticsEntry = _InterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1)
)
interfaceStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    interfaceStatisticsEntry.setStatus("current")
_InterfaceStatisticsGroup_Type = GroupType
_InterfaceStatisticsGroup_Object = MibTableColumn
interfaceStatisticsGroup = _InterfaceStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 1),
    _InterfaceStatisticsGroup_Type()
)
interfaceStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceStatisticsGroup.setStatus("current")


class _InterfaceStatisticsGroupIndex_Type(Integer32):
    """Custom type interfaceStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InterfaceStatisticsGroupIndex_Type.__name__ = "Integer32"
_InterfaceStatisticsGroupIndex_Object = MibTableColumn
interfaceStatisticsGroupIndex = _InterfaceStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 2),
    _InterfaceStatisticsGroupIndex_Type()
)
interfaceStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceStatisticsGroupIndex.setStatus("current")
_InterfaceStatisticsExternalPortBitReceiveRate_Type = Counter32
_InterfaceStatisticsExternalPortBitReceiveRate_Object = MibTableColumn
interfaceStatisticsExternalPortBitReceiveRate = _InterfaceStatisticsExternalPortBitReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 3),
    _InterfaceStatisticsExternalPortBitReceiveRate_Type()
)
interfaceStatisticsExternalPortBitReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortBitReceiveRate.setStatus("current")
_InterfaceStatisticsExternalPortBitTransmitRate_Type = Counter32
_InterfaceStatisticsExternalPortBitTransmitRate_Object = MibTableColumn
interfaceStatisticsExternalPortBitTransmitRate = _InterfaceStatisticsExternalPortBitTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 4),
    _InterfaceStatisticsExternalPortBitTransmitRate_Type()
)
interfaceStatisticsExternalPortBitTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortBitTransmitRate.setStatus("current")
_InterfaceStatisticsExternalPortEgressDroppedPackets_Type = Counter64
_InterfaceStatisticsExternalPortEgressDroppedPackets_Object = MibTableColumn
interfaceStatisticsExternalPortEgressDroppedPackets = _InterfaceStatisticsExternalPortEgressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 5),
    _InterfaceStatisticsExternalPortEgressDroppedPackets_Type()
)
interfaceStatisticsExternalPortEgressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortEgressDroppedPackets.setStatus("current")
_InterfaceStatisticsExternalPortIngressDroppedPackets_Type = Counter64
_InterfaceStatisticsExternalPortIngressDroppedPackets_Object = MibTableColumn
interfaceStatisticsExternalPortIngressDroppedPackets = _InterfaceStatisticsExternalPortIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 6),
    _InterfaceStatisticsExternalPortIngressDroppedPackets_Type()
)
interfaceStatisticsExternalPortIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortIngressDroppedPackets.setStatus("current")
_InterfaceStatisticsExternalPortPacketReceiveRate_Type = Counter32
_InterfaceStatisticsExternalPortPacketReceiveRate_Object = MibTableColumn
interfaceStatisticsExternalPortPacketReceiveRate = _InterfaceStatisticsExternalPortPacketReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 7),
    _InterfaceStatisticsExternalPortPacketReceiveRate_Type()
)
interfaceStatisticsExternalPortPacketReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortPacketReceiveRate.setStatus("current")
_InterfaceStatisticsExternalPortPacketTransmitRate_Type = Counter32
_InterfaceStatisticsExternalPortPacketTransmitRate_Object = MibTableColumn
interfaceStatisticsExternalPortPacketTransmitRate = _InterfaceStatisticsExternalPortPacketTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 8),
    _InterfaceStatisticsExternalPortPacketTransmitRate_Type()
)
interfaceStatisticsExternalPortPacketTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortPacketTransmitRate.setStatus("current")
_InterfaceStatisticsExternalPortReceivedBadCrcPackets_Type = Counter64
_InterfaceStatisticsExternalPortReceivedBadCrcPackets_Object = MibTableColumn
interfaceStatisticsExternalPortReceivedBadCrcPackets = _InterfaceStatisticsExternalPortReceivedBadCrcPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 9),
    _InterfaceStatisticsExternalPortReceivedBadCrcPackets_Type()
)
interfaceStatisticsExternalPortReceivedBadCrcPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortReceivedBadCrcPackets.setStatus("current")
_InterfaceStatisticsExternalPortReceivedBytes_Type = Counter64
_InterfaceStatisticsExternalPortReceivedBytes_Object = MibTableColumn
interfaceStatisticsExternalPortReceivedBytes = _InterfaceStatisticsExternalPortReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 10),
    _InterfaceStatisticsExternalPortReceivedBytes_Type()
)
interfaceStatisticsExternalPortReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortReceivedBytes.setStatus("current")
_InterfaceStatisticsExternalPortReceivedJabberPackets_Type = Counter64
_InterfaceStatisticsExternalPortReceivedJabberPackets_Object = MibTableColumn
interfaceStatisticsExternalPortReceivedJabberPackets = _InterfaceStatisticsExternalPortReceivedJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 11),
    _InterfaceStatisticsExternalPortReceivedJabberPackets_Type()
)
interfaceStatisticsExternalPortReceivedJabberPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortReceivedJabberPackets.setStatus("current")
_InterfaceStatisticsExternalPortReceivedOversizedPackets_Type = Counter64
_InterfaceStatisticsExternalPortReceivedOversizedPackets_Object = MibTableColumn
interfaceStatisticsExternalPortReceivedOversizedPackets = _InterfaceStatisticsExternalPortReceivedOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 12),
    _InterfaceStatisticsExternalPortReceivedOversizedPackets_Type()
)
interfaceStatisticsExternalPortReceivedOversizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortReceivedOversizedPackets.setStatus("current")
_InterfaceStatisticsExternalPortReceivedPackets_Type = Counter64
_InterfaceStatisticsExternalPortReceivedPackets_Object = MibTableColumn
interfaceStatisticsExternalPortReceivedPackets = _InterfaceStatisticsExternalPortReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 13),
    _InterfaceStatisticsExternalPortReceivedPackets_Type()
)
interfaceStatisticsExternalPortReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortReceivedPackets.setStatus("current")
_InterfaceStatisticsExternalPortTransmitErrorPackets_Type = Counter64
_InterfaceStatisticsExternalPortTransmitErrorPackets_Object = MibTableColumn
interfaceStatisticsExternalPortTransmitErrorPackets = _InterfaceStatisticsExternalPortTransmitErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 14),
    _InterfaceStatisticsExternalPortTransmitErrorPackets_Type()
)
interfaceStatisticsExternalPortTransmitErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortTransmitErrorPackets.setStatus("current")
_InterfaceStatisticsExternalPortTransmittedBytes_Type = Counter64
_InterfaceStatisticsExternalPortTransmittedBytes_Object = MibTableColumn
interfaceStatisticsExternalPortTransmittedBytes = _InterfaceStatisticsExternalPortTransmittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 15),
    _InterfaceStatisticsExternalPortTransmittedBytes_Type()
)
interfaceStatisticsExternalPortTransmittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortTransmittedBytes.setStatus("current")
_InterfaceStatisticsExternalPortTransmittedPackets_Type = Counter64
_InterfaceStatisticsExternalPortTransmittedPackets_Object = MibTableColumn
interfaceStatisticsExternalPortTransmittedPackets = _InterfaceStatisticsExternalPortTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 16),
    _InterfaceStatisticsExternalPortTransmittedPackets_Type()
)
interfaceStatisticsExternalPortTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortTransmittedPackets.setStatus("current")
_InterfaceStatisticsInternalPortBitReceiveRate_Type = Counter32
_InterfaceStatisticsInternalPortBitReceiveRate_Object = MibTableColumn
interfaceStatisticsInternalPortBitReceiveRate = _InterfaceStatisticsInternalPortBitReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 17),
    _InterfaceStatisticsInternalPortBitReceiveRate_Type()
)
interfaceStatisticsInternalPortBitReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortBitReceiveRate.setStatus("current")
_InterfaceStatisticsInternalPortBitTransmitRate_Type = Counter32
_InterfaceStatisticsInternalPortBitTransmitRate_Object = MibTableColumn
interfaceStatisticsInternalPortBitTransmitRate = _InterfaceStatisticsInternalPortBitTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 18),
    _InterfaceStatisticsInternalPortBitTransmitRate_Type()
)
interfaceStatisticsInternalPortBitTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortBitTransmitRate.setStatus("current")
_InterfaceStatisticsInternalPortEgressDroppedPackets_Type = Counter64
_InterfaceStatisticsInternalPortEgressDroppedPackets_Object = MibTableColumn
interfaceStatisticsInternalPortEgressDroppedPackets = _InterfaceStatisticsInternalPortEgressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 19),
    _InterfaceStatisticsInternalPortEgressDroppedPackets_Type()
)
interfaceStatisticsInternalPortEgressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortEgressDroppedPackets.setStatus("current")
_InterfaceStatisticsInternalPortIngressDroppedPackets_Type = Counter64
_InterfaceStatisticsInternalPortIngressDroppedPackets_Object = MibTableColumn
interfaceStatisticsInternalPortIngressDroppedPackets = _InterfaceStatisticsInternalPortIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 20),
    _InterfaceStatisticsInternalPortIngressDroppedPackets_Type()
)
interfaceStatisticsInternalPortIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortIngressDroppedPackets.setStatus("current")
_InterfaceStatisticsInternalPortPacketReceiveRate_Type = Counter32
_InterfaceStatisticsInternalPortPacketReceiveRate_Object = MibTableColumn
interfaceStatisticsInternalPortPacketReceiveRate = _InterfaceStatisticsInternalPortPacketReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 21),
    _InterfaceStatisticsInternalPortPacketReceiveRate_Type()
)
interfaceStatisticsInternalPortPacketReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortPacketReceiveRate.setStatus("current")
_InterfaceStatisticsInternalPortPacketTransmitRate_Type = Counter32
_InterfaceStatisticsInternalPortPacketTransmitRate_Object = MibTableColumn
interfaceStatisticsInternalPortPacketTransmitRate = _InterfaceStatisticsInternalPortPacketTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 22),
    _InterfaceStatisticsInternalPortPacketTransmitRate_Type()
)
interfaceStatisticsInternalPortPacketTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortPacketTransmitRate.setStatus("current")
_InterfaceStatisticsInternalPortReceivedBadCrcPackets_Type = Counter64
_InterfaceStatisticsInternalPortReceivedBadCrcPackets_Object = MibTableColumn
interfaceStatisticsInternalPortReceivedBadCrcPackets = _InterfaceStatisticsInternalPortReceivedBadCrcPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 23),
    _InterfaceStatisticsInternalPortReceivedBadCrcPackets_Type()
)
interfaceStatisticsInternalPortReceivedBadCrcPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortReceivedBadCrcPackets.setStatus("current")
_InterfaceStatisticsInternalPortReceivedBytes_Type = Counter64
_InterfaceStatisticsInternalPortReceivedBytes_Object = MibTableColumn
interfaceStatisticsInternalPortReceivedBytes = _InterfaceStatisticsInternalPortReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 24),
    _InterfaceStatisticsInternalPortReceivedBytes_Type()
)
interfaceStatisticsInternalPortReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortReceivedBytes.setStatus("current")
_InterfaceStatisticsInternalPortReceivedJabberPackets_Type = Counter64
_InterfaceStatisticsInternalPortReceivedJabberPackets_Object = MibTableColumn
interfaceStatisticsInternalPortReceivedJabberPackets = _InterfaceStatisticsInternalPortReceivedJabberPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 25),
    _InterfaceStatisticsInternalPortReceivedJabberPackets_Type()
)
interfaceStatisticsInternalPortReceivedJabberPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortReceivedJabberPackets.setStatus("current")
_InterfaceStatisticsInternalPortReceivedOversizedPackets_Type = Counter64
_InterfaceStatisticsInternalPortReceivedOversizedPackets_Object = MibTableColumn
interfaceStatisticsInternalPortReceivedOversizedPackets = _InterfaceStatisticsInternalPortReceivedOversizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 26),
    _InterfaceStatisticsInternalPortReceivedOversizedPackets_Type()
)
interfaceStatisticsInternalPortReceivedOversizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortReceivedOversizedPackets.setStatus("current")
_InterfaceStatisticsInternalPortReceivedPackets_Type = Counter64
_InterfaceStatisticsInternalPortReceivedPackets_Object = MibTableColumn
interfaceStatisticsInternalPortReceivedPackets = _InterfaceStatisticsInternalPortReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 27),
    _InterfaceStatisticsInternalPortReceivedPackets_Type()
)
interfaceStatisticsInternalPortReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortReceivedPackets.setStatus("current")
_InterfaceStatisticsInternalPortTransmitErrorPackets_Type = Counter64
_InterfaceStatisticsInternalPortTransmitErrorPackets_Object = MibTableColumn
interfaceStatisticsInternalPortTransmitErrorPackets = _InterfaceStatisticsInternalPortTransmitErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 28),
    _InterfaceStatisticsInternalPortTransmitErrorPackets_Type()
)
interfaceStatisticsInternalPortTransmitErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortTransmitErrorPackets.setStatus("current")
_InterfaceStatisticsInternalPortTransmittedBytes_Type = Counter64
_InterfaceStatisticsInternalPortTransmittedBytes_Object = MibTableColumn
interfaceStatisticsInternalPortTransmittedBytes = _InterfaceStatisticsInternalPortTransmittedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 29),
    _InterfaceStatisticsInternalPortTransmittedBytes_Type()
)
interfaceStatisticsInternalPortTransmittedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortTransmittedBytes.setStatus("current")
_InterfaceStatisticsInternalPortTransmittedPackets_Type = Counter64
_InterfaceStatisticsInternalPortTransmittedPackets_Object = MibTableColumn
interfaceStatisticsInternalPortTransmittedPackets = _InterfaceStatisticsInternalPortTransmittedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 30),
    _InterfaceStatisticsInternalPortTransmittedPackets_Type()
)
interfaceStatisticsInternalPortTransmittedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortTransmittedPackets.setStatus("current")
_InterfaceStatisticsExternalPortIngressOverloadPackets_Type = Counter64
_InterfaceStatisticsExternalPortIngressOverloadPackets_Object = MibTableColumn
interfaceStatisticsExternalPortIngressOverloadPackets = _InterfaceStatisticsExternalPortIngressOverloadPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 31),
    _InterfaceStatisticsExternalPortIngressOverloadPackets_Type()
)
interfaceStatisticsExternalPortIngressOverloadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortIngressOverloadPackets.setStatus("current")
_InterfaceStatisticsExternalPortIngressOverloadBytes_Type = Counter64
_InterfaceStatisticsExternalPortIngressOverloadBytes_Object = MibTableColumn
interfaceStatisticsExternalPortIngressOverloadBytes = _InterfaceStatisticsExternalPortIngressOverloadBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 32),
    _InterfaceStatisticsExternalPortIngressOverloadBytes_Type()
)
interfaceStatisticsExternalPortIngressOverloadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortIngressOverloadBytes.setStatus("current")
_InterfaceStatisticsExternalPortReceivedFecErrorPackets_Type = Counter64
_InterfaceStatisticsExternalPortReceivedFecErrorPackets_Object = MibTableColumn
interfaceStatisticsExternalPortReceivedFecErrorPackets = _InterfaceStatisticsExternalPortReceivedFecErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 33),
    _InterfaceStatisticsExternalPortReceivedFecErrorPackets_Type()
)
interfaceStatisticsExternalPortReceivedFecErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsExternalPortReceivedFecErrorPackets.setStatus("current")
_InterfaceStatisticsInternalPortReceivedFecErrorPackets_Type = Counter64
_InterfaceStatisticsInternalPortReceivedFecErrorPackets_Object = MibTableColumn
interfaceStatisticsInternalPortReceivedFecErrorPackets = _InterfaceStatisticsInternalPortReceivedFecErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 3, 1, 34),
    _InterfaceStatisticsInternalPortReceivedFecErrorPackets_Type()
)
interfaceStatisticsInternalPortReceivedFecErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceStatisticsInternalPortReceivedFecErrorPackets.setStatus("current")
_IpAddressStatisticsTable_Object = MibTable
ipAddressStatisticsTable = _IpAddressStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ipAddressStatisticsTable.setStatus("current")
_IpAddressStatisticsEntry_Object = MibTableRow
ipAddressStatisticsEntry = _IpAddressStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1)
)
ipAddressStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    ipAddressStatisticsEntry.setStatus("current")
_IpAddressStatisticsGroup_Type = GroupType
_IpAddressStatisticsGroup_Object = MibTableColumn
ipAddressStatisticsGroup = _IpAddressStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 1),
    _IpAddressStatisticsGroup_Type()
)
ipAddressStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressStatisticsGroup.setStatus("current")


class _IpAddressStatisticsGroupIndex_Type(Integer32):
    """Custom type ipAddressStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpAddressStatisticsGroupIndex_Type.__name__ = "Integer32"
_IpAddressStatisticsGroupIndex_Object = MibTableColumn
ipAddressStatisticsGroupIndex = _IpAddressStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 2),
    _IpAddressStatisticsGroupIndex_Type()
)
ipAddressStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipAddressStatisticsGroupIndex.setStatus("current")
_IpAddressStatisticsInUseAddresses_Type = Counter32
_IpAddressStatisticsInUseAddresses_Object = MibTableColumn
ipAddressStatisticsInUseAddresses = _IpAddressStatisticsInUseAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 3),
    _IpAddressStatisticsInUseAddresses_Type()
)
ipAddressStatisticsInUseAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsInUseAddresses.setStatus("current")
_IpAddressStatisticsInUseTrustedAddresses_Type = Counter32
_IpAddressStatisticsInUseTrustedAddresses_Object = MibTableColumn
ipAddressStatisticsInUseTrustedAddresses = _IpAddressStatisticsInUseTrustedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 4),
    _IpAddressStatisticsInUseTrustedAddresses_Type()
)
ipAddressStatisticsInUseTrustedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsInUseTrustedAddresses.setStatus("current")
_IpAddressStatisticsInUseUnclassifiedAddresses_Type = Counter32
_IpAddressStatisticsInUseUnclassifiedAddresses_Object = MibTableColumn
ipAddressStatisticsInUseUnclassifiedAddresses = _IpAddressStatisticsInUseUnclassifiedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 5),
    _IpAddressStatisticsInUseUnclassifiedAddresses_Type()
)
ipAddressStatisticsInUseUnclassifiedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsInUseUnclassifiedAddresses.setStatus("current")
_IpAddressStatisticsPanicGood_Type = Counter64
_IpAddressStatisticsPanicGood_Object = MibTableColumn
ipAddressStatisticsPanicGood = _IpAddressStatisticsPanicGood_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 6),
    _IpAddressStatisticsPanicGood_Type()
)
ipAddressStatisticsPanicGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPanicGood.setStatus("current")
_IpAddressStatisticsPanicGoodRate_Type = Counter32
_IpAddressStatisticsPanicGoodRate_Object = MibTableColumn
ipAddressStatisticsPanicGoodRate = _IpAddressStatisticsPanicGoodRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 7),
    _IpAddressStatisticsPanicGoodRate_Type()
)
ipAddressStatisticsPanicGoodRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPanicGoodRate.setStatus("current")
_IpAddressStatisticsPanicBad_Type = Counter64
_IpAddressStatisticsPanicBad_Object = MibTableColumn
ipAddressStatisticsPanicBad = _IpAddressStatisticsPanicBad_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 8),
    _IpAddressStatisticsPanicBad_Type()
)
ipAddressStatisticsPanicBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPanicBad.setStatus("current")
_IpAddressStatisticsPanicBadRate_Type = Counter32
_IpAddressStatisticsPanicBadRate_Object = MibTableColumn
ipAddressStatisticsPanicBadRate = _IpAddressStatisticsPanicBadRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 9),
    _IpAddressStatisticsPanicBadRate_Type()
)
ipAddressStatisticsPanicBadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPanicBadRate.setStatus("current")
_IpAddressStatisticsPanicTimedOut_Type = Counter64
_IpAddressStatisticsPanicTimedOut_Object = MibTableColumn
ipAddressStatisticsPanicTimedOut = _IpAddressStatisticsPanicTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 10),
    _IpAddressStatisticsPanicTimedOut_Type()
)
ipAddressStatisticsPanicTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPanicTimedOut.setStatus("current")
_IpAddressStatisticsPanicTimedOutRate_Type = Counter32
_IpAddressStatisticsPanicTimedOutRate_Object = MibTableColumn
ipAddressStatisticsPanicTimedOutRate = _IpAddressStatisticsPanicTimedOutRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 11),
    _IpAddressStatisticsPanicTimedOutRate_Type()
)
ipAddressStatisticsPanicTimedOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPanicTimedOutRate.setStatus("current")
_IpAddressStatisticsPromotedToTrusted_Type = Counter64
_IpAddressStatisticsPromotedToTrusted_Object = MibTableColumn
ipAddressStatisticsPromotedToTrusted = _IpAddressStatisticsPromotedToTrusted_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 12),
    _IpAddressStatisticsPromotedToTrusted_Type()
)
ipAddressStatisticsPromotedToTrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPromotedToTrusted.setStatus("current")
_IpAddressStatisticsPromotedToTrustedRate_Type = Counter32
_IpAddressStatisticsPromotedToTrustedRate_Object = MibTableColumn
ipAddressStatisticsPromotedToTrustedRate = _IpAddressStatisticsPromotedToTrustedRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 13),
    _IpAddressStatisticsPromotedToTrustedRate_Type()
)
ipAddressStatisticsPromotedToTrustedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsPromotedToTrustedRate.setStatus("current")
_IpAddressStatisticsTrackedTcpFlows_Type = Counter64
_IpAddressStatisticsTrackedTcpFlows_Object = MibTableColumn
ipAddressStatisticsTrackedTcpFlows = _IpAddressStatisticsTrackedTcpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 14),
    _IpAddressStatisticsTrackedTcpFlows_Type()
)
ipAddressStatisticsTrackedTcpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsTrackedTcpFlows.setStatus("current")
_IpAddressStatisticsTrackedTcpFlowsSuccess_Type = Counter64
_IpAddressStatisticsTrackedTcpFlowsSuccess_Object = MibTableColumn
ipAddressStatisticsTrackedTcpFlowsSuccess = _IpAddressStatisticsTrackedTcpFlowsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 15),
    _IpAddressStatisticsTrackedTcpFlowsSuccess_Type()
)
ipAddressStatisticsTrackedTcpFlowsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsTrackedTcpFlowsSuccess.setStatus("current")
_IpAddressStatisticsTrackedTcpFlowsSuccessRate_Type = Counter32
_IpAddressStatisticsTrackedTcpFlowsSuccessRate_Object = MibTableColumn
ipAddressStatisticsTrackedTcpFlowsSuccessRate = _IpAddressStatisticsTrackedTcpFlowsSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 16),
    _IpAddressStatisticsTrackedTcpFlowsSuccessRate_Type()
)
ipAddressStatisticsTrackedTcpFlowsSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsTrackedTcpFlowsSuccessRate.setStatus("current")
_IpAddressStatisticsTrackedTcpFlowsTimedOut_Type = Counter64
_IpAddressStatisticsTrackedTcpFlowsTimedOut_Object = MibTableColumn
ipAddressStatisticsTrackedTcpFlowsTimedOut = _IpAddressStatisticsTrackedTcpFlowsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 17),
    _IpAddressStatisticsTrackedTcpFlowsTimedOut_Type()
)
ipAddressStatisticsTrackedTcpFlowsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsTrackedTcpFlowsTimedOut.setStatus("current")
_IpAddressStatisticsTrackedTcpFlowsTimedOutRate_Type = Counter32
_IpAddressStatisticsTrackedTcpFlowsTimedOutRate_Object = MibTableColumn
ipAddressStatisticsTrackedTcpFlowsTimedOutRate = _IpAddressStatisticsTrackedTcpFlowsTimedOutRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 4, 1, 18),
    _IpAddressStatisticsTrackedTcpFlowsTimedOutRate_Type()
)
ipAddressStatisticsTrackedTcpFlowsTimedOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressStatisticsTrackedTcpFlowsTimedOutRate.setStatus("current")
_RuleStatisticsTable_Object = MibTable
ruleStatisticsTable = _RuleStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5)
)
if mibBuilder.loadTexts:
    ruleStatisticsTable.setStatus("current")
_RuleStatisticsEntry_Object = MibTableRow
ruleStatisticsEntry = _RuleStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1)
)
ruleStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "ruleStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "ruleStatisticsGroupIndex"),
    (0, "CORERO-CMS-STATISTICS-MIB", "ruleStatisticsRuleIndex"),
)
if mibBuilder.loadTexts:
    ruleStatisticsEntry.setStatus("current")
_RuleStatisticsGroup_Type = GroupType
_RuleStatisticsGroup_Object = MibTableColumn
ruleStatisticsGroup = _RuleStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 1),
    _RuleStatisticsGroup_Type()
)
ruleStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruleStatisticsGroup.setStatus("current")


class _RuleStatisticsGroupIndex_Type(Integer32):
    """Custom type ruleStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuleStatisticsGroupIndex_Type.__name__ = "Integer32"
_RuleStatisticsGroupIndex_Object = MibTableColumn
ruleStatisticsGroupIndex = _RuleStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 2),
    _RuleStatisticsGroupIndex_Type()
)
ruleStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruleStatisticsGroupIndex.setStatus("current")
_RuleStatisticsRuleIndex_Type = Integer32
_RuleStatisticsRuleIndex_Object = MibTableColumn
ruleStatisticsRuleIndex = _RuleStatisticsRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 3),
    _RuleStatisticsRuleIndex_Type()
)
ruleStatisticsRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruleStatisticsRuleIndex.setStatus("current")
_RuleStatisticsRuleName_Type = OctetString
_RuleStatisticsRuleName_Object = MibTableColumn
ruleStatisticsRuleName = _RuleStatisticsRuleName_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 4),
    _RuleStatisticsRuleName_Type()
)
ruleStatisticsRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsRuleName.setStatus("current")
_RuleStatisticsRuleDescription_Type = OctetString
_RuleStatisticsRuleDescription_Object = MibTableColumn
ruleStatisticsRuleDescription = _RuleStatisticsRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 5),
    _RuleStatisticsRuleDescription_Type()
)
ruleStatisticsRuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsRuleDescription.setStatus("current")
_RuleStatisticsBlockEventCount_Type = Counter64
_RuleStatisticsBlockEventCount_Object = MibTableColumn
ruleStatisticsBlockEventCount = _RuleStatisticsBlockEventCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 6),
    _RuleStatisticsBlockEventCount_Type()
)
ruleStatisticsBlockEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsBlockEventCount.setStatus("current")
_RuleStatisticsBlockPacketCount_Type = Counter64
_RuleStatisticsBlockPacketCount_Object = MibTableColumn
ruleStatisticsBlockPacketCount = _RuleStatisticsBlockPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 7),
    _RuleStatisticsBlockPacketCount_Type()
)
ruleStatisticsBlockPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsBlockPacketCount.setStatus("current")
_RuleStatisticsBlockByteCount_Type = Counter64
_RuleStatisticsBlockByteCount_Object = MibTableColumn
ruleStatisticsBlockByteCount = _RuleStatisticsBlockByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 8),
    _RuleStatisticsBlockByteCount_Type()
)
ruleStatisticsBlockByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsBlockByteCount.setStatus("current")
_RuleStatisticsDetectEventCount_Type = Counter64
_RuleStatisticsDetectEventCount_Object = MibTableColumn
ruleStatisticsDetectEventCount = _RuleStatisticsDetectEventCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 9),
    _RuleStatisticsDetectEventCount_Type()
)
ruleStatisticsDetectEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsDetectEventCount.setStatus("current")
_RuleStatisticsDetectPacketCount_Type = Counter64
_RuleStatisticsDetectPacketCount_Object = MibTableColumn
ruleStatisticsDetectPacketCount = _RuleStatisticsDetectPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 10),
    _RuleStatisticsDetectPacketCount_Type()
)
ruleStatisticsDetectPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsDetectPacketCount.setStatus("current")
_RuleStatisticsDetectByteCount_Type = Counter64
_RuleStatisticsDetectByteCount_Object = MibTableColumn
ruleStatisticsDetectByteCount = _RuleStatisticsDetectByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 11),
    _RuleStatisticsDetectByteCount_Type()
)
ruleStatisticsDetectByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsDetectByteCount.setStatus("current")
_RuleStatisticsBlockPacketRate_Type = Counter32
_RuleStatisticsBlockPacketRate_Object = MibTableColumn
ruleStatisticsBlockPacketRate = _RuleStatisticsBlockPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 12),
    _RuleStatisticsBlockPacketRate_Type()
)
ruleStatisticsBlockPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsBlockPacketRate.setStatus("current")
_RuleStatisticsDetectPacketRate_Type = Counter32
_RuleStatisticsDetectPacketRate_Object = MibTableColumn
ruleStatisticsDetectPacketRate = _RuleStatisticsDetectPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 13),
    _RuleStatisticsDetectPacketRate_Type()
)
ruleStatisticsDetectPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsDetectPacketRate.setStatus("current")
_RuleStatisticsBlockBitRate_Type = Counter32
_RuleStatisticsBlockBitRate_Object = MibTableColumn
ruleStatisticsBlockBitRate = _RuleStatisticsBlockBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 14),
    _RuleStatisticsBlockBitRate_Type()
)
ruleStatisticsBlockBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsBlockBitRate.setStatus("current")
_RuleStatisticsDetectBitRate_Type = Counter32
_RuleStatisticsDetectBitRate_Object = MibTableColumn
ruleStatisticsDetectBitRate = _RuleStatisticsDetectBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 15),
    _RuleStatisticsDetectBitRate_Type()
)
ruleStatisticsDetectBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsDetectBitRate.setStatus("current")
_RuleStatisticsEgressEventCount_Type = Counter64
_RuleStatisticsEgressEventCount_Object = MibTableColumn
ruleStatisticsEgressEventCount = _RuleStatisticsEgressEventCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 16),
    _RuleStatisticsEgressEventCount_Type()
)
ruleStatisticsEgressEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsEgressEventCount.setStatus("current")
_RuleStatisticsEgressPacketCount_Type = Counter64
_RuleStatisticsEgressPacketCount_Object = MibTableColumn
ruleStatisticsEgressPacketCount = _RuleStatisticsEgressPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 17),
    _RuleStatisticsEgressPacketCount_Type()
)
ruleStatisticsEgressPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsEgressPacketCount.setStatus("current")
_RuleStatisticsEgressByteCount_Type = Counter64
_RuleStatisticsEgressByteCount_Object = MibTableColumn
ruleStatisticsEgressByteCount = _RuleStatisticsEgressByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 18),
    _RuleStatisticsEgressByteCount_Type()
)
ruleStatisticsEgressByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsEgressByteCount.setStatus("current")
_RuleStatisticsEgressPacketRate_Type = Counter32
_RuleStatisticsEgressPacketRate_Object = MibTableColumn
ruleStatisticsEgressPacketRate = _RuleStatisticsEgressPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 19),
    _RuleStatisticsEgressPacketRate_Type()
)
ruleStatisticsEgressPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsEgressPacketRate.setStatus("current")
_RuleStatisticsEgressBitRate_Type = Counter32
_RuleStatisticsEgressBitRate_Object = MibTableColumn
ruleStatisticsEgressBitRate = _RuleStatisticsEgressBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 20),
    _RuleStatisticsEgressBitRate_Type()
)
ruleStatisticsEgressBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsEgressBitRate.setStatus("current")
_RuleStatisticsBlockFrameByteCount_Type = Counter64
_RuleStatisticsBlockFrameByteCount_Object = MibTableColumn
ruleStatisticsBlockFrameByteCount = _RuleStatisticsBlockFrameByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 21),
    _RuleStatisticsBlockFrameByteCount_Type()
)
ruleStatisticsBlockFrameByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsBlockFrameByteCount.setStatus("current")
_RuleStatisticsDetectFrameByteCount_Type = Counter64
_RuleStatisticsDetectFrameByteCount_Object = MibTableColumn
ruleStatisticsDetectFrameByteCount = _RuleStatisticsDetectFrameByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 22),
    _RuleStatisticsDetectFrameByteCount_Type()
)
ruleStatisticsDetectFrameByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsDetectFrameByteCount.setStatus("current")
_RuleStatisticsEgressFrameByteCount_Type = Counter64
_RuleStatisticsEgressFrameByteCount_Object = MibTableColumn
ruleStatisticsEgressFrameByteCount = _RuleStatisticsEgressFrameByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 23),
    _RuleStatisticsEgressFrameByteCount_Type()
)
ruleStatisticsEgressFrameByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsEgressFrameByteCount.setStatus("current")
_RuleStatisticsBlockFrameBitRate_Type = Counter32
_RuleStatisticsBlockFrameBitRate_Object = MibTableColumn
ruleStatisticsBlockFrameBitRate = _RuleStatisticsBlockFrameBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 24),
    _RuleStatisticsBlockFrameBitRate_Type()
)
ruleStatisticsBlockFrameBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsBlockFrameBitRate.setStatus("current")
_RuleStatisticsDetectFrameBitRate_Type = Counter32
_RuleStatisticsDetectFrameBitRate_Object = MibTableColumn
ruleStatisticsDetectFrameBitRate = _RuleStatisticsDetectFrameBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 25),
    _RuleStatisticsDetectFrameBitRate_Type()
)
ruleStatisticsDetectFrameBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsDetectFrameBitRate.setStatus("current")
_RuleStatisticsEgressFrameBitRate_Type = Counter32
_RuleStatisticsEgressFrameBitRate_Object = MibTableColumn
ruleStatisticsEgressFrameBitRate = _RuleStatisticsEgressFrameBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 5, 1, 26),
    _RuleStatisticsEgressFrameBitRate_Type()
)
ruleStatisticsEgressFrameBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleStatisticsEgressFrameBitRate.setStatus("current")
_SetupRateStatisticsTable_Object = MibTable
setupRateStatisticsTable = _SetupRateStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6)
)
if mibBuilder.loadTexts:
    setupRateStatisticsTable.setStatus("current")
_SetupRateStatisticsEntry_Object = MibTableRow
setupRateStatisticsEntry = _SetupRateStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1)
)
setupRateStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "setupRateStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "setupRateStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    setupRateStatisticsEntry.setStatus("current")
_SetupRateStatisticsGroup_Type = GroupType
_SetupRateStatisticsGroup_Object = MibTableColumn
setupRateStatisticsGroup = _SetupRateStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1, 1),
    _SetupRateStatisticsGroup_Type()
)
setupRateStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setupRateStatisticsGroup.setStatus("current")


class _SetupRateStatisticsGroupIndex_Type(Integer32):
    """Custom type setupRateStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SetupRateStatisticsGroupIndex_Type.__name__ = "Integer32"
_SetupRateStatisticsGroupIndex_Object = MibTableColumn
setupRateStatisticsGroupIndex = _SetupRateStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1, 2),
    _SetupRateStatisticsGroupIndex_Type()
)
setupRateStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setupRateStatisticsGroupIndex.setStatus("current")
_SetupRateStatisticsIcmpSetupRate_Type = Counter32
_SetupRateStatisticsIcmpSetupRate_Object = MibTableColumn
setupRateStatisticsIcmpSetupRate = _SetupRateStatisticsIcmpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1, 3),
    _SetupRateStatisticsIcmpSetupRate_Type()
)
setupRateStatisticsIcmpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setupRateStatisticsIcmpSetupRate.setStatus("current")
_SetupRateStatisticsNonTcpSetupRate_Type = Counter32
_SetupRateStatisticsNonTcpSetupRate_Object = MibTableColumn
setupRateStatisticsNonTcpSetupRate = _SetupRateStatisticsNonTcpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1, 4),
    _SetupRateStatisticsNonTcpSetupRate_Type()
)
setupRateStatisticsNonTcpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setupRateStatisticsNonTcpSetupRate.setStatus("current")
_SetupRateStatisticsOtherIPSetupRate_Type = Counter32
_SetupRateStatisticsOtherIPSetupRate_Object = MibTableColumn
setupRateStatisticsOtherIPSetupRate = _SetupRateStatisticsOtherIPSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1, 5),
    _SetupRateStatisticsOtherIPSetupRate_Type()
)
setupRateStatisticsOtherIPSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setupRateStatisticsOtherIPSetupRate.setStatus("current")
_SetupRateStatisticsTcpSetupRate_Type = Counter32
_SetupRateStatisticsTcpSetupRate_Object = MibTableColumn
setupRateStatisticsTcpSetupRate = _SetupRateStatisticsTcpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1, 6),
    _SetupRateStatisticsTcpSetupRate_Type()
)
setupRateStatisticsTcpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setupRateStatisticsTcpSetupRate.setStatus("current")
_SetupRateStatisticsUdpSetupRate_Type = Counter32
_SetupRateStatisticsUdpSetupRate_Object = MibTableColumn
setupRateStatisticsUdpSetupRate = _SetupRateStatisticsUdpSetupRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 6, 1, 7),
    _SetupRateStatisticsUdpSetupRate_Type()
)
setupRateStatisticsUdpSetupRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setupRateStatisticsUdpSetupRate.setStatus("current")
_UsageStatisticsTable_Object = MibTable
usageStatisticsTable = _UsageStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7)
)
if mibBuilder.loadTexts:
    usageStatisticsTable.setStatus("current")
_UsageStatisticsEntry_Object = MibTableRow
usageStatisticsEntry = _UsageStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1)
)
usageStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "usageStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "usageStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    usageStatisticsEntry.setStatus("current")
_UsageStatisticsGroup_Type = GroupType
_UsageStatisticsGroup_Object = MibTableColumn
usageStatisticsGroup = _UsageStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 1),
    _UsageStatisticsGroup_Type()
)
usageStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usageStatisticsGroup.setStatus("current")


class _UsageStatisticsGroupIndex_Type(Integer32):
    """Custom type usageStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsageStatisticsGroupIndex_Type.__name__ = "Integer32"
_UsageStatisticsGroupIndex_Object = MibTableColumn
usageStatisticsGroupIndex = _UsageStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 2),
    _UsageStatisticsGroupIndex_Type()
)
usageStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usageStatisticsGroupIndex.setStatus("current")
_UsageStatisticsFinishIcmpFlows_Type = Counter64
_UsageStatisticsFinishIcmpFlows_Object = MibTableColumn
usageStatisticsFinishIcmpFlows = _UsageStatisticsFinishIcmpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 3),
    _UsageStatisticsFinishIcmpFlows_Type()
)
usageStatisticsFinishIcmpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsFinishIcmpFlows.setStatus("current")
_UsageStatisticsFinishOtherFlows_Type = Counter64
_UsageStatisticsFinishOtherFlows_Object = MibTableColumn
usageStatisticsFinishOtherFlows = _UsageStatisticsFinishOtherFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 4),
    _UsageStatisticsFinishOtherFlows_Type()
)
usageStatisticsFinishOtherFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsFinishOtherFlows.setStatus("current")
_UsageStatisticsFinishTcpFlows_Type = Counter64
_UsageStatisticsFinishTcpFlows_Object = MibTableColumn
usageStatisticsFinishTcpFlows = _UsageStatisticsFinishTcpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 5),
    _UsageStatisticsFinishTcpFlows_Type()
)
usageStatisticsFinishTcpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsFinishTcpFlows.setStatus("current")
_UsageStatisticsFinishUdpFlows_Type = Counter64
_UsageStatisticsFinishUdpFlows_Object = MibTableColumn
usageStatisticsFinishUdpFlows = _UsageStatisticsFinishUdpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 6),
    _UsageStatisticsFinishUdpFlows_Type()
)
usageStatisticsFinishUdpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsFinishUdpFlows.setStatus("current")
_UsageStatisticsInUseFlows_Type = Counter32
_UsageStatisticsInUseFlows_Object = MibTableColumn
usageStatisticsInUseFlows = _UsageStatisticsInUseFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 7),
    _UsageStatisticsInUseFlows_Type()
)
usageStatisticsInUseFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsInUseFlows.setStatus("current")
_UsageStatisticsInUseIcmpFlows_Type = Counter32
_UsageStatisticsInUseIcmpFlows_Object = MibTableColumn
usageStatisticsInUseIcmpFlows = _UsageStatisticsInUseIcmpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 8),
    _UsageStatisticsInUseIcmpFlows_Type()
)
usageStatisticsInUseIcmpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsInUseIcmpFlows.setStatus("current")
_UsageStatisticsInUseOtherFlows_Type = Counter32
_UsageStatisticsInUseOtherFlows_Object = MibTableColumn
usageStatisticsInUseOtherFlows = _UsageStatisticsInUseOtherFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 9),
    _UsageStatisticsInUseOtherFlows_Type()
)
usageStatisticsInUseOtherFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsInUseOtherFlows.setStatus("current")
_UsageStatisticsInUseTcpFlows_Type = Counter32
_UsageStatisticsInUseTcpFlows_Object = MibTableColumn
usageStatisticsInUseTcpFlows = _UsageStatisticsInUseTcpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 10),
    _UsageStatisticsInUseTcpFlows_Type()
)
usageStatisticsInUseTcpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsInUseTcpFlows.setStatus("current")
_UsageStatisticsInUseUdpFlows_Type = Counter32
_UsageStatisticsInUseUdpFlows_Object = MibTableColumn
usageStatisticsInUseUdpFlows = _UsageStatisticsInUseUdpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 11),
    _UsageStatisticsInUseUdpFlows_Type()
)
usageStatisticsInUseUdpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsInUseUdpFlows.setStatus("current")
_UsageStatisticsStartIcmpFlows_Type = Counter64
_UsageStatisticsStartIcmpFlows_Object = MibTableColumn
usageStatisticsStartIcmpFlows = _UsageStatisticsStartIcmpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 12),
    _UsageStatisticsStartIcmpFlows_Type()
)
usageStatisticsStartIcmpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsStartIcmpFlows.setStatus("current")
_UsageStatisticsStartOtherFlows_Type = Counter64
_UsageStatisticsStartOtherFlows_Object = MibTableColumn
usageStatisticsStartOtherFlows = _UsageStatisticsStartOtherFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 13),
    _UsageStatisticsStartOtherFlows_Type()
)
usageStatisticsStartOtherFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsStartOtherFlows.setStatus("current")
_UsageStatisticsStartTcpFlows_Type = Counter64
_UsageStatisticsStartTcpFlows_Object = MibTableColumn
usageStatisticsStartTcpFlows = _UsageStatisticsStartTcpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 14),
    _UsageStatisticsStartTcpFlows_Type()
)
usageStatisticsStartTcpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsStartTcpFlows.setStatus("current")
_UsageStatisticsStartUdpFlows_Type = Counter64
_UsageStatisticsStartUdpFlows_Object = MibTableColumn
usageStatisticsStartUdpFlows = _UsageStatisticsStartUdpFlows_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 7, 1, 15),
    _UsageStatisticsStartUdpFlows_Type()
)
usageStatisticsStartUdpFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageStatisticsStartUdpFlows.setStatus("current")
_TunnelStatisticsTable_Object = MibTable
tunnelStatisticsTable = _TunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8)
)
if mibBuilder.loadTexts:
    tunnelStatisticsTable.setStatus("current")
_TunnelStatisticsEntry_Object = MibTableRow
tunnelStatisticsEntry = _TunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1)
)
tunnelStatisticsEntry.setIndexNames(
    (0, "CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsGroup"),
    (0, "CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsGroupIndex"),
    (0, "CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsTunnelName"),
)
if mibBuilder.loadTexts:
    tunnelStatisticsEntry.setStatus("current")
_TunnelStatisticsGroup_Type = GroupType
_TunnelStatisticsGroup_Object = MibTableColumn
tunnelStatisticsGroup = _TunnelStatisticsGroup_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 1),
    _TunnelStatisticsGroup_Type()
)
tunnelStatisticsGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsGroup.setStatus("current")


class _TunnelStatisticsGroupIndex_Type(Integer32):
    """Custom type tunnelStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TunnelStatisticsGroupIndex_Type.__name__ = "Integer32"
_TunnelStatisticsGroupIndex_Object = MibTableColumn
tunnelStatisticsGroupIndex = _TunnelStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 2),
    _TunnelStatisticsGroupIndex_Type()
)
tunnelStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsGroupIndex.setStatus("current")
_TunnelStatisticsTunnelName_Type = OctetString
_TunnelStatisticsTunnelName_Object = MibTableColumn
tunnelStatisticsTunnelName = _TunnelStatisticsTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 3),
    _TunnelStatisticsTunnelName_Type()
)
tunnelStatisticsTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTunnelName.setStatus("current")
_TunnelStatisticsReceivedPackets_Type = Counter64
_TunnelStatisticsReceivedPackets_Object = MibTableColumn
tunnelStatisticsReceivedPackets = _TunnelStatisticsReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 4),
    _TunnelStatisticsReceivedPackets_Type()
)
tunnelStatisticsReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsReceivedPackets.setStatus("current")
_TunnelStatisticsReceivedBytes_Type = Counter64
_TunnelStatisticsReceivedBytes_Object = MibTableColumn
tunnelStatisticsReceivedBytes = _TunnelStatisticsReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 5),
    _TunnelStatisticsReceivedBytes_Type()
)
tunnelStatisticsReceivedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsReceivedBytes.setStatus("current")
_TunnelStatisticsDroppedFragments_Type = Counter64
_TunnelStatisticsDroppedFragments_Object = MibTableColumn
tunnelStatisticsDroppedFragments = _TunnelStatisticsDroppedFragments_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 6),
    _TunnelStatisticsDroppedFragments_Type()
)
tunnelStatisticsDroppedFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsDroppedFragments.setStatus("current")
_TunnelStatisticsBlockPacketCount_Type = Counter64
_TunnelStatisticsBlockPacketCount_Object = MibTableColumn
tunnelStatisticsBlockPacketCount = _TunnelStatisticsBlockPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 7),
    _TunnelStatisticsBlockPacketCount_Type()
)
tunnelStatisticsBlockPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBlockPacketCount.setStatus("current")
_TunnelStatisticsBlockByteCount_Type = Counter64
_TunnelStatisticsBlockByteCount_Object = MibTableColumn
tunnelStatisticsBlockByteCount = _TunnelStatisticsBlockByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 8),
    _TunnelStatisticsBlockByteCount_Type()
)
tunnelStatisticsBlockByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBlockByteCount.setStatus("current")
_TunnelStatisticsDetectPacketCount_Type = Counter64
_TunnelStatisticsDetectPacketCount_Object = MibTableColumn
tunnelStatisticsDetectPacketCount = _TunnelStatisticsDetectPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 9),
    _TunnelStatisticsDetectPacketCount_Type()
)
tunnelStatisticsDetectPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsDetectPacketCount.setStatus("current")
_TunnelStatisticsDetectByteCount_Type = Counter64
_TunnelStatisticsDetectByteCount_Object = MibTableColumn
tunnelStatisticsDetectByteCount = _TunnelStatisticsDetectByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 10),
    _TunnelStatisticsDetectByteCount_Type()
)
tunnelStatisticsDetectByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsDetectByteCount.setStatus("current")
_TunnelStatisticsEgressPacketCount_Type = Counter64
_TunnelStatisticsEgressPacketCount_Object = MibTableColumn
tunnelStatisticsEgressPacketCount = _TunnelStatisticsEgressPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 11),
    _TunnelStatisticsEgressPacketCount_Type()
)
tunnelStatisticsEgressPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsEgressPacketCount.setStatus("current")
_TunnelStatisticsEgressByteCount_Type = Counter64
_TunnelStatisticsEgressByteCount_Object = MibTableColumn
tunnelStatisticsEgressByteCount = _TunnelStatisticsEgressByteCount_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 12),
    _TunnelStatisticsEgressByteCount_Type()
)
tunnelStatisticsEgressByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsEgressByteCount.setStatus("current")
_TunnelStatisticsPacketReceiveRate_Type = Counter32
_TunnelStatisticsPacketReceiveRate_Object = MibTableColumn
tunnelStatisticsPacketReceiveRate = _TunnelStatisticsPacketReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 13),
    _TunnelStatisticsPacketReceiveRate_Type()
)
tunnelStatisticsPacketReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPacketReceiveRate.setStatus("current")
_TunnelStatisticsBitReceiveRate_Type = Counter32
_TunnelStatisticsBitReceiveRate_Object = MibTableColumn
tunnelStatisticsBitReceiveRate = _TunnelStatisticsBitReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 14),
    _TunnelStatisticsBitReceiveRate_Type()
)
tunnelStatisticsBitReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBitReceiveRate.setStatus("current")
_TunnelStatisticsFragmentDropRate_Type = Counter32
_TunnelStatisticsFragmentDropRate_Object = MibTableColumn
tunnelStatisticsFragmentDropRate = _TunnelStatisticsFragmentDropRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 15),
    _TunnelStatisticsFragmentDropRate_Type()
)
tunnelStatisticsFragmentDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFragmentDropRate.setStatus("current")
_TunnelStatisticsBlockPacketRate_Type = Counter32
_TunnelStatisticsBlockPacketRate_Object = MibTableColumn
tunnelStatisticsBlockPacketRate = _TunnelStatisticsBlockPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 16),
    _TunnelStatisticsBlockPacketRate_Type()
)
tunnelStatisticsBlockPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBlockPacketRate.setStatus("current")
_TunnelStatisticsBlockBitRate_Type = Counter32
_TunnelStatisticsBlockBitRate_Object = MibTableColumn
tunnelStatisticsBlockBitRate = _TunnelStatisticsBlockBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 17),
    _TunnelStatisticsBlockBitRate_Type()
)
tunnelStatisticsBlockBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBlockBitRate.setStatus("current")
_TunnelStatisticsDetectPacketRate_Type = Counter32
_TunnelStatisticsDetectPacketRate_Object = MibTableColumn
tunnelStatisticsDetectPacketRate = _TunnelStatisticsDetectPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 18),
    _TunnelStatisticsDetectPacketRate_Type()
)
tunnelStatisticsDetectPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsDetectPacketRate.setStatus("current")
_TunnelStatisticsDetectBitRate_Type = Counter32
_TunnelStatisticsDetectBitRate_Object = MibTableColumn
tunnelStatisticsDetectBitRate = _TunnelStatisticsDetectBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 19),
    _TunnelStatisticsDetectBitRate_Type()
)
tunnelStatisticsDetectBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsDetectBitRate.setStatus("current")
_TunnelStatisticsEgressPacketRate_Type = Counter32
_TunnelStatisticsEgressPacketRate_Object = MibTableColumn
tunnelStatisticsEgressPacketRate = _TunnelStatisticsEgressPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 20),
    _TunnelStatisticsEgressPacketRate_Type()
)
tunnelStatisticsEgressPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsEgressPacketRate.setStatus("current")
_TunnelStatisticsEgressBitRate_Type = Counter32
_TunnelStatisticsEgressBitRate_Object = MibTableColumn
tunnelStatisticsEgressBitRate = _TunnelStatisticsEgressBitRate_Object(
    (1, 3, 6, 1, 4, 1, 41036, 4, 1, 5, 8, 1, 21),
    _TunnelStatisticsEgressBitRate_Type()
)
tunnelStatisticsEgressBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsEgressBitRate.setStatus("current")

# Managed Objects groups

coreroStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 2, 5)
)
coreroStatisticsGroup.setObjects(
      *(("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsContextOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsContextOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsEgressDropPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsEgressDropPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsEgressOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsEgressOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFinishTrustedAddresses"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFinishUnclassifiedAddresses"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFlexRuleOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFlexRuleOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFlowOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFlowOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFragmentOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsFragmentOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIngressDropPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIngressDropPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsInputOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsInputOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIpOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIpOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsSetupOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsSetupOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsSmartRuleOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsSmartRuleOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsSourceSmartRuleOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsSourceSmartRuleOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIngressOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIngressOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIngressOverloadBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsIngressOverloadBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsStartTrustedAddresses"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsStartUnclassifiedAddresses"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsTotalAddressAdds"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsStartTrackingFlow"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsStopTrackingFlow"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsDDoSScorecardOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "advancedStatisticsDDoSScorecardOverloadPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsAllRulesBlockPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsAllRulesBlockBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsAllRulesBlockFrameBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsAllRulesBlockPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsAllRulesBlockBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "blockRateStatisticsAllRulesBlockFrameBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortBitReceiveRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortBitTransmitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortEgressDroppedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortIngressDroppedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortPacketReceiveRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortPacketTransmitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortReceivedBadCrcPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortReceivedBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortReceivedJabberPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortReceivedOversizedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortReceivedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortTransmitErrorPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortTransmittedBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortTransmittedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortBitReceiveRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortBitTransmitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortEgressDroppedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortIngressDroppedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortPacketReceiveRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortPacketTransmitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortReceivedBadCrcPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortReceivedBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortReceivedJabberPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortReceivedOversizedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortReceivedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortTransmitErrorPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortTransmittedBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortTransmittedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortIngressOverloadPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortIngressOverloadBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsExternalPortReceivedFecErrorPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "interfaceStatisticsInternalPortReceivedFecErrorPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsInUseAddresses"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsInUseTrustedAddresses"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsInUseUnclassifiedAddresses"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPanicGood"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPanicGoodRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPanicBad"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPanicBadRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPanicTimedOut"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPanicTimedOutRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPromotedToTrusted"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsPromotedToTrustedRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsTrackedTcpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsTrackedTcpFlowsSuccess"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsTrackedTcpFlowsSuccessRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsTrackedTcpFlowsTimedOut"),
        ("CORERO-CMS-STATISTICS-MIB", "ipAddressStatisticsTrackedTcpFlowsTimedOutRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsBlockByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsBlockFrameByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsBlockBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsBlockFrameBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsBlockEventCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsBlockPacketCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsBlockPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsDetectByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsDetectFrameByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsDetectBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsDetectFrameBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsDetectEventCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsDetectPacketCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsDetectPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsEgressByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsEgressFrameByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsEgressBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsEgressFrameBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsEgressEventCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsEgressPacketCount"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsEgressPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsRuleDescription"),
        ("CORERO-CMS-STATISTICS-MIB", "ruleStatisticsRuleName"),
        ("CORERO-CMS-STATISTICS-MIB", "setupRateStatisticsIcmpSetupRate"),
        ("CORERO-CMS-STATISTICS-MIB", "setupRateStatisticsNonTcpSetupRate"),
        ("CORERO-CMS-STATISTICS-MIB", "setupRateStatisticsOtherIPSetupRate"),
        ("CORERO-CMS-STATISTICS-MIB", "setupRateStatisticsTcpSetupRate"),
        ("CORERO-CMS-STATISTICS-MIB", "setupRateStatisticsUdpSetupRate"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsFinishIcmpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsFinishOtherFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsFinishTcpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsFinishUdpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsInUseFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsInUseIcmpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsInUseOtherFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsInUseTcpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsInUseUdpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsStartIcmpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsStartOtherFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsStartTcpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "usageStatisticsStartUdpFlows"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsTunnelName"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsReceivedPackets"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsReceivedBytes"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsDroppedFragments"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsBlockPacketCount"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsBlockByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsDetectPacketCount"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsDetectByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsEgressPacketCount"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsEgressByteCount"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsPacketReceiveRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsBitReceiveRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsFragmentDropRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsBlockPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsBlockBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsDetectPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsDetectBitRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsEgressPacketRate"),
        ("CORERO-CMS-STATISTICS-MIB", "tunnelStatisticsEgressBitRate"))
)
if mibBuilder.loadTexts:
    coreroStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coreroCMSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41036, 4, 2, 1, 5)
)
coreroCMSMIBCompliance.setObjects(
    ("CORERO-CMS-STATISTICS-MIB", "coreroStatisticsGroup")
)
if mibBuilder.loadTexts:
    coreroCMSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CORERO-CMS-STATISTICS-MIB",
    **{"GroupType": GroupType,
       "statistics": statistics,
       "advancedStatisticsTable": advancedStatisticsTable,
       "advancedStatisticsEntry": advancedStatisticsEntry,
       "advancedStatisticsGroup": advancedStatisticsGroup,
       "advancedStatisticsGroupIndex": advancedStatisticsGroupIndex,
       "advancedStatisticsStartTrustedAddresses": advancedStatisticsStartTrustedAddresses,
       "advancedStatisticsStartUnclassifiedAddresses": advancedStatisticsStartUnclassifiedAddresses,
       "advancedStatisticsFinishTrustedAddresses": advancedStatisticsFinishTrustedAddresses,
       "advancedStatisticsFinishUnclassifiedAddresses": advancedStatisticsFinishUnclassifiedAddresses,
       "advancedStatisticsTotalAddressAdds": advancedStatisticsTotalAddressAdds,
       "advancedStatisticsInputOverloadPackets": advancedStatisticsInputOverloadPackets,
       "advancedStatisticsInputOverloadPacketRate": advancedStatisticsInputOverloadPacketRate,
       "advancedStatisticsSetupOverloadPackets": advancedStatisticsSetupOverloadPackets,
       "advancedStatisticsSetupOverloadPacketRate": advancedStatisticsSetupOverloadPacketRate,
       "advancedStatisticsContextOverloadPackets": advancedStatisticsContextOverloadPackets,
       "advancedStatisticsContextOverloadPacketRate": advancedStatisticsContextOverloadPacketRate,
       "advancedStatisticsEgressDropPackets": advancedStatisticsEgressDropPackets,
       "advancedStatisticsEgressDropPacketRate": advancedStatisticsEgressDropPacketRate,
       "advancedStatisticsIngressDropPackets": advancedStatisticsIngressDropPackets,
       "advancedStatisticsIngressDropPacketRate": advancedStatisticsIngressDropPacketRate,
       "advancedStatisticsEgressOverloadPackets": advancedStatisticsEgressOverloadPackets,
       "advancedStatisticsEgressOverloadPacketRate": advancedStatisticsEgressOverloadPacketRate,
       "advancedStatisticsFlowOverloadPackets": advancedStatisticsFlowOverloadPackets,
       "advancedStatisticsFlowOverloadPacketRate": advancedStatisticsFlowOverloadPacketRate,
       "advancedStatisticsSmartRuleOverloadPackets": advancedStatisticsSmartRuleOverloadPackets,
       "advancedStatisticsSmartRuleOverloadPacketRate": advancedStatisticsSmartRuleOverloadPacketRate,
       "advancedStatisticsSourceSmartRuleOverloadPackets": advancedStatisticsSourceSmartRuleOverloadPackets,
       "advancedStatisticsSourceSmartRuleOverloadPacketRate": advancedStatisticsSourceSmartRuleOverloadPacketRate,
       "advancedStatisticsFragmentOverloadPackets": advancedStatisticsFragmentOverloadPackets,
       "advancedStatisticsFragmentOverloadPacketRate": advancedStatisticsFragmentOverloadPacketRate,
       "advancedStatisticsIpOverloadPackets": advancedStatisticsIpOverloadPackets,
       "advancedStatisticsIpOverloadPacketRate": advancedStatisticsIpOverloadPacketRate,
       "advancedStatisticsFlexRuleOverloadPackets": advancedStatisticsFlexRuleOverloadPackets,
       "advancedStatisticsFlexRuleOverloadPacketRate": advancedStatisticsFlexRuleOverloadPacketRate,
       "advancedStatisticsIngressOverloadPackets": advancedStatisticsIngressOverloadPackets,
       "advancedStatisticsIngressOverloadPacketRate": advancedStatisticsIngressOverloadPacketRate,
       "advancedStatisticsIngressOverloadBytes": advancedStatisticsIngressOverloadBytes,
       "advancedStatisticsIngressOverloadBitRate": advancedStatisticsIngressOverloadBitRate,
       "advancedStatisticsStartTrackingFlow": advancedStatisticsStartTrackingFlow,
       "advancedStatisticsStopTrackingFlow": advancedStatisticsStopTrackingFlow,
       "advancedStatisticsDDoSScorecardOverloadPackets": advancedStatisticsDDoSScorecardOverloadPackets,
       "advancedStatisticsDDoSScorecardOverloadPacketRate": advancedStatisticsDDoSScorecardOverloadPacketRate,
       "blockRateStatisticsTable": blockRateStatisticsTable,
       "blockRateStatisticsEntry": blockRateStatisticsEntry,
       "blockRateStatisticsGroup": blockRateStatisticsGroup,
       "blockRateStatisticsGroupIndex": blockRateStatisticsGroupIndex,
       "blockRateStatisticsAllRulesBlockPackets": blockRateStatisticsAllRulesBlockPackets,
       "blockRateStatisticsAllRulesBlockPacketRate": blockRateStatisticsAllRulesBlockPacketRate,
       "blockRateStatisticsAllRulesBlockBytes": blockRateStatisticsAllRulesBlockBytes,
       "blockRateStatisticsAllRulesBlockBitRate": blockRateStatisticsAllRulesBlockBitRate,
       "blockRateStatisticsAllRulesBlockFrameBytes": blockRateStatisticsAllRulesBlockFrameBytes,
       "blockRateStatisticsAllRulesBlockFrameBitRate": blockRateStatisticsAllRulesBlockFrameBitRate,
       "interfaceStatisticsTable": interfaceStatisticsTable,
       "interfaceStatisticsEntry": interfaceStatisticsEntry,
       "interfaceStatisticsGroup": interfaceStatisticsGroup,
       "interfaceStatisticsGroupIndex": interfaceStatisticsGroupIndex,
       "interfaceStatisticsExternalPortBitReceiveRate": interfaceStatisticsExternalPortBitReceiveRate,
       "interfaceStatisticsExternalPortBitTransmitRate": interfaceStatisticsExternalPortBitTransmitRate,
       "interfaceStatisticsExternalPortEgressDroppedPackets": interfaceStatisticsExternalPortEgressDroppedPackets,
       "interfaceStatisticsExternalPortIngressDroppedPackets": interfaceStatisticsExternalPortIngressDroppedPackets,
       "interfaceStatisticsExternalPortPacketReceiveRate": interfaceStatisticsExternalPortPacketReceiveRate,
       "interfaceStatisticsExternalPortPacketTransmitRate": interfaceStatisticsExternalPortPacketTransmitRate,
       "interfaceStatisticsExternalPortReceivedBadCrcPackets": interfaceStatisticsExternalPortReceivedBadCrcPackets,
       "interfaceStatisticsExternalPortReceivedBytes": interfaceStatisticsExternalPortReceivedBytes,
       "interfaceStatisticsExternalPortReceivedJabberPackets": interfaceStatisticsExternalPortReceivedJabberPackets,
       "interfaceStatisticsExternalPortReceivedOversizedPackets": interfaceStatisticsExternalPortReceivedOversizedPackets,
       "interfaceStatisticsExternalPortReceivedPackets": interfaceStatisticsExternalPortReceivedPackets,
       "interfaceStatisticsExternalPortTransmitErrorPackets": interfaceStatisticsExternalPortTransmitErrorPackets,
       "interfaceStatisticsExternalPortTransmittedBytes": interfaceStatisticsExternalPortTransmittedBytes,
       "interfaceStatisticsExternalPortTransmittedPackets": interfaceStatisticsExternalPortTransmittedPackets,
       "interfaceStatisticsInternalPortBitReceiveRate": interfaceStatisticsInternalPortBitReceiveRate,
       "interfaceStatisticsInternalPortBitTransmitRate": interfaceStatisticsInternalPortBitTransmitRate,
       "interfaceStatisticsInternalPortEgressDroppedPackets": interfaceStatisticsInternalPortEgressDroppedPackets,
       "interfaceStatisticsInternalPortIngressDroppedPackets": interfaceStatisticsInternalPortIngressDroppedPackets,
       "interfaceStatisticsInternalPortPacketReceiveRate": interfaceStatisticsInternalPortPacketReceiveRate,
       "interfaceStatisticsInternalPortPacketTransmitRate": interfaceStatisticsInternalPortPacketTransmitRate,
       "interfaceStatisticsInternalPortReceivedBadCrcPackets": interfaceStatisticsInternalPortReceivedBadCrcPackets,
       "interfaceStatisticsInternalPortReceivedBytes": interfaceStatisticsInternalPortReceivedBytes,
       "interfaceStatisticsInternalPortReceivedJabberPackets": interfaceStatisticsInternalPortReceivedJabberPackets,
       "interfaceStatisticsInternalPortReceivedOversizedPackets": interfaceStatisticsInternalPortReceivedOversizedPackets,
       "interfaceStatisticsInternalPortReceivedPackets": interfaceStatisticsInternalPortReceivedPackets,
       "interfaceStatisticsInternalPortTransmitErrorPackets": interfaceStatisticsInternalPortTransmitErrorPackets,
       "interfaceStatisticsInternalPortTransmittedBytes": interfaceStatisticsInternalPortTransmittedBytes,
       "interfaceStatisticsInternalPortTransmittedPackets": interfaceStatisticsInternalPortTransmittedPackets,
       "interfaceStatisticsExternalPortIngressOverloadPackets": interfaceStatisticsExternalPortIngressOverloadPackets,
       "interfaceStatisticsExternalPortIngressOverloadBytes": interfaceStatisticsExternalPortIngressOverloadBytes,
       "interfaceStatisticsExternalPortReceivedFecErrorPackets": interfaceStatisticsExternalPortReceivedFecErrorPackets,
       "interfaceStatisticsInternalPortReceivedFecErrorPackets": interfaceStatisticsInternalPortReceivedFecErrorPackets,
       "ipAddressStatisticsTable": ipAddressStatisticsTable,
       "ipAddressStatisticsEntry": ipAddressStatisticsEntry,
       "ipAddressStatisticsGroup": ipAddressStatisticsGroup,
       "ipAddressStatisticsGroupIndex": ipAddressStatisticsGroupIndex,
       "ipAddressStatisticsInUseAddresses": ipAddressStatisticsInUseAddresses,
       "ipAddressStatisticsInUseTrustedAddresses": ipAddressStatisticsInUseTrustedAddresses,
       "ipAddressStatisticsInUseUnclassifiedAddresses": ipAddressStatisticsInUseUnclassifiedAddresses,
       "ipAddressStatisticsPanicGood": ipAddressStatisticsPanicGood,
       "ipAddressStatisticsPanicGoodRate": ipAddressStatisticsPanicGoodRate,
       "ipAddressStatisticsPanicBad": ipAddressStatisticsPanicBad,
       "ipAddressStatisticsPanicBadRate": ipAddressStatisticsPanicBadRate,
       "ipAddressStatisticsPanicTimedOut": ipAddressStatisticsPanicTimedOut,
       "ipAddressStatisticsPanicTimedOutRate": ipAddressStatisticsPanicTimedOutRate,
       "ipAddressStatisticsPromotedToTrusted": ipAddressStatisticsPromotedToTrusted,
       "ipAddressStatisticsPromotedToTrustedRate": ipAddressStatisticsPromotedToTrustedRate,
       "ipAddressStatisticsTrackedTcpFlows": ipAddressStatisticsTrackedTcpFlows,
       "ipAddressStatisticsTrackedTcpFlowsSuccess": ipAddressStatisticsTrackedTcpFlowsSuccess,
       "ipAddressStatisticsTrackedTcpFlowsSuccessRate": ipAddressStatisticsTrackedTcpFlowsSuccessRate,
       "ipAddressStatisticsTrackedTcpFlowsTimedOut": ipAddressStatisticsTrackedTcpFlowsTimedOut,
       "ipAddressStatisticsTrackedTcpFlowsTimedOutRate": ipAddressStatisticsTrackedTcpFlowsTimedOutRate,
       "ruleStatisticsTable": ruleStatisticsTable,
       "ruleStatisticsEntry": ruleStatisticsEntry,
       "ruleStatisticsGroup": ruleStatisticsGroup,
       "ruleStatisticsGroupIndex": ruleStatisticsGroupIndex,
       "ruleStatisticsRuleIndex": ruleStatisticsRuleIndex,
       "ruleStatisticsRuleName": ruleStatisticsRuleName,
       "ruleStatisticsRuleDescription": ruleStatisticsRuleDescription,
       "ruleStatisticsBlockEventCount": ruleStatisticsBlockEventCount,
       "ruleStatisticsBlockPacketCount": ruleStatisticsBlockPacketCount,
       "ruleStatisticsBlockByteCount": ruleStatisticsBlockByteCount,
       "ruleStatisticsDetectEventCount": ruleStatisticsDetectEventCount,
       "ruleStatisticsDetectPacketCount": ruleStatisticsDetectPacketCount,
       "ruleStatisticsDetectByteCount": ruleStatisticsDetectByteCount,
       "ruleStatisticsBlockPacketRate": ruleStatisticsBlockPacketRate,
       "ruleStatisticsDetectPacketRate": ruleStatisticsDetectPacketRate,
       "ruleStatisticsBlockBitRate": ruleStatisticsBlockBitRate,
       "ruleStatisticsDetectBitRate": ruleStatisticsDetectBitRate,
       "ruleStatisticsEgressEventCount": ruleStatisticsEgressEventCount,
       "ruleStatisticsEgressPacketCount": ruleStatisticsEgressPacketCount,
       "ruleStatisticsEgressByteCount": ruleStatisticsEgressByteCount,
       "ruleStatisticsEgressPacketRate": ruleStatisticsEgressPacketRate,
       "ruleStatisticsEgressBitRate": ruleStatisticsEgressBitRate,
       "ruleStatisticsBlockFrameByteCount": ruleStatisticsBlockFrameByteCount,
       "ruleStatisticsDetectFrameByteCount": ruleStatisticsDetectFrameByteCount,
       "ruleStatisticsEgressFrameByteCount": ruleStatisticsEgressFrameByteCount,
       "ruleStatisticsBlockFrameBitRate": ruleStatisticsBlockFrameBitRate,
       "ruleStatisticsDetectFrameBitRate": ruleStatisticsDetectFrameBitRate,
       "ruleStatisticsEgressFrameBitRate": ruleStatisticsEgressFrameBitRate,
       "setupRateStatisticsTable": setupRateStatisticsTable,
       "setupRateStatisticsEntry": setupRateStatisticsEntry,
       "setupRateStatisticsGroup": setupRateStatisticsGroup,
       "setupRateStatisticsGroupIndex": setupRateStatisticsGroupIndex,
       "setupRateStatisticsIcmpSetupRate": setupRateStatisticsIcmpSetupRate,
       "setupRateStatisticsNonTcpSetupRate": setupRateStatisticsNonTcpSetupRate,
       "setupRateStatisticsOtherIPSetupRate": setupRateStatisticsOtherIPSetupRate,
       "setupRateStatisticsTcpSetupRate": setupRateStatisticsTcpSetupRate,
       "setupRateStatisticsUdpSetupRate": setupRateStatisticsUdpSetupRate,
       "usageStatisticsTable": usageStatisticsTable,
       "usageStatisticsEntry": usageStatisticsEntry,
       "usageStatisticsGroup": usageStatisticsGroup,
       "usageStatisticsGroupIndex": usageStatisticsGroupIndex,
       "usageStatisticsFinishIcmpFlows": usageStatisticsFinishIcmpFlows,
       "usageStatisticsFinishOtherFlows": usageStatisticsFinishOtherFlows,
       "usageStatisticsFinishTcpFlows": usageStatisticsFinishTcpFlows,
       "usageStatisticsFinishUdpFlows": usageStatisticsFinishUdpFlows,
       "usageStatisticsInUseFlows": usageStatisticsInUseFlows,
       "usageStatisticsInUseIcmpFlows": usageStatisticsInUseIcmpFlows,
       "usageStatisticsInUseOtherFlows": usageStatisticsInUseOtherFlows,
       "usageStatisticsInUseTcpFlows": usageStatisticsInUseTcpFlows,
       "usageStatisticsInUseUdpFlows": usageStatisticsInUseUdpFlows,
       "usageStatisticsStartIcmpFlows": usageStatisticsStartIcmpFlows,
       "usageStatisticsStartOtherFlows": usageStatisticsStartOtherFlows,
       "usageStatisticsStartTcpFlows": usageStatisticsStartTcpFlows,
       "usageStatisticsStartUdpFlows": usageStatisticsStartUdpFlows,
       "tunnelStatisticsTable": tunnelStatisticsTable,
       "tunnelStatisticsEntry": tunnelStatisticsEntry,
       "tunnelStatisticsGroup": tunnelStatisticsGroup,
       "tunnelStatisticsGroupIndex": tunnelStatisticsGroupIndex,
       "tunnelStatisticsTunnelName": tunnelStatisticsTunnelName,
       "tunnelStatisticsReceivedPackets": tunnelStatisticsReceivedPackets,
       "tunnelStatisticsReceivedBytes": tunnelStatisticsReceivedBytes,
       "tunnelStatisticsDroppedFragments": tunnelStatisticsDroppedFragments,
       "tunnelStatisticsBlockPacketCount": tunnelStatisticsBlockPacketCount,
       "tunnelStatisticsBlockByteCount": tunnelStatisticsBlockByteCount,
       "tunnelStatisticsDetectPacketCount": tunnelStatisticsDetectPacketCount,
       "tunnelStatisticsDetectByteCount": tunnelStatisticsDetectByteCount,
       "tunnelStatisticsEgressPacketCount": tunnelStatisticsEgressPacketCount,
       "tunnelStatisticsEgressByteCount": tunnelStatisticsEgressByteCount,
       "tunnelStatisticsPacketReceiveRate": tunnelStatisticsPacketReceiveRate,
       "tunnelStatisticsBitReceiveRate": tunnelStatisticsBitReceiveRate,
       "tunnelStatisticsFragmentDropRate": tunnelStatisticsFragmentDropRate,
       "tunnelStatisticsBlockPacketRate": tunnelStatisticsBlockPacketRate,
       "tunnelStatisticsBlockBitRate": tunnelStatisticsBlockBitRate,
       "tunnelStatisticsDetectPacketRate": tunnelStatisticsDetectPacketRate,
       "tunnelStatisticsDetectBitRate": tunnelStatisticsDetectBitRate,
       "tunnelStatisticsEgressPacketRate": tunnelStatisticsEgressPacketRate,
       "tunnelStatisticsEgressBitRate": tunnelStatisticsEgressBitRate,
       "coreroCMSMIBCompliance": coreroCMSMIBCompliance,
       "coreroStatisticsGroup": coreroStatisticsGroup}
)
